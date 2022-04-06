from ast import Try
from posixpath import sep
from tokenize import String
import swim_entry as se
import tkinter as tk
import tkinter.ttk as ttk
import mariadb
import sys
import datetime

# entry = se.swim_entry("16.03.2022", 2, 1.7, (2 - 1.7))

# print("Eintrag vom", entry.get_date_time(), sep=" ")

class app(tk.Frame) :
	# Konstruktor
	def __init__(self) -> None:
		#self.db_connection()
		self.root = tk.Tk()
		super().__init__(self.root)
		self.root.geometry('640x640')
		self.root.title("Swim-App")
		self.create_widgets()
		self.mainloop()

	def db_connection(self):
		try:
			self.conn = mariadb.connect(host="localhost", user="swim_db", password="test", database="swim_db")
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
			sys.exit(1)
		# print(self.mydb)
		# self.curr = self.conn.cursor()
		# self.curr.execute(SQL)
		# self.mydb.close()

	def button_new_entry_pressed(self):
		#print(self.__entry_distance.get())
		#kommentar = self.__text_comment.get(1.0, tk.END)
		#print(kommentar)
		new_entry = se.swim_entry(date=self.__entry_date.get(), time=self.__entry_time.get(), distance=self.__entry_distance.get(), distance_freestyle=self.__entry_distance_freestyle.get(), distance_breast=self.__entry_distance_breast.get(), duration=self.__entry_duration.get(), comment=self.__text_comment.get(1.0, tk.END+"-1c"))
		#print(new_entry)
		self.save(new_entry)

	def save(self, entry):
		try:
			self.conn = mariadb.connect(
				host="localhost", user="swim_db", password="test", database="swim_db")
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
			sys.exit(1)
		cursor = self.conn.cursor();
		date = datetime.datetime.strptime(entry.get_date(), "%d.%m.%Y")
		sql = "INSERT INTO entries (start_date, start_time, distance, distance_freestyle, distance_breast, duration, comment) VALUES (\"" + datetime.datetime.strftime(date, "%Y-%m-%d") + "\", \"" + entry.get_time() + "\", " + entry.get_distance() + ", " + entry.get_distance_freestyle() + ", " + entry.get_distance_breast() + ", " + entry.get_duration() + ", \"" + entry.get_comment() + "\");"
		print(sql)
		try:
			cursor.execute(sql)
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
			#sys.exit(1)
		self.conn.commit()
		self.conn.close()

	def create_widgets(self):
		self.__entry_distance = tk.StringVar()
		self.__entry_distance_freestyle = tk.StringVar()
		self.__entry_distance_breast = tk.StringVar()
		self.__entry_time = tk.StringVar()
		self.__entry_date = tk.StringVar()
		self.__entry_duration = tk.StringVar()

		self.frm = ttk.Frame(self.root, padding=20)
		self.frm.grid()
		ttk.Label(self.frm, text="Datum: ", padding=5).grid(column=0, row=0)
		ttk.Label(self.frm, text="Startzeit: ", padding=5).grid(column=0, row=1)
		ttk.Label(self.frm, text="Entfernung in Meter: ", padding=5).grid(column=0, row=2)
		ttk.Label(self.frm, text="Entfernung Kraul in Meter: ", padding=5).grid(column=0, row=3)
		ttk.Label(self.frm, text="Entfernung Brust in Meter: ", padding=5).grid(column=0, row=4)
		ttk.Label(self.frm, text="Dauer in Minuten: ", padding=5).grid(column=0, row=5)
		ttk.Label(self.frm, text="Kommentar: ", padding=5).grid(column=0, row=6)

		ttk.Entry(self.frm, textvariable=self.__entry_date).grid(column=1, row=0)
		ttk.Entry(self.frm, textvariable=self.__entry_time).grid(column=1, row=1)
		ttk.Entry(self.frm, textvariable=self.__entry_distance).grid(column=1, row=2)
		ttk.Entry(self.frm, textvariable=self.__entry_distance_freestyle).grid(column=1, row=3)
		ttk.Entry(self.frm, textvariable=self.__entry_distance_breast).grid(column=1, row=4)
		ttk.Entry(self.frm, textvariable=self.__entry_duration).grid(column=1, row=5)
		#ttk.Entry(self.frm, textvariable=self.__entry_comment).grid(column=1, row=6)
		self.__text_comment = tk.Text(self.frm, height=5, width=20)
		self.__text_comment.grid(column=1, row=6)

		self.__entry_date.set(datetime.datetime.now().strftime("%d.%m.%Y"))
		self.__entry_time.set(datetime.datetime.now().strftime("%H:%M"))

		ttk.Button(self.frm, text="Eintrag anlegen", command=self.button_new_entry_pressed).grid(column=1, row=7)

app()
