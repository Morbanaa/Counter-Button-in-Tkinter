from tkinter import *

class MyGui():
    count = 0
    def __init__(self):
        self.window = Tk()

        self.photo =PhotoImage(file="M.png")

        self.button = Button(self.window,
                             text="click me",
                             command=self.click,
                             font=('Arial',30),
                             fg="red",
                             bg='black',
                             activeforeground="red",
                             activebackground="black",
                             image=self.photo,
                             compound="top") 
        self.button.pack()

        self.window.mainloop() 

    def click(self):
        self.count += 1
        print(self.count)

          
         
def main():
    my_gui = MyGui()
    
if __name__ == "__main__":
    main()
