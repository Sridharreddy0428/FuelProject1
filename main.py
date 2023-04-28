from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import json
import os

p = lambda:None
CwaDataToIotCore_json = 'D:/FuelProject/resources/parameters.json'
with open(CwaDataToIotCore_json) as f:
    json_data = f.read()
    #print(json_data)
    p.__dict__ = json.loads(json_data)
    f.close()

UserId=p.UserId
pump_name=p.pump_name
issues=p.Today_total_full_issues
transactions=p.Toatl_Transactions
Nozil_status=p.Nozil_status
dispenser_No=p.dispenser_no
Nozil_No=p.Nozil_no
price=p.Price
density=p.density
Fuel=p.Fuel_type
 
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
    diplay_label = Label(login_frame, text="Enter login credentials", bg="white", font=("Helvetica", 16,"bold"),fg="blue")
    username_label = Label(login_frame, text="Username:", bg="white", font=("Helvetica", 16))
    password_label = Label(login_frame, text="Password:", bg="white", font=("Helvetica", 16))
    username_entry = Entry(login_frame, width=25, font=("Helvetica", 16))
    password_entry = Entry(login_frame, width=25, show="*", font=("Helvetica", 16))
    login_status_label = Label(login_frame, text="", bg="white", font=("Helvetica", 12))

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
                dashboard_window()
            else:
                dashboard_window1()
        else:
            login_status_label.config(text="Invalid username or password",font=("Helvetica", 12,"bold"),fg="red")

    # Exit the application
    def exit_app():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            login.destroy()

    login_frame.pack() # Pack the login form frame
    Button(login_frame, text="Login", bg="#0B5394", fg="white", font=("Helvetica", 12), command=login_action).grid(row=3, columnspan=2, pady=20)

    # Add an exit button to quit the application
    exit_button = Button(login, text="Exit", bg="red", fg="white", font=("Helvetica", 12), command=exit_app)
    exit_button.pack(side=BOTTOM, pady=10)

    login.mainloop()

#settings window
def settings_window(dashboard1):
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
    logout_btn = Button(button_frame1, text="Logout", bg="red", fg="white", font=("Arial", 16), command=lambda: [settings.destroy(),dashboard1.destroy(),login_window()])
    
    back_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame1.pack(side='top', anchor='ne')
    
    # Create a frame for the login form
    details_frame = Frame(settings, bg="white", padx=50, pady=90, bd=2, relief="solid")
    # Create the login form
    id_label = Label(details_frame, text="Login User id:", bg="white", font=("Helvetica", 18))
    id_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
    id_label.grid(row=0, column=0, pady=10)
    id_entry.grid(row=0, column=1)
    
    pumpname_label = Label(details_frame, text="pump_name:", bg="white", font=("Helvetica", 18))
    pumpname_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
    pumpname_label.grid(row=1, column=0, pady=10)
    pumpname_entry.grid(row=1, column=1)
    
    dispenser_label = Label(details_frame, text="dispenser_no:", bg="white", font=("Helvetica", 18))
    dispenser_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
    dispenser_label.grid(row=2, column=0, pady=10)
    dispenser_entry.grid(row=2, column=1)
    
    nozil_label = Label(details_frame, text="Nozil_No:", bg="white", font=("Helvetica", 18))
    nozil_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
    nozil_label.grid(row=3, column=0, pady=10)
    nozil_entry.grid(row=3, column=1)
    
    price_label = Label(details_frame, text="dispenser_no:", bg="white", font=("Helvetica", 18))
    price_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
    price_label.grid(row=4, column=0, pady=10)
    price_entry.grid(row=4, column=1)
    
    density_label = Label(details_frame, text="density:", bg="white", font=("Helvetica", 18))
    density_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
    density_label.grid(row=5, column=0, pady=10)
    density_entry.grid(row=5, column=1)
    
    Fuel_label = Label(details_frame, text="Fuel Type:", bg="white", font=("Helvetica", 18))
    Fuel_entry = Entry(details_frame, width=25, font=("Helvetica", 18))
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
    Button(details_frame, text="Save", bg="#0B5394", fg="white", font=("Helvetica", 16), command=save_action).grid(row=7, columnspan=2, pady=20)
    
