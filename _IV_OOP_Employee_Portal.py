# Main Programmer for this Page : Porcare, Dana E.
import tkinter as tk # Importing tkinter module and renaming it as 'tk' for brevity
import sqlite3 # Importing sqlite3 module
from tkinter import * # Importing all classes and functions from tkinter module
from tkinter import Canvas, Scrollbar, messagebox # Importing Canvas, Scrollbar, and messagebox classes from tkinter module
from PIL import Image, ImageTk # Importing Image and ImageTk classes from PIL module
from io import BytesIO # Importing BytesIO from io module
from __OOP_Class import design_gui_interface # Importing design_gui_interface class from OOP_Class module

def main(username):
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               SETTING UP THE WINDOW
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    window = tk.Tk()
    window.geometry("1920x1080") # Setting the size of the window
    window.title("EMPLOYEE PORTAL") # Setting the title of the window
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
#                                                                                            ADDING SCROLLBAR AND CANVAS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    scrollbar_y = Scrollbar(window, orient=VERTICAL)
    scrollbar_y.pack(side=RIGHT, fill=Y)
    # Create a canvas for displaying content
    my_canvas = Canvas(window, width=1920, height=3000, yscrollcommand=scrollbar_y.set)
    my_canvas.pack(side=LEFT, fill=BOTH)
    # Configure scrollbars to work with the canvas
    scrollbar_y.config(command=my_canvas.yview)
    # Load background image and display it on the canvas
    background_image = Image.open("Registration_Background.png")
    background_photo = ImageTk.PhotoImage(background_image)
    my_canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
    # Function to adjust canvas size when resized
    def on_canvas_configure(event):
        my_canvas.itemconfig(event, width=event.width, height=event.height, anchor='nw')
    # Configure vertical scrollbar to update scroll region
    scrollbar_y.bind('<Configure>', lambda event: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Bind scrollbar movement to canvas scrolling
    scrollbar_y.bind("<B1-Motion>", lambda event: my_canvas.yview("moveto", event.y / my_canvas.winfo_height()))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                    ADDING FRAMES INSIDE THE MY_CANVAS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    header_frame = Frame(my_canvas, width=1900, height=50, bg="#065494")
    my_canvas.create_window((2, 0), window=header_frame, anchor=tk.NW)
    name_frame = Frame(my_canvas, width=978, height=81, bg="#3A8BC0")
    my_canvas.create_window((190, 250), window=name_frame, anchor=tk.NW)
    main_frame = Frame(my_canvas, width=1706, height=1638, bg="#E4F0FC")
    my_canvas.create_window((112, 745), window=main_frame, anchor=tk.NW)
    frame = Frame(my_canvas, width=1535, height=474, bg="#0C385E")
    my_canvas.create_window((385, 2526), window=frame, anchor=tk.NW)
    last_frame = Frame(my_canvas, width=1920, height=120, bg="#0C385E")
    my_canvas.create_window((2, 2880), window=last_frame, anchor=tk.NW)
    picture_frame = Frame(my_canvas, width=450, height=450, bg="#0C385E")
    my_canvas.create_window((1345, 136), window=picture_frame, anchor=tk.NW)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                            ADDING THE NEEDED CONTENTS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adding the needed label
    welcome_label = my_canvas.create_text(680, 361, text="Welcome to the Employee Portal", font=("Century Gothic", 45), fill="white")
    # Adding the needed image
    employee_image = gui.image1_design(picture_frame, 16, 16, "Profile_Picture.png", 416, 416)
    # Adding the Company Logo and Name
    # Logo and name reference: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2Funis%2Fcomments%2F1b8n8lt%2Funis_logo_explanation%2F&psig=AOvVaw2_P1D_MW8CvQHnIVHafCpT&ust=1717035739615000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCMj278nmsYYDFQAAAAAdAAAAABAE
    company_logo_image = Image.open("UNIS_Logo.png")
    company_logo_photo = ImageTk.PhotoImage(company_logo_image.resize((279, 128)))
    company_logo = my_canvas.create_image(53, 33, anchor=tk.NW, image=company_logo_photo)
    company_logo_image2 = Image.open("UNIS_Logo.png")
    company_logo_photo2 = ImageTk.PhotoImage(company_logo_image2.resize((162, 75)))
    company_logo2 = my_canvas.create_image(169, 2592, anchor=tk.NW, image=company_logo_photo2)
    # Adding the needed design
    line2 = gui.frame_design(frame, 0, 324, 1354, 7, "white")
    # Adding the needed frames for founders images
    profile_frame = gui.frame_design(main_frame, 26, 88, 495, 229, "#065494")
    payroll_frame = gui.frame_design(main_frame, 600, 88, 495, 229, "#065494")
    account_frame = gui.frame_design(main_frame, 1174, 88, 495, 229, "#065494")
    line = gui.frame_design(main_frame, 67, 437, 1559, 8, "#065494")
    founder_frame1 = gui.frame_design(main_frame, 408, 752, 266, 266, "#0C385E")
    founder_frame2 = gui.frame_design(main_frame, 408, 1136, 266, 266, "#0C385E")
    founder_frame3 = gui.frame_design(main_frame, 998, 823, 266, 266, "#0C385E")
    founder_frame4 = gui.frame_design(main_frame, 998, 1207, 266, 266, "#0C385E")
    images = {}
    images['founder_image1'] = ImageTk.PhotoImage(Image.open("CRUZ_Meagan_Ysabelle.jpg").resize((246, 246)))
    images['founder_image2'] = ImageTk.PhotoImage(Image.open("LEONIDA_Love_Joy.jpg").resize((246, 246)))
    images['founder_image3'] = ImageTk.PhotoImage(Image.open("PORCARE_Dana.jpg").resize((246, 246)))
    images['founder_image4'] = ImageTk.PhotoImage(Image.open("RABINO_Kimberly_Ann.png").resize((246, 246)))
    founder_image1 = Label(main_frame, image=images['founder_image1'])
    founder_image1.place(x=416, y=760)
    founder_image2 = Label(main_frame, image=images['founder_image2'])
    founder_image2.place(x=416, y=1144)
    founder_image3 = Label(main_frame, image=images['founder_image3'])
    founder_image3.place(x=1006, y=831)
    founder_image4 = Label(main_frame, image=images['founder_image4'])
    founder_image4.place(x=1006, y=1215)
    # Adding the needed labels
    employee_personal_information_label = gui.label_design(main_frame, 124, 201, "Employee Personal\nInformation", "#065494", "white", ("Century Gothic", 25))
    employee_choice_payroll_label = gui.label_design(main_frame, 713, 201, "Employee Choice\nPayroll", "#065494", "white", ("Century Gothic", 25))
    employee_user_information_label = gui.label_design(main_frame, 1304, 201, "Employee User\nInformation", "#065494", "white", ("Century Gothic", 25))
    the_founders_label = gui.label_design(main_frame, 593, 528, "THE FOUNDERS:", "#E4F0FC", "#0C385E", ("Century Gothic", 50, 'bold'))
    founder_label1 = gui.label_design(main_frame, 307, 1041, "CRUZ, Meagan Ysabelle", "#E4F0FC", "#0C385E", ("Century Gothic", 30))
    founder_label2 = gui.label_design(main_frame, 354, 1425, "LEONIDA, Love Joy", "#E4F0FC", "#0C385E", ("Century Gothic", 30))
    founder_label3 = gui.label_design(main_frame, 965, 752, "PORCARE, Dana", "#E4F0FC", "#0C385E", ("Century Gothic", 30))
    founder_label4 = gui.label_design(main_frame, 915, 1136, "RABINO, Kimberly Ann", "#E4F0FC", "#0C385E", ("Century Gothic", 30))
    services_label = gui.label_design(frame, 75, 75, "SERVICES", "#0C385E", "white", ("Century Gothic", 25, 'bold'))
    contact_us_label = gui.label_design(frame, 268, 75, "CONTACT US", "#0C385E", "white", ("Century Gothic", 25, 'bold'))
    founders_label = gui.label_design(frame, 815, 75, "FOUNDERS", "#0C385E", "white", ("Century Gothic", 25, 'bold'))
    services_info_label = gui.label_design(frame, 75, 132, "Profile\nPayroll\nAccount", "#0C385E", "white", ("Century Gothic", 20))
    services_info_label.config(anchor='w', justify='left')
    contact_us_info_label = gui.label_design(frame, 268, 132, "Call the service desk for help with your\nIT requests, questions, and problems.\n    800-444-4444\n    helpdesk@unis.co.ph", "#0C385E", "white", ("Century Gothic", 20))
    contact_us_info_label.config(anchor='w', justify='left')
    founders_info_label = gui.label_design(frame, 815, 132,"meagan.ysabelle.cruz@adamson.edu.ph\nlove.joy.leonida@adamson.edu.ph\ndana.porcare@adamson.edu.ph\nkimberly.ann.rabino@adamson.edu.ph", "#0C385E", "white", ("Century Gothic", 20))
    founders_info_label.config(anchor='w', justify='left')
    copyright_label = gui.label_design(last_frame, 177, 17, "Copyright 2024, All rights reserved", "#0C385E", "white",("Century Gothic", 26, 'bold'))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             ADDING THE A FUNCTION THAT AUTOMATICALLY PUT INPUTS ONCE LOG IN
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def populate_user_info(username): # For needed input once logIn
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Username=?", (username,))
        user = cursor.fetchone()
        if user:
            image_data = user[52]
            with BytesIO(image_data) as image:
                employee_profile_picture = gui.image1_design(picture_frame, 16, 16, image, 416, 416)
            full_name = f"{user[0]} {user[2]}"
            hello_label = Label(name_frame, bg="#3A8BC0", fg="white", text=f"Hello {full_name},", font=("Century Gothic", 40, 'bold'))
            hello_label.place(x=0, y=0, width=978, height=81)
            hello_label.config(anchor='w', justify='left')
        else:
            messagebox.showerror("Error", "User not found in the database.")
    populate_user_info(username)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               ADDING FUNCTIONS AND BOTTONS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def log_out(): # For LogOut Button
        window.destroy()
        import _II_OOP_Log_In_Page
    def switch_to_profile_page(): # For Profile Button
        window.destroy()
        import _V_OOP_Profile_Page
        _V_OOP_Profile_Page.main(username)
    def switch_to_payroll_page(): # For Payroll Button
        window.destroy()
        import _VI_OOP_Payroll_Page
        _VI_OOP_Payroll_Page.main(username)
    def switch_to_account_page(): # For Account Button
        window.destroy()
        import _VII_OOP_Account_Page
        _VII_OOP_Account_Page.main(username)
    # Adding the needed buttons
    log_out_image = ImageTk.PhotoImage(Image.open("Log_Out_Logo.png").resize((39, 32)))
    log_out_button = gui.button_design(header_frame, 1690, 0, 210, 58, "#065494", "white", " Log Out", ("Century Gothic", 21, 'bold'))
    log_out_button.config(image=log_out_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#065494", command=log_out)
    profile_image = ImageTk.PhotoImage(Image.open("Profile_Logo.png").resize((56, 61)))
    profile_button = gui.button_design(main_frame, 26, 88, 495, 104, "#065494", "white", " PROFILE",("Century Gothic", 30, 'bold'))
    profile_button.config(image=profile_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#065494", command=switch_to_profile_page)
    payroll_image = ImageTk.PhotoImage(Image.open("Payroll_Logo.png").resize((56, 61)))
    payroll_button = gui.button_design(main_frame, 600, 88, 495, 104, "#065494", "white", " PAYROLL",("Century Gothic", 30, 'bold'))
    payroll_button.config(image=payroll_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#065494",  command=switch_to_payroll_page)
    account_image = ImageTk.PhotoImage(Image.open("Account_Logo.png").resize((56, 61)))
    account_button = gui.button_design(main_frame, 1174, 88, 495, 104, "#065494", "white", " ACCOUNT",("Century Gothic", 30, 'bold'))
    account_button.config(image=account_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#065494", command=switch_to_account_page)

    window.state('zoomed')  # Functionality to keep the page on auto-full screen
    window.mainloop()  # Start the GUI event loop