# Instalación de librerías necesarias:
# pip install pybluez
# pip install bleak

import socket
import asyncio
from bleak import BleakScanner, BleakClient
import time

# ============================================
# socket CLÁSICO con PyBluez
# ============================================

def escanear_dispositivos_clasicos():
    """Escanea dispositivos socket clásicos cercanos"""
    print("Escaneando dispositivos socket clásicos...")
    
    # Buscar dispositivos durante 8 segundos
    dispositivos = socket.discover_devices(
        duration=8, 
        lookup_names=True, 
        flush_cache=True
    )
    
    print(f"Encontrados {len(dispositivos)} dispositivos:")
    for addr, nombre in dispositivos:
        print(f"  {nombre} - {addr}")
    
    return dispositivos

def buscar_servicios(direccion_mac):
    """Busca servicios disponibles en un dispositivo específico"""
    print(f"Buscando servicios en {direccion_mac}...")
    
    servicios = socket.find_service(address=direccion_mac)
    
    for servicio in servicios:
        print(f"Servicio: {servicio['name']}")
        print(f"  Protocolo: {servicio['protocol']}")
        print(f"  Puerto: {servicio['port']}")
        print(f"  Descripción: {servicio.get('description', 'N/A')}")
        print()

class Servidorsocket:
    """Servidor RFCOMM simple para recibir conexiones"""
    
    def __init__(self, puerto=socket.PORT_ANY):
        self.socket = socket.socketSocket(socket.RFCOMM)
        self.puerto = puerto
        
    def iniciar_servidor(self):
        # Bind al puerto
        self.socket.bind(("", self.puerto))
        self.socket.listen(1)
        
        puerto = self.socket.getsockname()[1]
        print(f"Servidor iniciado en puerto {puerto}")
        
        # Registrar el servicio
        socket.advertise_service(
            self.socket,
            "Servidor Python",
            service_id="1e0ca4ea-299d-4335-93eb-27fcfe7fa848",
            service_classes=["1101"],
            profiles=["1101"]
        )
        
        print("Esperando conexiones...")
        return puerto
    
    def manejar_conexiones(self):
        """Maneja conexiones entrantes"""
        while True:
            try:
                cliente, info = self.socket.accept()
                print(f"Conexión desde {info}")
                
                # Leer datos del cliente
                datos = cliente.recv(1024)
                print(f"Datos recibidos: {datos.decode('utf-8')}")
                
                # Enviar respuesta
                cliente.send("Mensaje recibido correctamente")
                cliente.close()
                
            except socket.socketError as e:
                print(f"Error: {e}")
                break

# ============================================
# socket LOW ENERGY con Bleak
# ============================================

async def escanear_dispositivos_ble():
    """Escanea dispositivos socket Low Energy"""
    print("Escaneando dispositivos BLE...")
    
    dispositivos = await BleakScanner.discover(timeout=10.0)
    
    print(f"Encontrados {len(dispositivos)} dispositivos BLE:")
    for dispositivo in dispositivos:
        print(f"  {dispositivo.name or 'Sin nombre'} - {dispositivo.address} (RSSI: {dispositivo.rssi})")
    
    return dispositivos

async def conectar_dispositivo_ble(direccion_mac):
    """Conecta a un dispositivo BLE específico"""
    async with BleakClient(direccion_mac) as cliente:
        print(f"Conectado a {direccion_mac}")
        
        # Obtener servicios
        servicios = await cliente.get_services()
        
        print("Servicios disponibles:")
        for servicio in servicios:
            print(f"  Servicio: {servicio.uuid}")
            for caracteristica in servicio.characteristics:
                print(f"    Característica: {caracteristica.uuid}")
                print(f"      Propiedades: {caracteristica.properties}")

async def leer_caracteristica_ble(direccion_mac, uuid_caracteristica):
    """Lee una característica específica de un dispositivo BLE"""
    async with BleakClient(direccion_mac) as cliente:
        if await cliente.is_connected():
            valor = await cliente.read_gatt_char(uuid_caracteristica)
            print(f"Valor leído: {valor}")
            return valor

