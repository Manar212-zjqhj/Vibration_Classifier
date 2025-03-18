# Vibration_Classifier
# Projet TinyML : Surveillance Intelligente et Reconnaissance des Composants

Ce projet utilise des techniques de **Machine Learning embarqué (TinyML)** pour implémenter des applications pratiques dans des environnements industriels et technologiques. Il est divisé en deux parties : classification des vibrations et reconnaissance visuelle des composants électroniques.

# Partie 1 : Classification des Vibrations avec Arduino Nano 33 BLE et TensorFlow Lite

Dans cette première phase, des données de vibrations sont collectées en temps réel à l'aide du capteur IMU intégré de l'Arduino Nano 33 BLE. Ces données servent à entraîner un modèle capable de classer différents types de vibrations. Une fois entraîné, le modèle est déployé sur la carte Arduino pour une classification en temps réel, facilitant ainsi le diagnostic et la maintenance prédictive.

### Objectifs de la Partie 1 :

- Collecter et analyser des données de vibrations avec le capteur IMU de l'Arduino.

- Entraîner un modèle de Machine Learning avec TensorFlow Lite.

- Déployer le modèle sur l'Arduino pour la classification en temps réel.

# Partie 2 : Reconnaissance Visuelle des Composants avec Caméra et Node-RED

Cette partie se concentre sur la reconnaissance visuelle des composants électroniques. Une caméra capture les images, qui sont ensuite traitées par un modèle de classification pré-entraîné. Les résultats sont envoyés à Node-RED, un outil IoT pour automatiser le traitement des données.

### Objectifs de la Partie 2 :

- Capturer des images des composants avec une caméra.

- Classer les images via un modèle pré-entraîné.

- Intégrer les résultats dans Node-RED pour automatisation et analyse.

- Technologies Utilisées

**Arduino Nano 33 BLE** : Collecte des données de vibrations.

**TensorFlow Lite** : Entraînement et déploiement du modèle.

**Caméra** : Capture d'images des composants électroniques.

**Node-RED** : Automatisation et gestion des flux de données.<<
