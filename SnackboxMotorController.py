import tornado.ioloop
import tornado.web
import asyncio
import time
import RPi.GPIO as GPIO

from ajsonrpc.backend.tornado import JSONRPCTornado
from typing import final

api = JSONRPCTornado()

SERVO_PIN: final = 23

SERVO_MIN_ANGLE_PULSE: final = 0.00045
SERVO_MAX_ANGLE_PULSE: final = 0.0025

SERVO_PULSE_INTERVAL: final = 0.02

SNACKBOX_OPEN_PERCENTAGE: final = 8
SNACKBOX_CLOSED_PERCENTAGE: final = 0


def Pulse(pinNumber, highTime, lowTime):
    GPIO.output(pinNumber, GPIO.HIGH)
    time.sleep(highTime)

    GPIO.output(pinNumber, GPIO.LOW)
    time.sleep(lowTime)


async def ServoPulse(position):
    delayDuration = SERVO_MIN_ANGLE_PULSE + ((SERVO_MAX_ANGLE_PULSE - SERVO_MIN_ANGLE_PULSE) * position) / 100
    Pulse(SERVO_PIN, delayDuration, SERVO_PULSE_INTERVAL)


async def MotorTask():
    global ServoRotationPercentage, ServoRotationLock
    while True:
        ServoRotationLock.acquire()
        await ServoPulse(ServoRotationPercentage)
        await asyncio.sleep(0.1)
        ServoRotationLock.release()


def RunMotorTask():
    asyncio.run(MotorTask())


@api.add_function
async def Lock():
    for i in range(50):
        await ServoPulse(SNACKBOX_OPEN_PERCENTAGE)
    return 0

@api.add_function
async def Unlock(UnlockTimeMS: int):
    for i in range(50):
        await ServoPulse(SNACKBOX_CLOSED_PERCENTAGE)
    return 0


def SetupWebApp():
    return tornado.web.Application([
        (r"/rpc", api.handler),
    ])


def SetupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(0)
    GPIO.setup(SERVO_PIN, GPIO.OUT)


def Main():
    SetupGPIO()

    app = SetupWebApp()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    Main()
