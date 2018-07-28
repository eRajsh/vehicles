class Vehicle():

	def __init__(self, name, wheels, sp, wt, clr, lc):
		self.name = name
		self.no_of_wheels = wheels
		self.speed = sp
		self.weight = wt
		self.color = clr
		self.loc = lc

	no_of_wheels = 0
	speed = 0
	weight = 0
	color = "Black"
	loc = 0

	def go_forward(self, dist):
		loc = loc + dist
		print("Current location is: " + str(loc))

	def reverse(self, dist):
		loc = loc - dist
		print("Current location after reverse is: " + str(loc))

	def stop(self):
		print("All Stop")


	def printState(self):
		print("---------ALL VEHICLE PARAMETERS----------")
		print("Speed  = " + str(self.speed))
		print("Weight = " + str(self.weight))
		print("No of wheels = " + str(self.no_of_wheels))
		print("Color = " + self.color)
		print("Location = " + str(self.loc))

class Bike(Vehicle):
	def __init__(self, name, wheels, sp, wt, clr, lc, hdl, gred):
		super().__init__(name, wheels, sp, wt, clr, lc)
		self.has_handle = hdl
		self.is_geared = gred		

	has_handle = True
	is_geared = True

	def do_wheelie(self):
		print("Wheeeeeiieeee")

	

class Car(Vehicle):
	def __init__(self, name, wheels, sp, wt, clr, lc, steer, cooler, sblt, aud):
		super().__init__(name, wheels, sp, wt, clr, lc)
		self.has_steering = steer
		self.has_AC = cooler
		self.has_seatbelt = sblt
		self.has_audio = aud

	has_steering = True
	has_AC = False
	has_seatbelt = True
	has_audio = True

	def drift(self):
		print("Check it out, I am Drifting!")

	def deploy_airbags(self):
		print("CRASH - airbags deployed, whew!")

class Truck(Vehicle):
	def __init__(self, name, wheels, sp, wt, clr, lc, mload, speedL):
		super().__init__(name, wheels, sp, wt, clr, lc)
		self.max_load = mload
		self.current_load = mload
		self.speed_limit = speedL

	max_load = 0
	current_load = 0
	speed_limit = 80
	
	def load_truck(self, payload_weight):
		if payload_weight > max_load:
			print("overload, reduce payload")
		else:
			current_load = payload_weight + current_load
			print("Truck loaded, current load: " + str(current_load))

		
		
	
