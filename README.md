# Intro Project: PIR Motion Sensor and Raspberry Pi (RPi) Connection
This is a basic, intro project, explaining that how to connect Raspberry Pi with PIR Motion Sensor.

## Raspberry Pi (RPi)
In this intro project, I have used "Raspberry Pi 3 Model B V1.2" board. 

OS is "Raspbian - Jessie (8)"

Python installed in this OS: Python 2.7.9

|![Raspberry Pi 3 Model B V1.2](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/RPi_modelName.jpg) | 
|:--:| 
| *Raspberry Pi 3 Model B V1.2* |

## PIR Motion Sensor
PIR (Passive Infrared) Motion Sensor, available on Amazon. Several blogs are live on Internet for the details of this sensor. Hence, I am sharing few crucial details about this sensor:
1. Range: up to 10 meters (approx.), but sensitivity is good up to 6 meters
2. Angular Coverage: 70° to 110°
3. Power Required: 3.3V to 5V

Following is the picture of PIR Motion Sensor used here:

|![PIR Motion Sensor Front Side](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/motionSensor_frontSide.jpg) |![PIR Motion Sensor Back Side](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/motionSensor_backSide.jpg) |
|:--:|:--:|
| *PIR Motion Sensor Front Side* | *PIR Motion Sensor Back Side* |

PIR Motion Sensors have three pins:
1. VCC
2. OUT
3. GND

What I have noticed is that, these pin names are mentioned on the board of sensor, which is generally covered by the plastic globe. If we remove this plastic globe, then we can easily see the name of these pins:

|![PIR Motion Sensor - PIN Name](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/motionSensor_front_pinName.jpg) | 
|:--:| 
| *PIR Motion Sensor - PIN Name* |

## PIR Motion Sensor and Raspberry Pi (RPi) connection

|![Raspberry Pi - PIN layout](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/gpio-pinout.jpg) | 
|:--:| 
| *Raspberry Pi - PIN layout* |

As per above pin layout of Raspberry Pi, connections are made as following:
1. VCC pin of PIR Motion Sensor -> Pin 2 (+5V) of RPi
2. OUT pin of PIR Motion Sensor -> Pin 11 (GPIO) of RPi 
3. GND pin of PIR Motion Sensor -> Pin 6 (GND) of RPi

|![1. PIR Motion Sensor and RPi Connection](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/motionSensor_RPi_connection.jpg) |![2. PIR Motion Sensor and RPi Connection](https://github.com/sansinghsanjay/PIRMotionSensor_RPi_Connection/blob/master/images/motionSensor_RPi_connections.jpg) |
|:--:|:--:|
| *1. PIR Motion Sensor and RPi Connection* | *2. PIR Motion Sensor and RPi Connection* |
