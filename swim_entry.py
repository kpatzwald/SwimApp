from tokenize import String


class swim_entry :
	def __init__(self, date, time, distance, distance_freestyle, distance_breast, duration, comment):
		self.__date = date
		self.__time = time
		self.__distance = distance
		self.__distance_freestyle = distance_freestyle
		self.__distance_breast = distance_breast
		self.__duration: int = duration
		self.__comment = comment

	def __str__(self) -> str:
			return "swim:entry: " + "Datum: " + self.__date + "; Zeit: " + self.__time + "; Distanz: " + self.__distance + "; Freestyle: " + self.__distance_freestyle + "; Burst: " + self.__distance_breast + "; Dauer: " + self.__duration + "; Kommentar: " + self.__comment

	def get_date(self):
		return self.__date

	def get_distance(self) :
		return self.__distance

	def get_distance_freestyle(self) :
		return self.__distance_freestyle
		
	def get_distance_breast (self) :
		return self.__distance_breast

	def set_distance_breast(self, distance) :
		self.__distance_breast = distance

	def set_distance(self, distance) :
		self.__distance = distance

	def set_distance_freestyle(self, distance) :
		self.__distance_freestyle = distance

	def set_date(self, date):
		self.__date = date

	def get_time(self):
		return self.__time

	def set_time(self, time):
		self.__time = time

	def get_comment(self):
		return self.__comment

	def set_comment(self, comment):
		self.__comment = comment

	def get_duration(self):
		return self.__duration

	def set_duration(self, duration):
		self.__duration = duration