#Fuel start window   
def start_fuel():
    global UserId,issues,transactions,Fuel,density,price,Nozil_status,Nozil_No,dispenser_No
    # Create the window and set it to full screen
    fuelPage = Tk()
    fuelPage.title("Dashboard")
    fuelPage.attributes('-fullscreen', True)
    fuelPage.configure(bg="white")
    
    # Create a frame to hold the buttons
    button_frame = Frame(fuelPage, bg="white", padx=10, pady=10)
    Qr_frame = Frame(fuelPage, bg="white", padx=325, pady=60, bd=1, relief="solid")
    details_frame = Frame(fuelPage)
    pump_detail_frame = Frame(fuelPage)
    

    def settings():
        fuelPage.destroy()
        settings_window(fuelPage)
        
    # Create the settings and logout buttons
    settings_btn = Button(button_frame, text="Settings", bg="blue", fg="white", font=("Arial", 16),command=settings) #(command=settings)
    logout_btn = Button(button_frame, text="Logout", bg="red", fg="white", font=("Arial", 16), command=lambda: [fuelPage.destroy(), login_window()])

    # Pack the buttons inside the frame
    
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame.pack(side='top', anchor='ne')
    
    userId_label = Label(fuelPage, text="Login User id : {} ".format(UserId), bg="white", font=("Helvetica", 24))
    userId_label.pack(side="top", padx=40, pady=50)
    
    issue_label = Label(details_frame, text="Today Total Full issues : {} ".format(issues), bg="white", font=("Helvetica", 18))
    issue_label.grid(row=0, column=0, padx=10, pady=10)

    transaction_label = Label(details_frame, text="Today Transactions : {} ".format(transactions), bg="white", font=("Helvetica", 18))
    transaction_label.grid(row=0, column=1, padx=10, pady=10)

    nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", font=("Helvetica", 18))
    nozil_label.grid(row=0, column=2, padx=10, pady=10)
    
    details_frame.place(relx=0.25,rely=0.3)
        
    # create a frame for the labels
    details_frame = Frame(fuelPage)
    details_frame.pack(side=LEFT, padx=10, pady=5)

    # create the labels and add them to the frame
    dispenser_no_label = Label(pump_detail_frame, text="Dispenser No: {}".format(dispenser_No), bg="white", font=("Arial", 24))
    dispenser_no_label.pack(pady=4)

    nozzle_no_label = Label(pump_detail_frame, text="Nozzle No: {}".format(Nozil_No), bg="white", font=("Arial", 24))
    nozzle_no_label.pack(pady=4)

    price_label = Label(pump_detail_frame, text="Price: {}".format(price), bg="white", font=("Arial", 24))
    price_label.pack(pady=4)

    density_label = Label(pump_detail_frame, text="Density: {}".format(density), bg="white", font=("Arial", 24))
    density_label.pack(pady=4)

    fuel_type_label = Label(pump_detail_frame, text="Fuel Type: {}".format(Fuel), bg="white", font=("Arial", 24))
    fuel_type_label.pack(pady=4)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    details_label = Label(Qr_frame, text="Please Scan Vehicle Qr code", bg="white", font=("Helvetica", 20))
    details_label.pack(side="top", padx=1, pady=50)
    Qr_frame.place(relx=0.25, rely=0.45)

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
        settings_window(dashboard1)
            
    # Create the settings and logout buttons
    settings_btn = Button(button_frame1, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) 
    logout_btn = Button(button_frame1, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [dashboard1.destroy(), login_window()])

    # Pack the buttons inside the frame
   
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame1.pack(side='top', anchor='ne')
    
    details_label = Label(Text_frame, text="Settings not available please set dispenser settings", bg="white", font=("Helvetica", 24))
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
    pump_detail_frame = Frame(dashboard, bg="white", padx=10, pady=10, bd=1, relief="solid")
    promotion_frame = Frame(dashboard, bg="white", padx=325, pady=60, bd=1, relief="solid")
    button_frame = Frame(dashboard, bg="white", padx=10, pady=10)

    def settings():
        dashboard.destroy()
        settings_window(dashboard)
    def fuel():
        dashboard.destroy()
        start_fuel()
        
    # Create the settings and logout buttons
    settings_btn = Button(button_frame, text="Settings", bg="blue", fg="white", font=("Arial", 14),command=settings) #(command=settings)
    logout_btn = Button(button_frame, text="Logout", bg="red", fg="white", font=("Arial", 14), command=lambda: [dashboard.destroy(), login_window()])
    Button(dashboard, text="Start Fuel", bg="#0B5394", fg="white", font=("Helvetica", 12), command=fuel).pack(side=BOTTOM,pady=10)
    
    # Pack the buttons inside the frame    
    settings_btn.grid(row=0, column=0,padx=0.5,pady=20)
    logout_btn.grid(row=0, column=1,padx=0.5,pady=20)
    
    button_frame.pack(side='top', anchor='ne')
    
    userId_label = Label(dashboard, text="Login User id : {} ".format(UserId), bg="white", bd=1, font=("Helvetica", 24),relief="solid")
    userId_label.pack(side="top", padx=40, pady=50)
    
    issue_label = Label(details_frame, text="Today Total Full issues : {} ".format(issues), bg="white", font=("Helvetica", 18),bd=1,relief="solid")
    issue_label.grid(row=0, column=0, padx=10, pady=10)

    transaction_label = Label(details_frame, text="Today Transactions : {} ".format(transactions), bg="white", font=("Helvetica", 18),bd=1,relief="solid")
    transaction_label.grid(row=0, column=1, padx=10, pady=10)

    nozil_label = Label(details_frame, text="nozil status : {}".format(Nozil_status), bg="white", font=("Helvetica", 18),bd=1,relief="solid")
    nozil_label.grid(row=0, column=2, padx=10, pady=10)
    
    details_frame.place(relx=0.25,rely=0.3)
        
    # create a frame for the labels
    details_frame = Frame(dashboard)
    details_frame.pack(side=LEFT, padx=10, pady=5)

    # create the labels and add them to the frame
    dispenser_no_label = Label(pump_detail_frame, text="Dispenser No: {}".format(dispenser_No), bg="white", font=("Arial", 24),bd=1,relief="solid")
    dispenser_no_label.pack(pady=4)

    nozzle_no_label = Label(pump_detail_frame, text="Nozzle No: {}".format(Nozil_No), bg="white", font=("Arial", 24),bd=1,relief="solid")
    nozzle_no_label.pack(pady=4)

    price_label = Label(pump_detail_frame, text="Price: {}".format(price), bg="white", font=("Arial", 24),bd=1,relief="solid")
    price_label.pack(pady=4)

    density_label = Label(pump_detail_frame, text="Density: {}".format(density), bg="white", font=("Arial", 24),bd=1,relief="solid")
    density_label.pack(pady=4)

    fuel_type_label = Label(pump_detail_frame, text="Fuel Type: {}".format(Fuel), bg="white", font=("Arial", 24),bd=1,relief="solid")
    fuel_type_label.pack(pady=4)

    pump_detail_frame.place(relx=0,rely=0.45)
    
    promotion_label = Label(promotion_frame, text="Promotion Banner", bg="white", font=("Arial", 24))
    promotion_label.pack(side="top", padx=1, pady=50)
    # promotion_label.pack(pady=4)
    promotion_frame.place(relx=0.25, rely=0.45)
    dashboard.mainloop()
if __name__=="__main__":
    # Start the application by showing the login window
    login_window()
