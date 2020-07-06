#!/usr/bin/env python
from seismob_wheels_driver.srv import WheelsSettings
from motors_drivers import WheelDrive
import time
import rospy


def handle_wheels_directions(req):
#	print(type(req))
#	print(dir(req))
#	print(req.directions)
#	print(req.directions[0])
#	print(req.directions[1])
	print(req.directions[0])
	print(req.directions[1])
	print(req.directions[2])
	print(req.directions[3])
	print(req.speeds[0])
	print(req.speeds[1])
	print(req.speeds[2])
	print(req.speeds[3])
	print(type(req.directions[0]))
	print(type(str(req.directions[0])))
	print(type(req.speeds[0]))
	print(type(int(req.speeds[0])))
	if all(speed == 0 for speed in (req.speeds[0], req.speeds[1],
					req.speeds[2], req.speeds[3])):
		robo_body.stop()
	else:
		robo_body.set_motors(req.directions[0], req.speeds[0],
				     req.directions[1], req.speeds[1],
				     req.directions[2], req.speeds[2],
				     req.directions[3], req.speeds[3])
#	time.sleep(1)
#	robo_body.stop()
#	robo_body.front_right.MotorStop(0)
#	robo_body.front_left.MotorStop(1)
#	robo_body.set_motors(req.directions[0], req.speeds[0],
#			     req.directions[1], req.speeds[1],
#			     req.directions[2], req.speeds[2],
#			     req.directions[3], req.speeds[3])
	return True

def wheels_settings_server():
	rospy.init_node('wheels_settings_server')
	s = rospy.Service('wheels_settings_server', WheelsSettings, handle_wheels_directions)
	rospy.spin()

if __name__ == "__main__":
	robo_body = WheelDrive()
	wheels_settings_server()
