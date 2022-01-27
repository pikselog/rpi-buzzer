import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24
BUZZER = 4
LED = 26

print ("HC-SR04 mesafe sensoru")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

while True:

  GPIO.output(TRIG, False)
  print ("Olculuyor...")
  time.sleep(1)

  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150
  distance = round(distance, 2)

  if distance > 2 and distance < 70:
    print ("Mesafe:",distance - 0.5,"cm")
    GPIO.output(BUZZER,GPIO.HIGH)
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(BUZZER,GPIO.LOW)
    GPIO.output(LED,GPIO.LOW)
  else:
    print ("Menzil asildi")
    GPIO.output(BUZZER,GPIO.LOW)
    