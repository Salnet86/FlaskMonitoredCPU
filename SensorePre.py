import smbus2
import bme280
import time

# Configura il bus I2C
bus = smbus2.SMBus(1)

# Indirizzo I2C del sensore BME280
address = 0x76

# Inizializza il sensore BME280
calibration_params = bme280.load_calibration_params(bus, address)

# Funzione per leggere i dati dal sensore
def read_sensor_data():
    data = bme280.sample(bus, address, calibration_params)
    temperature = data.temperature  # in gradi Celsius
    humidity = data.humidity        # in %
    pressure = data.pressure        # in hPa (hectopascal)
    return temperature, humidity, pressure

# Ciclo di lettura e stampa dei dati
while True:
    temperature, humidity, pressure = read_sensor_data()
    print(f"Temperatura: {temperature:.2f}°C")
    print(f"Umidità: {humidity:.2f}%")
    print(f"Pressione: {pressure:.2f} hPa")
    time.sleep(2)  # Pausa di 2 secondi tra ogni lettura