async def escribir_caracteristica_ble(direccion_mac, uuid_caracteristica, datos):
    """Escribe datos a una característica BLE"""
    async with BleakClient(direccion_mac) as cliente:
        if await cliente.is_connected():
            await cliente.write_gatt_char(uuid_caracteristica, datos)
            print(f"Datos escritos: {datos}")

# ============================================
# APLICACIÓN PARA DOMÓTICA
# ============================================

class ControladorDomotica:
    """Controlador para dispositivos de domótica vía socket"""
    
    def __init__(self):
        self.dispositivos_conectados = {}
    
    async def descubrir_dispositivos_domotica(self):
        """Busca dispositivos de domótica específicos"""
        dispositivos = await BleakScanner.discover()
        
        # Filtrar por nombres conocidos o servicios específicos
        domotica = []
        for disp in dispositivos:
            nombre = disp.name or ""
            if any(palabra in nombre.lower() for palabra in 
                   ["smart", "light", "sensor", "thermostat", "plug"]):
                domotica.append(disp)
        
        return domotica
    
    async def controlar_luz(self, direccion_mac, encender=True):
        """Controla una bombilla inteligente"""
        # UUID típico para control de luz (ejemplo genérico)
        uuid_control = "12345678-1234-5678-9abc-123456789abc"
        
        comando = b'\x01' if encender else b'\x00'
        
        try:
            async with BleakClient(direccion_mac) as cliente:
                await cliente.write_gatt_char(uuid_control, comando)
                estado = "encendida" if encender else "apagada"
                print(f"Luz {estado}")
        except Exception as e:
            print(f"Error controlando luz: {e}")
    
    async def leer_sensor_temperatura(self, direccion_mac):
        """Lee la temperatura de un sensor"""
        # UUID típico para temperatura
        uuid_temp = "00002a6e-0000-1000-8000-00805f9b34fb"
        
        try:
            async with BleakClient(direccion_mac) as cliente:
                datos = await cliente.read_gatt_char(uuid_temp)
                # Conversión típica (depende del fabricante)
                temperatura = int.from_bytes(datos, byteorder='little') / 100.0
                print(f"Temperatura: {temperatura}°C")
                return temperatura
        except Exception as e:
            print(f"Error leyendo temperatura: {e}")
            return None

# ============================================
# EJEMPLO DE USO
# ============================================

async def ejemplo_principal():
    """Ejemplo principal que demuestra el uso de las funciones"""
    
    print("=== DEMOSTRACIÓN socket ===\n")
    
    # 1. Escaneo de dispositivos clásicos
    print("1. Escaneando dispositivos socket clásicos:")
    dispositivos_clasicos = escanear_dispositivos_clasicos()
    print()
    
    # 2. Escaneo de dispositivos BLE
    print("2. Escaneando dispositivos BLE:")
    dispositivos_ble = await escanear_dispositivos_ble()
    print()
    
    # 3. Ejemplo de domótica
    print("3. Buscando dispositivos de domótica:")
    controlador = ControladorDomotica()
    dispositivos_domotica = await controlador.descubrir_dispositivos_domotica()
    
    for disp in dispositivos_domotica:
        print(f"  Dispositivo domótica: {disp.name} - {disp.address}")
    
    # Si hay dispositivos, intentar controlar el primero
    if dispositivos_domotica:
        direccion = dispositivos_domotica[0].address
        print(f"\nIntentando controlar {direccion}...")
        await controlador.controlar_luz(direccion, True)
        time.sleep(2)
        await controlador.controlar_luz(direccion, False)

if __name__ == "__main__":
    # Para dispositivos clásicos
    print("Ejecutando escaneo de dispositivos clásicos...")
    escanear_dispositivos_clasicos()
    
    # Para dispositivos BLE (requiere asyncio)
    print("\nEjecutando funciones BLE...")
    asyncio.run(ejemplo_principal())