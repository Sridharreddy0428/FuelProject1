from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter as tk
import json,os

p = lambda:None
CwaDataToIotCore_json = 'D:/FuelProject/resources/parameters.json'
with open(CwaDataToIotCore_json) as f:
    json_data = f.read()
    #print(json_data)
    p.__dict__ = json.loads(json_data)
    f.close()

# UserId=p.UserId
# pump_name=p.pump_name
issues=p.Today_total_full_issues
transactions=p.Toatl_Transactions
Nozil_status=p.Nozil_status
# dispenser_No=p.dispenser_no
# Nozil_No=p.Nozil_no
# price=p.Price
# density=p.density
# Fuel=p.Fuel_type

UserId=None
pump_name=None
dispenser_No=None
Nozil_No=None
price=None
density=None
Fuel=None
 
# Login window
def login_window():
    # Create the window and set it to full screen
    login = Tk()
    login.title("Login")
    login.attributes('-fullscreen', True)
    login.configure(bg="white")

    # Load the logo image
    logo_image = Image.open("logo.png")

    # Resize the image to fit the window
    logo_image = logo_image.resize((300, 300), Image.ANTIALIAS)

    # Convert the image to a Tkinter PhotoImage
    logo_photo = ImageTk.PhotoImage(logo_image)

    # Create a label to display the logo
    logo_label = Label(login, image=logo_photo, bg="white")
    logo_label.pack(side=TOP, pady=10)

    # Create a frame for the login form
    login_frame = Frame(login, bg="white", padx=50, pady=10, bd=1, relief="solid")

    # Create the login form
    diplay_label = Label(login_frame, text="Enter login credentials", bg="white", font=("Arial", 16,"bold"),fg="blue")
    username_label = Label(login_frame, text="Username:", bg="white", font=("Arial", 16))
    password_label = Label(login_frame, text="Password:", bg="white", font=("Arial", 16))
    username_entry = Entry(login_frame, width=25, font=("Arial", 16))
    password_entry = Entry(login_frame, width=25, show="*", font=("Arial", 16))
    login_status_label = Label(login_frame, text="", bg="white", font=("Arial", 12))

    diplay_label.grid(row=0, column=1, pady=10)
    username_label.grid(row=1, column=0, pady=10)
    username_entry.grid(row=1, column=1)
    password_label.grid(row=2, column=0, pady=10)
    password_entry.grid(row=2, column=1)
    login_status_label.grid(row=4, columnspan=2, pady=10)

    def login_action():
        # Authenticate user credentials here
        if username_entry.get() == "admin" and password_entry.get() == "admin123":
            login.destroy()
            if UserId is None:
                dashboard_window1()
            else:
                dashboard_window()
        else:
            login_status_label.config(text="Invalid username or password",font=("Arial", 12,"bold"),fg="red")

    # Exit the application
    def exit_app():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            login.destroy()

    Button(login_frame, text="Login", bg="#0B5394", fg="white", font=("Arial", 12), command=login_action).grid(row=3, columnspan=2, pady=20)

    # # Add an exit button to quit the application
    # exit_button = Button(login, text="Exit", bg="red", fg="white", font=("Arial", 12), command=exit_app)
    # # exit_button.pack(side=TOP, anchor='ne')
    # exit_button.pack(side=BOTTOM, pady=10)
    # Pack the login form frame
    login_frame.pack() 

    login.mainloop()

