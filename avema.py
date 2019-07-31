'''
АВК ОМА Козырев С.А.

опрос УТК138 для Авемы цех 5
1 - этап IBM PC c АС3-М
2 - этап Raspberry PI с преобразователем RS485 с гальванической развязкой 3.3в


22.10.18 попытка запустить УТК38, Raspberry PI, DS18B20  (22.10.18, 23,24,25,26,27,28,29,30.10.18 по 11-12часов)
31.10.18г старт работ с УТК138 + IBM PC   Ubuntu 
V1.0 на 16 каналов УТК138 по RS485
V1.1   разгрузил ядро процессора добавил sleep(0.02) вместо continue


'''

from struct import *
import time
import requests
import pymodbus
import serial
import threading
import math
from datetime import datetime, date, timedelta

from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient #initialize a serial RTU client instance
from pymodbus.transaction import ModbusRtuFramer

import logging
i=0
#logging.basicConfig()
#log = logging.getLogger()
#log.setLevel(logging.DEBUG)

#count= the number of registers to read
#unit= the slave unit this request is targeting
#address= the starting address to read from


def two_sec ():
    global l
    time.sleep(5)
    l = 1

client= ModbusClient(method = "rtu", port="/dev/ttyS0",stopbits = 1, bytesize = 8, parity = 'N', baudrate= 19200)
while True:
	l = 0
	my_thread = threading.Thread(target=two_sec, name='two', args=())
	my_thread.start()                                                                             #Connect to the serial modbus server
	connection = client.connect()
	qt = '+0000'
	qt1 = '+0000'
	qt2 = '+0000'
	qt3 = '+0000'
	qt4 = '+0000'
	qt5 = '+0000'
	qt6 = '+0000'
	qt7 = '+0000'
	qt8 = '+0000'
	qqt = '+0000'
	qqt1 = '+0000'
	qqt2 = '+0000'
	qqt3 = '+0000'
	qqt4 = '+0000'
	qqt5 = '+0000'
	qqt6 = '+0000'
	qqt7 = '+0000'
	qqt8 = '+0000'


                                                                                        #print (connection)  !!!!!!!!!!!

                                                                                        #Starting add, num of reg to read, slave unit.
	try:       
		                                                                     
		result = client.read_input_registers(0x0,5,unit= 8)
		#print(result.registers)

		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура первого    датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt = '{:0=+5d}'.format((tt[0]))
		#print(qt)
	except:
		print ("Ошибка адреса 0x0")  
	try:
		
		result = client.read_input_registers(0x5,5,unit= 8)
		#print(result.registers)

		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt1 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt1)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура второго    датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#print(tt[0])
		#qt1 = '{:0=+5d}'.format((tt[0]))
		#print(qt1)

	except:
        	print ("Ошибка адреса 0x5")   
	try:
		result = client.read_input_registers(10,5,unit= 8)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt2 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt2)

		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура третьего   датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt2 = '{:0=+5d}'.format((tt[0]))
		#print(qt2)
	except:
        	print ("Ошибка адреса 10")   
	try:
		result = client.read_input_registers(15,5,unit= 8)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt3 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt3)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура четвертого датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt3 = '{:0=+5d}'.format((tt[0]))
		#print(qt3)
	except:
        	print ("Ошибка адреса 15")   
	try:
		result = client.read_input_registers(20,5,unit= 8)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt4 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt4)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура пятого     датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt4 = '{:0=+5d}'.format((tt[0]))
		#print(qt4)
	except:
        	print ("Ошибка адреса 20") 
	try:
		result = client.read_input_registers(25,5,unit= 8)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt5 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt5)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура шестого    датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt5 = '{:0=+5d}'.format((tt[0]))
		#print(qt5)
	except:
        	print ("Ошибка адреса 25") 
	try:
		result = client.read_input_registers(30,5,unit= 8)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt6 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt6)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура седьмого   датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt6 = '{:0=+5d}'.format((tt[0]))
		#print(qt6)
	except:
        	print ("Ошибка адреса 30") 
	try:
		result = client.read_input_registers(35,5,unit= 8)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qt7 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qt7)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('температура восьмого   датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qt7 = '{:0=+5d}'.format((tt[0]))
		#print(qt7)
	except:
        	print ("Ошибка адреса 35") 
# **************************************************************************************************
	time.sleep(.2)
	try:                                                                                    
		result = client.read_input_registers(0x0,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура первого    датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt = '{:0=+5d}'.format((tt[0]))
		#print(qqt)
	except:
		print ("Ошибка адреса 0x0")  
	try:
		result = client.read_input_registers(0x5,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt1 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt1)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура второго    датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt1 = '{:0=+5d}'.format((tt[0]))
		#print(qqt1)
	except:
        	print ("Ошибка адреса 0x5")   
	try:
		result = client.read_input_registers(10,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt2 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt2)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура третьего   датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt2 = '{:0=+5d}'.format((tt[0]))
		#print(qqt2)
	except:
        	print ("Ошибка адреса 10")   
	try:
		result = client.read_input_registers(15,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt3 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt3)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура четвертого датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt3 = '{:0=+5d}'.format((tt[0]))
		#print(qqt3)
	except:
        	print ("Ошибка адреса 15")   
	try:
		result = client.read_input_registers(20,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt4 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt4)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура пятого     датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt4 = '{:0=+5d}'.format((tt[0]))
		#print(qqt4)
	except:
        	print ("Ошибка адреса 20") 
	try:
		result = client.read_input_registers(25,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt5 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt5)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура шестого    датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt5 = '{:0=+5d}'.format((tt[0]))
		#print(qqt5)
	except:
        	print ("Ошибка адреса 25") 
	try:
		result = client.read_input_registers(30,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt6 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt6)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура седьмого   датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt6 = '{:0=+5d}'.format((tt[0]))
		#print(qqt6)
	except:
        	print ("Ошибка адреса 30") 
	try:
		result = client.read_input_registers(35,5,unit= 16)
		t=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		#print(t[0])
		qqt7 = '{:0=+5d}'.format(math.trunc(t[0]*10))
		print(qqt7)
		tt=unpack('!f',pack('!H',result.registers[3])+pack('!H',result.registers[4]))
		qt_='{:0=+6.1f}'.format(tt[0])
		print('2 температура восьмого   датчика:'+qt_)
		#tt=unpack('!H',pack('!H',result.registers[1]))
		#qqt7 = '{:0=+5d}'.format((tt[0]))
		#print(qqt7)
	except:
        	print ("Ошибка адреса 35") 





	payload ={'key1':(qt+'$'+qt1+'$'+qt2+'$'+qt3+'$'+qt4+'$'+qt5+'$'+qt6+'$'+qt7+'$'+qqt+'$'+qqt1+'$'+qqt2+'$'+qqt3+'$'+qqt4+'$'+qqt5+'$'+qqt6+'$'+qqt7+'$01')}
	print(payload)
	try:
		r = requests.get('http://10.3.2.19/exempl100.php',params=payload)
		#print(r)
		#print(r.text)
	except:
		print("Нет связи с сервером")
	while l == 0:
		time.sleep(.02)  #continue
	print (" after 5 sek :",(datetime.now()).ctime()) 
	#time.sleep(5)

client.close()
