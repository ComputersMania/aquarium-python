class aquarii:

	class manual:
		# def set_heater(self, heater):
		# 	self.heater = heater
		heater = bool
		# def set_fan(self, fan):
		# 	self.fan = fan
		fan = bool
		# def set_lamp(self, lamp):
		# 	self.lamp = lamp
		lamp = bool
		# def set_led(self, led):
		# 	self.led = led
		led = int
		# def set_buzz(self, buzz):
		# 	self.buzz = buzz
		buzz = bool

	class temperature:
		# def set_actual(self, actual):
		# 	self.actual = actual
		actual = int
		# def set_sensitivity(self, sensitivity):
		# 	self.sensitivity = sensitivity
		sensitivity = int
		# def set_extreme(self, extreme):
		# 	self.extreme = extreme
		extreme = int
		# def set_desired(self, desired):
		# 	self.desired = desired
		desired = int
		def heater(self):
			return self.actual < self.desired - self.sensitivity
		def fan(self):
			return self.actual > self.desired + self.sensitivity
		def emergency(self):
			return self.actual < self.desired - self.extreme or self.actual > self.desired +self.sensitivity

	# class illumination:

	class salinity:
		# def set_actual(self, actual):
		# 	self.actual = actual
		actual = int
		# def set_maximum(self, maximum):
		# 	self.maximum = maximum
		maximum = int
		def emergency(self):
			return self.actual > self.maximum

	def buzzer(self):
		return self.temperature.emergency() or self.salinity.emergency()

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
		sal_maximum
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