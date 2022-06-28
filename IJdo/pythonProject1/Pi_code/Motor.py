import RPi.GPIO as GPIO
import time as time
import robothond
import UDP


class motor:
    def __init__(self, motorIN1, motorIN2, motorIN3, motorIN4, motorPWM1, motorPWM2):
        GPIO.setmode(GPIO.BCM)
        self.MotorIN1 = motorIN1
        self.MotorIN2 = motorIN2
        self.PWM1 = motorPWM1
        self.MotorIN3 = motorIN3
        self.MotorIN4 = motorIN4
        self.PWM2 = motorPWM2
        self.Odometry = 0

        GPIO.setup(self.MotorIN1, GPIO.OUT)
        GPIO.setup(self.MotorIN2, GPIO.OUT)
        GPIO.setup(self.PWM1, GPIO.OUT)
        self.pi_pwm1 = GPIO.PWM(self.PWM1, 1000)  # create PWM instance with frequency
        self.pi_pwm1.start(0)

        GPIO.setup(self.MotorIN3, GPIO.OUT)
        GPIO.setup(self.MotorIN4, GPIO.OUT)
        GPIO.setup(self.PWM2, GPIO.OUT)
        self.pi_pwm2 = GPIO.PWM(self.PWM2, 1000)  # create PWM instance with frequency
        self.pi_pwm2.start(0)

    def correct_right(self, speed):
        GPIO.output(self.MotorIN1, GPIO.LOW)  # motor1(rechts)staat stil
        GPIO.output(self.MotorIN2, GPIO.LOW)
        GPIO.output(self.MotorIN3, GPIO.HIGH)  # motor2(links)draait vooruit
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        # time.sleep(duration)
        # self.pi_pwm1.ChangeDutyCycle(50)
        # self.pi_pwm2.ChangeDutyCycle(50)
        # GPIO.output(self.MotorIN1, GPIO.LOW)
        # GPIO.output(self.MotorIN2, GPIO.LOW)
        # GPIO.output(self.MotorIN3, GPIO.LOW)
        # GPIO.output(self.MotorIN4, GPIO.LOW)

    def correct_left(self, speed):
        GPIO.output(self.MotorIN1, GPIO.LOW)
        GPIO.output(self.MotorIN2, GPIO.HIGH)  # motor1(recths) draait vooruit
        GPIO.output(self.MotorIN3, GPIO.LOW)
        GPIO.output(self.MotorIN4, GPIO.LOW)  # motor2(links)staat stil
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        # time.sleep(duration)
        # self.pi_pwm1.ChangeDutyCycle(50)
        # self.pi_pwm2.ChangeDutyCycle(50)
        # GPIO.output(self.MotorIN1, GPIO.LOW)
        # GPIO.output(self.MotorIN2, GPIO.LOW)
        # GPIO.output(self.MotorIN3, GPIO.LOW)
        # GPIO.output(self.MotorIN4, GPIO.LOW)

    def Drive_forward(self, speed):
        GPIO.output(self.MotorIN1, GPIO.LOW)  # Motor1(rechts) forward laten rijden is In1 laag en In2 hoog
        GPIO.output(self.MotorIN2, GPIO.HIGH)
        GPIO.output(self.MotorIN3, GPIO.HIGH)  # motor2(links) forward latenrijden is in3 hoog en in4 laag
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        # time.sleep(0.01)
        # m1 = GPIO.PWM(18, 1)
        # m2 = GPIO.PWM(13, 1)
        # m1.start(speed)
        # m2.start(speed)
        # time.sleep(duration)
        # GPIO.output(self.MotorPWM1, GPIO.HIGH)
        # GPIO.output(self.MotorPWM2, GPIO.HIGH)
        # GPIO.PWM(self.MotorPWM2, GPIO.HIGH)
        # GPIO.output(self.MotorIN1, GPIO.LOW)
        # GPIO.output(self.MotorIN2, GPIO.LOW)
        # GPIO.output(self.MotorIN3, GPIO.LOW)
        # GPIO.output(self.MotorIN4, GPIO.LOW)
        # self.pi_pwm1.ChangeDutyCycle(50)
        # self.pi_pwm2.ChangeDutyCycle(50)
        # GPIO.PWM(self.MotorPWM1, GPIO.LOW)
        # GPIO.PWM(self.MotorPWM2, GPIO.LOW)

    def Turn_left(self, speed, duration):
        GPIO.output(self.MotorIN1, GPIO.LOW)
        GPIO.output(self.MotorIN2, GPIO.HIGH)
        GPIO.output(self.MotorIN3, GPIO.LOW)
        GPIO.output(self.MotorIN4, GPIO.HIGH)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        time.sleep(duration)
        # GPIO.output(self.MotorIN1, GPIO.LOW)
        # GPIO.output(self.MotorIN2, GPIO.LOW)
        # GPIO.output(self.MotorIN3, GPIO.LOW)
        # GPIO.output(self.MotorIN4, GPIO.LOW)
        # self.pi_pwm1.ChangeDutyCycle(0)
        # self.pi_pwm2.ChangeDutyCycle(0)

        self.Odometry = (self.Odometry + 90) % 360

    def Turn_right(self, duration, speed):
        GPIO.output(self.MotorIN1, GPIO.HIGH)
        GPIO.output(self.MotorIN2, GPIO.LOW)
        GPIO.output(self.MotorIN3, GPIO.HIGH)
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(speed)
        self.pi_pwm2.ChangeDutyCycle(speed)
        time.sleep(duration)
        GPIO.output(self.MotorIN1, GPIO.LOW)
        GPIO.output(self.MotorIN2, GPIO.LOW)
        GPIO.output(self.MotorIN3, GPIO.LOW)
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(0)
        self.pi_pwm2.ChangeDutyCycle(0)
        self.Odometry = (self.Odometry + 270) % 360

    def Stop(self):
        GPIO.output(self.MotorIN1, GPIO.LOW)
        GPIO.output(self.MotorIN2, GPIO.LOW)
        GPIO.output(self.MotorIN3, GPIO.LOW)
        GPIO.output(self.MotorIN4, GPIO.LOW)
        self.pi_pwm1.ChangeDutyCycle(0)
        self.pi_pwm2.ChangeDutyCycle(0)
        # time.sleep(duration)


