from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import tkinter as tk
import json,os
import http.client
import requests

p = lambda:None
CwaDataToIotCore_json = './resources/parameters.json'
with open(CwaDataToIotCore_json) as f:
    json_data = f.read()
    p.__dict__ = json.loads(json_data)
    f.close()

issues=p.Today_total_full_issues
transactions=p.Toatl_Transactions
Nozil_status=p.Nozil_status
token=p.Token

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

    # Load the logo image & Create a label to display the logo
    logo_photo = PhotoImage(file="logo.png") 
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
        login_status,login_message=loginAuthentication()
        print(login_status,login_message)
        if login_status == 1 and login_message == "success":
            if UserId is None:
                dashboard_window1(login)
            else:
                dashboard_window(login)
        else:
            login_status_label.config(text="Invalid username or password",font=("Arial", 12,"bold"),fg="red")

    # Exit the application
    def exit_app():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            login.destroy()
            
    def loginAuthentication():
        url = "https://tspvahan.tspolice.gov.in/api/auto-fuel/v1/login"
        login_user_Id=username_entry.get()
        password=password_entry.get()
        payload = {'emp_id': str(login_user_Id),'password': str(password)}
        files=[]
        UserJson = './resources/users.json'
        # Read the JSON file
        with open(UserJson) as file:
            jsonData = json.load(file)

        # Check if the key exists in the 'users' dictionary
        if login_user_Id not in jsonData['users']:
            headers = {}
        else:
            token=jsonData['users'][login_user_Id]
            headers={}
            headers['Authorization']='Bearer '+token

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        data=(json.loads(response.text))
        
        login_status=(data['statusCode'])
        login_message=(data['message'])
        if login_status ==1 and login_message =="success":
            token=(data['response']['token'])
            
            # Check if the key exists in the 'users' dictionary
            if login_user_Id not in jsonData['users']:
                # Append the key-value pair to the 'users' dictionary
                jsonData['users'][login_user_Id] = token
                #print("new data is",jsonData)

                # Write the updated JSON back to the file
                with open(UserJson, 'w') as file:
                    json.dump(jsonData, file)
            file.close()
        return login_status,login_message

    Button(login_frame, text="Login", bg="#0B5394", fg="white", font=("Arial", 12), command=login_action).grid(row=3, columnspan=2, pady=20)

    # # Add an exit button to quit the application
    exit_button = Button(login, text="Exit", bg="red", fg="white", font=("Arial", 12), command=exit_app)
    # exit_button.pack(side=TOP, anchor='ne')
    exit_button.pack(side=BOTTOM, pady=10)
    # Pack the login form frame
    login_frame.pack() 
    
    login.mainloop()
    
#settings window
def settings_window(page):
    page.destroy()
    settings = Tk()
    settings.title("Settings")
    settings.attributes('-fullscreen', True)
    settings.configure(bg="white")
    
    # Create the Frames
    button_frame1 = Frame(settings, bg="white", padx=10, pady=10)
    
    def dashboard_page():
        if UserId != None:
            dashboard_window(settings)
        else:
            dashboard_window1(settings)
    
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
    
    fields = [
        ("Login User id:", "id_entry"),
        ("pump_name:", "pumpname_entry"),
        ("dispenser_no:", "dispenser_entry"),
        ("Nozil_No:", "nozil_entry"),
        ("price:", "price_entry"),
        ("density:", "density_entry"),
        ("Fuel Type:", "Fuel_entry")
    ]
    entry_fields = {}
    for row, (label_text, entry_name) in enumerate(fields):
        label = Label(details_frame, text=label_text, bg="white", font=("Arial", 18))
        entry = tk.Entry(details_frame, width=25, font=("Arial", 18), validate="key", validatecommand=(details_frame.register(validate_input), '%P'))
        label.grid(row=row, column=0, pady=10)
        entry.grid(row=row, column=1)
        entry_fields[entry_name] = entry
       
    def save_action():
        # save user data here
        global UserId,pump_name,dispenser_No,Nozil_No,price,density,Fuel
        UserId=entry_fields["id_entry"].get()
        pump_name=entry_fields["pumpname_entry"].get()
        dispenser_No=entry_fields["dispenser_entry"].get()
        Nozil_No=entry_fields["nozil_entry"].get()
        price=entry_fields["price_entry"].get()
        density=entry_fields["density_entry"].get()
        Fuel=entry_fields["Fuel_entry"].get()
        print("id :{},pump_name : {},dispenser_No :{},Nozil_No : {},price : {},density {},Fuel : {}".format(UserId,pump_name,dispenser_No,Nozil_No,price,density,Fuel))
        if not all([UserId, pump_name, dispenser_No, Nozil_No, price, density, Fuel]):
            messagebox.showerror("Error", "Please fill all fields.")
            return

        dashboard_window(settings)
        
    details_frame.pack()
    Button(details_frame, text="Save", bg="#0B5394", fg="white", font=("Arial", 16), command=save_action).grid(row=7, columnspan=2, pady=20)
    
