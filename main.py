from fastapi import FastAPI
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
import os

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

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

@app.post("/streamdeck/{distrib}")
def control_relay(distrib: str):
    if distrib not in ["windows", "linux"]:
        return {"error": "state doit etre 'windows' ou 'linux'" }
    mqtt_client.publish("maison/streamdeck/startpc", distrib)
    return {"status": "commande envoyee", "state": distrib}