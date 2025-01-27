# IoT Device Simulation with MQTT, Docker, and Ignition Integration

This project simulates IoT devices using Docker containers, publishes sensor data via an MQTT broker (Mosquitto), and visualizes it in real-time using Ignition. Data is stored in a PostgreSQL database, with pgAdmin for database management. It provides a complete framework for simulating and processing IoT sensor data. Perfect for testing IoT systems and real-time analytics.

## Architecture Overview
![Image Description](./images/architecture.png)

## Features

- Simulate multiple IoT devices that generate various types of sensor data (e.g., temperature, humidity).

- Each IoT device publishes its sensor data to an MQTT broker (Mosquitto) using the MQTT protocol.

- Configure the MQTT Engine module in Ignition to subscribe to the MQTT broker and retrieve real-time data from the IoT devices.

- Establish a connection between Ignition and PostgreSQL, allowing Ignition to send the real-time data to PostgreSQL for storage.

- Set up pgAdmin to query and manage the data stored in PostgreSQL, providing a user-friendly interface for data management.

- Build a dashboard in Ignition Perspective to visualize the real-time data retrieved from the sensors, 

## Requirements
- Docker 
- Mosquitto (MQTT Broker)
- Ignition + MQTT Engine Module
- PostgreSQL
- pgAdmin

## Overview of Mosquitto Terminal
![alt text](images/mosquito_.png)


## Ignition Designer Interface

![alt text](images/interface_tags_designer.png)

## Ignition Dashboard
![alt text](images/pages_02.png) 
![alt text](./images/Dashboard_perspective.png)
![alt text](images/iot_dashboard_from_phone.png)


## PostgreSQL Data from pgAdmin

![alt text](images/pg_admin_interface.png)