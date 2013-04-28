#-*- coding:utf8 -*-
#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
def get_params(b):
	#  Light(b, PORT_4).set_illuminated(False)
	light=Light(b, PORT_4).get_sample())# Вывод на экран сообщения о состоянии датчика света? (2 состояния: активное и пассивное)
	#  Light(b, PORT_4).get_input_values())
	#  Light(b, PORT_4).get_lightness())
	button=Touch(b, PORT_3).get_sample())
	ultrasonic=Ultrasonic(b, PORT_1).get_sample())
	sound=Sound(b, PORT_2).get_sample())
	return light, button, ultrasonic, sound

