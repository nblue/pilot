from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")

label = Label(window, text="This is our first GUI!")
label.pack()

def greet():
    print("Hello: ",input_box.get())
    
greet_button = Button(window, text="Greet", command=greet)
greet_button.pack()

close_button = Button(window, text="Close", command=window.quit)
close_button.place(anchor=NW)

input_box = Entry(window)
input_box.pack()

window.mainloop()