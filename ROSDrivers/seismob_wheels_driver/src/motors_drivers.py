#!/usr/bin/python

from PCA9685 import PCA9685
import time
import tkinter as tk

direction = [
    'forward',
    'backward',
]

frontPwm = PCA9685(0x40, debug=True)
frontPwm.setPWMFreq(50)

backPwm = PCA9685(0x41, debug=True)
backPwm.setPWMFreq(50)

class FrontMotorDriver():
    def __init__(self):
        self.PWMA = 0
#        self.AIN1 = 1
#        self.AIN2 = 2
        self.AIN1 = 2
        self.AIN2 = 1
        self.PWMB = 5
# Change because my motors runs in different directions
        self.BIN1 = 3
        self.BIN2 = 4
#        self.BIN1 = 4
#        self.BIN2 = 3

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            frontPwm.setDutycycle(self.PWMA, speed)
            if(index == direction[0]):
                frontPwm.setLevel(self.AIN1, 0)
                frontPwm.setLevel(self.AIN2, 1)
            else:
                frontPwm.setLevel(self.AIN1, 1)
                frontPwm.setLevel(self.AIN2, 0)
        else:
            frontPwm.setDutycycle(self.PWMB, speed)
            if(index == direction[0]):
                frontPwm.setLevel(self.BIN1, 0)
                frontPwm.setLevel(self.BIN2, 1)
            else:
                frontPwm.setLevel(self.BIN1, 1)
                frontPwm.setLevel(self.BIN2, 0)

    def MotorSpeed(self, motor, speed):
        if speed > 100:
            return
        if(motor == 0):
            frontPwm.setDutycycle(self.PWMA, speed)
        else:
            frontPwm.setDutycycle(self.PWMB, speed)


    def MotorStop(self, motor):
        if (motor == 0):
            frontPwm.setDutycycle(self.PWMA, 0)
        else:
            frontPwm.setDutycycle(self.PWMB, 0)

class BackMotorDriver():
    def __init__(self):
        self.PWMA = 0
#        self.AIN1 = 1
#        self.AIN2 = 2
        self.AIN1 = 2
        self.AIN2 = 1
        self.PWMB = 5
# Change because my motors runs in different directions
        self.BIN1 = 3
        self.BIN2 = 4
#        self.BIN1 = 4
#        self.BIN2 = 3

    def MotorRun(self, motor, index, speed):
        if speed > 100:
            return
        if(motor == 0):
            backPwm.setDutycycle(self.PWMA, speed)
            if(index == direction[0]):
                backPwm.setLevel(self.AIN1, 0)
                backPwm.setLevel(self.AIN2, 1)
            else:
                backPwm.setLevel(self.AIN1, 1)
                backPwm.setLevel(self.AIN2, 0)
        else:
            backPwm.setDutycycle(self.PWMB, speed)
            if(index == direction[0]):
                backPwm.setLevel(self.BIN1, 0)
                backPwm.setLevel(self.BIN2, 1)
            else:
                backPwm.setLevel(self.BIN1, 1)
                backPwm.setLevel(self.BIN2, 0)

    def MotorSpeed(self, motor, speed):
        if speed > 100:
            return
        if(motor == 0):
            backPwm.setDutycycle(self.PWMA, speed)
        else:
            backPwm.setDutycycle(self.PWMB, speed)

    def MotorStop(self, motor):
        if (motor == 0):
            backPwm.setDutycycle(self.PWMA, 0)
        else:
            backPwm.setDutycycle(self.PWMB, 0)


