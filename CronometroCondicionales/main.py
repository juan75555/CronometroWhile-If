import time

print("Hola, esto es un contador.")
Segundos=0
Minutos=0
Horas=0
TiempoSegundos=0
TiempoMinutos=0
while 1==1:
     time.sleep(0.1)
     TiempoMinutos=TiempoMinutos+1
     TiempoSegundos=TiempoSegundos+1
     Segundos=Segundos+1
     Minutos=int((Minutos+TiempoSegundos)/60)
     Horas=int((Horas+TiempoMinutos)/3600)
     print(Horas ,':',  Minutos ,':',  Segundos)
     if Segundos==60:
        time.sleep(0.1)
        Segundos=0
        TiempoMinutos=TiempoMinutos+1
        TiempoSegundos=TiempoSegundos+1
        Segundos=Segundos+1
        Minutos=int((Minutos+TiempoSegundos)/60)
        Horas=int((Horas+TiempoMinutos)/3600)
        print(Horas ,':',  Minutos ,':',  Segundos)
     if TiempoSegundos>=3600:
        time.sleep(0.1)
        Segundos=Segundos+1
        TiempoSegundos=0
        TiempoSegundos=TiempoSegundos+1
        TiempoMinutos=TiempoMinutos+1
        TiempoMinutos=TiempoMinutos+1
        Minutos=Minutos+1
        Horas=int((Horas+TiempoMinutos)/3600)
        print(Horas ,':',  Minutos ,':',  Segundos)




























