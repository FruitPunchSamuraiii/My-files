from tkinter import *
import customtkinter

root = customtkinter.CTk()

#Creating the functions
def sliding(value):
    my_label.configure(text=int(value))


#Creating the slider
my_slider = customtkinter.CTkSlider(root,
                                    from_=0, # underscore because from is a python keyword
                                    to=100,
                                    command=sliding,
                                    orientation="horizontal",
                                    number_of_steps=100,
                                    width=100,
                                    height=25,
                                    border_width=3,
                                    fg_color="Red",
                                    bg_color="MediumPurple3",
                                    progress_color="Gray",
                                    button_color="Orange",
                                    state="normal",
                                    hover=True #lets you disable colour change when hovered over if false
                                    )
my_slider.pack(pady=40)

#Define starting point
my_slider.set(0)

my_label = customtkinter.CTkLabel(root, text=my_slider.get(), font=("Arial", 20))
my_label.pack(pady=10)

root.mainloop()