# Main Programmer for this Page (GUI Design and Class): Leonida, Love Joy G.
# Sub Programmer for this Page (Functionalities): Porcare, Dana E.
import tkinter as tk # Importing tkinter module and renaming it as 'tk' for brevity
import sqlite3 # Importing sqlite3 module
from tkinter import * # Importing all classes and functions from tkinter module
from tkinter import ttk # Importing ttk classes from tkinter module
from tkinter import Canvas, Scrollbar, filedialog, messagebox  # Importing Canvas, Scrollbar, filedialog, and messagebox classes from tkinter module
from tkcalendar import * # Importing all classes and functions from tkcalendar module
from PIL import Image, ImageTk # Importing Image and ImageTk classes from PIL module
from __OOP_Class import design_gui_interface # Importing design_gui_interface class from OOP_Class module

def main(username):
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                               SETTING UP THE WINDOW
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    window = tk.Tk()
    window.geometry("1920x1080") # Setting the size of the window
    window.title("INFORMATION PORTAL") # Setting the title of the window
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                          CONNECT THE DATEBASE FROM SQLITE3
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    con = sqlite3.connect("Employee_Data_db")
    cursor = con.cursor()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                             SETTING UP THE CLASS NEEDED
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    class DesignGUIInterface():
        # Method to create a title label
        def title(self, x, y):
            label = tk.Label(main_frame,bg='#065494', text="EMPLOYEE PERSONAL INFORMATION", fg='white' ,font=("Century Gothic", 50 ,"bold"))
            label.place(x=x, y=y)
            return label
        def frame1(self, x, y):
            # Function to create frames
            self.frame = Frame(main_frame, width=1482, height=278, border=0, bg='#e4f0fc')
            self.frame.place(x=x, y=y)
            return self.frame
        def frame2(self, x, y, width, bg, height):
            # Function to create second frame
            self.frame = Frame(main_frame, width=width, height=height, border=0, bg=bg)
            self.frame.place(x=x, y=y)
            return self.frame
        def frame3(self, x, y, width, bg, height):
            # Function to create second frame
            self.frame = Frame(main_frame, width=width, height=height, border=0, bg=bg)
            self.frame.place(x=x, y=y)
            return self.frame
        def image_design(self, image_location, x, y, length, width):
            # Function to display image
            self.length = length
            self.width = width
            self.image_location = image_location
            self.image = Image.open(image_location)
            self.bck_pic = ImageTk.PhotoImage(self.image.resize((length, width)))
            self.lbl = Label(window, image=self.bck_pic)
            self.lbl.place(x=x, y=y)
            return self.lbl
        def label_design1(self, x, y, text, font=("Century Gothic", 18, "bold"), bg='#e4f0fc', fg="#0C385E"):
            label = tk.Label(main_frame, text=text, font=font, bg=bg, fg=fg)
            label.place(x=x, y=y)
            return label
        def label_design2(self, x, y, text, font=("Century Gothic", 10, "bold"), bg='e4f0fc', fg='#0C385E'):
            label = tk.Label(main_frame, text=text, font=font, bg=bg, fg=fg)
            label.place(x=x, y=y)
            return label
        def label_design3(self, x, y, text, font=("Century Gothic", 24, "bold"), bg='#065494', fg="white"):
            label = tk.Label(main_frame, text=text, font=font, bg=bg, fg=fg)
            label.place(x=x, y=y)
            return label
        def textbox_design(self, x, y, width, bg="white", font=("Century Gothic", 16)):
            textbox = tk.Entry(main_frame, bg=bg, fg="#0C385E", font=font, relief=SOLID, bd=1, highlightbackground="#0C385E", highlightcolor="#0C385E", highlightthickness=0)
            textbox.place(x=x, y=y, width=width, height=55)
            return textbox
        def button_design(self, x, y, text, width, bg, fg, command):
            button = tk.Button(main_frame, text=text, width=width, bg=bg, fg=fg, command=command)
            button.place(x=x, y=y)
            return button
        def button_design2(self, x, y):
            button = tk.Button(main_frame, text="SEARCH", bg="#0C385E", width=9, fg="white")
            button.place(x=x, y=y)
            return button
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                          CALLING OR IMPORTING THE OOP_CLASS AND THE NEWLY BUILT CLASS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GUIDesign = DesignGUIInterface()
    gui = design_gui_interface()
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
    # Create a main frame inside the canvas
    main_frame = Frame(my_canvas, width=1600, height=2067, bg="#065494")
    my_canvas.create_window((160, 393), window=main_frame, anchor=tk.NW)
    # Function to adjust canvas size when resized
    def on_canvas_configure(event):
        main_frame.itemconfig(event, width=event.width, height=event.height, anchor='nw')
    # Configure vertical scrollbar to update scroll region
    scrollbar_y.bind('<Configure>', lambda event: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    # Bind scrollbar movement to canvas scrolling
    scrollbar_y.bind("<B1-Motion>", lambda event: my_canvas.yview("moveto", event.y / my_canvas.winfo_height()))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                    ADDING FRAMES INSIDE THE MY_CANVAS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    header_frame = Frame(my_canvas, width=1900, height=50, bg="#065494")
    my_canvas.create_window((2, 0), window=header_frame, anchor=tk.NW)
    frame = Frame(my_canvas, width=1535, height=474, bg="#0C385E")
    my_canvas.create_window((385, 2526), window=frame, anchor=tk.NW)
    last_frame = Frame(my_canvas, width=1920, height=120, bg="#0C385E")
    my_canvas.create_window((2, 2880), window=last_frame, anchor=tk.NW)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                            ADDING THE NEEDED CONTENTS
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Adding the needed label
    welcome_label = my_canvas.create_text(970, 250, text="Welcome to the Information Portal", font=("Century Gothic", 50), fill="white")
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
    # Adding the needed labels
    services_label = gui.label_design(frame, 75, 75, "SERVICES", "#0C385E", "white", ("Century Gothic", 25, 'bold'))
    contact_us_label = gui.label_design(frame, 268, 75, "CONTACT US", "#0C385E", "white", ("Century Gothic", 25, 'bold'))
    founders_label = gui.label_design(frame, 815, 75, "FOUNDERS", "#0C385E", "white", ("Century Gothic", 25, 'bold'))
    services_info_label = gui.label_design(frame, 75, 132, "Profile\nPayroll\nAccount", "#0C385E", "white", ("Century Gothic", 20))
    services_info_label.config(anchor='w', justify='left')
    contact_us_info_label = gui.label_design(frame, 268, 132, "Call the service desk for help with your\nIT requests, questions, and problems.\n    800-444-4444\n    helpdesk@unis.co.ph", "#0C385E", "white", ("Century Gothic", 20))
    contact_us_info_label.config(anchor='w', justify='left')
    founders_info_label = gui.label_design(frame, 815, 132, "meagan.ysabelle.cruz@adamson.edu.ph\nlove.joy.leonida@adamson.edu.ph\ndana.porcare@adamson.edu.ph\nkimberly.ann.rabino@adamson.edu.ph", "#0C385E", "white", ("Century Gothic", 20))
    founders_info_label.config(anchor='w', justify='left')
    copyright_label = gui.label_design(last_frame, 177, 17, "Copyright 2024, All rights reserved", "#0C385E", "white", ("Century Gothic", 26, 'bold'))
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                          ADDING CONFIGURATION STYLE FOR THE DATE ENTRY AND COMBO BOXES
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    style = ttk.Style()
    # Create a new style for the date entry fields
    style.configure('Custom.TEntry', bg="#FFEEF3", fg="#0C385E", font=("Century Gothic", 16, "bold"), relief=SOLID, bd=1, highlightbackground="#0C385E", highlightcolor="#0C385E", highlightthickness=0, fieldbackground="white")
    style.configure('Custom.TCombobox', bg="#FFEEF3", fg="#0C385E", font=("Century Gothic", 16, "bold"), relief=SOLID, bd=1, highlightbackground="#0C385E", highlightcolor="#0C385E", highlightthickness=0, fieldbackground="white")
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                    ADDING FRAMES INSIDE THE MAIN_FRAME
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    GUIDesign.title(x=230, y=70)
    GUIDesign.frame1(x=47, y=341)
    GUIDesign.frame1(x=47, y=648)
    GUIDesign.frame2(x=47, y=992, width=1482, height=280, bg='#e4f0fc')
    GUIDesign.frame3(x=47, y=1336, width=1482, height=616, bg='#e4f0fc')
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                        ADDING THE CONTENTS INSIDE THE FRAME 1 INCULDING THE PICTURE FRAME FOR THE EMPLOYEE'S PROFILE PICTURE
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    picture_frame = gui.frame_design(main_frame, 61, 207, 243, 243, "#0C385E")
    employee_profile_picture = gui.image1_design(main_frame, 70, 215, 'Profile_Picture.png', 226, 226)
    def loadData(): # For Choose File Button
        global photo
        filename       = filedialog.askopenfilename(initialdir="", title="Choose File", filetypes=(("JPG files", "*.jpg"), ("PNG files", "*.png")))
        chosen_image   = gui.image1_design(main_frame, 70, 215, filename, 226, 226)
        Picture_Path.insert(0, filename)
        Picture_Path.config(state='readonly')
        no_file_chosen_label.configure(text = "File Chosen")
    choose_file_button = gui.button_design(main_frame, 61, 465, 128,31, "#0C385E", "white", "Choose File", ('Century Gothic', 11, 'bold'))
    choose_file_button.config(command=loadData)
    no_file_chosen_label = gui.label_design(main_frame, 193, 465, 'No File Choosen', "#E4F0FC", "#0C385E", ("Century Gothic", 14, "bold"))
    # Display frame1 labels
    FirstNameLabel = GUIDesign.label_design1(355, 368, 'First Name')
    MiddleNameLabel = GUIDesign.label_design1(692, 368, 'Middle Name')
    LastNameLabel = GUIDesign.label_design1(982, 368, 'Last Name')
    Suffix = GUIDesign.label_design1(1309, 368, 'Suffix')
    # Create textboxes for frame1
    First_Name = GUIDesign.textbox_design(357, 400, 321)
    Middle_Name = GUIDesign.textbox_design(694, 400, 274)
    Last_Name = GUIDesign.textbox_design(984, 400, 318)
    Suffix = GUIDesign.textbox_design(1311, 400, 178)
    # Create the date of birth label and date entry field
    date_of_birth_label = gui.label_design(main_frame, 355, 484, "Date of Birth", "#E4F0FC", "#0C385E", ("Century Gothic", 16, "bold"))
    Date_of_Birth = DateEntry(main_frame, style='Custom.TEntry', date_pattern="dd/mm/yyyy")
    Date_of_Birth.place(x=357, y=514, width=367, height=55)
    # Create the gender label and combobox field
    gender_label = gui.label_design(main_frame, 741, 484, "Gender", "#E4F0FC", "#0C385E", ("Century Gothic", 16, "bold"))
    Gender = ttk.Combobox(main_frame, values=["--select one--", "Woman", "Man", "Transgender", "Non-binary"], style='Custom.TCombobox')
    Gender.place(x=743, y=514, width=272, height=55)  # Placing the combobox at specific coordinates
    Gender.current(0)
    # Create the nationality label and combobox field
    nationality_label = gui.label_design(main_frame, 1029, 484, "Nationality", "#E4F0FC", "#0C385E", ("Century Gothic", 16, "bold"))
    Nationality = ttk.Combobox(main_frame, values=["Filipino", "Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Anguillan", "Citizen of Antigua and Barbuda", "Argentine", "Armenian","Australian", "Austrian", "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi", "Barbadian", "Belarusian", "Belgian", "Belizean", "Beninese", "Bermudian","Bhutanese", "Bolivian", "Citizen of Bosnia and Herzegovina", "Botswanan", "Brazilian", "British", "British Virgin Islander", "Bruneian", "Bulgarian","Burkinan", "Burmese", "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean", "Cayman Islander", "Central African", "Chadian", "Chilean","Chinese", "Colombian", "Comoran", "Congolese", "Cook Islander", "Costa Rican", "Croatian", "Cuban", "Cymraes", "Cymro", "Cypriot", "Czech", "Danish","Djiboutian", "Dominican", "Citizen of the Dominican Republic", "Dutch", "East Timorese", "Ecuadorean", "Egyptian", "Emirati", "English", "Equatorial Guinean","Eritrean", "Estonian", "Ethiopian", "Faroese", "Fijian", "Finnish", "French", "Gabonese", "Gambian", "Georgian", "German", "Ghanaian", "Gibraltarian", "Greek","Greenlandic", "Grenadian", "Guamanian", "Guatemalan", "Citizen of Guinea-Bissau", "Guinean", "Guyanese", "Haitian", "Honduran", "Hong Konger", "Hungarian","Icelandic", "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican", "Japanese", "Jordanian", "Kazakh", "Kenyan","Kittitian", "Citizen of Kiribati", "Kosovan", "Kuwaiti", "Kyrgyz", "Lao", "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtenstein citizen", "Lithuanian","Luxembourger", "Macanese", "Macedonian", "Malagasy", "Malawian", "Malaysian", "Maldivian", "Malian", "Maltese", "Marshallese", "Martiniquais", "Mauritanian","Mauritian", "Mexican", "Micronesian", "Moldovan", "Monegasque", "Mongolian", "Montenegrin", "Montserratian", "Moroccan", "Mosotho", "Mozambican", "Namibian","Nauruan", "Nepalese", "New Zealander", "Nicaraguan", "Nigerian", "Nigerien", "Niuean", "North Korean", "Northern Irish", "Norwegian", "Omani", "Pakistani","Palauan", "Palestinian", "Panamanian", "Papua New Guinean", "Paraguayan", "Peruvian", "Pitcairn Islander", "Polish", "Portuguese", "Prydeinig", "Puerto Rican","Qatari", "Romanian", "Russian", "Rwandan", "Salvadorean", "Sammarinese", "Samoan", "Sao Tomean", "Saudi Arabian", "Scottish", "Senegalese", "Serbian","Citizen of Seychelles", "Sierra Leonean", "Singaporean", "Slovak", "Slovenian", "Solomon Islander", "Somali", "South African", "South Korean", "South Sudanese","Spanish", "Sri Lankan", "St Helenian", "St Lucian", "Stateless", "Sudanese", "Surinamese", "Swazi", "Swedish", "Swiss", "Syrian", "Taiwanese", "Tajik","Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian", "Tristanian", "Tunisian", "Turkish", "Turkmen", "Turks and Caicos Islander", "Tuvaluan", "Ugandan","Ukrainian", "Uruguayan", "Uzbek", "Vatican citizen", "Citizen of Vanuatu", "Venezuelan", "Vietnamese", "Vincentian", "Wallisian", "Welsh", "Yemeni", "Zambian","Zimbabwean"], style='Custom.TCombobox')
    Nationality.place(x=1031, y=514, width=178, height=55)  # Placing the combobox at specific coordinates
    Nationality.current(0)
    # Create the civil status label and combobox field
    civil_status_label = gui.label_design(main_frame, 1222, 484, "Civil Status", "#E4F0FC", "#0C385E", ("Century Gothic", 16, "bold"))
    Civil_Status = ttk.Combobox(main_frame, values=["--select one--", "Single", "Married", "Common-law married", "Separated", "Divorced", "Widowed"], style='Custom.TCombobox')
    Civil_Status.place(x=1224, y=514, width=273, height=55)  # Placing the combobox at specific coordinates
    Civil_Status.current(0)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                       ADDING THE CONTENTS INSIDE THE FRAME 2
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Display frame2 labels
    DepartmentLabel = GUIDesign.label_design1(82, 677, 'Department')
    DesignationLabel = GUIDesign.label_design1(800, 677, 'Designation')
    EmployeeStatusLabel = GUIDesign.label_design1(82, 788, 'Employee Status')
    EmployeeNumberLabel = GUIDesign.label_design1(1131, 788, 'Employee Number')
    # Create textboxes for frame2
    Department = GUIDesign.textbox_design(84, 710, 706)
    Designation = GUIDesign.textbox_design(802, 710, 342)
    Employee_Status = GUIDesign.textbox_design(84, 821, 848)
    Employee_Number = GUIDesign.textbox_design(1133, 821, 367)
    # Adding functionality to improve and decrease the errors of having similar Employee_Number to the data base
    cursor.execute('''SELECT MAX (Employee_Number) FROM main_employee_information_tbl''')
    Last_Employee_Number = cursor.fetchone()[0]
    if Last_Employee_Number is None or Last_Employee_Number == '':
        next_employee_number = 20240000
    else:
        next_employee_number = int(Last_Employee_Number) + 1
        Employee_Number.insert(0, next_employee_number)
        Employee_Number.config(state='readonly')
    Employee_Number.insert(0, next_employee_number)
    Employee_Number.config(state='readonly')
    # Create the qualified dep status label and combobox field
    QualifiedDepStatusLabel = GUIDesign.label_design1(1156, 677, 'Qualified Dep. Status')
    Qualified_Dep_Status = ttk.Combobox(main_frame, values=["--select one--","PhD", "Masters", "Post Graduate Diploma", "Bachelor's Degree", "Advance Diploma", "Diploma", "Higher Certificate"], style='Custom.TCombobox')
    Qualified_Dep_Status.place(x=1158, y=710, width=339, height=55)  # Placing the combobox at specific coordinates
    Qualified_Dep_Status.current(0)
    # Create the paydate label and date entry field
    PaydateLabel = GUIDesign.label_design1(939, 788, 'Paydate')
    Paydate = DateEntry(main_frame, style='Custom.TEntry', date_pattern="dd/mm/yy")
    Paydate.place(x=941, y=821, width=180, height=55)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                       ADDING THE CONTENTS INSIDE THE FRAME 3
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Display frame3 labels
    ContactInfo = GUIDesign.label_design3(52, 942, 'Contact Info')
    ContactNumber = GUIDesign.label_design1(82, 1021, 'Contact Number')
    EmailLabel = GUIDesign.label_design1(681, 1021, 'Email')
    SocialMediaAccountId = GUIDesign.label_design1(681, 1134, 'Social Media Account')
    # Create textboxes for frame3
    Contact_Number = GUIDesign.textbox_design(84, 1055, 581)
    Email = GUIDesign.textbox_design(683, 1055, 814)
    Social_Media_Account_Id = GUIDesign.textbox_design(683, 1167, 814)
    # Create the other social media label and combobox field
    OtherSocialMedia = GUIDesign.label_design1(82, 1134, 'Other Social Media')
    Other_Social_Media = ttk.Combobox(main_frame, values=["--select one--","Facebook", "Instagram", "Twitter", "LinkedIn", "Snapchat", "Pinterest", "Reddit", "TikTok", "Tumblr", "YouTube"], style='Custom.TCombobox')
    Other_Social_Media.place(x=84, y=1167, width=581, height=55)  # Placing the combobox at specific coordinates
    Other_Social_Media.current(0)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                       ADDING THE CONTENTS INSIDE THE FRAME 4
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # Display frame4 labels
    Address = GUIDesign.label_design3(52, 1286, 'Address')
    AddressLine1 = GUIDesign.label_design1(82, 1370, 'Address Line 1')
    AddressLine2 = GUIDesign.label_design1(82, 1482, 'Address Line 2')
    CityMunicipality = GUIDesign.label_design1(82, 1595, 'City/Municipality')
    StateProvince = GUIDesign.label_design1(800, 1595, 'State/Province')
    ZipCode = GUIDesign.label_design1(800, 1707, 'Zip Code')
    PicturePathLabel = GUIDesign.label_design1(82, 1816, 'Picture Path')
    # Create textboxes for frame4
    Address_Line_1 = GUIDesign.textbox_design(84, 1405, 1413)
    Address_Line_2 = GUIDesign.textbox_design(84, 1515, 1413)
    City_Municipality = GUIDesign.textbox_design(84, 1628, 703)
    State_Province = GUIDesign.textbox_design(802, 1628, 695)
    Zip_Code = GUIDesign.textbox_design(802, 1740, 695)
    Picture_Path = GUIDesign.textbox_design(82, 1848, 1413)
    # Create the country label and combobox field
    CountryLabel = GUIDesign.label_design1(82, 1707, 'Country')
    Country = ttk.Combobox(main_frame, values=["Philippines", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",  "Azerbaijan","Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan",  "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil","Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",  "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia","Comoros", "Congo", "Costa Rica",  "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador","Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",  "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",  "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",  "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",  "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",  "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",  "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",  "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Poland",  "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino",  "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",  "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",  "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",  "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"], style='Custom.TCombobox')
    Country.place(x=84, y=1740, width=703, height=55)  # Placing the combobox at specific coordinates
    Country.current(0)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                            ADDING THE QUERIES, FUNCTIONS, AND BOTTONS FOR THE DATABASE
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def saveData():  # For Save Button
        image_path = Picture_Path.get()
        Username = Employee_Number.get()
        Password = Contact_Number.get()
        with open(image_path, 'rb') as file:
            image_data = file.read()
        query1 = """INSERT INTO main_employee_information_tbl (First_Name, Middle_Name, Last_Name, Suffix, Date_of_Birth, Gender, Nationality, Civil_Status, Department, Designation, Qualified_Dep_Status, Employee_Status, 
                                                            Paydate, Employee_Number, Contact_Number, Email, Other_Social_Media, Social_Media_Account_Id, Address_Line_1, Address_Line_2, City_Municipality, State_Province, 
                                                            Country, Zip_Code, Picture_Path, Username, Password, image_data)
                                                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        query2 = """INSERT INTO I_employee_personal_information_tbl (First_Name, Middle_Name, Last_Name, Suffix, Date_of_Birth, Gender, Nationality, Civil_Status, Department, Designation, Qualified_Dep_Status, Employee_Status, 
                                                            Paydate, Employee_Number, Contact_Number, Email, Other_Social_Media, Social_Media_Account_Id, Address_Line_1, Address_Line_2, City_Municipality, State_Province, 
                                                            Country, Zip_Code, Picture_Path)
                                                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        query3 = """INSERT INTO III_employee_user_account_information_tbl (Username, Password, Employee_Number) VALUES (?,?,?)"""
        query1_tuple = [First_Name.get(), Middle_Name.get(), Last_Name.get(), Suffix.get(), Date_of_Birth.get(), Gender.get(), Nationality.get(), Civil_Status.get(), Department.get(), Designation.get(),
                        Qualified_Dep_Status.get(), Employee_Status.get(), Paydate.get(), Employee_Number.get(), Contact_Number.get(), Email.get(), Other_Social_Media.get(), Social_Media_Account_Id.get(),
                        Address_Line_1.get(), Address_Line_2.get(), City_Municipality.get(), State_Province.get(), Country.get(), Zip_Code.get(), Picture_Path.get(), Username, Password, image_data]
        query2_tuple = [First_Name.get(), Middle_Name.get(), Last_Name.get(), Suffix.get(), Date_of_Birth.get(), Gender.get(), Nationality.get(), Civil_Status.get(), Department.get(), Designation.get(),
                        Qualified_Dep_Status.get(), Employee_Status.get(), Paydate.get(), Employee_Number.get(), Contact_Number.get(), Email.get(), Other_Social_Media.get(), Social_Media_Account_Id.get(),
                        Address_Line_1.get(), Address_Line_2.get(), City_Municipality.get(), State_Province.get(), Country.get(), Zip_Code.get(), Picture_Path.get()]
        query3_tuple = [Username, Password, Employee_Number.get()]
        con.execute(query1, query1_tuple)
        con.execute(query2, query2_tuple)
        con.execute(query3, query3_tuple)
        con.commit()
        messagebox.showinfo("Success", "Data Saved Successfully")
    def cancelData(): # For Cancel Button
        Picture_Path.config(state='normal')
        info = [First_Name, Middle_Name, Last_Name, Suffix, Date_of_Birth, Department, Designation, Employee_Status, Paydate, Employee_Number, Contact_Number, Email, Social_Media_Account_Id, Address_Line_1, Address_Line_2,
                City_Municipality, State_Province, Zip_Code, Picture_Path]
        for  i in range(19):
            info[i].delete(0, 'end')
        Gender.current(0)
        Nationality.current(0)
        Civil_Status.current(0)
        Country.current(0)
        Other_Social_Media.current(0)
        Qualified_Dep_Status.current(0)
        no_file_chosen_label.configure(text='No File Chosen')
        gui.image1_design(main_frame, 70, 215,'Profile_Picture.png',226, 226)
    def back():
        window.destroy()
        import _III_OOP_Admin_Portal
        _III_OOP_Admin_Portal.main(username)
    # Adding the needed buttons
    back_image = ImageTk.PhotoImage(Image.open("Back_Logo.png").resize((39, 32)))
    back_button = gui.button_design(header_frame, 1690, 0, 210, 58, "#065494", "white", " Back",("Century Gothic", 21, 'bold'))
    back_button.config(image=back_image, compound=tk.LEFT, relief=tk.FLAT, activebackground="#065494", command=back)
    save_button = gui.button_design(main_frame, 52, 1976, 185,42, "#88DDDF", "#0C385E", "SAVE", ("Century Gothic", 17, 'bold')) # Create the save button
    save_button.config(command=saveData)
    cancel_button = gui.button_design(main_frame, 245, 1976, 185, 42, "#5FB2DF", "#0C385E", "CANCEL", ("Century Gothic", 17, 'bold')) # Create the cancel button
    cancel_button.config(command=cancelData)

    window.state('zoomed') # Functionality to keep the page on auto-full screen
    window.mainloop() # Start the GUI event loop