#settings window
def settings_window():
    settings = Tk()
    settings.title("Settings")
    settings.attributes('-fullscreen', True)
    settings.configure(bg="white")
    
    # Create the Frames
    button_frame1 = Frame(settings, bg="white", padx=10, pady=10)
    
    def dashboard_page():
        settings.destroy()
        if UserId != None:
            dashboard_window()
        else:
            dashboard_window1()
    
    # Create the settings and logout buttons
    back_btn = Button(button_frame1, text="Back", bg="blue", fg="white", font=("Arial", 16),command=dashboard_page)
    logout_btn = Button(button_frame1, text="Logout", bg="red", fg="white", font=("Arial", 16), command=lambda: [settings.destroy(),login_window()])
    
    back_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame1.pack(side='top', anchor='ne')
    
    # Create a frame for the login form
    details_frame = Frame(settings, bg="white", padx=50, pady=90, bd=2, relief="solid")
    # Create the login form


    def validate_input(new_value):
        if len(new_value) > 20:
            messagebox.showerror("Error", "Input can only be up to 20 characters.")
            return False
        return True

    id_label = Label(details_frame, text="Login User id:", bg="white", font=("Arial", 18))
    id_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    #id_entry = Entry(details_frame, width=25, font=("Arial", 18))
    id_label.grid(row=0, column=0, pady=10)
    id_entry.grid(row=0, column=1)
    
    pumpname_label = Label(details_frame, text="pump_name:", bg="white", font=("Arial", 18))
    pumpname_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    # pumpname_entry = Entry(details_frame, width=25, font=("Arial", 18))
    pumpname_label.grid(row=1, column=0, pady=10)
    pumpname_entry.grid(row=1, column=1)
    
    dispenser_label = Label(details_frame, text="dispenser_no:", bg="white", font=("Arial", 18))
    #dispenser_entry = Entry(details_frame, width=25, font=("Arial", 18))
    dispenser_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    dispenser_label.grid(row=2, column=0, pady=10)
    dispenser_entry.grid(row=2, column=1)
    
    nozil_label = Label(details_frame, text="Nozil_No:", bg="white", font=("Arial", 18))
    #nozil_entry = Entry(details_frame, width=25, font=("Arial", 18))
    nozil_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    nozil_label.grid(row=3, column=0, pady=10)
    nozil_entry.grid(row=3, column=1)
    
    price_label = Label(details_frame, text="price:", bg="white", font=("Arial", 18))
    #price_entry = Entry(details_frame, width=25, font=("Arial", 18))
    price_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    price_label.grid(row=4, column=0, pady=10)
    price_entry.grid(row=4, column=1)
    
    density_label = Label(details_frame, text="density:", bg="white", font=("Arial", 18))
    #density_entry = Entry(details_frame, width=25, font=("Arial", 18))
    density_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    density_label.grid(row=5, column=0, pady=10)
    density_entry.grid(row=5, column=1)
    
    Fuel_label = Label(details_frame, text="Fuel Type:", bg="white", font=("Arial", 18))
    #Fuel_entry = Entry(details_frame, width=25, font=("Arial", 18))
    Fuel_entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
    Fuel_label.grid(row=6, column=0, pady=10)
    Fuel_entry.grid(row=6, column=1)
       
    def save_action():
        # save user data here
        global UserId,pump_name,dispenser_No,Nozil_No,price,density,Fuel
        UserId=id_entry.get()
        pump_name=pumpname_entry.get()
        dispenser_No=dispenser_entry.get()
        Nozil_No=nozil_entry.get()
        price=price_entry.get()
        density=density_entry.get()
        Fuel=Fuel_entry.get()
        print("id :{},pump_name : {},dispenser_No :{},Nozil_No : {},price : {},density {},Fuel : {}".format(UserId,pump_name,dispenser_No,Nozil_No,price,density,Fuel))
        if not all([UserId, pump_name, dispenser_No, Nozil_No, price, density, Fuel]):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        settings.destroy()
        dashboard_window()
        
    details_frame.pack()
    Button(details_frame, text="Save", bg="#0B5394", fg="white", font=("Arial", 16), command=save_action).grid(row=7, columnspan=2, pady=20)
    
