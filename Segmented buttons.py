from tkinter import *
import customtkinter

root = customtkinter.CTk()

def clicker(value):
    my_label.configure(text=f"Hello {value}") # you can also do {my_seg_button.get()}, but you should use value

my_values = ["John", "Greg", "Philip"]

my_seg_button = customtkinter.CTkSegmentedButton(root, values=my_values, 
                                                 command=clicker,
                                                 width=300,
                                                 height=100,
                                                 font=("Arial", 20),
                                                 corner_radius=3,
                                                 border_width=5,
                                                 fg_color="MediumPurple3",
                                                 bg_color="Red",
                                                 selected_hover_color="pink",
                                                 selected_color="Green",
                                                 unselected_color="yellow",
                                                 unselected_hover_color="gray",
                                                 text_color="Orange",
                                                 text_color_disabled="Red",
                                                 state="normal",
                                                 dynamic_resizing="True" # this changes the size to the text size, true by default
                                                 ) #you can also type the list manually, but it's easier to do a list out of it and it looks cleaner
my_seg_button.pack(pady=40)

#set default selection
#my_seg_button.set("John")

my_label = customtkinter.CTkLabel(root, text=(""))
my_label.pack(pady=20)

root.mainloop()
