from motor_module.motorclass import MotorInstance
from time import sleep

M1 = MotorInstance() #instanciate motor 1
print(M1)

M2 = MotorInstance(PIN_PWM = 27,PIN_OUT1 = 1,PIN_OUT2 = 0,PIN_IN1 = 19,PIN_IN2 = 16) #instanciate motor 2
print(M2)

M1.move(720)
sleep(3)
M1.move(720)

sleep(3)

M2.move(720)
sleep(3)
M2.move(720)