#Fuel start window   
def start_fuel():
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    Nozil_status='Open'
    
    # Create the window and set it to full screen
    fuelPage = Tk()
    fuelPage.title("Fuel-Page-1")
    fuelPage.attributes('-fullscreen', True)
    fuelPage.configure(bg="white")
    
    # Create a frame to hold the buttons
    details_frame = Frame(fuelPage, bg="white", padx=10, pady=10, bd=1, relief="solid")
    pump_detail_frame = Frame(fuelPage, bg="white", padx=30, pady=10, bd=1, relief="solid")
    button_frame = Frame(fuelPage, bg="white", padx=10, pady=10)
    #Qr_frame = Frame(fuelPage, bg="white", padx=400, pady=60, bd=1, relief="solid")
    
    Qr_frame = tk.Frame(fuelPage, bg="white", padx=325, pady=60, bd=1, relief="solid")

    def settings():
        fuelPage.destroy()
        settings_window()
        
    # Create the settings and logout buttons
    settings_btn = Button(button_frame, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) #(command=settings)
    logout_btn = Button(button_frame, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [fuelPage.destroy(), login_window()])

    # Pack the buttons inside the frame
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame.pack(side='top', anchor='ne')
    
    userId_label = Label(fuelPage, text="Login User id : {} ".format(UserId), bg="white",bd=1, font=("Arial bold", 24),relief="solid")
    userId_label.pack(side="top", padx=40, pady=50)
    
    issue_label = Label(details_frame, text="Today Total Full issues : {} ".format(issues), bg="white",bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    issue_label.grid(row=0, column=0, padx=10, pady=10)

    transaction_label = Label(details_frame, text="Today Transactions : {} ".format(transactions), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    transaction_label.grid(row=0, column=1, padx=10, pady=10)

    nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    nozil_label.grid(row=0, column=2, padx=10, pady=10)
    
    details_frame.place(relx=0.25,rely=0.3)
        
    # create a frame for the labels
    details_frame = Frame(fuelPage)
    details_frame.pack(side=LEFT, padx=10, pady=5)
    
    # create the labels and add them to the frame
    headings = ['Pump Name: ', 'Dispenser No: ', 'Nozzle No: ', 'Price: ', 'Density: ', 'Fuel type: ']
    values = [pump_name,dispenser_No,Nozil_No,price,density,Fuel]
    
    for i in range(len(headings)):
        Label(pump_detail_frame, text=headings[i]+values[i],bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    details_label = Label(Qr_frame, text="Please Scan Vehicle Qr code", bg="white", font=("Arial", 16),relief="solid")
    details_label.pack(side="top", padx=1, pady=50)
    Qr_frame.place(relx=0.25, rely=0.45)

    # Schedule the function to run after 10 seconds
    fuelPage.after(15000, lambda: fuel_afterScan(fuelPage))
    
def fuel_afterScan(Page):
    Page.destroy()
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    
    # Create the window and set it to full screen
    fuel_afterScan = Tk()
    fuel_afterScan.title("Fuel-Page-after-scan-1")
    fuel_afterScan.attributes('-fullscreen', True)
    fuel_afterScan.configure(bg="white")
    
    # Create a frame to hold the buttons
    details_frame = Frame(fuel_afterScan, bg="white", padx=10, pady=10, bd=1, relief="solid")
    pump_detail_frame = Frame(fuel_afterScan, bg="white", padx=30, pady=10, bd=1, relief="solid")
    button_frame = Frame(fuel_afterScan, bg="white", padx=10, pady=10)
    #Qr_frame = Frame(fuelPage, bg="white", padx=400, pady=60, bd=1, relief="solid")
    
    afterScanDetails_frame = tk.Frame(fuel_afterScan, bg="white", padx=50, pady=30, bd=1, relief="solid")

    def settings():
        fuel_afterScan.destroy()
        settings_window()
        
    # Create the settings and logout buttons
    settings_btn = Button(button_frame, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) #(command=settings)
    logout_btn = Button(button_frame, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [fuel_afterScan.destroy(), login_window()])

    # Pack the buttons inside the frame
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame.pack(side='top', anchor='ne')
    
    userId_label = Label(fuel_afterScan, text="Login User id : {} ".format(UserId), bg="white",bd=1, font=("Arial bold", 24),relief="solid")
    userId_label.pack(side="top", padx=40, pady=50)
    
    issue_label = Label(details_frame, text="Today Total Full issues : {} ".format(issues), bg="white",bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    issue_label.grid(row=0, column=0, padx=10, pady=10)

    transaction_label = Label(details_frame, text="Today Transactions : {} ".format(transactions), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    transaction_label.grid(row=0, column=1, padx=10, pady=10)

    nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    nozil_label.grid(row=0, column=2, padx=10, pady=10)
    
    details_frame.place(relx=0.25,rely=0.3)
    
    # create the labels and add them to the frame
    headings = ['Pump Name: ', 'Dispenser No: ', 'Nozzle No: ', 'Price: ', 'Density: ', 'Fuel type: ']
    values = [pump_name,dispenser_No,Nozil_No,price,density,Fuel]
    
    for i in range(len(headings)):
        Label(pump_detail_frame, text=headings[i]+values[i],bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    headings1 = ['Vehicle No: ', 'name: ', 'Status: ', 'officer: ', 'Driver: ', 'Fuel type: ']
    values1 = ['01','MM boloro','officer /mtpool','officer name','driver name','diesel']
    headings2=['Total quota:','Available quota: ','Down: ','Tank Capacity: ','Current transactions: ','Transaction id: ']
    values2=['150','100','50','25 ltrs','25','--']
    
    for i in range(len(headings1)):
        Label(afterScanDetails_frame, text=headings1[i]+values1[i],bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=i, column=0, sticky="w", pady=6,padx=90)

    for j in range(len(headings2)):
        Label(afterScanDetails_frame, text=headings2[j]+values2[j],bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=j, column=4, sticky="w", pady=6,padx=90)

    afterScanDetails_frame.place(relx=0.25, rely=0.45)
       
    login_status_label = Label(afterScanDetails_frame, text="Started Filling", bg="white", font=("Arial bold", 16),fg='green')
    login_status_label.grid(row=j+2, columnspan=5, pady=10)
    fuel_afterScan.after(15000, lambda: completion_window())
    
    def completion_window():
        global Nozil_status
        login_status_label = Label(afterScanDetails_frame, text="Completed Filling", bg="white", font=("Arial bold", 16),fg='green')
        login_status_label.grid(row=j+2, columnspan=5, pady=10)
        Nozil_status="Close"
        nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
        nozil_label.grid(row=0, column=2, padx=10, pady=10)
        fuel_afterScan.after(15000, lambda: transactions_window(fuel_afterScan))    
   
def transactions_window(fuelPage):
    fuelPage.destroy()
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    # Create the window and set it to full screen
    transaction = Tk()
    transaction.title("Transactions")
    transaction.attributes('-fullscreen', True)
    transaction.configure(bg="white")
    
    # Create a frame to hold the buttons
    details_frame = Frame(transaction, bg="white", padx=10, pady=10, bd=1, relief="solid")
    pump_detail_frame = Frame(transaction, bg="white", padx=30, pady=10, bd=1, relief="solid")
    button_frame = Frame(transaction, bg="white", padx=10, pady=10)
    
    #Qr_frame = tk.Frame(transaction, bg="white", padx=325, pady=60, bd=1, relief="solid")

    def settings():
        transaction.destroy()
        settings_window()
        
    # Create the settings and logout buttons
    settings_btn = Button(button_frame, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) #(command=settings)
    logout_btn = Button(button_frame, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [transaction.destroy(), login_window()])

    # Pack the buttons inside the frame
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame.pack(side='top', anchor='ne')
    
    userId_label = Label(transaction, text="Login User id : {} ".format(UserId), bg="white",bd=1, font=("Arial bold", 24),relief="solid",wraplength=1000)
    userId_label.pack(side="top", padx=40, pady=50)
    
    issue_label = Label(details_frame, text="Today Total Full issues : {} ".format(issues), bg="white",bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    issue_label.grid(row=0, column=0, padx=10, pady=10)

    transaction_label = Label(details_frame, text="Today Transactions : {} ".format(transactions), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    transaction_label.grid(row=0, column=1, padx=10, pady=10)

    nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
    nozil_label.grid(row=0, column=2, padx=10, pady=10)
    
    details_frame.place(relx=0.25,rely=0.3)
        
    # create a frame for the labels
    details_frame = Frame(transaction)
    details_frame.pack(side=LEFT, padx=10, pady=5)

    # create the labels and add them to the frame
    headings = ['Pump Name: ', 'Dispenser No: ', 'Nozzle No: ', 'Price: ', 'Density: ', 'Fuel type: ']
    values = [pump_name,dispenser_No,Nozil_No,price,density,Fuel]
    
    for i in range(len(headings)):
        Label(pump_detail_frame, text=headings[i]+values[i],bg='white',bd=1,font=("Arial", 14),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    # Create a frame to hold the table
    table_frame = Frame(transaction,bg='white',bd=1,relief="solid")
    table_frame.pack(pady=50)
    
    # Define the headings and values for the table
    table_headings = ['Vehicle No', 'Name', 'Status', 'Officer', 'Driver', 'Total Quota', 'Available Quota', 'Down', 'Current transactions','Fuel Type']
    table_values = ['10', 'MM boloro', 'Officer / mt-pool', 'Officer name', 'Driver Name', '150', '100', '50','25','Diesel']
    
    # Create the grid lines for the table
    for i in range(len(table_headings)):
        for j in range(2):
            table_frame.grid_columnconfigure(i, weight=1)
            table_frame.grid_rowconfigure(j, weight=1)
            if j==0:
                Label(table_frame, text=table_headings[i], bg='white', font=("Arial", 14),bd=1, relief="solid",wraplength=125).grid(row=j, column=i, sticky='nsew')
            else:
                Label(table_frame, text=table_values[i], bg='white', font=("Arial", 14), bd=1,relief="solid",wraplength=150).grid(row=j, column=i, sticky='nsew')
    
    # Position the table in the center of the screen
    table_frame.place(relx=0.60, rely=0.60, anchor=CENTER)
    transaction.mainloop()

#Empty data dashboard window       
def dashboard_window1():
    # Create the window and set it to full screen
    dashboard1 = Tk()
    dashboard1.title("Dashboard")
    dashboard1.attributes('-fullscreen', True)
    dashboard1.configure(bg="white")
    button_frame1 = Frame(dashboard1, bg="white", padx=10, pady=10)
    Text_frame = Frame(dashboard1, bg="white", padx=250, pady=10, bd=1, relief="solid")
    
    def settings():
        dashboard1.destroy() 
        settings_window()
            
    # Create the settings and logout buttons
    settings_btn = Button(button_frame1, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) 
    logout_btn = Button(button_frame1, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [dashboard1.destroy(), login_window()])

    # Pack the buttons inside the frame
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame1.pack(side='top', anchor='ne')
    
    details_label = Label(Text_frame, text="Settings not available please set dispenser settings", bg="white", font=("Arial bold", 20))
    details_label.pack(side="top", padx=10, pady=250)
    
    Text_frame.place(relx=0.05, rely=0.15)
    
# Dashboard window
def dashboard_window():
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    # Create the window and set it to full screen
    dashboard = Tk()
    dashboard.title("Dashboard")
    dashboard.attributes('-fullscreen', True)
    dashboard.configure(bg="white")
    
    # Create a frame to hold the buttons
    details_frame = Frame(dashboard, bg="white", padx=10, pady=10, bd=1, relief="solid")
    pump_detail_frame = Frame(dashboard, bg="white", padx=30, pady=10, bd=1, relief="solid")
    button_frame = Frame(dashboard, bg="white", padx=10, pady=10)

    def settings():
        dashboard.destroy()
        settings_window()
    def fuel():
        dashboard.destroy()
        start_fuel()
        
    # Create the settings and logout buttons
    settings_btn = Button(button_frame, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) 
    logout_btn = Button(button_frame, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [dashboard.destroy(), login_window()])
    Button(dashboard, text="Start Fuel", bg="#0B5394", fg="white", font=("Arial", 12), command=fuel).pack(side=BOTTOM,pady=10)
    
    # Pack the buttons inside the frame    
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame.pack(side='top', anchor='ne')
    
    userId_label = Label(dashboard, text="Login User id : {} ".format(UserId), bg="white", bd=1, font=("Arial bold", 24),relief="solid")
    userId_label.pack(side="top", padx=40, pady=50)
    
    issue_label = Label(details_frame, text="Today Total Full issues : {} ".format(issues), bg="white", font=("Arial", 16),bd=1,relief="solid",wraplength=400)
    issue_label.grid(row=0, column=0, padx=10, pady=10)

    transaction_label = Label(details_frame, text="Today Transactions : {} ".format(transactions), bg="white", font=("Arial", 16),bd=1,relief="solid",wraplength=400)
    transaction_label.grid(row=0, column=1, padx=10, pady=10)

    nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", font=("Arial", 16),bd=1,relief="solid",wraplength=400)
    nozil_label.grid(row=0, column=2, padx=10, pady=10)
    
    details_frame.place(relx=0.25,rely=0.3)
        
    # create a frame for the labels
    details_frame = Frame(dashboard)
    details_frame.pack(side=LEFT, padx=10, pady=5)
    
    # create the labels and add them to the frame
    headings = ['Pump Name: ', 'Dispenser No: ', 'Nozzle No: ', 'Price: ', 'Density: ', 'Fuel type: ']
    values = [pump_name,dispenser_No,Nozil_No,price,density,Fuel]
    
    for i in range(len(headings)):
        Label(pump_detail_frame, text=headings[i]+values[i],bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    # Set up the promotion_frame and promotion_label as before
    promotion_frame = tk.Frame(dashboard, bg="white", padx=270, pady=60, bd=1, relief="solid")
    promotion_label = tk.Label(promotion_frame, text="Promotion Banner", bg="white", font=("Arial", 24))
    promotion_label.pack(side="top", padx=0, pady=50)
    promotion_frame.place(relx=0.25, rely=0.45)

    # Define a function to get a list of image filenames in a directory
    def get_image_filenames(dir):
        return [f for f in os.listdir(dir) if f.endswith(".jpg") or f.endswith(".PNG")]

    # Get a list of image filenames in the "images" directory
    image_filenames = get_image_filenames("images")
    
    if len(image_filenames)==0:
        promotion_label = Label(promotion_frame, text="Promotion Banner", bg="white", font=("Arial", 24))
        promotion_label.pack(side="top", padx=1, pady=0)
        promotion_frame.place(relx=0.30, rely=0.45)
    else:    
        # Create a label to display the images
        image_label = tk.Label(promotion_frame, height=20, width=600)
        image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Set the size of the image_label widget to match the size of the promotion_frame
        promotion_frame.update()
        image_label.config(height=promotion_frame.winfo_height()-10, width=promotion_frame.winfo_width()-15)

        # Define a function to update the image displayed in the label
        def update_image():
            # Get the next image filename in the list
            if update_image.index < len(image_filenames):
                filename = image_filenames[update_image.index]
            else:
                update_image.index = 0
                filename = image_filenames[update_image.index]
            
            # Load the image from the file
            image = tk.PhotoImage(file=os.path.join("images", filename))
            
            # Display the image in the label
            image_label.config(image=image)
            image_label.image = image
            
            # Increment the index and wrap around if necessary
            update_image.index = (update_image.index + 1) % len(image_filenames)
            
            # Schedule the next update after a delay of 2 seconds
            image_label.after(2000, update_image)

        # Set the initial image index to 0
        update_image.index = 0

        # Start the slideshow
        update_image()

    dashboard.mainloop()

if __name__=="__main__":
    # Start the application by showing the login window
    login_window()
