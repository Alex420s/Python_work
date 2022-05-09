from tkinter import *
main_window = Tk()
main_window.title("Random")#titulo de la ventana principal
main_window.geometry("600x400")
#main_window.resizable (0,0) #"bloquea" el tamaño de la ventana
main_window.configure(bg='#23e32b')
label_title = Label(main_window, text="Test",bg="#00B4DB",fg='#2c3e50',  
                    font=('Arial',35, 'bold') )#titulo dentro de la ventana
label_title.pack(pady=10)
main_window.mainloop()