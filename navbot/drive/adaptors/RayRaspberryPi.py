import RPi.GPIO as GPIO

from navbot.drive.DriveController import DriveController

class RayRaspberryPi(DriveController):
    
    def __init__(self):
        super(RayRaspberryPi, self).__init__()
        
        # Setting up pins for connecting Motor Controller to Raspberry Pi GPIO pins
        self.MOTOR1A = 16
        self.MOTOR1B = 18
        self.MOTOR1E = 22
        self.MOTOR2A = 19
        self.MOTOR2B = 21
        self.MOTOR2E = 23
    
    def __enter__(self):
        ''' Here we'll start the connection to the Pi GPIO pins '''
        
        super(RayRaspberryPi, self).__enter__()
        
        # GPIO module is special - just one to controller the Pi
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(self.MOTOR1A,GPIO.OUT)
        GPIO.setup(self.MOTOR1B,GPIO.OUT)
        GPIO.setup(self.MOTOR1E,GPIO.OUT)
        
        GPIO.setup(self.MOTOR2A,GPIO.OUT)
        GPIO.setup(self.MOTOR2B,GPIO.OUT)
        GPIO.setup(self.MOTOR2E,GPIO.OUT)
        
    def __exit__(self, exc_type, exc_value, traceback):
        ''' Should clean up the GPIO connection to the raspberry pi
        '''
        GPIO.cleanup()
        
        
    def _right_wheel(self, direction):
        if direction == 0:
            GPIO.output(self.MOTOR2E,GPIO.LOW)
        
        if direction > 0:
            GPIO.output(self.MOTOR2A,GPIO.LOW)
            GPIO.output(self.MOTOR2B,GPIO.HIGH)
            GPIO.output(self.MOTOR2E,GPIO.HIGH)
            
        if direction < 0:
            GPIO.output(self.MOTOR2A,GPIO.HIGH)
            GPIO.output(self.MOTOR2B,GPIO.LOW)
            GPIO.output(self.MOTOR2E,GPIO.HIGH)
    
    
    def _left_wheel(self, direction):
        if direction == 0:
            GPIO.output(self.MOTOR1E,GPIO.LOW)
        
        if direction > 0:
            GPIO.output(self.MOTOR1A,GPIO.LOW)
            GPIO.output(self.MOTOR1B,GPIO.HIGH)
            GPIO.output(self.MOTOR1E,GPIO.HIGH)
            
        if direction < 0:
            GPIO.output(self.MOTOR1A,GPIO.HIGH)
            GPIO.output(self.MOTOR1B,GPIO.LOW)
            GPIO.output(self.MOTOR1E,GPIO.HIGH)
    
    def move_forward(self):
        self._left_wheel(10)
        self._right_wheel(10)
    
    def move_backwards(self):
        self._left_wheel(-10)
        self._right_wheel(-10)
    
    def move_right(self):
        self._left_wheel(10)
        self._right_wheel(0)
    
    def move_left(self):
        self._right_wheel(10)
        self._left_wheel(0)
    
    def stop(self):
        self._left_wheel(0)
        self._right_wheel(0)
        
    def spin_left(self):
        self._left_wheel(-10)
        self._right_wheel(10)
    
    def spin_right(self):
        self._left_wheel(10)
        self._right_wheel(-10)