# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy necessary files
COPY iot_simulator.py /app/

# Install required Python libraries
RUN pip install --upgrade paho-mqtt

# Set the default command to run the IoT simulator
CMD ["python", "iot_simulator.py"]