if __name__ == "__main__":
    print("Main")
    IN1Motor1 = 6
    IN2Motor1 = 5
    PWM1 = 13
    IN3Motor2 = 21
    IN4Motor2 = 20
    PWM2 = 18

    Motor1 = motor(IN1Motor1, IN2Motor1, IN3Motor2, IN4Motor2, PWM1, PWM2)
    Ultrasoon_front = robothond.Ultrasonic_sensor(26, 24)
    Ultrasoon_right = robothond.Ultrasonic_sensor(19, 16)
    Ultrasoon_left = robothond.Ultrasonic_sensor(12, 23)
    UDP_socket = UDP.UDP_Socket('192.168.203.128', 65000)  # 192.168.55.128 mobiele hotspot ijdo
    # distance = Ultrasoon_front.distance()
    # distance = Ultrasoon_right.distance()
    # distance = Ultrasoon_left.distance()

    try:

        while True:
            # for i in range(11):
            # Motor1.Drive_forward(0.1)
            #            Motor1.Turn_left(0.3)
            #            Motor1.Turn_right(0.3)

            distance_front = ((
                                          Ultrasoon_front.distance() + Ultrasoon_front.distance() + Ultrasoon_front.distance() + Ultrasoon_front.distance()) / 4)

            distance_left = ((
                                         Ultrasoon_left.distance() + Ultrasoon_left.distance() + Ultrasoon_left.distance() + Ultrasoon_left.distance()) / 4)

            distance_right = ((
                                          Ultrasoon_right.distance() + Ultrasoon_right.distance() + Ultrasoon_right.distance() + Ultrasoon_right.distance()) / 4)
            # time.sleep(0.01)
            UDP_socket.pack_float(distance_front, distance_left, distance_right, 0, 1)

            Motor1.Drive_forward(55)
            time.sleep(0.14)

            if distance_front <= 10:
                Motor1.Stop()
                # time.sleep(0.2)
                # left = Motor1.Turn_left(1)
                # time.sleep(0.2)
                # distance = Ultrasoon_front.distance()
                # distance = Ultrasoon_right.distance()
                # distance = Ultrasoon_left.distance()
                # UDP_socket.pack_float(distance, left)


    except KeyboardInterrupt:
        print("meeting gestopt")
        UDP_socket.pack_float(distance_front, distance_left, distance_right, 0, 0)
        GPIO.cleanup()



