class Crewmember:
	def __init__(self, first_name, last_name, middle_name,crew_position):
		self.first_name = first_name
		self.last_name = last_name
		self.middle_name = middle_name
		self.crew_position = crew_position
		self.full_name = f"{last_name}, {first_name} {middle_name}"

