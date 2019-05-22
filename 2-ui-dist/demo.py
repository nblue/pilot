from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")

label = Label(window, text="This is our first GUI!")
label.pack()

def greet():
    print("Greetings!")
    
greet_button = Button(window, text="Greet", command=greet)
greet_button.pack()

close_button = Button(window, text="Close", command=window.quit)
close_button.place(anchor=NW)
 
window.mainloop()