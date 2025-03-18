import serial
import csv
import time

ser = serial.Serial("COM3", 115200)
time.sleep(2)

with open("vibrations.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["X", "Y", "Z", "Label"])

    print("Collecte en cours... Appuyez sur Ctrl+C pour arrêter !")
    
    try:
        while True:
            ligne = ser.readline().decode('utf-8').strip()
            writer.writerow(ligne.split(","))
    except KeyboardInterrupt:
        print("Arrêt de la collecte.")
        ser.close()
