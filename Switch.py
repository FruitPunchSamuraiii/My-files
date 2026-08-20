from tkinter import *
import customtkinter

root = customtkinter.CTk()

def switcher():
    my_label.configure(text=switch_var.get())

#Create a toggle function
def clicker():
    #my_switch.deselect()
    #my_switch.select()
    my_switch.toggle() # this gives text since it calls the command of the switch so it updates the label

#Create a stringvar, keeps track of things
switch_var = customtkinter.StringVar(value=on) #you can change the default here

#Create switch
my_switch = customtkinter.CTkSwitch(root, text="Switch", command=switcher,
                                    variable=switch_var, onvalue="on", offvalue="off",
                                    switch_height=25,
                                    switch_width=200,
                                    corner_radius=5,
                                    border_color="MediumPurple3",
                                    border_width=6,
                                    text_color="red",
                                    hover=True,
                                    fg_color="orange",
                                    bg_color="pink",
                                    progress_color="green",
                                    button_color="black",
                                    button_hover_color="Gray",
                                    font=("Arial", 20),
                                    state="normal" #if you disable this, it grays out the switch and even disables the button
                                    )
my_switch.pack(pady=40)

#Create a label
my_label = customtkinter.CTkLabel(root, text="")
my_label.pack(10)

#Create a button
my_button = customtkinter.CTkButton(root, text="Click Me!", command=clicker)
my_button.pack(pady=10)


root.mainloop()