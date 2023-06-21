import sqlite3
from tkinter import *
from tkinter import messagebox,Tk,Text,ttk
from ik import kinematics
from Actuator import Actuate
import cv2
import customtkinter
import PIL
import time
import threading
import Socket

# from ctk import ctkLabel, ctkTabView
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
conn = sqlite3.connect('Employee_DB.db')
c = conn.cursor()

def change_appearance_mode_event(self, new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

def change_scaling_event(self, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)

def Login():
    Login.login_page=customtkinter.CTk()
    Login.login_page.geometry("500x350")

    frame=customtkinter.CTkFrame(master=Login.login_page)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label=customtkinter.CTkLabel(master=frame, text="Login")
    label.pack(pady=12, padx=10)

    Login.username_entry=customtkinter.CTkEntry(master=frame, placeholder_text="Username", placeholder_text_color="grey",takefocus=YES)
    Login.username_entry.pack(pady=12, padx=10)
    Login.username_entry.focus_set()
    Login.password_entry=customtkinter.CTkEntry(master=frame, placeholder_text="Password", placeholder_text_color="grey", show="*")
    Login.password_entry.pack(pady=12, padx=10)

    button=customtkinter.CTkButton(master=frame, text="Login", command=login_clicked)
    button.pack(pady=12, padx=10)

    Login.login_page.bind('<Return>', login_clicked)

    Login.login_page.mainloop()

def verify_login(username, password):
    c.execute("SELECT Employee_Field FROM Operator_Info WHERE Operator_Login=? AND Operator_Key=?", (username, password))
    # print (c.fetchall())
    verify_login.designation =c.fetchone()[0]
    c.execute("SELECT Employee_ID FROM Operator_Info WHERE Operator_Login=? AND Operator_Key=?", (username, password))
    # print (c.fetchall())
    verify_login.Employee_ID =c.fetchone()[0]
    return verify_login.designation

def login_clicked(self):
    # Get the entered username and password
    username = Login.username_entry.get()
    password = Login.password_entry.get()
    print(username,password)
    # Verify the login credentials
    if verify_login(username, password)=='Manager':
        manager_login()
    # elif verify_login(username, password)=='Operator':
    else:
        messagebox.showerror("Access Denied", "Please contact administer...")

# def login_clicked():
#     # Get the entered username and password
#     username = Login.username_entry.get()
#     password = Login.password_entry.get()
#     print(username,password)
#     # Verify the login credentials
#     if verify_login(username, password)=='Manager':
#         manager_login()
#     # elif verify_login(username, password)=='Operator':
#     else:
#         messagebox.showerror("Access Denied", "Please contact administer...")

def redirect_to_Login(self):
    messagebox.showinfo("Logging Out !!!", "You are being logged out of the system...")
    if verify_login.designation=="Manager":
        manager_login.monitor_window.destroy()
    # else:
    Login()

# def redirect_to_Login():
#     messagebox.showinfo("Logging Out !!!", "You are being logged out of the system...")
#     if verify_login.designation=="Manager":
#         manager_login.monitor_window.destroy()
#     # else:
#     Login()

def manager_login():
    jog_Loop=""
    messagebox.showinfo("Login Successful", "Press OK to continue to Main Interface...")
    Login.login_page.destroy()  # Close the login window
    
    manager_login.monitor_window = customtkinter.CTk()
    Screen_width= manager_login.monitor_window.winfo_screenwidth()               
    Screen_height= manager_login.monitor_window.winfo_screenheight()               
    manager_login.monitor_window.geometry(f"{Screen_width}x{Screen_height}+0+0")
    manager_login.monitor_window.title("Robot Monitoring")
    manager_login.monitor_window.grid_rowconfigure((0,1,2), weight=1)
    manager_login.monitor_window.grid_columnconfigure(1, weight=1)
    manager_login.monitor_window.grid_columnconfigure((2,3), weight=0)

    sidebar_frame = customtkinter.CTkFrame(manager_login.monitor_window,width=140, corner_radius=30)
    sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
    sidebar_frame.grid_rowconfigure(4, weight=1)
    logo_label = customtkinter.CTkLabel(sidebar_frame, text="Delta Robot User Interface", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    # sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, command=sidebar_button_event)
    # sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
    # sidebar_button_2 = customtkinter.CTkButton(sidebar_frame, command=sidebar_button_event)
    # sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
    # sidebar_button_3 = customtkinter.CTkButton(sidebar_frame, command=sidebar_button_event)
    # sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
    Start_button=customtkinter.CTkButton(master=sidebar_frame, text="Start", command=Start_Operation)
    Start_button.grid(row=1, column=0,columnspan=2, padx=20,pady=20, sticky="ew")
    Stop_button=customtkinter.CTkButton(master=sidebar_frame, text="Stop", command=Stop_Operation)
    Stop_button.grid(row=2, column=0,columnspan=2, padx=20,pady=20, sticky="ew")
    Socket_button=customtkinter.CTkButton(master=sidebar_frame, text="Socket", command=threading.Thread(target=Socket.open_socket).start())
    Socket_button.grid(row=3, column=0,columnspan=2, padx=20,pady=20, sticky="ew")
    # Operation_Log_button=customtkinter.CTkButton(master=sidebar_frame, text="Operation Log", command=Retieve_Operation_Log)
    # Operation_Log_button.grid(row=4, column=0,columnspan=2, padx=20,pady=20, sticky="ew")
    Logout_button=customtkinter.CTkButton(master=sidebar_frame, text="Logout", command=redirect_to_Login)
    Logout_button.grid(row=6, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    # Create the camera feed
    # camera_feed = cv2.VideoCapture(0)  
    
    # label =customtkinter.CTkLabel(manager_login.monitor_window,text="")
    # label.grid(row=0, column=2)
    # def update_camera_feed():
    #     # Get the latest frame and convert into Image
    #     cv2image= cv2.cvtColor(camera_feed.read()[1],cv2.COLOR_BGR2RGB)
    #     img = PIL.Image.fromarray(cv2image)
    #     # Convert image to PhotoImage
    #     imgtk = PIL.ImageTk.PhotoImage(image = img)
    #     label.imgtk = customtkinter.CTkImage
    #     label.configure(image=imgtk)
    #     # Repeat after an interval to capture continiously
    #     label.after(20, update_camera_feed)
    # update_camera_feed()

    # # create scrollable textbox
    # Ctk_Textbox = Text(manager_login.monitor_window, highlightthickness=0)
    # Ctk_Textbox.grid(row=0, column=1, sticky="nsew")

    # # create CTk scrollbar
    # ctk_textbox_scrollbar = customtkinter.CTkScrollbar(manager_login.monitor_window, command=Ctk_Textbox.yview)
    # ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

    # # connect textbox scroll event to CTk scrollbar
    # Ctk_Textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

    Controltab=customtkinter.CTkTabview(manager_login.monitor_window, width=250)
    Controltab.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
    Controltab.add("Preset Positions")
    Controltab.tab("Preset Positions").grid_columnconfigure(0, weight=1)
    Controltab.add("Jog Positions")
    Controltab.tab("Jog Positions").grid_columnconfigure(0, weight=1) 

    # manager_login.actuation_value=0
    # Home_position=customtkinter.CTkRadioButton(master=Controltab.tab("Preset Positions"), text="Home Position", variable= manager_login.actuation_value, value=1)
    # Home_position.grid(row=1, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    # Pick_position=customtkinter.CTkRadioButton(master=Controltab.tab("Preset Positions"), text="Pick Up Position", variable= manager_login.actuation_value, value=2)
    # Pick_position.grid(row=2, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    # Drop_position=customtkinter.CTkRadioButton(master=Controltab.tab("Preset Positions"), text="Drop Position", variable= manager_login.actuation_value, value=3)
    # Drop_position.grid(row=3, column=0,columnspan=2, padx=20,pady=20, sticky="ew")
    def preset_home_position():
        home_position=[0,0,-281]
        kinematics.Actuate_to_position(home_position)
        
    def preset_pick_position():
        pick_position=[100,60,-433]
        kinematics.Actuate_to_position(pick_position)

    def preset_drop_position():
        drop_position=[-120,-60,-433]
        kinematics.Actuate_to_position(drop_position)

    def y_axis_jog():
        yjogposition=[0,120,-430]
        kinematics.Actuate_to_position(yjogposition)
        x_count=0
        for x_count in range (12):
            yjogposition[1]-=20
            kinematics.Actuate_to_position(yjogposition)
            time.sleep(0.2)
            # x_count+=1

    def x_axis_jog():
        xjogposition=[120,0,-430]
        kinematics.Actuate_to_position(xjogposition)
        x_count=0
        for x_count in range (12):
            xjogposition[0]-=20
            kinematics.Actuate_to_position(xjogposition)
            time.sleep(0.2)
            # x_count+=1
    
    def preset_jog():
        # while True:
        intermidiate=[0,0,-360]
        for repeat in range (6):
            preset_home_position()
            time.sleep(0.5)
            preset_pick_position()
            time.sleep(0.5)
            kinematics.Actuate_to_position(intermidiate)
            time.sleep(0.5)
            preset_drop_position()
            time.sleep(0.5)
            preset_home_position()
            # if jog_Loop=="False":
            #     break

    Home_position=customtkinter.CTkButton(master=Controltab.tab("Preset Positions"), text="Home Position", command=preset_home_position)
    Home_position.grid(row=1, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    Pick_position=customtkinter.CTkButton(master=Controltab.tab("Preset Positions"), text="Pick Up Position", command=preset_pick_position)
    Pick_position.grid(row=2, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    Drop_position=customtkinter.CTkButton(master=Controltab.tab("Preset Positions"), text="Drop Position", command=preset_drop_position)
    Drop_position.grid(row=3, column=0,columnspan=2, padx=20,pady=20, sticky="ew")

    jog_work=customtkinter.CTkButton(master=Controltab.tab("Preset Positions"), text="Cycle between workareas", command=preset_jog)
    jog_work.grid(row=4, column=0,columnspan=2, padx=20,pady=20, sticky="ew")
    # checkbox = customtkinter.CTkCheckBox(master=Controltab.tab("Preset Positions"), text="Auto-Repeat", variable=jog_Loop, onvalue="True", offvalue="False")
    # checkbox.grid(row=4, column=0,columnspan=1, padx=20,pady=20, sticky="ew")

    XJog_position=customtkinter.CTkButton(master=Controltab.tab("Jog Positions"), text="Jog along x-axis", command=x_axis_jog)
    XJog_position.grid(row=0, column=0,columnspan=5, padx=20,pady=20, sticky="ew")

    yJog_position=customtkinter.CTkButton(master=Controltab.tab("Jog Positions"), text="Jog along y-axis", command=y_axis_jog)
    yJog_position.grid(row=1, column=0,columnspan=5, padx=20,pady=20, sticky="ew")

    # Motor_1_Position=customtkinter.CTkLabel(Controltab.tab("Teach Positions"),text="1st Motor Position: ",)
    # Motor_1_Position.grid(row=0, column=0, padx=20, pady=(20, 10))
    # Motor_1_Position_value=customtkinter.CTkLabel(Controltab.tab("Teach Positions"),text=str(Actuate.present_position(Actuate.DXL_ID0)))
    # Motor_1_Position_value.grid(row=0, column=1, padx=20, pady=(20, 10))
    # Motor_2_Position=customtkinter.CTkLabel(Controltab.tab("Teach Positions"),text="2nd Motor Position: ")
    # Motor_2_Position.grid(row=1, column=0, padx=20, pady=(20, 10))
    # Motor_2_Position_value=customtkinter.CTkLabel(Controltab.tab("Teach Positions"),text=str(Actuate.present_position(Actuate.DXL_ID1)))
    # Motor_2_Position_value.grid(row=1, column=1, padx=20, pady=(20, 10))
    # Motor_3_Position=customtkinter.CTkLabel(Controltab.tab("Teach Positions"),text="3rd Motor Position: ")
    # Motor_3_Position.grid(row=2, column=0, padx=20, pady=(20, 10))
    # Motor_3_Position_value=customtkinter.CTkLabel(Controltab.tab("Teach Positions"),text=str(Actuate.present_position(Actuate.DXL_ID2)))
    # Motor_3_Position_value.grid(row=2, column=1, padx=20, pady=(20, 10))
    # Tab_name=Controltab._current_name
    manager_login.monitor_window.bind('<Escape>', redirect_to_Login)
    manager_login.monitor_window.mainloop()
        
def Retieve_Operation_Log():
    c.execute("SELECT * FROM Operation_Log ")

def Stop_Operation():
    Actuate.Disable_all_Motors()

def Start_Operation():
    Actuate.Enable_all_Motors()
    

def Update_Teach_Position(Tab_Name):
    # Tab_name=manager_login.Controltab._current_name  
    print(Tab_Name)
    # if Tab_Name=="Teach Positions":
    while True:
        Motor_1_Position=customtkinter.CTkLabel(manager_login.Controltab.tab("Teach Positions"),text="1st Motor Position: ")
        Motor_1_Position.grid(row=1, column=0, padx=20, pady=(20, 10))
        Motor_1_Position_value=customtkinter.CTkLabel(manager_login.Controltab.tab("Teach Positions"),text=str(Actuate.present_position(Actuate.DXL_ID0)))
        Motor_1_Position_value.grid(row=1, column=1, padx=20, pady=(20, 10))
        Motor_2_Position=customtkinter.CTkLabel(manager_login.Controltab.tab("Teach Positions"),text="2nd Motor Position: ")
        Motor_2_Position.grid(row=2, column=0, padx=20, pady=(20, 10))
        Motor_2_Position_value=customtkinter.CTkLabel(manager_login.Controltab.tab("Teach Positions"),text=str(Actuate.present_position(Actuate.DXL_ID1)))
        Motor_2_Position_value.grid(row=2, column=1, padx=20, pady=(20, 10))
        Motor_3_Position=customtkinter.CTkLabel(manager_login.Controltab.tab("Teach Positions"),text="3rd Motor Position: ")
        Motor_3_Position.grid(row=3, column=0, padx=20, pady=(20, 10))
        Motor_3_Position_value=customtkinter.CTkLabel(manager_login.Controltab.tab("Teach Positions"),text=str(Actuate.present_position(Actuate.DXL_ID2)))
        Motor_3_Position_value.grid(row=3, column=1, padx=20, pady=(20, 10))
        manager_login.monitor_window.bind('<Escape>', redirect_to_Login)
        manager_login.monitor_window.mainloop()

# def send_preset_actuation_signal(value1,value2,value3):
#     # if manager_login.actuation_value==1:
#     #     value1=1500
#     #     value2=1500
#     #     value3=1500
#     # elif manager_login.actuation_value==2:
#     #     value1=2000
#     #     value2=2000
#     #     value3=1500
#     # elif manager_login.actuation_value==3:
#     #     value1=2000
#     #     value2=1500
#     #     value3=2000

#     print("Numbers passed to actuate motor:",value1,value2,value3)
#     # act=Actuate()
#     # act.actuate_motors(value1,value2,value3)

Login()