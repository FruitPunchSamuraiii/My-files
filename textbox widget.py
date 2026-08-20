from tkinter import *
import customtkinter

root = customtkinter.CTk()

thing= ''

#Functions
def delete():
    my_text.delete(0.0, 'end') #very first character is 0.0 final one is end

def copy():
    global thing
    thing = my_text.get(0.0, 'end')

def paste():
    if thing:
        my_text.insert('end', thing)
    else:
        my_text.insert('end', "There is nothing to paste!")


my_text = customtkinter.CTkTextbox(root,
                                    width=650,
                                    height=200,
                                    corner_radius=3,
                                    border_color="pink",
                                    border_width=6,
                                    bg_color="orange",
                                    border_spacing=4,
                                    fg_color="purple",
                                    font=("Arial", 20),
                                    text_color="Black",
                                    wrap="char", #char wraps the character, word wraps the entire word, and none (gives a scroll bar)
                                    activate_scrollbars= True, #by default true, this is what scrolls when wrap is none
                                    scrollbar_button_color="DarkBlue",
                                    scrollbar_button_hover_color="Silver"
                                   )
my_text.pack(pady=20)

my_frame = customtkinter.CTkFrame(root)
my_frame.pack(pady=10)

delete_button = customtkinter.CTkButton(my_frame, text="Delete", command=delete)
copy_button = customtkinter.CTkButton(my_frame, text="Copy", command=copy)
paste_button = customtkinter.CTkButton(my_frame, text="Paste", command=paste)

delete_button.grid(row=0, column=1)
copy_button.grid(row=0, column=2, padx=10)
paste_button.grid(row=0, column=3)

root.mainloop()
