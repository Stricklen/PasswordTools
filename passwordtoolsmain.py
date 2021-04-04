from tkinter import Tk, Button, Frame, Label, LabelFrame, OptionMenu, Checkbutton, StringVar, IntVar, Entry
import generator

def main():
    def genpress():
        print("Submit attempted")

    # Initialise root
    root = Tk()
    root.title("Password Tools")
    # root.geometry("300x450")
    titlefont = ("times", 20, "bold")
    entryfont = ("times", 15)

    # Create app title
    title_label = Label(root,
                        text="PASSWORD TOOLS",
                        font=titlefont,
                        pady="10",
                        padx="10")
    title_label.grid(row=0,column=0)


    # Create label frame for generation options
    generator_labelframe = LabelFrame(root, text="Generator")
    generator_labelframe.grid(row=1,column=0)
    # Creating option menu and label
    length_label = Label(generator_labelframe,
                        text="Password Length:")
    length_label.grid(row=0,column=0)
    var1 = StringVar()
    pass_length = OptionMenu(generator_labelframe, 
                            var1,
                            "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"
                            )
    pass_length.config(text="Length")
    pass_length.grid(row=1,column=0)
    # Create 'Generate' button
    generator_button = Button(generator_labelframe,
                                text="Generate!",
                                command=lambda: genpress())
    generator_button.grid(row=2,column=0,rowspan="2")
    # Creating the three checkboxes
    s_var = IntVar()
    symbols_box = Checkbutton(generator_labelframe,
                                text="Symbols",
                                variable=s_var)
    symbols_box.grid(row=0,column=1)
    n_var = IntVar()
    numbers_box = Checkbutton(generator_labelframe,
                                text="Numbers",
                                variable=n_var)
    numbers_box.grid(row=1,column=1)
    u_var = IntVar()
    uppers_box = Checkbutton(generator_labelframe,
                                text="Uppercase",
                                variable=u_var)
    uppers_box.grid(row=2,column=1)
    l_var = IntVar()
    lowers_box = Checkbutton(generator_labelframe,
                                text="Lowercase",
                                variable=l_var)
    lowers_box.grid(row=3,column=1)
    # Create field for generated password
    generator_output = Entry(generator_labelframe,
                                width="25",
                                font=entryfont)
    generator_output.grid(row=4,column=0,columnspan=2)


    # Create label frame from strength tester
    strength_labelframe = LabelFrame(root,
                                    text="Strength Tester")
    strength_labelframe.grid(row=2,column=0)
    # Entry for password strength checker
    strength_entry = Entry(strength_labelframe,
                            width="25",
                            font=entryfont)
    strength_entry.pack()
    # Label for result of the strength test
    result_label = Label(strength_labelframe,
                        text="RESULTS ARE IN: YOU ARE WEAK")
    result_label.pack()

    close_button = Button(root,
                          text="Close",
                          command=lambda: root.destroy()
    )
    close_button.grid(row=3,column=0)

    root.mainloop()

if __name__ == "__main__":
    main()