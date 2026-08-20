from tkinter import *
import customtkinter

root = customtkinter.CTk()

def clicker():
    my_button.configure(text="You clicked the tab!")

#Create Tabview
my_tab = customtkinter.CTkTabview(root,
                                  width = 600,
                                  height = 250,
                                  corner_radius=3, # if it's too round, it can chop off what is inside
                                  fg_color="red",
                                  segmented_button_fg_color="orange",
                                  segmented_button_selected_color="green",
                                  segmented_button_selected_hover_color="gray",
                                  segmented_button_unselected_color="purple",
                                  segmented_button_unselected_hover_color="black",
                                  text_color="silver",
                                  state="normal",
                                  command=clicker,
                                  anchor="W"
                                  )
my_tab.pack(pady=10)

#Creat tabs
tab_1 = my_tab.add("Tab 1")
tab_2 = my_tab.add("Tab 2")

#Put stuff in tabs
my_button = customtkinter.CTkButton(tab_1, text="click me")
my_button.pack(pady=40)



root.mainloop()