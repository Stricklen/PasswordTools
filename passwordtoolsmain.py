from tkinter import Tk, Button, Frame, Label, LabelFrame, OptionMenu, Checkbutton, StringVar
import random

def do_nothing():
    return

def main():
    # Initialise root
    root = Tk()
    root.title("Password Tools")
    root.geometry("300x450")

    # Create label frame for generation options
    option_labelframe = LabelFrame(root)
    option_labelframe.pack()
    # # Creating option menu
    var1 = StringVar()
    pass_length = OptionMenu(option_labelframe, 
                            var1,
                            "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    pass_length.config(text="Length")
    pass_length.pack()

    print(pass_length.selection_get())

    # Create label frame from strength tester
    strength_labelframe = LabelFrame(root)
    strength_labelframe.pack()



    close_button = Button(root,
                          text="Close",
                          command=lambda: root.destroy()
    )
    close_button.pack(side="bottom")

    root.mainloop()

if __name__ == "__main__":
    main()