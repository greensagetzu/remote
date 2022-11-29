from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from view import *
import sys

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
	MIN_VOLUME = 0
	MAX_VOLUME = 2
	MIN_CHANNEL = 0
	MAX_CHANNEL = 3
	

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setupUi(self)
		

		self.__status = False
		self.__muted = False
		self.slider_volume.setValue(0)
		self.slider_volume.setMinimum(0)
		self.slider_volume.setMaximum(2)
		self.__volume = Controller.MIN_VOLUME
		self.__channel = Controller.MIN_CHANNEL

		self.pixmap_0 = QPixmap("nhk.png")
		self.pixmap_0 = self.pixmap_0.scaled(256, 256, QtCore.Qt.KeepAspectRatioByExpanding)
		self.pixmap_1 = QPixmap("netflix.png")
		self.pixmap_1 = self.pixmap_1.scaled(256, 256, QtCore.Qt.KeepAspectRatioByExpanding)
		self.pixmap_2 = QPixmap("disney.png")
		self.pixmap_2 = self.pixmap_2.scaled(256, 256, QtCore.Qt.KeepAspectRatioByExpanding)
		self.pixmap_3 = QPixmap("discovery.png")
		self.pixmap_3 = self.pixmap_3.scaled(256, 256, QtCore.Qt.KeepAspectRatioByExpanding)
		self.pixmap_4 = QPixmap("origin.png")
		self.pixmap_4 = self.pixmap_4.scaled(256, 256, QtCore.Qt.KeepAspectRatioByExpanding)




		self.btn_power.clicked.connect(lambda: self.power())
		self.btn_mute.clicked.connect(lambda: self.mute())
		
		self.btn_channel_up.clicked.connect(lambda: self.channel_up())
		self.btn_channel_down.clicked.connect(lambda: self.channel_down())
		self.btn_vol_up.clicked.connect(lambda: self.volume_up())
		self.btn_vol_down.clicked.connect(lambda: self.volume_down())


	def power(self):
		if self.__status == False:
			self.__status = True
			#self.label_image.setPixmap(self.pixmap_0)
	
			self.slider_volume.setValue(1)

			if self.__channel == 0:
				self.label_image.setPixmap(self.pixmap_0)
			elif self.__channel == 1:
				self.label_image.setPixmap(self.pixmap_1)
			elif self.__channel == 2:
				self.label_image.setPixmap(self.pixmap_2)
			elif self.__channel == 3:
				self.label_image.setPixmap(self.pixmap_3)

		else:
			self.__status = False
			self.label_image.setPixmap(self.pixmap_4)
			self.slider_volume.setValue(0)
			self.btn_mute.setStyleSheet("background-color: none")

	

	def mute(self):
		if self.__status == True:
			if self.__muted == False: 
				self.__muted = True
				self.btn_mute.setStyleSheet("background-color: red")
				self.slider_volume.setValue(self.__volume)
			else:
				self.__muted = False
				self.btn_mute.setStyleSheet("background-color: none")
				self.slider_volume.setValue(self.__volume )

	def volume_up(self):
		if self.__status == True:
			if self.__muted == False: 
				if self.__volume != Controller.MAX_VOLUME:
					self.__volume += 1
					self.slider_volume.setValue(self.__volume)
				else:
					self.__volume = Controller.MAX_VOLUME
					self.slider_volume.setValue(self.__volume)

		
	def volume_down(self):
		if self.__status == True:
			if self.__muted == False: 
				if self.__volume != Controller.MIN_VOLUME:
					self.__volume -= 1
					self.slider_volume.setValue(self.__volume)
				else:
					self.__volume = Controller.MIN_VOLUME
					self.slider_volume.setValue(self.__volume)


	def channel_up(self):
		if self.__status == True:
			if self.__channel != Controller.MAX_CHANNEL:
				self.__channel += 1
				if self.__channel == 0:
					self.label_image.setPixmap(self.pixmap_0)
				elif self.__channel == 1:
					self.label_image.setPixmap(self.pixmap_1)
				elif self.__channel == 2:
					self.label_image.setPixmap(self.pixmap_2)
				elif self.__channel == 3:
					self.label_image.setPixmap(self.pixmap_3)
				
			else:
				self.__channel = Controller.MIN_CHANNEL
				self.label_image.setPixmap(self.pixmap_0)


	def channel_down(self):
		if self.__status == True:
			if self.__channel != Controller.MIN_CHANNEL:
				self.__channel -= 1
				if self.__channel == 0:
					self.label_image.setPixmap(self.pixmap_0)
				elif self.__channel == 1:
					self.label_image.setPixmap(self.pixmap_1)
				elif self.__channel == 2:
					self.label_image.setPixmap(self.pixmap_2)
				elif self.__channel == 3:
					self.label_image.setPixmap(self.pixmap_3)
			else:
				self.__channel = Controller.MAX_CHANNEL
				self.label_image.setPixmap(self.pixmap_3)
			

	