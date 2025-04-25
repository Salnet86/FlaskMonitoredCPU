# Flask Monitored CPU SENORI RASPBERRY 

# Flask System Monitor Project

## Descrizione
Il **Flask System Monitor** è un'applicazione web che monitora in tempo reale il sistema operativo, raccogliendo e visualizzando informazioni come l'utilizzo della CPU, la memoria RAM, lo spazio su disco e altre metriche di sistema. Questo progetto è stato sviluppato come parte di un **progetto di stage** per l'azienda **Oltre Formazione**.

## Autori 
- **Silvia**
- **Salvatore**
- **Mirco**
- **Teresa**

## Anno
2024

## Tecnologie utilizzate
Il progetto utilizza le seguenti tecnologie:
- **Python:** Utilizzato per lo sviluppo del backend con il framework **Flask**.
- **HTML:** Per strutturare le pagine web e visualizzare le informazioni in modo chiaro.
- **CSS:** Per lo stile e la presentazione delle pagine.
- **JavaScript:** Per interattività e aggiornamenti in tempo reale dei dati di monitoraggio.
- **psutil:** Una libreria Python per raccogliere le informazioni sul sistema operativo.

## Tutorial

### Panoramica
Il progetto **Flask System Monitor** è una semplice applicazione web che raccoglie e visualizza informazioni sul sistema operativo, come l'utilizzo della CPU, la memoria, lo spazio su disco e altre metriche di sistema. L'applicazione è realizzata utilizzando **Flask**, un framework web per Python.

### Come funziona
L'applicazione è composta da un server Flask che raccoglie i dati di sistema attraverso il modulo **psutil** e li visualizza in tempo reale tramite una pagina web. È utile per monitorare le risorse di sistema di una macchina in modo facile e veloce.

### Struttura del progetto
1. **Backend (Flask/Python):**
   - `app.py`: Il server principale Flask che raccoglie i dati di sistema.
   - `psutil`: Libreria Python per ottenere informazioni sulla CPU, memoria, disco, etc.

2. **Frontend (HTML, CSS, JavaScript):**
   - **HTML**: La struttura della pagina web che mostra le informazioni di sistema.
   - **CSS**: Per migliorare l'aspetto della pagina e renderla più user-friendly.
   - **JavaScript**: Per aggiornare dinamicamente le informazioni di sistema senza ricaricare la pagina, creando un'esperienza interattiva.

### Come eseguire il progetto

1. **Clona il repository:**
   Prima di tutto, clona il repository sul tuo computer locale:
    ```bash
    git clone https://github.com/Salnet86/FlaskMonitoredCPU.git
    ```

2. **Entra nella directory del progetto:**
    ```bash
    cd FlaskMonitoredCPU
    ```

3. **Crea un ambiente virtuale (Opzionale ma consigliato):**
   È buona norma creare un ambiente virtuale per gestire le dipendenze. Se non lo hai già fatto, crea un ambiente virtuale:
    ```bash
    python3 -m venv venv
    ```

4. **Attiva l'ambiente virtuale:**
    - Su Linux/macOS:
      ```bash
      source venv/bin/activate
      ```
    - Su Windows:
      ```bash
      venv\Scripts\activate
      ```




5. **Installa le dipendenze:**
   Installa tutte le librerie necessarie per eseguire il progetto:
    ```bash
    pip install -r requirements.txt
    
    ```

 Installazione librerie per    sensori 
sudo apt update
sudo apt install python3-smbus
sudo apt install python3-pip
pip3 install bme280
    

6. **Avvia il server Flask:**
   Avvia l'applicazione Flask con il comando:
    ```bash
    python3 app.py
    ```
   Questo avvierà il server Flask, e dovresti vedere qualcosa del genere:
    ```
    * Serving Flask app 'flas_monitored'
    * Debug mode: on
    * Running on http://127.0.0.1:5000
    ```
   
7. **Accedi all'applicazione:**
   Una volta avviato il server, puoi accedere all'applicazione nel tuo browser all'indirizzo:
    ```
    http://127.0.0.1:5000
    ```

8. **Monitoraggio del sistema:**
   L'applicazione mostrerà in tempo reale vari dettagli sul sistema, tra cui:
   - **CPU Usage:** Percentuale di utilizzo della CPU.
   - **Memory Usage:** Utilizzo della memoria RAM.
   - **Disk Usage:** Utilizzo del disco fisso.
   - **Network Activity:** Statistiche di rete.

### Funzionalità avanzate
L'applicazione è pensata per un uso personale o in ambienti di sviluppo. Se desideri usarla in un ambiente di produzione, ti consigliamo di configurare un server WSGI come **Gunicorn** o **uWSGI** per gestire le richieste in modo più efficiente. Inoltre, puoi aggiungere altre funzionalità come:
- **Autenticazione utente**
- **Allarmi e notifiche quando le risorse di sistema superano una certa soglia**
- **Visualizzazioni avanzate con grafici delle statistiche in tempo reale**


