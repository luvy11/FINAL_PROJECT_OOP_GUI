# Main Programmer for this Page : Porcare, Dana E.
import tkinter as tk # Importing tkinter module and renaming it as 'tk' for brevity
import sqlite3 # Importing sqlite3 module
from tkinter import * # Importing all classes and functions from tkinter module
from tkinter import Canvas, Scrollbar, filedialog, messagebox # Importing Canvas, Scrollbar, filedialog, and messagebox classes from tkinter module
from PIL import Image, ImageTk # Importing Image and ImageTk classes from PIL module
from io import BytesIO # Importing BytesIO from io module
from __OOP_Class import design_gui_interface, AnimatedGIFLabel  # Importing design_gui_interface and AnimatedGIFLabel classes from OOP_Class module

def main(username):
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               SETTING UP THE WINDOW
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    window = tk.Tk()
    window.geometry("1920x1080")
    window.title("PROFILE PAGE")
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
    my_canvas = Canvas(window, width=1920, height=1080, yscrollcommand=scrollbar_y.set)
    my_canvas.pack(side=LEFT, fill=BOTH)
    # Configure scrollbars to work with the canvas
    scrollbar_y.config(command=my_canvas.yview)
    # Load background image and display it on the canvas
    frame = Frame(my_canvas, width=1920, height=1080)
    my_canvas.create_window((0, 0), window=frame, anchor=tk.NW)
    background_image_path = "Portal2_Background.gif"
    animated_bg = AnimatedGIFLabel(frame, background_image_path)
    animated_bg.place(relwidth=1, relheight=1)
    # Function to adjust canvas size when resized
    def on_canvas_configure(event):
        my_canvas.itemconfig(event, width=event.width, height=event.height, anchor='nw')
    # Configure vertical scrollbar to update scroll region
    scrollbar_y.bind('<Configure>', lambda event: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Bind scrollbar movement to canvas scrolling
    scrollbar_y.bind("<B1-Motion>", lambda event: my_canvas.yview("moveto", event.y / my_canvas.winfo_height()))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                    ADDING FRAMES INSIDE THE MAIN FRAME
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    picture_frame = gui.frame_design(frame, 57, 57, 147, 147, "#0C385E")
    frame1 = gui.frame_design(frame, 303, 102, 709, 402, "#1E6CAB")
    frame2 = gui.frame_design(frame, 303, 515, 709, 386, "white")
    frame3 = gui.frame_design(frame, 303, 912, 709, 129, "#1E6CAB")
    frame4 = gui.frame_design(frame, 1025, 102, 389, 402, "white")
    frame5 = gui.frame_design(frame, 1427, 102, 303, 402, "white")
    frame6 = gui.frame_design(frame, 1743, 102, 132, 402, "#1E6CAB")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                            ADDING THE NEEDED CONTENTS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adding the needed images
    images = {}
    images['employee_image'] = ImageTk.PhotoImage(Image.open("Profile_Picture.png").resize((295, 295)))
    images['company_logo'] = ImageTk.PhotoImage(Image.open("UNIS_Logo3.png").resize((108, 50)))
    picture_frame = gui.frame_design(frame, 352, 148, 310, 310, "#0C385E")
    employee_image = Label(frame, image=images['employee_image'])
    employee_image.place(x=358, y=154)
    # Adding the needed labels
    profile_label = gui.label_design(frame, 310, 31, "Profile", "#E4F0FC", "#0C385E", ("Century Gothic", 33, 'bold'))
    email_label = gui.label_design(frame, 696, 190, "Email", "#1E6CAB", "white", ("Century Gothic", 14, 'bold'))
    contact_number_label = gui.label_design(frame, 696, 266, "Contact No.", "#1E6CAB", "white", ("Century Gothic", 14, 'bold'))
    address_label = gui.label_design(frame, 331, 546, "ADDRESS:", "white", "#0C385E", ("Century Gothic", 16, 'bold'))
    address_line1_label = gui.label_design(frame, 331, 587, "Address Line 1", "white", "#0C385E", ("Century Gothic", 12, 'bold'))
    address_line2_label = gui.label_design(frame, 331, 660, "Address Line 2", "white", "#0C385E", ("Century Gothic", 12, 'bold'))
    city_municipality_label = gui.label_design(frame, 331, 734, "City/Municipality", "white", "#0C385E", ("Century Gothic", 12, 'bold'))
    state_province_label = gui.label_design(frame, 680, 734, "State/Province", "white", "#0C385E", ("Century Gothic", 12, 'bold'))
    country_label = gui.label_design(frame, 331, 807, "Country", "white", "#0C385E", ("Century Gothic", 12, 'bold'))
    zip_code_label = gui.label_design(frame, 680, 807, "Zip Code", "white", "#0C385E", ("Century Gothic", 12, 'bold'))
    contact_info_label = gui.label_design(frame, 322, 927, "CONTACT INFO:", "#1E6CAB", "white", ("Century Gothic", 16, 'bold'))
    other_social_media_label = gui.label_design(frame, 322, 962, "Other (Social Media)", "#1E6CAB", "white", ("Century Gothic", 12, 'bold'))
    social_media_id_label = gui.label_design(frame, 664, 962, "Social Media Account ID/No.", "#1E6CAB", "white", ("Century Gothic", 12, 'bold'))
    first_name_label = gui.label_design(frame, 1047, 126, "First Name", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    middle_name_label = gui.label_design(frame, 1047, 198, "Middle Name", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    last_name_label = gui.label_design(frame, 1047, 270, "Last Name", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    suffix_label = gui.label_design(frame, 1047, 343, "Suffix", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    civil_status_label = gui.label_design(frame, 1047, 415, "Civil Status", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    date_of_birth_label = gui.label_design(frame, 1450, 130, "Date of Birth", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    gender_label = gui.label_design(frame, 1450, 220, "Gender", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    nationality_label = gui.label_design(frame, 1450, 311, "Nationality", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    employee_number_label = gui.label_design(frame, 1450, 396, "Employee Number", "white", "#0C385E", ("Century Gothic", 14, 'bold'))
    # Adding the needed entries
    Email = gui.entry_design(frame, 698, 220, 266, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Contact_Number = gui.entry_design(frame, 698, 298, 266, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Picture_Path = gui.entry_design(frame, 333, 614, 258, 34, "#E4F0FC", "#E4F0FC", ("Century Gothic", 10), "#E4F0FC", "#E4F0FC")
    Address_Line_1 = gui.entry_design(frame, 333, 614, 655, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Address_Line_2 = gui.entry_design(frame, 333, 687, 655, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    City_Municipality = gui.entry_design(frame, 333, 760, 332, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    State_Province = gui.entry_design(frame, 682, 760, 308, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Country = gui.entry_design(frame, 333, 833, 332, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Zip_Code = gui.entry_design(frame, 682, 833, 308, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Other_Social_Media = gui.entry_design(frame, 324, 990, 332, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Social_Media_Account_Id = gui.entry_design(frame, 666, 990, 328, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    First_Name = gui.entry_design(frame, 1049, 156, 341, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Middle_Name = gui.entry_design(frame, 1049, 228, 341, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Last_Name = gui.entry_design(frame, 1049, 301, 341, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Suffix = gui.entry_design(frame, 1049, 373, 341, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Civil_Status = gui.entry_design(frame, 1049, 445, 341, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Date_of_Birth = gui.entry_design(frame, 1452, 169, 258, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Gender = gui.entry_design(frame, 1452, 260, 258, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Nationality = gui.entry_design(frame, 1452, 345, 258, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    Employee_Number = gui.entry_design(frame, 1452, 435, 258, 34, "white", "#0C385E", ("Century Gothic", 10), "#0C385E", "#0C385E")
    # Company Logo
    company_logo = Label(frame, image=images['company_logo'])
    company_logo.place(x=699, y=357)
    company_logo.config(borderwidth=0)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             ADDING THE A FUNCTION THAT AUTOMATICALLY PUT INPUTS ONCE LOG IN
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def populate_user_info(username): # For needed input once logIn
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Username=?", (username,))
        user = cursor.fetchone()
        if user:
            info =[Email, Contact_Number, First_Name, Middle_Name, Last_Name, Suffix, Civil_Status, Date_of_Birth, Gender, Nationality, Employee_Number, Address_Line_1, Address_Line_2, City_Municipality,
                   State_Province, Country, Zip_Code, Other_Social_Media, Social_Media_Account_Id]
            for i in range(19):
                info[i].delete(0, 'end')
            Email.insert(0, user[15])
            Contact_Number.insert(0, user[14])
            Address_Line_1.insert(0, user[18])
            Address_Line_2.insert(0, user[19])
            City_Municipality.insert(0, user[20])
            State_Province.insert(0, user[21])
            Country.insert(0, user[22])
            Zip_Code.insert(0, user[23])
            Other_Social_Media.insert(0, user[16])
            Social_Media_Account_Id.insert(0, user[17])
            First_Name.insert(0, user[0])
            Middle_Name.insert(0, user[1])
            Last_Name.insert(0, user[2])
            Suffix.insert(0, user[3])
            Civil_Status.insert(0, user[7])
            Date_of_Birth.insert(0, user[4])
            Gender.insert(0, user[5])
            Nationality.insert(0, user[6])
            Employee_Number.insert(0, user[13])
            Employee_Number.config(state='readonly')
            Picture_Path.insert(0, user[24])
            image_data = user[52]
            with BytesIO(image_data) as image:
                images = {}
                images['employee_image'] = ImageTk.PhotoImage(Image.open(image).resize((137, 137)))
                images['employee_image2'] = ImageTk.PhotoImage(Image.open(image).resize((295, 295)))
                employee_image = Label(frame, image=images['employee_image'])
                employee_image.image = images['employee_image']  # Keep a reference to the image
                employee_image.place(x=60, y=60)
                employee_image2 = Label(frame, image=images['employee_image2'])
                employee_image2.image = images['employee_image2']  # Keep a reference to the image
                employee_image2.place(x=358, y=154)
            full_name = f"{user[0]} {user[2]}"
            employee_name_label = gui.label_design(frame, 2, 217, f"{full_name}", "#1968A4", "white", ("Century Gothic", 14, 'bold'))
            employee_name_label.config(width=23, height=0)
            employee_name_label2 = gui.label_design(frame, 696, 151, f"{full_name}", "#1E6CAB", "white", ("Century Gothic", 14, 'bold'))
        else:
            messagebox.showerror("Error", "User not found in the database.")
    populate_user_info(username)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               ADDING FUNCTIONS AND BOTTONS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def loadData():  # For Choose File Button
        global photo
        filename = filedialog.askopenfilename(initialdir="", title="Choose File", filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")))
        chosen_image = gui.image1_design(frame, 358, 154, filename, 295, 295)
        Picture_Path.insert(0, filename)
    change_profile_button = gui.button_design(frame, 698, 425, 164, 36, "#0C385E", "white", "Change Profile", ("Century Gothic", 13))
    change_profile_button.config(command=loadData)
    def updateData():  # For Save Button
        image_path = Picture_Path.get()
        employee_number = Employee_Number.get()
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Employee_Number=?", (employee_number,))
        cursor.execute("SELECT * FROM I_employee_personal_information_tbl WHERE Employee_Number=?", (employee_number,))
        record = cursor.fetchone()
        if not record:
            messagebox.showerror("Error", "Employee not found!")
            return
        with open(image_path, 'rb') as file:
            image_data = file.read()
        query1 = """UPDATE main_employee_information_tbl SET Email=?, Contact_Number=?, First_Name=?, Middle_Name=?, Last_Name=?, Suffix=?, Civil_Status=?, Date_of_Birth=?, Gender=?, 
                                                                     Nationality=?, Address_Line_1=?, Address_Line_2=?, City_Municipality=?, State_Province=?, Country=?, Zip_Code=?, 
                                                                     Other_Social_Media=?, Social_Media_Account_Id=?, Picture_Path=?, image_data=? WHERE Employee_Number=?"""
        query2 = """UPDATE I_employee_personal_information_tbl SET Email=?, Contact_Number=?, First_Name=?, Middle_Name=?, Last_Name=?, Suffix=?, Civil_Status=?, Date_of_Birth=?, Gender=?, 
                                                                     Nationality=?, Address_Line_1=?, Address_Line_2=?, City_Municipality=?, State_Province=?, Country=?, Zip_Code=?, 
                                                                     Other_Social_Media=?, Social_Media_Account_Id=?, Picture_Path=? WHERE Employee_Number=?"""
        query1_tuple = [Email.get(), Contact_Number.get(), First_Name.get(), Middle_Name.get(), Last_Name.get(),Suffix.get(), Civil_Status.get(), Date_of_Birth.get(), Gender.get(), Nationality.get(),
                        Address_Line_1.get(), Address_Line_2.get(), City_Municipality.get(), State_Province.get(),Country.get(), Zip_Code.get(), Other_Social_Media.get(), Social_Media_Account_Id.get(),
                        Picture_Path.get(), image_data, employee_number]
        query2_tuple = [Email.get(), Contact_Number.get(), First_Name.get(), Middle_Name.get(), Last_Name.get(), Suffix.get(), Civil_Status.get(), Date_of_Birth.get(), Gender.get(), Nationality.get(),
                        Address_Line_1.get(), Address_Line_2.get(), City_Municipality.get(), State_Province.get(), Country.get(), Zip_Code.get(), Other_Social_Media.get(), Social_Media_Account_Id.get(),
                        Picture_Path.get(), employee_number]
        try:
            cursor.execute(query1, query1_tuple)
            cursor.execute(query2, query2_tuple)
            con.commit()
            messagebox.showinfo("Success", "Employee data updated successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def switch_to_profile_page():
        window.destroy()  # Close current window
        import _V_OOP_Profile_Page
        _V_OOP_Profile_Page.main(username)
    def switch_to_payroll_page():
        window.destroy()  # Close current window
        import _VI_OOP_Payroll_Page
        _VI_OOP_Payroll_Page.main(username)
    def switch_to_account_page():
        window.destroy()  # Close current window
        import _VII_OOP_Account_Page
        _VII_OOP_Account_Page.main(username)
    def switch_to_employee_or_admin_portal():  # For Logo Button
        cursor.execute("SELECT Employee_Number FROM main_employee_information_tbl WHERE Username=?", (username,))
        user = cursor.fetchone()
        if user:
            employee_number = user[-1]  # Assuming the Employee_Number is the first column in the database
            if employee_number == 20240000:
                window.destroy()
                import _III_OOP_Admin_Portal
                _III_OOP_Admin_Portal.main(username)
            else:
                window.destroy()
                import _IV_OOP_Employee_Portal
                _IV_OOP_Employee_Portal.main(username)
    def log_out(): # For LogOut Button
        window.destroy()
        import _II_OOP_Log_In_Page
    # Adding the needed buttons
    profile_image = ImageTk.PhotoImage(Image.open("Profile_Logo.png").resize((46, 51)))
    profile_button = gui.button_design(frame, 2, 311, 259, 64, "#2676AF", "white", " PROFILE", ("Century Gothic", 14, 'bold'))
    profile_button.config(image=profile_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#2676AF",  command=switch_to_profile_page)
    profile_indicate = tk.Label(frame, text="", bg="white")
    profile_indicate.place(x=255, y=311, width=5, height=64)
    payroll_image = ImageTk.PhotoImage(Image.open("Payroll_Logo.png").resize((51, 51)))
    payroll_button = gui.button_design(frame, 2, 380, 259, 64, "#2D7DB4", "white", "  PAYROLL", ("Century Gothic", 14, 'bold'))
    payroll_button.config(image=payroll_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#2D7DB4", command=switch_to_payroll_page)
    account_image = ImageTk.PhotoImage(Image.open("Account_Logo.png").resize((53, 51)))
    account_button = gui.button_design(frame, 2, 449, 259, 64, "#3484BB", "white", "  ACCOUNT", ("Century Gothic", 14, 'bold'))
    account_button.config(image=account_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#3484BB", command=switch_to_account_page)
    logo_image = ImageTk.PhotoImage(Image.open("UNIS_Logo.png").resize((199, 92)))
    logo_button = gui.button_design(frame, 2, 822, 259, 125, "#5AACDB", "white", "", ("Century Gothic", 12, 'bold'))
    logo_button.config(image=logo_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#5AACDB", command=switch_to_employee_or_admin_portal)
    UNIS_corporation_label = gui.label_design(frame, 61, 922, "UNIS Corporation", "#5AACDB", "white", ("Century Gothic", 11, 'bold'))
    log_out_image = ImageTk.PhotoImage(Image.open("Log_Out_Logo.png").resize((39, 32)))
    log_out_button = gui.button_design(frame, 2, 1001, 259, 79, "#5EB0DE", "white", "  Log Out", ("Century Gothic", 12, 'bold'))
    log_out_button.config(image=log_out_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#5EB0DE", command=log_out)
    Update_button = gui.button_design(frame, 866, 426, 94, 36, "#5AACDB", "white", "Update", ("Century Gothic", 13))
    Update_button.config(command=updateData)

    window.state('zoomed')  # Functionality to keep the page on auto-full screen
    window.mainloop()  # Start the GUI event loop