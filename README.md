
# Quality Control of Products using 4-DOF Delta Robot





## Introduction

A Delta Robot is a type of parallel robotic manipulator known for its high-speed and precise motion capabilities. Unlike traditional serial robotic manipulators, which use a series of connected joints and links, Delta Robots employ a parallel mechanism with multiple arms connected to a common base. This design allows for greater agility, reduced inertia, and improved performance in high-speed applications, making them ideal for tasks that require rapid and accurate movements. The 4-DOF Delta Robot for Quality Control presented here harnesses these unique characteristics to carry out quality control operations efficiently.


## Problem Description
The problem is to develop a solution for pick and place operations in industrial settings using a delta robot. The objective is to create a system that can efficiently and accurately pick up objects from one location and place them in another, based on predefined parameters or instructions. The solution should be designed to handle various types of objects, sizes, and weights commonly found in industrial environments.

The system needs to be reliable, capable of operating for extended periods without significant downtime. It should also be versatile, allowing for easy adaptation to different production lines or processes. The solution should offer precise control and positioning, ensuring that objects are picked up and placed with high accuracy and repeatability.

Efficiency is a key requirement, as the solution should optimize the pick and place operations to minimize cycle times and increase overall productivity. It should be capable of handling a high volume of objects within a given time frame, while maintaining quality and safety standards.

Integration with existing manufacturing systems and equipment is crucial. The solution should be compatible with industry-standard protocols and interfaces, enabling seamless communication and coordination with other machinery or control systems. Additionally, the solution should be user-friendly, providing intuitive interfaces for operators to monitor and control the pick and place operations effectively.

## Problem Statement
Develop a Cost and Power-efficient 4-DOF Delta Robot which can be used for the inspection and quality control of QR Code Equipped Industrial packages by referring to required dimensions stored in the database model. The segregated packages need to be sent back for re-evaluation.
## Features and Capabilities
- 4 degrees of freedom (4-DOF)
- Precise and accurate performance for quality control operations
- Dimension-based item classification
- Payload capacity of 100 grams, allowing for versatility in handling different products

#### Capabilities
1. Autonomous Operation
 - Detecting the Product
 - Differentiate betweenfaulty and non-faulty
 - Determining the position of the product w.r.t the conveyer
 - Pick Product
 - Handle Product
 - Deliver Product
 - Intersystem Communication
 - Database Management
2. Safety
 - Pick Product Safely
 - Handle Product Safely
 - Place Product Safely
 - Facilitates emergency STOP feature
3. Standby Mode
4. Easy adaptability to newer environment
## Dependencies
1. **Book Reference:** "Practical Model-Based System Engineering" by Carlos Hernandez and Jose L. Fernandez. This book served as a valuable resource for adopting a systematic approach in our project. It guided us in identifying the project's needs and defining its capabilities. 
2. **MATLAB:** 
 - Simulink: The project utilizes Simulink, an extension of MATLAB, for system-level modeling and simulation of the Delta Robot's control system. Simulink diagrams are used to visualize the robot's behavior and test control strategies in a virtual environment.

 - Simscape: Simscape, a part of the MATLAB/Simulink ecosystem, is utilized to model the physical dynamics of the Delta Robot in a multi-domain simulation environment. It allows for the accurate representation of the robot's mechanical, electrical, and hydraulic components, enabling realistic simulation of the robot's motion and behavior.
 - System Composer: The project leverages System Composer, a powerful tool in the MATLAB/Simulink ecosystem, for modeling and analyzing the system architecture and requirements. System Composer helps us gain a comprehensive understanding of the Delta Robot's behavior, interactions between components, and supports our systematic approach to system engineering.
3. **SolidWorks:** A 3D computer-aided design (CAD) software used for mechanical and product design. SolidWorks was employed to create detailed models of the Delta Robot's physical components and analyze their mechanical behavior.
4. **Trossen Robotics Community Guide:** A valuable resource used for programming the Delta Robot. This guide provides essential information, code examples, and best practices for effectively controlling and integrating the Delta Robot into various applications.
5. Marginally Clever Rotary Delta Robot Forward/Inverse Kinematics Calculator
6. Proto G Engineering. “Simplified Delta Robot Kinematics Equations”, YouTube, Feb. 11, 2018[Video File]. Available: https://www.youtube.com/watch?v=FTRCwuAnr6o&t=57s&ab_channel=ProtoGEngineering
7. **Dynamixel Wizard 2.0:**  A software tool provided by Dynamixel for configuring and managing Dynamixel servos used in the Delta Robot. Dynamixel Wizard 2.0 allows for easy setup, calibration, and fine-tuning of the servos to achieve precise movements and control.
