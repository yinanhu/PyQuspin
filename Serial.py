import serial
import time
# import some essential modules
ser1=serial.Serial(port='COM3', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
ser2=serial.Serial(port='COM4', baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=2)
# Build the communication

ser1.write('>'.encode())
ser2.write('>'.encode())
time.sleep(180)
# Turn on the sensors and heat up

ser1.write('F'.encode())
ser2.write('F'.encode())
#set the sensitive axis to Y

'''' Auto Zerofield '''
def  Zerofield():
     ser1.write('D'.encode())
     ser2.write('D'.encode())
     time.sleep(0.5)
     # start compensate

     ser1.write('E'.encode())
     ser2.write('E'.encode())
     compensated_00F3 = ser2.readline()
     compensated_00F4 = ser1.readline()

     if str(compensated_00F3[2])=='7':
            Bz00F3=round(((float(str(compensated_00F3[3:8])[2:9]) - 32768)), 3)
            Bz00F3m=[]

        elif  str(compensated_00F3[2])=='8':
            By00F3 =round(((float(str(compensated_00F3[3:8])[2:9]) -32768)), 3)

        elif str(compensated_00F3[2])=='9':
            B000F3 =round(((float(str(compensated_00F3[3:8])[2:9]) - 32768)), 3)
            bz=1


     if str(compensated_00F4[2])=='7':
            Bz00F4=round(((float(str(compensated_00F3[3:8])[2:9]) - 32768)), 3)
            Bz00F4m=[]

         elif  str(compensated_00F4[2])=='8':
            By00F4 =round(((float(str(compensated_00F3[3:8])[2:9]) -32768)), 3)

         elif str(compensated_00F4[2])=='9':
            B000F4 =round(((float(str(compensated_00F3[3:8])[2:9]) - 32768)), 3)

     time.sleep(15)
      return (Bz, By, B0)


ser1.write('9'.encode())
ser2.write('9'.encode())
time.sleep(10)
# Calibrate

i=1
while i<100000:
    a=ser2.readline()
    #if len(a)>=1:
    i=1+i
    B=round(((float(str(a[1:8])[2:9])-8388608)*0.01),3)
    if B>3000:
        Zerofield()

       #time.sleep(0.01)

