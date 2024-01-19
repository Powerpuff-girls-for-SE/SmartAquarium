# Smart Aquarium Project - Software Engineering for Internet of Things
The IoT-Based Smart Aquarium System is an advanced solution designed to monitor and maintain optimal conditions within an aquarium. Utilizing a suite of sensors, this system will continuously monitor various environmental factors, such as temperature, pH levels, diffused oxygen, dissolved ammonia-nitrogen, and water level. The primary goal is to ensure a healthy habitat for aquatic life by providing real-time data monitoring and customised thresholds according to the species of fish present in the aquarium.

<img width="30%" alt="image" src="https://github.com/Powerpuff-girls-for-SE/SmartAquarium/assets/46968591/6bf31956-791a-4a45-9329-b7068b704065">

## Steps to Execute Project
1. Install Docker Desktop [link](https://www.docker.com/products/docker-desktop/)
2. Start Docker Desktop
3. Open the project folder in the terminal and run the following commands sequentially:
```console
docker-compose build
docker-compose up
```

## Functional Requirements
The following are the functional requirements for the system.
| ID | Requirement Name    | Description                                                                                                                            |
|----|----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 1. | Sensor Integration   | The system must be able to incorporate the use of multiple precise sensors for the measurement of temperature, pH, diffused oxygen, dissolved ammonia, and water level. |
| 2. | Data Gathering       | The system should be able to support continuous in-flow of data collected from the sensors.                                             |
| 3. | Efficient Storage    | The system should be able to store data for historical data analysis and trend prediction.                                              |
| 4. | Remote Monitoring    | The system should allow monitoring of the collected data through a web or mobile-based application.                                       |
| 5. | Data Visualization   | The system should be able to present the stored data through easily interpretable charts.                                               |


## Non-functional Requirements
The following are the non-functional requirements of the system:
| ID | Requirement Name  | Description                                                                                                                |
|----|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| 1. | Reliability        | The system must be able to function without significant downtime.                                                           |
| 2. | Scalability        | The system should support easy integration of additional sensors or functionalities.                                       |
| 3. | Usability          | The system should be user-friendly and provide intuitive visualization and interaction for users of varying technical expertise. |
| 4. | Security           | The system should support secure communication channels to prevent unauthorized access and data breaches.                   |
| 5. | Maintainability    | The system should be easily maintainable and flexible to account for updates and enhancements.                              |
| 6. | Availability       | The system should be available to allow monitoring and alerting.                                                          |

## Technologies used for the project implementation
* Python: for generating the synthetic dataset
* Docker: for container orchestration
* Node-red: for developing the data flow within the project
* Mosquitto: for communication between the different project components
* InfluxDB: for data storage
* Grafana: for visualization

## Data Visualization
<img width="150%" alt="image" src="https://github.com/Powerpuff-girls-for-SE/SmartAquarium/assets/46968591/c86d1340-86d7-49a5-b3ce-8d264498af3d">


