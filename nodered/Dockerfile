FROM nodered/node-red:latest
USER root
RUN npm install node-red-contrib-influxdb
COPY aquarium_sensor_data.csv /sensor.csv