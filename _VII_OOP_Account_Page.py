# Main Programmer for this Page (GUI Design): Cruz, Meagan Ysabelle M.
# Sub Programmer for this Page (Functionalities): Porcare, Dana E.
import tkinter as tk  # Importing tkinter module and renaming it as 'tk' for brevity
import sqlite3  # Importing sqlite3 module
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
    window.geometry("1920x1080")
    window.title("ACCOUNT PAGE")
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
    background_image = Image.open("Portal2_Background.png")
    background_photo = ImageTk.PhotoImage(background_image)
    image_label = Label(frame, image=background_photo)
    image_label.pack()
    # Function to adjust canvas size when resized
    def on_canvas_configure(event):
        my_canvas.itemconfig(event, width=event.width, height=event.height, anchor='nw')
    # Configure vertical scrollbar to update scroll region
    scrollbar_y.bind('<Configure>', lambda event: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Bind scrollbar movement to canvas scrolling
    scrollbar_y.bind("<B1-Motion>", lambda event: my_canvas.yview("moveto", event.y / my_canvas.winfo_height()))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                            ADDING THE NEEDED CONTENTS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adding the needed frame for employee image and the needed label for employee name
    picture_frame = gui.frame_design(frame, 57, 57, 147, 147, "#0C385E")
    employee_name_label = gui.label_design(frame, 51, 217, "Employee Name", "#1968A4", "white", ("Century Gothic", 14, 'bold'))
    # Frames
    Frame2 = Frame(frame, width=411, height=402, bg="#2676AF").place(x=303, y=102)
    Frame3 = Frame(frame, width=1001, height=402, bg="#0C385E").place(x=727, y=102)
    Frame4 = Frame(frame, width=132, height=400, bg="#2676AF").place(x=1743, y=102)
    Frame5 = Frame(frame, width=1571, height=314, bg="white").place(x=303, y=520)
    # Labels
    AccountLabel = gui.label_design(frame, 303, 32, "Account", "#E4F0FC", "#0C385E", ("Century Gothic", 33, "bold"))
    # Images
    images = {}
    images['employee_image'] = ImageTk.PhotoImage(Image.open("Profile_Picture.png").resize((295, 295)))
    images['company_logo'] = ImageTk.PhotoImage(Image.open("UNIS_Logo4.png").resize((515, 237)))
    picture_frame = gui.frame_design(frame, 352, 148, 310, 310, "#0C385E")
    employee_image = Label(frame, image=images['employee_image'])
    employee_image.place(x=358, y=154)
    company_logo = Label(frame, image=images['company_logo'])
    company_logo.place(x=971, y=149)
    company_logo.config(borderwidth=0)
    # Labels
    UNIS_corporation_label2 = gui.label_design(frame, 1050, 391, "UNIS Corporation", "#0C385E", "white", ('Century Gothic', 31, 'bold'))
    FirstNameLabel = gui.label_design(frame, 340, 560, "First Name", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    MiddleNameLabel = gui.label_design(frame, 720, 560, "Middle Name", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    LastNameLabel = gui.label_design(frame, 1116, 560, "Last Name", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    SuffixLabel = gui.label_design(frame, 1504, 560, "Suffix", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    DepartmentLabel = gui.label_design(frame, 340, 640, "Department", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    DesignationLabel = gui.label_design(frame, 720, 640, "Designation", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    UsernameLabel = gui.label_design(frame, 1116, 640, "Username", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    PasswordLabel = gui.label_design(frame, 1504, 640, "Password", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    ConfirmPasswordLabel = gui.label_design(frame, 340, 720, "Confirm Password", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    UserTypeLabel = gui.label_design(frame, 720, 720, "User Type", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    UserStatusLabel = gui.label_design(frame, 1116, 720, "User Status", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    EmployeeNumberLabel = gui.label_design(frame, 1504, 720, "Employee Number", "white", "#2676AF", ("Century Gothic", 14, "bold"))
    #Entries
    First_Name = gui.entry_design(frame, 340, 590, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Middle_Name = gui.entry_design(frame, 720, 590, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Last_Name = gui.entry_design(frame, 1116, 590, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Suffix = gui.entry_design(frame, 1504, 590, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Department = gui.entry_design(frame, 340, 670, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Designation = gui.entry_design(frame, 720, 670, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Username = gui.entry_design(frame, 1116, 670, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Password = gui.entry_design(frame, 1504, 670, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Confirm_Password = gui.entry_design(frame, 340, 750, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    User_Type = gui.entry_design(frame, 720, 750, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    User_Status = gui.entry_design(frame, 1116, 750, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
    Employee_Number = gui.entry_design(frame, 1504, 750, 330, 30, "white", "#2676AF", ("Century Gothic", 12), "white", "white")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             ADDING THE A FUNCTION THAT AUTOMATICALLY PUT INPUTS ONCE LOG IN
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def populate_user_info(username): # For needed input once logIn
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Username=?", (username,))
        user = cursor.fetchone()
        if user:
            info = [First_Name, Middle_Name, Last_Name, Suffix, Department, Designation, Username, Password, Employee_Number]
            for i in range(9):
                info[i].delete(0, 'end')
            First_Name.insert(0, user[0])
            Middle_Name.insert(0, user[1])
            Last_Name.insert(0, user[2])
            Suffix.insert(0, user[3])
            Department.insert(0, user[8])
            Designation.insert(0, user[9])
            Username.insert(0, user[47])
            Password.insert(0, user[48])
            Employee_Number.insert(0, user[13])
            Employee_Number.config(state='readonly')
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
            if user[50] is not None:
                User_Type.delete(0, 'end')
                User_Type.insert(0, user[50])
            if user[51] is not None:
                User_Status.delete(0, 'end')
                User_Status.insert(0, user[51])
        else:
            messagebox.showerror("Error", "User not found in the database.")
    populate_user_info(username)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            ADDING THE QUERIES, FUNCTIONS, AND BOTTONS FOR THE DATABASE
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def updateData():  # For Update Button
        employee_number = Employee_Number.get()
        # Checking if password and confirm password are the same
        if Password.get() != Confirm_Password.get():
            messagebox.showerror("Error", "Passwords do not match!")
            return
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Employee_Number=?", (employee_number,))
        record_main = cursor.fetchone()
        cursor.execute("SELECT * FROM I_employee_personal_information_tbl WHERE Employee_Number=?", (employee_number,))
        record_personal = cursor.fetchone()
        cursor.execute("SELECT * FROM III_employee_user_account_information_tbl WHERE Employee_Number=?", (employee_number,))
        record_account = cursor.fetchone()
        if record_main and record_personal and record_account:
            query3 = """UPDATE main_employee_information_tbl SET First_Name=?, Middle_Name=?, Last_Name=?, Suffix=?, Department=?, Designation=?, Username=?, Password=?, 
                                                                 Confirm_Password=?, User_Type=?, User_Status=? WHERE Employee_Number=?"""
            query4 = """UPDATE main_employee_information_tbl SET First_Name=?, Middle_Name=?, Last_Name=?, Suffix=?, Department=?, Designation=? WHERE Employee_Number=?"""
            query5 = """UPDATE III_employee_user_account_information_tbl SET Username=?, Password=?, Confirm_Password=?, User_Type=?, User_Status=? WHERE Employee_Number=?"""
            query3_tuple = [First_Name.get(), Middle_Name.get(), Last_Name.get(), Suffix.get(), Department.get(), Designation.get(), Username.get(), Password.get(),
                            Confirm_Password.get(), User_Type.get(), User_Status.get(), employee_number]
            query4_tuple = [First_Name.get(), Middle_Name.get(), Last_Name.get(), Suffix.get(), Department.get(), Designation.get(), employee_number]
            query5_tuple = [Username.get(), Password.get(), Confirm_Password.get(), User_Type.get(), User_Status.get(), employee_number]
            cursor.execute(query3, query3_tuple)
            cursor.execute(query4, query4_tuple)
            cursor.execute(query5, query5_tuple)
            con.commit()
            messagebox.showinfo("Success", "Employee data updated successfully!")
        else:
            messagebox.showerror("Error", "Employee number does not exist. Cannot Update Data.")
    def deleteData():  # For Delete Button
        employee_number = Employee_Number.get()
        cursor.execute("DELETE FROM main_employee_information_tbl WHERE Employee_Number=?", (employee_number,))
        cursor.execute("DELETE FROM II_employee_payroll_information_tbl WHERE Employee_Number=?", (employee_number,))
        cursor.execute("DELETE FROM I_employee_personal_information_tbl WHERE Employee_Number=?", (employee_number,))
        cursor.execute("DELETE FROM III_employee_user_account_information_tbl WHERE Employee_Number=?", (employee_number,))
        con.commit()
        messagebox.showinfo("Success", "Employee data deleted successfully!")
        window.destroy()
    def cancelData(): # For Cancel Button
        info = [First_Name, Middle_Name, Last_Name, Suffix, Department, Designation, Username, Password, Confirm_Password, User_Type, User_Status]
        for i in range(11):
            info[i].delete(0, 'end')
    def switch_to_profile_page(): # For Profile Button
        window.destroy()  # Close current window
        import _V_OOP_Profile_Page
        _V_OOP_Profile_Page.main(username)
    def switch_to_payroll_page(): # For Payroll Button
        window.destroy()  # Close current window
        import _VI_OOP_Payroll_Page
        _VI_OOP_Payroll_Page.main(username)
    def switch_to_account_page(): # For Account Button
        window.destroy()  # Close current window
        import _VII_OOP_Account_Page
        _VII_OOP_Account_Page.main(username)
    def switch_to_employee_or_admin_portal(): # For Logo Button
        cursor.execute("SELECT Employee_Number FROM main_employee_information_tbl WHERE Username=?",(username,))
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
    profile_button.config(image=profile_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#2676AF", command=switch_to_profile_page)
    payroll_image = ImageTk.PhotoImage(Image.open("Payroll_Logo.png").resize((51, 51)))
    payroll_button = gui.button_design(frame, 2, 380, 259, 64, "#2D7DB4", "white", "  PAYROLL", ("Century Gothic", 14, 'bold'))
    payroll_button.config(image=payroll_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#2D7DB4", command=switch_to_payroll_page)
    account_image = ImageTk.PhotoImage(Image.open("Account_Logo.png").resize((53, 51)))
    account_button = gui.button_design(frame, 2, 449, 259, 64, "#3484BB", "white", "  ACCOUNT", ("Century Gothic", 14, 'bold'))
    account_button.config(image=account_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#3484BB", command=switch_to_account_page)
    account_indicate = tk.Label(frame, text="", bg="white")
    account_indicate.place(x=255, y=449, width=5, height=64)
    logo_image = ImageTk.PhotoImage(Image.open("UNIS_Logo.png").resize((199, 92)))
    logo_button = gui.button_design(frame, 2, 822, 259, 125, "#5AACDB", "white", "", ("Century Gothic", 12, 'bold'))
    logo_button.config(image=logo_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#5AACDB", command=switch_to_employee_or_admin_portal)
    UNIS_corporation_label = gui.label_design(frame, 61, 922, "UNIS Corporation", "#5AACDB", "white", ("Century Gothic", 11, 'bold'))
    log_out_image = ImageTk.PhotoImage(Image.open("Log_Out_Logo.png").resize((39, 32)))
    log_out_button = gui.button_design(frame, 2, 1001, 259, 79, "#5EB0DE", "white", "  Log Out",("Century Gothic", 12, 'bold'))
    log_out_button.config(image=log_out_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#5EB0DE",  command=log_out)
    update_button = gui.button_design(frame, 1486, 857, 118, 40, "#5CABD7", "white", "UPDATE", ("Century Gothic", 13))
    update_button.config(command=updateData)
    delete_button = gui.button_design(frame, 1621, 857, 118, 40, "#0C385E", "white", "DELETE", ("Century Gothic", 13))
    delete_button.config(command=deleteData)
    cancel_button = gui.button_design(frame, 1756, 857, 118, 40, "#1E6CAB", "white", "CANCEL", ("Century Gothic", 13))
    cancel_button.config(command=cancelData)

    window.state('zoomed')  # Functionality to keep the page on auto-full screen
    window.mainloop()  # Start the GUI event loop