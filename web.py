from bottle import route, run, template, request

class aquarii:

	class manual:
		heater = bool
		fan = bool
		lamp = bool
		led = int
		buzz = bool

	class temperature:
		actual = int
		sensitivity = int
		extreme = int
		desired = int
		def heater(self):
			return self.actual < self.desired - self.sensitivity
		def fan(self):
			return self.actual > self.desired + self.sensitivity
		def emergency(self):
			return self.actual < self.desired - self.extreme or self.actual > self.desired +self.extreme

	# class illumination:

	class salinity:
		actual = int
		maximum = int
		def emergency(self):
			return self.actual > self.maximum

	level = bool

	def buzzer(self):
		return self.temperature.emergency(self.temperature) or self.salinity.emergency(self.salinity) or not self.level

	def __init__(
		self,
		manual_enabled,
		manual_heater,
		manual_fan,
		manual_lamp,
		manual_led,
		manual_buzz,
		temp_default,
		temp_sensitivity,
		temp_extreme,
		temp_desired,
		sal_actual,
		sal_maximum,
		level
	):
		self.manual.enabled = manual_enabled
		self.manual.heater = manual_heater
		self.manual.fan = manual_fan
		self.manual.lamp = manual_lamp
		self.manual.led = manual_led
		self.manual.buzz = manual_buzz
		self.temperature.actual = temp_default
		self.temperature.sensitivity = temp_sensitivity
		self.temperature.extreme = temp_extreme
		self.temperature.desired = temp_desired
		self.salinity.actual = sal_actual
		self.salinity.maximum = sal_maximum
		self.level = level

aquarium = aquarii(
	False,				#manual_enabled
	True,				#manual_heater
	False,				#manual_fan
	True,				#manual_lamp
	255,				#manual_led
	False,				#manual_buzz
	23,					#temp_default
	2,					#temp_sensitivity
	4,					#temp_extreme
	13,					#temp_desired
	13,					#sal_actual
	15,					#sal_maximum
	True 				#is level enougth
)

@route('/')
def index():
	return template('Temperature is {{temperature}}<br> and salinity is {{salinity}}', temperature=aquarium.temperature.actual, salinity=aquarium.salinity.actual)

@route('/backend')
def backend():
	if request.query.temp != None: 
		aquarium.temperature.actual = int(request.query.temp)
	if request.query.sal != None:
		aquarium.salinity.actual = int(request.query.sal)
	if request.query.lev != None:
		if request.query.lev == 'True':
			aquarium.level = True
		else:
			aquarium.level = False
	if aquarium.manual.enabled:
		return template('backend',
			heater = aquarium.manual.heater,
			fan = aquarium.manual.fan,
			lamp = aquarium.manual.lamp,
			led = aquarium.manual.led,
			buzz = aquarium.manual.buzz	
		)
	else:
		return template('backend',
			heater = aquarium.temperature.heater(aquarium.temperature),
			fan = aquarium.temperature.fan(aquarium.temperature),
			# lamp = aquarium.illumination.lamp(),
			lamp = True,
			# led = aquarium.illumination.led(),
			led = True,
			buzz = aquarium.buzzer()
		)


if __name__ == '__main__':
	run(debug=True, port=80, reloader=False)