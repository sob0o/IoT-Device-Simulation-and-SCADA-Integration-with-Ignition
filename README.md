# IoT Device Simulation with MQTT, Docker, and Ignition Integration

This project simulates IoT devices using Docker containers, publishes sensor data via an MQTT broker (Mosquitto), and visualizes it in real-time using Ignition. Data is stored in a PostgreSQL database, with pgAdmin for database management. It provides a complete framework for simulating and processing IoT sensor data. Perfect for testing IoT systems and real-time analytics.

## Architecture Overview
![Image Description](./images/architecture.png)

## Features
- Simulates multiple IoT devices with various sensor data (e.g., temperature, humidity).
- Publishes data to an MQTT broker (Mosquitto).
- Integrates with Ignition for real-time data visualization.
- Connects to a PostgreSQL database for data storage.
- Supports data ingestion into PostgreSQL for persistent storage.
- Provides pgAdmin setup for querying and managing PostgreSQL data.

## Requirements
- Docker
- Mosquitto (MQTT Broker)
- Ignition
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