#Fuel start window   
def start_fuel(page):
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    Nozil_status='Open'
    page.destroy()

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
        settings_window(fuelPage)
        
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
        Label(pump_detail_frame, text=headings[i]+str(values[i]),bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    details_label = Label(Qr_frame, text="Please Scan Vehicle Qr code", bg="white", font=("Arial", 16),relief="solid")
    details_label.pack(side="top", padx=1, pady=50)
    Qr_frame.place(relx=0.25, rely=0.45)

    # Schedule the function to run after 10 seconds
    fuelPage.after(5000, lambda: transactions_window(fuelPage))
    
def Qr_details(vehicle_no):
    global vehicle_name,emp_status,officer,driver_name,fuel_type,total_quota,available_quota,drown,tank_capacity,current_meter_reading,driver_id
    conn = http.client.HTTPSConnection("tspvahan.tspolice.gov.in")
    payload = ''
    headers = {
    'Authorization': token,
    'Cookie': 'XSRF-TOKEN=eyJpdiI6ImVPNW5lZnI3d2p5Um5DV25uS0dYdmc9PSIsInZhbHVlIjoiNDh4WWg1dFlDeFBUWlB4RXphTzZkR2laTHFWSm5CT3V1VmVPZDhoTjRFdTFSSzlDWGN1MkwvbVA4T3JDeGlMb3V1SnFGRXIxbEcybUtKWFVOSmNJVXpvcHhXbUI2ZG1MMVB6TUg5N3J2alJFYUJPM3N5dVR1UktTcTdTOTNOS2ciLCJtYWMiOiIzMzE3NmNhNzdhZTMwNDM0MjM5YmJkNzA4ZjZiNGExOGEyMDcwMGExOGIxOTRmMGNkYzNkZDQ3ZGUwNWJmYTBkIiwidGFnIjoiIn0%3D; tspvahan_session=eyJpdiI6ImVEMklSRVhTVjVVRkFiM0tuQVJlaGc9PSIsInZhbHVlIjoiSUY2cStEN0QvdWlhcDNFenBrWU1HU1lDc1djNGwyWktsQ2JySWVFTTZyRzR4KzF6ajlMUVhvQmxBcURSbzJ1ekg5Sk0vR0JmbnpWVjdGWXI5QjZUdUZJaU1LNVpENVdyNTFLSE82dmFXUVBzTit5VWdPamMyMVZvZmpwODltVU8iLCJtYWMiOiI0MGViOTM1Zjc0ZTRmNTVkNWE5N2QzMjc1MzZiNjVmZmJhMjJiM2VlN2ZhYTBlYWZiNzFkZDE0YzEzNmJiODNiIiwidGFnIjoiIn0%3D'
    }
    conn.request("POST", "/api/auto-fuel/v1/vehicle/{}".format(vehicle_no), payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    Data=json.loads(data.decode("utf-8"))
    #print(Data)

    statusCode=(Data['statusCode'])
    messageStatus=(Data['message'])
    vehicle_name=(Data['response']['vehicle_name'])
    emp_status=(Data['response']['status'])
    officer=(Data['response']['officer'])
    driver_id=(Data['response']['drivers'][0]['id'])
    driver_name=(Data['response']['drivers'][0]['full_name'])
    mobile_no=(Data['response']['drivers'][0]['mobile_no'])
    fuel_type=(Data['response']['fuel_type'])
    current_meter_reading=(Data['response']['current_meter_reading'])
    vehicle_unit_name=(Data['response']['vehicle_unit_name'])
    vehicle_category=print(Data['response']['vehicle_category'])
    vehicle_groups=print(Data['response']['vehicle_groups'])
    vehicle_usage_purpose=print(Data['response']['vehicle_usage_purpose'])
    regular_quota=(Data['response']['regular_quota'])
    additional_quota=(Data['response']['additional_quota'])
    total_quota=(Data['response']['total_quota'])
    drown=(Data['response']['drown'])
    available_quota=(Data['response']['available_quota'])
    tank_capacity=(Data['response']['tank_capacity'])

    return vehicle_name,emp_status,officer,driver_name,fuel_type,total_quota,available_quota,drown,tank_capacity,current_meter_reading,driver_id
   
def fuel_afterScan(Page):    
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    Page.destroy()
    
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
    afterScanDetails_frame.pack_propagate(0)
    def settings():
        settings_window(fuel_afterScan)
        
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
        Label(pump_detail_frame, text=headings[i]+str(values[i]),bg='white',bd=1,font=("Arial", 15),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    headings1 = ['Vehicle No: ', 'name: ', 'Status: ', 'officer: ', 'Driver: ', 'Fuel type: ']
    values1 = [vehicle_no,vehicle_name,emp_status,officer,driver_name,fuel_type]
    headings2=['Total quota:','Available quota: ','Down: ','Tank Capacity: ','Current transactions: ','Transaction id: ']
    values2=[total_quota,available_quota,drown,tank_capacity,current_meter_reading,driver_id]
    
    for i in range(len(headings1)):
        Label(afterScanDetails_frame, text=headings1[i]+str(values1[i]),width=30,bg='white',bd=1,font=("Arial", 14),relief="solid",wraplength=300).grid(row=i, column=0, sticky="w", pady=6,padx=90)

    for j in range(len(headings2)):
        Label(afterScanDetails_frame, text=headings2[j]+str(values2[j]),width=30,bg='white',bd=1,font=("Arial", 14),relief="solid",wraplength=300).grid(row=j, column=4, sticky="w", pady=6,padx=90)

    afterScanDetails_frame.place(relx=0.25, rely=0.45)
       
    fuel_status_label = Label(afterScanDetails_frame, text="Started Filling", bg="white", font=("Arial bold", 16),fg='green')
    fuel_status_label.grid(row=j+2, columnspan=5, pady=10)
    fuel_afterScan.after(5000, lambda: completion_window())
    
    def completion_window():
        global Nozil_status
        fuel_status_label = Label(afterScanDetails_frame, text="Completed Filling", bg="white", font=("Arial bold", 16),fg='green')
        fuel_status_label.grid(row=j+2, columnspan=5, pady=10)
        Nozil_status="Close"
        nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", bd=1, font=("Arial", 16),relief="solid",wraplength=400)
        nozil_label.grid(row=0, column=2, padx=10, pady=10)
        fuel_afterScan.after(10000, lambda: dashboard_window(fuel_afterScan))    
   
def transactions_window(page):
    global vehicle_no,vehicle_name,emp_status,officer,driver_name,fuel_type,total_quota,available_quota,drown,tank_capacity,current_meter_reading,driver_id
    vehicle_no='TS09PA3565'
    vehicle_name,emp_status,officer,driver_name,fuel_type,total_quota,available_quota,drown,tank_capacity,current_meter_reading,driver_id=Qr_details(vehicle_no)
    page.destroy()
    
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
        settings_window(transaction)
        
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
        Label(pump_detail_frame, text=headings[i]+str(values[i]),bg='white',bd=1,font=("Arial", 14),relief="solid",wraplength=250).grid(row=i+1, column=0, sticky="w", pady=6)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    # Create a frame to hold the table
    table_frame = Frame(transaction,bg='white',bd=1,relief="solid")
    table_frame.pack(pady=50)
    
    # Define the headings and values for the table
    table_headings = ['Vehicle No', 'Name', 'Status', 'Officer', 'Driver', 'Total Quota', 'Available Quota', 'Down', 'Current transactions','Fuel Type']
    table_values = [vehicle_no, vehicle_name, emp_status, officer, driver_name, total_quota, available_quota, drown,current_meter_reading,fuel_type]
    
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
    transaction.after(5000, lambda: fuel_afterScan(transaction))
    transaction.mainloop()

#Empty data dashboard window       
def dashboard_window1(page):
    # Create the window and set it to full screen
    page.destroy()
    dashboard1 = Tk()
    dashboard1.title("Dashboard")
    dashboard1.attributes('-fullscreen', True)
    dashboard1.configure(bg="white")
    button_frame1 = Frame(dashboard1, bg="white", padx=10, pady=10)
    Text_frame = Frame(dashboard1, bg="white", padx=250, pady=10, bd=1, relief="solid")
    
    def settings(): 
        settings_window(dashboard1)
            
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
def dashboard_window(page):
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    # Create the window and set it to full screen
    page.destroy()
    dashboard = Tk()
    dashboard.title("Dashboard")
    dashboard.attributes('-fullscreen', True)
    dashboard.configure(bg="white")
    
    # Create a frame to hold the buttons
    details_frame = Frame(dashboard, bg="white", padx=10, pady=10, bd=1, relief="solid")
    pump_detail_frame = Frame(dashboard, bg="white", padx=30, pady=10, bd=1, relief="solid")
    button_frame = Frame(dashboard, bg="white", padx=10, pady=10)

    def settings():
        settings_window(dashboard)
    def fuel():
        start_fuel(dashboard)
        
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
        Label(pump_detail_frame, text=headings[i],width=20,bg='white',bd=1,font=("Arial bold", 15),wraplength=200,anchor="w").grid(row=i*2, column=0,pady=(6, 2), padx=10)
        Label(pump_detail_frame, text=str(values[i]),width=23,bg='white',bd=1,font=("Arial", 14),relief="solid",wraplength=250,anchor="w").grid(row=2*i+1, column=0,pady=(2, 6), padx=10)
        
    pump_detail_frame.place(relx=0,rely=0.35)
    
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
