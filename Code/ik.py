
import Actuator
from Actuator import Actuate
import math
import Socket
import threading
# import Main

e  =  35.0
f  =  140.0
re =  340.0
rf =  160.0

# Trigonometric constants
s      = 165*2
sqrt3  = math.sqrt(3.0)
pi     = 3.141592653
sin120 = sqrt3 / 2.0
cos120 = -0.5
tan60  = sqrt3
sin30  = 0.5
tan30  = 1.0 / sqrt3

class kinematics():

    # Forward kinematics: (theta1, theta2, theta3) -> (x0, y0, z0)
    #   Returned {error code,theta1,theta2,theta3}
    def forward(theta1, theta2, theta3):
        x0 = 0.0
        y0 = 0.0
        z0 = 0.0
        
        t = (f-e) * tan30 / 2.0
        dtr = math.pi / 180.0
        
        theta1 *= dtr
        theta2 *= dtr
        theta3 *= dtr
        
        y1 = -(t + rf*math.cos(theta1) )
        z1 = -rf * math.sin(theta1)
        
        y2 = (t + rf*math.cos(theta2)) * sin30
        x2 = y2 * tan60
        z2 = -rf * math.sin(theta2)
        
        y3 = (t + rf*math.cos(theta3)) * sin30
        x3 = -y3 * tan60
        z3 = -rf * math.sin(theta3)
        
        dnm = (y2-y1)*x3 - (y3-y1)*x2
        
        w1 = y1*y1 + z1*z1
        w2 = x2*x2 + y2*y2 + z2*z2
        w3 = x3*x3 + y3*y3 + z3*z3
        
        # x = (a1*z + b1)/dnm
        a1 = (z2-z1)*(y3-y1) - (z3-z1)*(y2-y1)
        b1= -( (w2-w1)*(y3-y1) - (w3-w1)*(y2-y1) ) / 2.0
        
        # y = (a2*z + b2)/dnm
        a2 = -(z2-z1)*x3 + (z3-z1)*x2
        b2 = ( (w2-w1)*x3 - (w3-w1)*x2) / 2.0
        
        # a*z^2 + b*z + c = 0
        a = a1*a1 + a2*a2 + dnm*dnm
        b = 2.0 * (a1*b1 + a2*(b2 - y1*dnm) - z1*dnm*dnm)
        c = (b2 - y1*dnm)*(b2 - y1*dnm) + b1*b1 + dnm*dnm*(z1*z1 - re*re)
        
        # discriminant
        d = b*b - 4.0*a*c
        if d < 0.0:
            return [1,0,0,0] # non-existing povar. return error,x,y,z
        
        z0 = -0.5*(b + math.sqrt(d)) / a
        x0 = (a1*z0 + b1) / dnm
        y0 = (a2*z0 + b2) / dnm

        return [0,x0,y0,z0]

    # Inverse kinematics
    # Helper functions, calculates angle theta1 (for YZ-pane)
    def angle_yz(x0, y0, z0, theta=None):
        y1 = -0.5*0.57735*f # f/2 * tg 30
        y0 -= 0.5*0.57735*e # shift center to edge
        # z = a + b*y
        a = (x0*x0 + y0*y0 + z0*z0 + rf*rf - re*re - y1*y1) / (2.0*z0)
        b = (y1-y0) / z0

        # discriminant
        d = -(a + b*y1)*(a + b*y1) + rf*(b*b*rf + rf)
        if d<0:
            return [1,0] # non-existing povar.  return error, theta

        yj = (y1 - a*b - math.sqrt(d)) / (b*b + 1) # choosing outer povar
        zj = a + b*yj
        theta = math.atan(-zj / (y1-yj)) * 180.0 / pi + (180.0 if yj>y1 else 0.0)
        
        return [0,theta] # return error, theta

    def inverse(x0, y0, z0):
        theta1 = 0
        theta2 = 0
        theta3 = 0
        status = kinematics.angle_yz(x0,y0,z0)

        if status[0] == 0:
            theta1 = status[1]
            status = kinematics.angle_yz(x0*cos120 + y0*sin120,
                                    y0*cos120-x0*sin120,
                                    z0,
                                    theta2)
        if status[0] == 0:
            theta2 = status[1]
            status = kinematics.angle_yz(x0*cos120 - y0*sin120,
                                    y0*cos120 + x0*sin120,
                                    z0,
                                    theta3)
        theta3 = status[1]

        return [status[0],theta1,theta2,theta3]
    
    def convert_deg_to_steps(deg):
        steps=deg
        for i in range(1,4):
            steps[i]=round((180-steps[i])*11.375)
            print(steps[i])
        return steps
# value=120
    def Actuate_to_position(Coordinates):
        req_position=0
        deg=kinematics.inverse(Coordinates[0],Coordinates[1],Coordinates[2])
        if deg[0]==0:
            print("Degrees before conversion: ",deg)
            Actuator.Current_Deg=deg
            print("Actuator Current Degree: ",Actuator.Current_Deg)
            for send_index in range(4):
                Socket.send_angles[send_index]=(Actuator.Current_Deg[send_index]*(pi/180))
            print("send angles: ",Socket.send_angles)
            print("Degrees after inverse: ",deg)
            for req_position in range(3):
                Actuate.actuate_motors(req_position,deg[req_position+1])
        else:
            print("\nError during inverse kinematic calculation (of angles)\nfor coordinates: ",Coordinates[0],Coordinates[1],Coordinates[2])
    
# pos=kinematics.forward(60,37,54)
# print("Error Code: ",pos[0])
# print("Position 1: ",pos[1])
# print("Position 2: ",pos[2])
# print("Position 3: ",pos[3])
# x-axis max is 170
# z-axis max is 281
# deg=kinematics.inverse(0,0,-281)
# print("Error Code: ",deg[0])
# print("Angle 1:",deg[1])
# print("Angle 2:",deg[2])
# print("Angle 3:",deg[3])
# for simulink model where sagging=0 deg=90-deg
# # for 0 degree step count is 2048
# # deg=[0,-2,-2,-2]
# steps=kinematics.convert_deg_to_steps(deg)
# print(steps)