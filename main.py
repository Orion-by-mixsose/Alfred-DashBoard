from fastapi import FastAPI
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_USER = "esp32"
MQTT_PASSWORD = "Rives/38140"

app = FastAPI()
mqtt_client = mqtt.Client()

@app.on_event("startup")
def startup_event():
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
    mqtt_client.loop_start()

@app.get("/")
def read_root():
    return {"message": "Serveur en ligne"}