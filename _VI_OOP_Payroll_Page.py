# Main Programmer for this Page (GUI Design): Rabino, Kimberly Ann F.
# Sub Programmer for this Page (Functionalities): Porcare, Dana E.
import tkinter as tk # Importing tkinter module and renaming it as 'tk' for brevity
import sqlite3 # Importing sqlite3 module
from tkinter import * # Importing all classes and functions from tkinter module
from tkinter import Canvas, Scrollbar, messagebox # Importing Canvas, Scrollbar, and messagebox classes from tkinter module
from PIL import Image, ImageTk # Importing Image and ImageTk classes from PIL module
from io import BytesIO # Importing BytesIO from io module
from __OOP_Class import design_gui_interface # Importing design_gui_interface class from OOP_Class module
from __OOP_Calculations import EmployeePayroll # Importing EmployeePayroll class from OOP_Calculations module

def main(username):
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               SETTING UP THE WINDOW
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    window = tk.Tk()
    window.geometry("1920x1080")
    window.title("PAYROLL PAGE")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                              CALLING OR IMPORTING THE OOP_CLASS AND OOP_COMPUTATIONS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    my_gui_design = design_gui_interface()
    obj = EmployeePayroll()
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
#                                                                                    ADDING FRAMES INSIDE THE MAIN FRAME
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    picture_frame = my_gui_design.frame_design(frame, 57, 57, 147, 147, "#0C385E")
    employee_image = my_gui_design.image1_design(frame, 61, 61, "Profile_Picture.png", 140, 140)
    # Adding the needed label
    payroll_label = my_gui_design.label_design(frame, 303, 31, "Payroll", "#E4F0FC", "#0C385E", ('Century Gothic', 33, 'bold'))
    # Adding the needed frames
    my_gui_design.frame_design(frame,303, 102, 709, 402,  '#1e6cab')
    my_gui_design.frame_design(frame,1025, 102, 389, 402, 'white')
    my_gui_design.frame_design(frame,1427, 102, 303, 402, 'white')
    my_gui_design.frame_design(frame,1743, 102, 132, 402, '#1e6cab')
    my_gui_design.frame_design(frame,303, 518, 709, 398, 'white')
    my_gui_design.frame_design(frame,1025, 518, 849, 471, 'white')
    my_gui_design.frame_design(frame,303, 928, 709, 112, '#1e6cab')
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                            ADDING THE NEEDED CONTENTS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adding the needed images
    images = {}
    images['employee_image'] = ImageTk.PhotoImage(Image.open("Profile_Picture.png").resize((295, 295)))
    picture_frame = my_gui_design.frame_design(frame, 352, 148, 310, 310, "#0C385E")
    employee_image = Label(frame, image=images['employee_image'])
    employee_image.place(x=358, y=154)
    # Label
    EN_label = my_gui_design.label_design(frame,696,188, 'Employee Number', '#1e6cab', "white", ('Century Gothic', 14, 'bold'))
    Department_label = my_gui_design.label_design(frame,696, 336, 'Department', '#1e6cab', "white", ('Century Gothic', 14, 'bold'))
    # Entry
    Employee_Number = my_gui_design.entry_design(frame,698, 217, 217, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Department = my_gui_design.entry_design(frame,698, 366, 217, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # frame 3 label
    First_name_label = my_gui_design.label_design(frame, 1047, 126, 'First Name', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    Middle_name_label = my_gui_design.label_design(frame, 1047, 198, 'Middle Name', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    Surname_label = my_gui_design.label_design(frame, 1047, 270, 'Last Name', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    S_Label = my_gui_design.label_design(frame, 1047, 343, 'Suffix', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    Civil_status_label = my_gui_design.label_design(frame, 1047, 415, 'Civil Status', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    # entry
    First_Name = my_gui_design.entry_design(frame,1049, 156, 341, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Middle_Name = my_gui_design.entry_design(frame,1049, 228, 341, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Last_Name = my_gui_design.entry_design(frame,1049, 301, 341, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Suffix = my_gui_design.entry_design(frame,1049, 373, 341, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Civil_Status = my_gui_design.entry_design(frame,1049, 445, 341, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # frame 4 label
    Qualified_Dep_Status_label = my_gui_design.label_design(frame, 1450, 130, 'Qualified Dep. Status', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    Paydate_label = my_gui_design.label_design(frame, 1450, 220, 'Paydate', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    Employee_S_label = my_gui_design.label_design(frame, 1450, 311, 'Employee Status', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    Designation_label = my_gui_design.label_design(frame, 1450, 396, 'Designation', "white", "#1E6CAB", ('Century Gothic', 14, 'bold'))
    # entry
    Qualified_Dep_Status = my_gui_design.entry_design(frame,1452, 169, 260, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Paydate = my_gui_design.entry_design(frame,1452, 260, 260, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Employee_Status = my_gui_design.entry_design(frame,1452, 345,260, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Designation = my_gui_design.entry_design(frame,1452, 435,260, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # frame 5 label
    Basic_income_label = my_gui_design.label_design(frame, 323, 544, 'BASIC INCOME:', "white", "#1e6cab", ("Century Gothic", 16, "bold"))
    Rate1_label = my_gui_design.label_design(frame, 323, 586, 'Rate / Hour', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Cutoff1_label = my_gui_design.label_design(frame, 554, 586, ' No. of Hours/ Cut Off: ', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Income_Cut_label = my_gui_design.label_design(frame, 784, 586, 'Income/ Cut Off: ', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Honorarium_income_label = my_gui_design.label_design(frame, 323, 662, 'HONORARIUM INCOME:', "white", "#1e6cab", ("Century Gothic", 16, "bold"))
    Rate2_label = my_gui_design.label_design(frame, 323, 704, 'Rate / Hour', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Cutoff2_label = my_gui_design.label_design(frame, 554, 704, ' No. of Hours/ Cut Off: ', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Income2_Cut_label = my_gui_design.label_design(frame, 784, 704, 'Income/ Cut Off: ', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Other_income_label = my_gui_design.label_design(frame, 323, 781, 'OTHER INCOME:', "white", "#1e6cab", ("Century Gothic", 16, "bold"))
    Rate3_label = my_gui_design.label_design(frame, 323, 823, 'Rate / Hour', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Cutoff3_label = my_gui_design.label_design(frame, 554, 823, ' No. of Hours/ Cut Off: ', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Income3_Cut_label = my_gui_design.label_design(frame, 784, 823, 'Income/ Cut Off: ', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    # entry
    Rate_per_Hour1 = my_gui_design.entry_design(frame,325, 612, 204, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    No_of_Hours_per_Cut_Off1 = my_gui_design.entry_design(frame,556, 612, 204, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Income_per_Cut_Off1 = my_gui_design.entry_design(frame,786, 612, 204, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Rate_per_Hour2 = my_gui_design.entry_design(frame,325, 731, 204, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    No_of_Hours_per_Cut_Off2 = my_gui_design.entry_design(frame,556, 731, 204, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Income_per_Cut_Off2 = my_gui_design.entry_design(frame,786, 731, 204, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Rate_per_Hour3 = my_gui_design.entry_design(frame,325, 849, 204, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    No_of_Hours_per_Cut_Off3 = my_gui_design.entry_design(frame,556, 849, 204, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Income_per_Cut_Off3 = my_gui_design.entry_design(frame,786, 849, 204, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # frame7 label
    regular_label = my_gui_design.label_design(frame, 1059, 546, 'REGULAR DEDUCTIONS:', "white", "#1e6cab", ("Century Gothic", 16, "bold"))
    SSS_label = my_gui_design.label_design(frame, 1060, 591, 'SSS Contributions', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    PhilHealth_label = my_gui_design.label_design(frame, 1060, 642, 'PhilHealth Contribution', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Pagibig_label = my_gui_design.label_design(frame, 1461, 591, 'Pagibig Contribution', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Income_tax_label = my_gui_design.label_design(frame, 1461, 642, ' Income Tax Contribution', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    # entry
    SSS_Contibution = my_gui_design.entry_design(frame,1269, 583, 175, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    PhilHealth_Contibution = my_gui_design.entry_design(frame,1269, 656, 175, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    PagIbig_Contibution = my_gui_design.entry_design(frame,1667, 583, 175, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Income_Tax_Contibution = my_gui_design.entry_design(frame,1667, 656, 175, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # other deductions label
    Other_deductions_label = my_gui_design.label_design(frame, 1059, 690, 'OTHER DEDUCTIONS:', "white", "#1e6cab", ("Century Gothic", 16, "bold"))
    SSS_loan_label = my_gui_design.label_design(frame, 1060, 733, 'SSS Loan', "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    pagibig_label = my_gui_design.label_design(frame, 1060, 783, "Pagibig Loan", "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    faculty_deposit_label = my_gui_design.label_design(frame, 1060, 833, "Faculty Savings Deposit", "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    faculty_loan_label = my_gui_design.label_design(frame, 1461, 733, "Faculty Savings Loan ", "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Salary_loan_label = my_gui_design.label_design(frame, 1461, 783, "Salary Loan ", "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    other_loans_label = my_gui_design.label_design(frame, 1461, 833, "Other Loan", "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    # entry
    SSS_Loan = my_gui_design.entry_design(frame, 1269, 726, 175, 34, 'white', "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    PagIbig_Loan = my_gui_design.entry_design(frame, 1269, 777, 175, 34, 'white', "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Faculty_Saving_Deposit = my_gui_design.entry_design(frame, 1269, 827, 175, 34, 'white', "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Faculty_Saving_Loan = my_gui_design.entry_design(frame, 1667, 726, 175, 34, 'white', "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Salary_Loan = my_gui_design.entry_design(frame, 1667, 777, 175, 34, 'white', "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Other_Loan = my_gui_design.entry_design(frame, 1667, 827, 175, 34, 'white', "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # Deduction summary
    Deduction_summary_label = my_gui_design.label_design(frame, 1059, 886, "DEDUCTION SUMMARY: ", "white", "#1e6cab", ("Century Gothic", 16, "bold"))
    Total_deductions_label = my_gui_design.label_design(frame, 1060, 929, "Total Deductions", "white", "#1e6cab", ("Century Gothic", 12, "bold"))
    Total_Deductions = my_gui_design.entry_design(frame, 1269, 922, 175, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    # Summary Income
    Summary_income_label = my_gui_design.label_design(frame, 326, 953, 'SUMMARY INCOME:', "#1E6CAB", "white", ("Century Gothic", 16, "bold"))
    Gross_income_label = my_gui_design.label_design(frame, 326, 994, 'GROSS INCOME', "#1E6CAB", "white", ("Century Gothic", 12, "bold"))
    Net_income_label = my_gui_design.label_design(frame, 682, 994, ' NET INCOME', "#1E6CAB", "white", ("Century Gothic", 12, "bold"))
    # entry
    Gross_Income = my_gui_design.entry_design(frame, 474, 986, 189, 34, "white", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
    Net_Income = my_gui_design.entry_design(frame, 804, 986, 189, 34, "#DDDDDD", "#1e6cab", ('Century Gothic', 10, 'bold'), "#1e6cab", "#1e6cab")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                             ADDING THE A FUNCTION THAT AUTOMATICALLY PUT INPUTS ONCE LOG IN
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def populate_user_info(username): # For needed input once logIn
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Username=?", (username,))
        user = cursor.fetchone()
        if user:
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
            employee_name_label = my_gui_design.label_design(frame, 2, 217, f"{full_name}", "#1968A4", "white", ("Century Gothic", 14, 'bold'))
            employee_name_label.config(width=23, height=0)
            employee_name_label2 = my_gui_design.label_design(frame, 696, 151, f"{full_name}", "#1E6CAB", "white", ("Century Gothic", 14, 'bold'))
        else:
            messagebox.showerror("Error", "User not found in the database.")
    populate_user_info(username)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               ADDING FUNCTIONS AND BOTTONS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def searchEmployee():  # For Search Button
        employee_number = Employee_Number.get()
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Employee_Number = ?",(employee_number,))
        employee = cursor.fetchone()
        if employee:
            info = [Department, First_Name, Middle_Name, Last_Name, Suffix, Civil_Status, Qualified_Dep_Status, Paydate, Employee_Status, Designation]
            for i in range(10):
                info[i].config(state='normal')
                info[i].delete(0, 'end')
            Department.insert(0, employee[8])
            First_Name.insert(0, employee[0])
            Middle_Name.insert(0, employee[1])
            Last_Name.insert(0, employee[2])
            Suffix.insert(0, employee[3])
            Civil_Status.insert(0, employee[7])
            Qualified_Dep_Status.insert(0, employee[10])
            Paydate.insert(0, employee[12])
            Employee_Status.insert(0, employee[11])
            Designation.insert(0, employee[9])
            info2 = [Department, First_Name, Middle_Name, Last_Name, Suffix, Civil_Status, Employee_Status, Designation]
            for i in range(8):
                info2[i].config(state='readonly')
        else:
            messagebox.showerror("Error", "Employee not found")
    def grossIncome():  # For Gross Income Button
        if not all([Rate_per_Hour1.get(), No_of_Hours_per_Cut_Off1.get()]):
            messagebox.showerror("Error", "Please fill in all required fields for basic income.")
            return
        elif not all([Rate_per_Hour2.get(), No_of_Hours_per_Cut_Off2.get()]):
            messagebox.showerror("Error", "Please fill in all required fields for honorarium income.")
            return
        elif not all([Rate_per_Hour3.get(), No_of_Hours_per_Cut_Off3.get()]):
            messagebox.showerror("Error", "Please fill in all required fields for other income.")
            return
        info = [Income_per_Cut_Off1, Income_per_Cut_Off2, Income_per_Cut_Off3, Gross_Income, SSS_Contibution, PhilHealth_Contibution, PagIbig_Contibution, Income_Tax_Contibution]
        for i in range(8):
            info[i].config(state='normal')
            info[i].delete(0, 'end')
        basic_income = obj.get_basic_income_data(float(Rate_per_Hour1.get()), float(No_of_Hours_per_Cut_Off1.get()))
        Income_per_Cut_Off1.insert(0, basic_income)
        honorarium_income = obj.get_honorarium_income_data(float(Rate_per_Hour2.get()), float(No_of_Hours_per_Cut_Off2.get()))
        Income_per_Cut_Off2.insert(0, honorarium_income)
        other_income = obj.get_other_income_data(float(Rate_per_Hour3.get()), float(No_of_Hours_per_Cut_Off3.get()))
        Income_per_Cut_Off3.insert(0, other_income)
        gross_income = obj.calculate_gross_income()
        Gross_Income.insert(0, gross_income)
        employee_gross_income = float(gross_income)
        SSS_contribution = obj.calculate_sss_contribution(employee_gross_income)
        SSS_Contibution.insert(0, SSS_contribution)
        PhilHealth_contribution = obj.calculate_philhealth_contribution(employee_gross_income)
        PhilHealth_Contibution.insert(0, PhilHealth_contribution)
        PagIBIG_contribution = obj.calculate_pagIBIG_contribution()
        PagIbig_Contibution.insert(0, PagIBIG_contribution)
        Income_Tax_contribution = obj.calculate_income_tax(employee_gross_income)
        Income_Tax_Contibution.insert(0, Income_Tax_contribution)
        info2 = [Income_per_Cut_Off1, Income_per_Cut_Off2, Income_per_Cut_Off3, Gross_Income, SSS_Contibution, PhilHealth_Contibution, PagIbig_Contibution, Income_Tax_Contibution]
        for i in range(8):
            info2[i].config(state='readonly')
    def netIncome():  # For Net Income Button
        if not all([SSS_Loan.get(), PagIbig_Loan.get(), Faculty_Saving_Deposit.get(), Faculty_Saving_Loan.get(), Salary_Loan.get(), Other_Loan.get()]):
            messagebox.showerror("Error", "Please fill in all required fields for other deductions.")
            return
        regular_deduction = obj.get_regular_deductions()
        other_deduction = obj.get_other_deductions(float(SSS_Loan.get()), float(PagIbig_Loan.get()), float(Faculty_Saving_Deposit.get()), float(Faculty_Saving_Loan.get()), float(Salary_Loan.get()), float(Other_Loan.get()))
        info = [Total_Deductions, Net_Income]
        for i in range(2):
            info[i].config(state='normal')
            info[i].delete(0, 'end')
        Total_deductions = obj.calculate_total_deductions()
        Total_Deductions.insert(0, Total_deductions)
        net_income = obj.calculate_net_income()
        Net_Income.insert(0, net_income)
        info2 = [Total_Deductions, Net_Income]
        for i in range(2):
            info2[i].config(state='readonly')
    def saveData():  # For Save Button
        employee_number = Employee_Number.get()
        cursor.execute("SELECT Employee_Number FROM main_employee_information_tbl WHERE Employee_Number = ?",(employee_number,))
        cursor.execute("SELECT Employee_Number FROM I_employee_personal_information_tbl WHERE Employee_Number=?", (employee_number,))
        result = cursor.fetchone()
        if result is None:
            messagebox.showerror("Error", "Employee number does not exist. Cannot Save Data.")
            return
        query1 = """INSERT INTO II_employee_payroll_information_tbl (Rate_per_Hour1, No_of_Hours_per_Cut_Off1, Income_per_Cut_Off1, Rate_per_Hour2, No_of_Hours_per_Cut_Off2, Income_per_Cut_Off2, Rate_per_Hour3,  
                                                                    No_of_Hours_per_Cut_Off3, Income_per_Cut_Off3, SSS_Contibution, PhilHealth_Contibution, PagIbig_Contibution, Income_Tax_Contibution, SSS_Loan,  
                                                                    PagIbig_Loan, Faculty_Saving_Deposit, Faculty_Saving_Loan, Salary_Loan, Other_Loan, Gross_Income, Total_Deductions, Net_Income, Employee_Number)  
                                                                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        query2 = """UPDATE main_employee_information_tbl SET Rate_per_Hour1=?, No_of_Hours_per_Cut_Off1=?, Income_per_Cut_Off1=?, Rate_per_Hour2=?, No_of_Hours_per_Cut_Off2=?, Income_per_Cut_Off2=?, 
                                                             Rate_per_Hour3=?, No_of_Hours_per_Cut_Off3=?, Income_per_Cut_Off3=?, SSS_Contibution=?, PhilHealth_Contibution=?, PagIbig_Contibution=?, 
                                                             Income_Tax_Contibution=?, SSS_Loan=?, PagIbig_Loan=?, Faculty_Saving_Deposit=?, Faculty_Saving_Loan=?, Salary_Loan=?, Other_Loan=?, 
                                                             Gross_Income=?, Total_Deductions=?, Net_Income=?, Qualified_Dep_Status=?, Paydate=? WHERE Employee_Number=?"""
        query3 = """UPDATE main_employee_information_tbl SET Qualified_Dep_Status=?, Paydate=? WHERE Employee_Number=?"""
        query1_tuple = [Rate_per_Hour1.get(), No_of_Hours_per_Cut_Off1.get(), Income_per_Cut_Off1.get(), Rate_per_Hour2.get(), No_of_Hours_per_Cut_Off2.get(), Income_per_Cut_Off2.get(), Rate_per_Hour3.get(),
                        No_of_Hours_per_Cut_Off3.get(), Income_per_Cut_Off3.get(), SSS_Contibution.get(), PhilHealth_Contibution.get(), PagIbig_Contibution.get(), Income_Tax_Contibution.get(), SSS_Loan.get(),
                        PagIbig_Loan.get(), Faculty_Saving_Deposit.get(), Faculty_Saving_Loan.get(), Salary_Loan.get(), Other_Loan.get(), Gross_Income.get(), Total_Deductions.get(), Net_Income.get(),
                        Employee_Number.get()]
        query2_tuple = [Rate_per_Hour1.get(), No_of_Hours_per_Cut_Off1.get(), Income_per_Cut_Off1.get(), Rate_per_Hour2.get(), No_of_Hours_per_Cut_Off2.get(), Income_per_Cut_Off2.get(), Rate_per_Hour3.get(),
                        No_of_Hours_per_Cut_Off3.get(), Income_per_Cut_Off3.get(), SSS_Contibution.get(), PhilHealth_Contibution.get(), PagIbig_Contibution.get(), Income_Tax_Contibution.get(), SSS_Loan.get(),
                        PagIbig_Loan.get(), Faculty_Saving_Deposit.get(), Faculty_Saving_Loan.get(), Salary_Loan.get(), Other_Loan.get(), Gross_Income.get(), Total_Deductions.get(), Net_Income.get(),
                        Qualified_Dep_Status.get(), Paydate.get(), employee_number]
        query3_tuple = [Qualified_Dep_Status.get(), Paydate.get(), employee_number]
        if not all(query1_tuple):
            messagebox.showerror("Error", "Fill in all of the Information")
            return
        try:
            cursor.execute(query1, query1_tuple)
            cursor.execute(query2, query2_tuple)
            cursor.execute(query3, query3_tuple)
            con.commit()
            messagebox.showinfo("Success", "Data Saved Successfully")
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Data must be Saved Already. Try the Update Button")
    def updateData():  # For Update Button
        employee_number = Employee_Number.get()
        if not employee_number:
            messagebox.showerror("Error", "Employee Number is required")
            return
        cursor.execute("SELECT * FROM main_employee_information_tbl WHERE Employee_Number=?", (employee_number,))
        record_main = cursor.fetchone()
        cursor.execute("SELECT * FROM I_employee_personal_information_tbl WHERE Employee_Number=?", (employee_number,))
        record_personal = cursor.fetchone()
        cursor.execute("SELECT * FROM II_employee_payroll_information_tbl WHERE Employee_Number=?", (employee_number,))
        record_payroll = cursor.fetchone()
        if not record_main or not record_personal or not record_payroll:
            messagebox.showerror("Error", "Employee number does not exist. Cannot Update Data.")
            return
        query4 = """UPDATE II_employee_payroll_information_tbl SET Rate_per_Hour1=?, No_of_Hours_per_Cut_Off1=?, Income_per_Cut_Off1=?, Rate_per_Hour2=?, No_of_Hours_per_Cut_Off2=?, Income_per_Cut_Off2=?, 
                                                                   Rate_per_Hour3=?, No_of_Hours_per_Cut_Off3=?, Income_per_Cut_Off3=?, SSS_Contibution=?, PhilHealth_Contibution=?, PagIbig_Contibution=?, 
                                                                   Income_Tax_Contibution=?, SSS_Loan=?, PagIbig_Loan=?, Faculty_Saving_Deposit=?, Faculty_Saving_Loan=?, Salary_Loan=?, Other_Loan=?, 
                                                                   Gross_Income=?, Total_Deductions=?, Net_Income=? WHERE Employee_Number=?"""
        query5 = """UPDATE main_employee_information_tbl SET Qualified_Dep_Status=?, Paydate=? WHERE Employee_Number=?"""
        query6 = """UPDATE main_employee_information_tbl SET Rate_per_Hour1=?, No_of_Hours_per_Cut_Off1=?, Income_per_Cut_Off1=?, Rate_per_Hour2=?, No_of_Hours_per_Cut_Off2=?, Income_per_Cut_Off2=?, 
                                                             Rate_per_Hour3=?, No_of_Hours_per_Cut_Off3=?, Income_per_Cut_Off3=?, SSS_Contibution=?, PhilHealth_Contibution=?, PagIbig_Contibution=?, 
                                                             Income_Tax_Contibution=?, SSS_Loan=?, PagIbig_Loan=?, Faculty_Saving_Deposit=?, Faculty_Saving_Loan=?, Salary_Loan=?, Other_Loan=?, 
                                                             Gross_Income=?, Total_Deductions=?, Net_Income=?, Qualified_Dep_Status=?, Paydate=? WHERE Employee_Number=?"""
        query4_tuple = [Rate_per_Hour1.get(), No_of_Hours_per_Cut_Off1.get(), Income_per_Cut_Off1.get(), Rate_per_Hour2.get(), No_of_Hours_per_Cut_Off2.get(), Income_per_Cut_Off2.get(), Rate_per_Hour3.get(),
                        No_of_Hours_per_Cut_Off3.get(), Income_per_Cut_Off3.get(), SSS_Contibution.get(), PhilHealth_Contibution.get(), PagIbig_Contibution.get(), Income_Tax_Contibution.get(), SSS_Loan.get(),
                        PagIbig_Loan.get(), Faculty_Saving_Deposit.get(), Faculty_Saving_Loan.get(), Salary_Loan.get(), Other_Loan.get(), Gross_Income.get(), Total_Deductions.get(), Net_Income.get(), employee_number]
        query5_tuple = [Qualified_Dep_Status.get(), Paydate.get(), employee_number]
        query6_tuple = [Rate_per_Hour1.get(), No_of_Hours_per_Cut_Off1.get(), Income_per_Cut_Off1.get(), Rate_per_Hour2.get(), No_of_Hours_per_Cut_Off2.get(), Income_per_Cut_Off2.get(), Rate_per_Hour3.get(),
                        No_of_Hours_per_Cut_Off3.get(), Income_per_Cut_Off3.get(), SSS_Contibution.get(), PhilHealth_Contibution.get(), PagIbig_Contibution.get(), Income_Tax_Contibution.get(), SSS_Loan.get(),
                        PagIbig_Loan.get(), Faculty_Saving_Deposit.get(), Faculty_Saving_Loan.get(), Salary_Loan.get(), Other_Loan.get(), Gross_Income.get(), Total_Deductions.get(), Net_Income.get(),
                        Qualified_Dep_Status.get(), Paydate.get(), employee_number]
        if not all(query4_tuple) or not all(query6_tuple):
            messagebox.showerror("Error", "Fill in all of the Information")
            return
        try:
            cursor.execute(query4, query4_tuple)
            cursor.execute(query5, query5_tuple)
            cursor.execute(query6, query6_tuple)
            con.commit()
            messagebox.showinfo("Success", "Employee data updated successfully!")
        except Exception:
            messagebox.showerror("Error", "Employee number does not exist. Cannot Update Data.")
    def newData():  # For New Button
        info = [Department, First_Name, Middle_Name, Last_Name, Suffix, Civil_Status, Qualified_Dep_Status, Paydate, Employee_Status, Designation, Rate_per_Hour1, No_of_Hours_per_Cut_Off1, Income_per_Cut_Off1,
                Rate_per_Hour2, No_of_Hours_per_Cut_Off2, Income_per_Cut_Off2, Rate_per_Hour3, No_of_Hours_per_Cut_Off3, Income_per_Cut_Off3, SSS_Contibution, PhilHealth_Contibution, PagIbig_Contibution, Income_Tax_Contibution,
                SSS_Loan, PagIbig_Loan, Faculty_Saving_Deposit, Faculty_Saving_Loan, Salary_Loan, Other_Loan, Gross_Income, Total_Deductions, Net_Income]
        for i in range(32):
            info[i].config(state='normal')
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
    # Buttons
    profile_image = ImageTk.PhotoImage(Image.open("Profile_Logo.png").resize((46, 51)))
    profile_button = my_gui_design.button_design(frame, 2, 311, 259, 64, "#2676AF", "white", " PROFILE", ("Century Gothic", 14, 'bold'))
    profile_button.config(image=profile_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#2676AF",  command=switch_to_profile_page)
    payroll_image = ImageTk.PhotoImage(Image.open("Payroll_Logo.png").resize((51, 51)))
    payroll_button = my_gui_design.button_design(frame, 2, 380, 259, 64, "#2D7DB4", "white", "  PAYROLL", ("Century Gothic", 14, 'bold'))
    payroll_button.config(image=payroll_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#2D7DB4", command=switch_to_payroll_page)
    payroll_indicate = tk.Label(frame, text="", bg="white")
    payroll_indicate.place(x=255, y=380, width=5, height=64)
    account_image = ImageTk.PhotoImage(Image.open("Account_Logo.png").resize((53, 51)))
    account_button = my_gui_design.button_design(frame, 2, 449, 259, 64, "#3484BB", "white", "  ACCOUNT", ("Century Gothic", 14, 'bold'))
    account_button.config(image=account_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#3484BB", command=switch_to_account_page)
    logo_image = ImageTk.PhotoImage(Image.open("UNIS_Logo.png").resize((199, 92)))
    logo_button = my_gui_design.button_design(frame, 2, 822, 259, 125, "#5AACDB", "white", "", ("Century Gothic", 12, 'bold'))
    logo_button.config(image=logo_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#5AACDB", command=switch_to_employee_or_admin_portal)
    UNIS_corporation_label = my_gui_design.label_design(frame, 61, 922, "UNIS Corporation", "#5AACDB", "white", ("Century Gothic", 11, 'bold'))
    log_out_image = ImageTk.PhotoImage(Image.open("Log_Out_Logo.png").resize((39, 32)))
    log_out_button = my_gui_design.button_design(frame, 2, 1001, 259, 79, "#5EB0DE", "white", "  Log Out", ("Century Gothic", 12, 'bold'))
    log_out_button.config(image=log_out_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#5EB0DE", command=log_out)
    search_button = my_gui_design.button_design(frame, 699, 277, 106, 36, "#0C385E", "white", "Search", ('Century Gothic', 13))
    search_button.config(command=searchEmployee)
    gross_income_button = my_gui_design.button_design(frame, 1132, 1001, 150, 36, "#1E6CAB", "white", "GROSS INCOME", ('Century Gothic', 13))
    gross_income_button.config(command=grossIncome)
    net_income_button = my_gui_design.button_design(frame, 1297, 1001, 130, 36, "#1E6CAB", "white", "NET INCOME", ('Century Gothic', 13))
    net_income_button.config(command=netIncome)
    save_button = my_gui_design.button_design(frame, 1442, 1001, 106, 36, "#5CABD7", "white", "SAVE", ('Century Gothic', 13))
    save_button.config(command=saveData)
    update_button = my_gui_design.button_design(frame, 1563, 1001, 106, 36, "#5CABD7", "white", "UPDATE", ('Century Gothic', 13))
    update_button.config(command=updateData)
    new_button = my_gui_design.button_design(frame, 1684, 1001, 106, 36, "#0C385E", "white", "NEW", ('Century Gothic', 13))
    new_button.config(command=newData)

    window.state('zoomed')  # Functionality to keep the page on auto-full screen
    window.mainloop()  # Start the GUI event loop