class WheelDrive():
    def __init__(self):
        self.front_left = FrontMotorDriver()
        self.front_right = FrontMotorDriver()
        self.back_left =  BackMotorDriver()
        self.back_right = BackMotorDriver()

    def set_speed(self, motor_speed):
        self.front_left.MotorSpeed(0, motor_speed)
        self.front_right.MotorSpeed(1, motor_speed)
        self.back_left.MotorSpeed(0, motor_speed)
        self.back_right.MotorSpeed(1, motor_speed)

    def forward(self, speed=100, duration=None):
        self.front_left.MotorRun(0, 'forward', speed)
        self.front_right.MotorRun(1, 'forward', speed)
        self.back_left.MotorRun(0, 'forward', speed)
        self.back_right.MotorRun(1, 'forward', speed)

    def backward(self, speed=100, duration=None):
        self.front_left.MotorRun(0, 'backward', speed)
        self.front_right.MotorRun(1, 'backward', speed)
        self.back_left.MotorRun(0, 'backward', speed)
        self.back_right.MotorRun(1, 'backward', speed)

    def right(self, speed=100, duration=None):
        self.front_left.MotorRun(0, 'forward', speed)
        self.front_right.MotorRun(1, 'backward', speed)
        self.back_left.MotorRun(0, 'backward', speed)
        self.back_right.MotorRun(1, 'forward', speed)

    def left(self, speed=100, duration=None):
        self.front_left.MotorRun(0, 'backward', speed)
        self.front_right.MotorRun(1, 'forward', speed)
        self.back_left.MotorRun(0, 'forward', speed)
        self.back_right.MotorRun(1, 'backward', speed)

    def set_motors(self, front_right_direction, front_right_speed,
                         front_left_direction,  front_left_speed,
                         back_right_direction, back_right_speed,
                         back_left_direction,  back_left_speed):
        self.front_right.MotorRun(0, front_right_direction, front_right_speed)
        self.front_left.MotorRun(1, front_left_direction, front_left_speed)
        self.back_right.MotorRun(0, back_right_direction, back_right_speed)
        self.back_left.MotorRun(1, back_left_direction, back_left_speed)

    def stop(self):
        self.front_left.MotorStop(0)
        self.front_right.MotorStop(1)
        self.back_left.MotorStop(0)
        self.back_right.MotorStop(1)


if __name__ == "__main__":
    truck = WheelDrive()

    start_speed = 10

    def change_speed(value=None):
        truck.set_speed(speed.get())
        print(speed.get())

    def on_move_forward():
        frontPwm.write(0x00, 0x00)
        backPwm.write(0x00, 0x00)
        truck.forward(start_speed)
        print("Move forward!")

    def on_move_backward():
        frontPwm.write(0x00, 0x00)
        backPwm.write(0x00, 0x00)
        truck.backward(start_speed)
        print("Move backward!")

    def on_move_right():
        frontPwm.write(0x00, 0x00)
        backPwm.write(0x00, 0x00)
        truck.right(start_speed)
        print("Move right!")

    def on_move_left():
        frontPwm.write(0x00, 0x00)
        backPwm.write(0x00, 0x00)
        truck.left(start_speed)
        print("Move left!")

    def on_stop():
        truck.stop()
        print("STOP!")

    window = tk.Tk()
    window.geometry("500x230")
    speedlabel = tk.Label(text="Speed")
    speedlabel.pack()
    speed = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL,
                     command = change_speed)
    speed.set(start_speed)


    speed.pack(fill=tk.X)

    forwardbtn = tk.Button(window, text="Forward", command=on_move_forward)
    forwardbtn.pack(fill=tk.X)

    backwardbtn = tk.Button(window, text="Backward", command=on_move_backward)
    backwardbtn.pack(fill=tk.X)

    rightbtn = tk.Button(window, text="Right", command=on_move_right)
    rightbtn.pack(fill=tk.X)

    leftbtn = tk.Button(window, text="Left", command=on_move_left)
    leftbtn.pack(fill=tk.X)

    stopbtn = tk.Button(window, text="Stop", bg="red", command=on_stop)
    stopbtn.pack(fill=tk.X)

    window.mainloop()















    #truck.forward()
    #time.sleep(3)
    #truck.stop()
    #time.sleep(1)
    #truck.backward()
    #time.sleep(3)
    #truck.stop()
    #truck.right()
    #time.sleep(3)
    #truck.forward()
    #time.sleep(3)
    #truck.left()
    #time.sleep(3)
    #truck.set_speed(50)
    #time.sleep(3)
    #truck.set_speed(10)
    #time.sleep(3)
    #truck.stop()

    '''
    time.sleep(1)
    truck.forward()
    time.sleep(3)
    truck.stop()
    time.sleep(2)
    truck.forward()
    time.sleep(2)
    truck.stop()
    truck.backward()
    time.sleep(3)
    truck.stop()
    truck.backward()
    time.sleep(2)
    truck.stop()
    '''

'''
print("this is a motor driver test code")
Motor = BackMotorDriver()

print("forward 2 s")
Motor.MotorRun(0, 'forward', 100)
Motor.MotorRun(1, 'forward', 100)
time.sleep(2)

print("backward 2 s")
Motor.MotorRun(0, 'backward', 100)
Motor.MotorRun(1, 'backward', 100)
time.sleep(2)

print("stop")
Motor.MotorStop(0)
Motor.MotorStop(1)
'''
