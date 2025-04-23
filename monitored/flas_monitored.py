

import matplotlib
matplotlib.use('Agg')  # Usa il backend Agg, che non richiede un display grafico
import matplotlib.pyplot as plt
import io
from flask import Flask, jsonify, render_template, Response
import psutil

app = Flask(__name__)

cpu_usage_history = []
battery_usage_history = []
temperature_history = []
disk_usage_history = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status')
def status():
    cpu_usage = psutil.cpu_percent(interval=1)
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None
    temperatures = psutil.sensors_temperatures()
    cpu_temp = None
    if 'coretemp' in temperatures:
        cpu_temp = temperatures['coretemp'][0].current
    
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent  # Percentuale di utilizzo del disco

    return jsonify({
        'cpu_usage': cpu_usage,
        'battery_percent': battery_percent,
        'cpu_temperature': cpu_temp,
        'disk_usage': disk_percent  # Aggiungi il dato dell'utilizzo del disco
    })





@app.route('/cpu_graph')
def cpu_graph():
    global cpu_usage_history
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_usage_history.append(cpu_usage)
    
    plt.figure(figsize=(8, 5))
    plt.plot(cpu_usage_history, label='CPU Usage (%)', color='blue')
    plt.xlabel('Time (s)')
    plt.ylabel('CPU Usage (%)')
    plt.title('CPU Usage Over Time')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')



@app.route('/battery_graph')
def battery_graph():
    global battery_usage_history
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None

    if battery_percent is None:
        return Response("Battery data not available", status=404)

    battery_usage_history.append(battery_percent)

    plt.figure(figsize=(8, 5))
    plt.bar(range(len(battery_usage_history)), battery_usage_history, color='green')
    plt.xlabel('Time (s)')
    plt.ylabel('Battery Usage (%)')
    plt.title('Battery Usage Over Time')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')



@app.route('/temperature_graph')
def temperature_graph():
    global temperature_history
    temperatures = psutil.sensors_temperatures()
    cpu_temp = None
    if 'coretemp' in temperatures:
        cpu_temp = temperatures['coretemp'][0].current

    if cpu_temp is None:
        return Response("Temperature data not available", status=404)

    temperature_history.append(cpu_temp)

    plt.figure(figsize=(8, 5))
    plt.plot(temperature_history, label='CPU Temperature (°C)', color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.title('CPU Temperature Over Time')
    plt.grid(True)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')



@app.route('/disk_graph')
def disk_graph():
    disk_usage = psutil.disk_usage('/')
    total = disk_usage.total
    used = disk_usage.used
    free = disk_usage.free
    percent = disk_usage.percent

    labels = ['Used', 'Free']
    sizes = [used, free]
    
    # Modifica dei colori
    colors = ['#FF6347', '#90EE90']  # Esempio di colori rosso e verde chiaro

    plt.figure(figsize=(8, 5))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title(f'Disk Usage: {percent}%')

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    return Response(img.getvalue(), mimetype='image/png')





if __name__ == '__main__':
    app.run(debug=True)
