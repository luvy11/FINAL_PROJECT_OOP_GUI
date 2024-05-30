# Main Programmer for this Page : Porcare, Dana E.
import tkinter as tk # Importing tkinter module and renaming it as 'tk' for brevity
import sqlite3 # Importing sqlite3 module
from tkinter import messagebox  # Importing messagebox classes from tkinter module
from PIL import Image, ImageTk  # Importing Image and ImageTk classes from PIL module
from __OOP_Class import design_gui_interface, AnimatedGIFLabel # Importing design_gui_interface and AnimatedGIFLabel classes from OOP_Class module
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               SETTING UP THE WINDOW
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window = tk.Tk()
window.geometry("1920x1080") # Setting the size of the window
window.title("LOG IN") # Setting the title of the window
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                         CALLING OR IMPORTING THE OOP_CLASS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
gui = design_gui_interface()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                          CONNECT THE DATEBASE FROM SQLITE3
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
con = sqlite3.connect("Employee_Data_db")
cursor = con.cursor()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                              ADDING BACKGROUND TO GUI
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
background_image_path = "Log_In_Background.gif"
animated_bg = AnimatedGIFLabel(window, background_image_path)
animated_bg.place(relwidth=1, relheight=1)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                            ADDING THE NEEDED CONTENTS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Adding the Company Logo and Name
# Logo and name reference: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2Funis%2Fcomments%2F1b8n8lt%2Funis_logo_explanation%2F&psig=AOvVaw2_P1D_MW8CvQHnIVHafCpT&ust=1717035739615000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCMj278nmsYYDFQAAAAAdAAAAABAE
company_logo = gui.image1_design(window, 255, 251, "UNIS_Logo2.png", 199, 92)
UNIS_corporation_label = gui.label_design(window, 287, 343, "UNIS Corporation", "#81AFD2", "#0C385E", ("Century Gothic", 12, 'bold'))
# Adding needed labels
log_in_label = gui.label_design(window, 176, 408, "LOG IN", "#88B6D8", "white", ("Century Gothic", 28, 'bold'))
username_label = gui.label_design(window, 176, 474, "Username", "#8AB8D9", "white", ("Century Gothic", 15, 'bold'))
password_label = gui.label_design(window, 176, 550, "Password", "#8EBCDD", "white", ("Century Gothic", 15, 'bold'))
# Adding needed entries
Username = gui.entry_design(window, 176, 505, 364, 35, "white", "#0C385E", ("Century Gothic", 10, 'bold'), "#0C385E", "#0C385E")
Password = gui.entry_design(window, 176, 582, 364, 35, "white", "#0C385E", ("Century Gothic", 10, 'bold'), "#0C385E", "#0C385E")
Password.config(show="•")
# Additional functionalities
eye_open_photo = Image.open("Show_Password_Logo.png")
eye_open_image = ImageTk.PhotoImage(eye_open_photo.resize((29, 19)))
eye_closed_photo = Image.open("Don't_Show_Password_Logo.png")
eye_closed_image = ImageTk.PhotoImage(eye_closed_photo.resize((29, 19)))
show_password = False
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                 ADDING FUNCTIONS AND BOTTONS FOR THE DATABASE
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def toggle_password(): # For Showing Password
    global show_password
    if show_password:
        Password.config(show="•")
        show_password_button.config(image=eye_closed_image)
    else:
        Password.config(show="")
        show_password_button.config(image=eye_open_image)
    show_password = not show_password
def logIn(): # For LogIn Button
    username = Username.get()
    password = Password.get()
    cursor.execute("SELECT Employee_Number FROM main_employee_information_tbl WHERE Username=? AND Password=?", (username, password))
    user = cursor.fetchone()
    if user:
        employee_number = user[-1] # Assuming the Employee_Number is the first column in the database
        if employee_number == 20240000:
            window.destroy()
            import _III_OOP_Admin_Portal
            _III_OOP_Admin_Portal.main(username)
        else:
            window.destroy()
            import _IV_OOP_Employee_Portal
            _IV_OOP_Employee_Portal.main(username)
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        messagebox.showinfo("Reminder", "Use your employee number as the username and contact number as the password. For Example, Username:202212345 & Password:09123456789")
def cancelData(): # For Cancel Button
    Username.delete(0, 'end')
    Password.delete(0, 'end')
    window.destroy()
# Adding the needed buttons
log_in_button = gui.button_design(window, 197, 650, 150, 34, "#0C385E", "white", "LOG IN", ("Century Gothic", 12, 'bold'))
log_in_button.config(command=logIn)
cancel_button = gui.button_design(window, 367, 650, 150, 34, "#1E6CAB", "white", "CANCEL", ("Century Gothic", 12, 'bold'))
cancel_button.config(command=cancelData)
show_password_button = gui.button_design(window, 499, 588, 40, 25, "white", "white", "", ("Century Gothic", 10,))
show_password_button.config(image=eye_closed_image, command=toggle_password, borderwidth=0, relief=tk.FLAT, activebackground="white")

window.state('zoomed') # Functionality to keep the page on auto-full screen
window.mainloop() # Start the GUI event loop