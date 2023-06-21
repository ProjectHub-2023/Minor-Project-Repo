import os


if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import * 

Current_Deg=[0,0.0,0.0,0.0]

class Actuate():
    ADDR_TORQUE_ENABLE          = 64
    ADDR_GOAL_POSITION          = 116
    ADDR_PRESENT_POSITION       = 132
    ADDR_PROFILE_VELOCITY       = 112
    DXL_MINIMUM_POSITION_VALUE  = 1000      # Refer to the Minimum Position Limit of product eManual
    DXL_MAXIMUM_POSITION_VALUE  = 2600      # Refer to the Maximum Position Limit of product eManual
    BAUDRATE                    = 57600

    PROTOCOL_VERSION            = 2.0

    # Factory default ID of all DYNAMIXEL is 1
    DXL_ID0                      = 0
    DXL_ID1                      = 1
    DXL_ID2                      = 2
    # Use the actual port assigned to the U2D2.
    # ex) Windows: "COM*", Linux: "/dev/ttyUSB*", Mac: "/dev/tty.usbserial-*"
    DEVICENAME                  = "COM9"

    TORQUE_ENABLE               = 1     # Value for enabling the torque
    TORQUE_DISABLE              = 0     # Value for disabling the torque
    DXL_MOVING_STATUS_THRESHOLD = 20    # Dynamixel moving status threshold
    PROFILE_VELOCITY 			= 100   # Dynamixel Velocity

    index = 0
    dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]         # Goal position
    portHandler = PortHandler(DEVICENAME)
    packetHandler = PacketHandler(PROTOCOL_VERSION)
    
    Motor_ID_Dict={1:DXL_ID0 ,2:DXL_ID1, 3:DXL_ID2}

    def __init__(self):
        print("Init works!!!")
        if Actuate.portHandler.openPort():
            print("Succeeded to open the port")
        else:
            print("Failed to open the port")
            print("Press any key to terminate...")
            getch()
            quit()
        if Actuate.portHandler.setBaudRate(Actuate.BAUDRATE):
            print("Succeeded to change the baudrate")
        else:
            print("Failed to change the baudrate")
            print("Press any key to terminate...")
            getch()
            quit()
        Actuate.Enable_all_Motors()

    def enable_torque(id):
        dxl_comm_result, dxl_error = Actuate.packetHandler.write1ByteTxRx(Actuate.portHandler, Actuate.Motor_ID_Dict[id], Actuate.ADDR_TORQUE_ENABLE, Actuate.TORQUE_ENABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % Actuate.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % Actuate.packetHandler.getRxPacketError(dxl_error))
        else:
            print("\nTorque has been enabled for Motor ID: ",id)

    def enable_velocity(id):
        dxl_comm_result, dxl_error = Actuate.packetHandler.write4ByteTxRx(Actuate.portHandler, Actuate.Motor_ID_Dict[id], Actuate.ADDR_PROFILE_VELOCITY, Actuate.PROFILE_VELOCITY)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % Actuate.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % Actuate.packetHandler.getRxPacketError(dxl_error))
        else:
            print("\nVelocity has been enabled for Motor ID: ",id)

    def actuate_motors(id,value1):
        value1=round((180-value1)*11.375)
        print(value1)
        if(value1>=Actuate.DXL_MINIMUM_POSITION_VALUE and value1<=Actuate.DXL_MAXIMUM_POSITION_VALUE):
            dxl_comm_result, dxl_error = Actuate.packetHandler.write4ByteTxRx(Actuate.portHandler, id,Actuate.ADDR_GOAL_POSITION, value1)
            if dxl_comm_result != COMM_SUCCESS: 	
                print("%s" % Actuate.packetHandler.getTxRxResult(dxl_comm_result))
            elif dxl_error != 0:
                print("%s" % Actuate.packetHandler.getRxPacketError(dxl_error))
            
            dxl_present_position, dxl_comm_result, dxl_error = Actuate.packetHandler.read4ByteTxRx(Actuate.portHandler, id, Actuate.ADDR_PRESENT_POSITION)
            print("[ID:%03d] GoalPos:%03d  PresPos:%03d" % (Actuate.DXL_ID0, value1, dxl_present_position))
            return dxl_present_position
            print()
        else:
            print("Values out of range")

    def disable_torque(id):
        dxl_comm_result, dxl_error = Actuate.packetHandler.write1ByteTxRx(Actuate.portHandler, id, Actuate.ADDR_TORQUE_ENABLE, Actuate.TORQUE_DISABLE)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % Actuate.packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % Actuate.packetHandler.getRxPacketError(dxl_error))
        print("Torque has been disabled for Motor ID: ",id)
    
    def Disable_all_Motors():
        print("Recieved request to disable all motors...")
        for disable_all in range (3):
            Actuate.disable_torque(disable_all) 
            print("Disabling Motor ID: ",disable_all)
        print("All Motors Disabled !!!")

    def Enable_all_Motors():
        print("Recieved request to enable all motors...")
        for activate_motors in range(1,4):
            print("Enabling torque for Dynamixel Motor ID: ",activate_motors)
            Actuate.enable_torque(activate_motors)
            print("Enabling velocity for Dynamixel Motor ID: ",activate_motors)
            Actuate.enable_velocity(activate_motors)


    def present_position(id):
        dxl_present_position, dxl_comm_result, dxl_error = Actuate.packetHandler.read4ByteTxRx(Actuate.portHandler, id, Actuate.ADDR_PRESENT_POSITION)
        return dxl_present_position   





act=Actuate()