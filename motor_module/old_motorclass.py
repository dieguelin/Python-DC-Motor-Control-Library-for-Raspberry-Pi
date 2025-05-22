import RPi.GPIO as gpio
import time as t

class MotorInstance:

    def __init__(self,PIN_PWM = 18,PIN_OUT1 = 25,PIN_OUT2 = 9,PIN_IN1 = 22,PIN_IN2 = 23,
                  freq = 50, kp = 2.1, kd = 0.05, ki = 0, Ts = 0.01, revs = 492, n = 100, count = 0):

        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

        self.PIN_PWM = PIN_PWM
        self.PIN_OUT1 = PIN_OUT1
        self.PIN_OUT2 = PIN_OUT2
        self.PIN_IN1 = PIN_IN1
        self.PIN_IN2 = PIN_IN2
        self.freq = freq
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.Ts = Ts
        self.revs = revs
        self.n = n
        self.count = count

        gpio.setup(self.PIN_OUT1,gpio.OUT)
        gpio.setup(self.PIN_OUT2,gpio.OUT)
        gpio.setup(self.PIN_PWM,gpio.OUT)
        self.pwm_in = gpio.PWM(PIN_PWM,freq)
        gpio.setup(self.PIN_IN1,gpio.IN)
        gpio.setup(self.PIN_IN2,gpio.IN)
        gpio.add_event_detect(self.PIN_IN1, gpio.RISING, callback=self.cb)

    def forward(self):
        gpio.output(self.PIN_OUT1,True)
        gpio.output(self.PIN_OUT2,False)

    def backward(self):
        gpio.output(self.PIN_OUT1,False)
        gpio.output(self.PIN_OUT2,True)

    def stop_motor(self):
        gpio.output(self.PIN_OUT1,False)
        gpio.output(self.PIN_OUT2,False)

    def cb(self,channel):
        # global cnt
        if gpio.event_detected(channel):
            if gpio.input(self.PIN_IN2):
                #print('cw')
                self.count += 1
                #print(cnt)
            else:
                #print('ccw')
                self.count -= 1
                #print(cnt)
        else:
            self.count += 0
            #print(cnt)
        return self.count

    def move(self, deg):

        self.count = 0
        Eacum = 0
        x = deg*self.revs/360 
        E = [x]
        # e = x
        self.pwm_in.start(0)
        stopper = False
            
        while not stopper:
            
            t.sleep(self.Ts) 
            pos = self.cb(self.PIN_IN1) # lectura posicion
            e=x-pos #error
            # print(x)
            # print(pos)
            e=round(e,1)        
            #parte integral
            Eacum += e
            #parte derivativa:
            E.append(e)
            d_e = (E[-1] - E[-2]) / self.Ts #retrieve last 2 values of array.
            
            #PID:
            P = self.kp*e
            D = self.kd*d_e
            I = self.ki*Eacum
            u = P + I + D #control law
            u =round(u,2)

            if abs(u) <= 100:
                if u >= 0: 
                    if u > self.n:
                        u = self.n
                        self.pwm_in.ChangeDutyCycle(u)
                        self.forward()
                        
                    else:
                        self.pwm_in.ChangeDutyCycle(u)
                        self.forward()
                else:
                    u = abs(u)
                    if u > self.n:
                        u = self.n
                        self.pwm_in.ChangeDutyCycle(u)
                        self.backward()
                    else: 
                        self.pwm_in.ChangeDutyCycle(u)
                        self.backward()
            else:
                if u > 0: 

                    u = self.n
                    self.pwm_in.ChangeDutyCycle(u)
                    self.forward()

                else:
                    u= self.n
                    self.pwm_in.ChangeDutyCycle(u)
                    self.backward()
            
            #print('pos: ',str(pos),', error: ', \
            #    str(e),', control law: ',str(u))
            
            if (len(E) >= 50):
                E.pop(0)
                
                if (e <= 7):
                    j2 = len(E)            
                    stopper = E[j2-1] == E[j2-2] == E[j2-3] == E[j2-4] == E[j2-5] \
                            == E[j2-6] == E[j2-7] == E[j2-8] == E[j2-9] == E[j2-10] \
                            == E[j2-11] == E[j2-12] == E[j2-13] == E[j2-14] == E[j2-15]                    
    
        self.stop_motor() #stop motor once we get to desired position


if __name__ == "__main__":
    print("hello from module")
    myinstance = MotorInstance()
    print(myinstance.pwm_in)
    myinstance.move(30)
    myinstance.move(30)
