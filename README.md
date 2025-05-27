# Python-DC-Motor-Control-Library-for-Raspberry-Pi

Welcome to the DC Motor Control Library designed for the Raspberry Pi 4 with Python. This library provides robust functionality for controlling DC motor position (i.e. angle) using PID control. To successfully use and understand this library, you'll need to understand the basics about brushed DC motors, incremental motor encoders, basics about using a Raspberry Pi and micro-controller programming, and control systems especially PID control.

# Introductory Concepts

PID Control: The library incorporates PID (Proportional-Integral-Derivative) for conrolling position. PID controllers use feedback from encoders to adjust motor commands dynamically, ensuring stable and accurate motor control, particularly under varying load conditions. These parameters can be optimized for specific motor loads (e.g. connecting motor to wheel subject to heavy load).

Pulse Width Modulation (PWM): PWM is an effective way to control motor speed and direction by varying the width of the pulses, enabling precise adjustments in motor operations. PWM varies the intensity of the voltage to the motor. 

Interrupts: Handling real-time events accurately is crucial in motor control. This library uses interrupts from the encoder to read current motor position in relation to the desired position. This is used as input for the controller. 

DC Motor with Encoder: Encoders provide necessary feedback for accurate control over motor position and speed, which is indispensable for closed-loop control systems.

For more information about controlling DC brushed motors with encoders, refer to the following source: https://curiores.com/positioncontrol

# Features

Port Mapping and Instantiation: The library provides a class where you can configure port mappings for setting up PWM (pulse width modulation) output pins and input pins for motor encoder in the Raspberry Pi 4.

Control Methods: Utilize intuitive control methods such as `.move(degrees)` to specify precise motor movements, enhancing ease of use in motor management tasks.

PID Parameters Customization: The library offers flexibility in defining PID control parameters, enabling you to fine-tune the motor control system tailored to your project's requirements. Additionally, class instantiation comes with pre-defined values for PID, gpio pin mappings, and others. It is recommended to take a look at the class and see what comes pre-configured. These values can be changed during instantiation simply specifying the desired value in the instance arguement.

This library assumes the use of incremental motor encoders. For more information, refer to the following source: https://www.dynapar.com/technology/encoder_basics/motor_encoders/

# Example Hardware
You can use any motor driver or DC motors you wish, provided you understand how to use them and integrate them with the raspberry pi. For our example, the following hardware is used:

Motor driver : L298N https://www.cimech3d.cl/producto/driver-l298n-doble-accionamiento-para-arduino/

<div align="center">
  <img src="images/H-bridge-driver.jpg" alt="Alt Text"  width="500" height="auto">
</div>

Motor: DC brushed motor with incremental encoder:  https://www.amazon.com/uxcell-Motor-Encoder-463RPM-Ratio/dp/B0792T5445

<div align="center">
  <img src="images/dc_motor.png" alt="Alt Text"  width="500" height="auto">
</div>

# Getting started

1. Clone repo in desired folder. This must be done inside a Raspberry Pi (guaranteed to work under Raspberry pi 4).
2. Inside the folder, install a virtual environment (see: https://docs.python.org/3/library/venv.html)
3. Activate virtual environment using the command: `source /path/to/env/bin/activate`
4. install RPi.GPIO library using pip command: `pip install RPi.GPIO` (can use alternative package administrator though pip is recommended).
5. Test library as a module. In source folder, run: `python -m motor_module.motorclass` . This will run code inside `if __name__ == "__main__"`. Alternatively, you can test using the main.py file which direcrtly imports module.

# Example Code

Example instantiation where RaspberryPi pin mappings are specified:
`MotorInstance(PIN_PWM = 27,PIN_OUT1 = 1,PIN_OUT2 = 0,PIN_IN1 = 19,PIN_IN2 = 16)`

Note: This library uses the BCM pin convention at the moment. Library could be updated to handle both BCM and BOARD.

# Circuit schematic
Provided bellow is an example implementation of the hardware wiring between the Raspberry Pi 4, two DC brushed motors with their encoders, and the L298N motor driver. This library is not limited to the hardware used in the example implementation.

<div align="center">
  <img src="images/circuit_schematic.png" alt="Alt Text"  width="500" height="auto">
</div>
