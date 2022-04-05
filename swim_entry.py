from tokenize import String


class swim_entry :
	def __init__(self, date_time, distance, distance_freestyle, distance_breast, time, comment):
		self.__start_date_time = date_time
		self.__distance = distance
		self.__distance_freestyle = distance_freestyle
		self.__distance_breast = distance_breast
		self.__time: int = time
		self.__comment = comment


	def get_start_date_time(self):
		return self.__start_date_time

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

	def set_start_date_time(self, start_date_time):
		self.__start_date_time = start_date_time

	def get_time(self):
		return self.__time

	def set_time(self, time):
		self.__time = time

	def get_comment(self):
		return self.__comment

	def set_comment(self, comment):
		self.__comment = comment
