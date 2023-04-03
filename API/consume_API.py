import requests

# Using httpbin API
# Oftentimes you will have the option to have query parameters, and then we can provide a dictionary
params = {
    "name": "Alex",
    "age": 25

}

response = requests.get("https://httpbin.org/get", params= params)
print(response.url)

resp_json = response.json()
del resp_json ['origin'] # Delete the JSON 'origin' field (this is the IP address) 
print(resp_json)

# It works differently

payload = {
    "edad": 25,
    "nombre": "Alex"
}
respuesta = requests.post("https://httpbin.org/post", data=payload )
print(respuesta.url)
print(respuesta.json())

estado = requests.get("https://httpbin.org/status/500")

if estado.status_code == requests.codes.not_found:
    print('Not Found') # 404 code 
else: 
    print(estado.status_code)

# User Agent is essentially an identification that tells the web service what software you´re using.
# By default it´s 'User-Agent': 'python-requests/2.28.2', we can specify a different  user agent manually
# UA from Safari mobile version

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Accept": "image/png"
 }

resp_user = requests.get( "https://httpbin.org/user-agent", headers= headers )
print(resp_user.text)


# type suggest by the Accept header
resp_img = requests.get( "https://httpbin.org/image", headers= headers)

#Save into a binary file
with open ("myimage.png", "wb") as f:
    f.write(resp_img.content)

headers = {
   "Accept": "image/jpeg"
 }
resp_img = requests.get( "https://httpbin.org/image", headers= headers)
with open ("myimage.jpg", "wb") as f:
    f.write(resp_img.content)

# If response is slow you can specify a certain timout or tolerance you´re going to raise an exception and continue 
response = requests.get("http://httpbin.org/delay/2", timeout=3)
resp_json = response.json()
del resp_json ['origin'] # Delete the JSON 'origin' field (this is the IP address) 
print(resp_json)

# Using Proxies 

proxies = {
    "http": "139.99.237.62:80",
    "https":"139.99.237.62:80"
    }
response = requests.get("http://httpbin.org/get", proxies=proxies)
print(response.text)
print(response.request.url)
print(response.cookies) # Cookies recibidas del servidor

print(response.headers) # Cabeceras de la respuesta
print(response.request.headers) # Cabeceras de la peticion
print(response.content) # Devuelve el body en bytes
print(response.text) #devuelve en formato str
print(response.json())