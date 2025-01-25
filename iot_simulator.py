import random
import time
import paho.mqtt.client as mqtt
import json  # Import JSON library

# MQTT Broker Configuration
BROKER = "mosquitto"  # Service name from docker-compose.yml
PORT = 1883

# Simulation Parameters
DEVICE_COUNT = 1
PUBLISH_INTERVAL = 2  # seconds

# Initialize MQTT Client
client = mqtt.Client()

def connect_mqtt():
    while True:
        try:
            client.connect(BROKER, PORT, 60)
            print(f"Connected to MQTT Broker at {BROKER}:{PORT}")
            break
        except Exception as e:
            print(f"Failed to connect to MQTT Broker: {e}")
            time.sleep(5)  # Retry after 5 seconds

def simulate_device_data(device_id):
    # Simulate sensor data
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    return {
        "device_id": f"device_{device_id}",
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
    }

def publish_data():
    while True:
        for device_id in range(1, DEVICE_COUNT + 1):
            data = simulate_device_data(device_id)
            topic = f"iot_topic/data"
            # Serialize the dictionary as a JSON string
            json_payload = json.dumps(data)
            client.publish(topic, json_payload)
            print(f"Published to {topic}: {json_payload}")
        time.sleep(PUBLISH_INTERVAL)

if __name__ == "__main__":
    connect_mqtt()
    client.loop_start()
    try:
        publish_data()
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
        client.loop_stop()
        client.disconnect()
