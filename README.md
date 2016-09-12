#Reactor Control System
Andrew Marone  
Chris Enoch

##Installation
Nothing needed to set up the application

##Running the Application:
1. Run reactor_control.py

##Description
Demonstrates failure detection of critical system components by utilizing a heartbeat
pattern accross multiple processes. 

Upon detection of failure, the system will output the following message:
'Human input is needed to perform maintenance tasks'

##Critical Components:
- Control Rods
- Cooling Pump

##Quality Attributes:

_**Control Rods**_  
**Source**: Internal   
**Stimulus**: Omission  
**Environment**: Normal  
**Artifact**: Control Rod Management Process  
**Response**: Notify   
**Response Measure**: Failure Detected within 2 seconds  

**RQ1**: Control Rod Management Process shall notify the plant control room of process failure within 2 seconds

_**Cooling Pump**_  
**Source**: Internal   
**Stimulus**: Omission  
**Environment**: Normal  
**Artifact**: Cooling Pump Management Process 
**Response**: Restart Coolant_Pump process and notify plant control room  
**Response Measure**: Failure detected and service restarted within 5 seconds

**RQ2**: Coolant pump shall be restarted and notify the plant control room within 5 seconds of failure
