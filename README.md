# efishery-test

## Sensor Node
Sensor Node menggunakan ESP32. Random Number Generator, mengirimkan data setiap 10 detik.

### Cara Instalasi
1. Buka File esp32.ino pada Arduino IDE.
2. Pilih Board -> NodeMCU ESP32-S
3. Pilih Port untuk flash.
4. Tekan Tombol Upload

## Forwarder Node
Forwarder Node Menggunakan Raspberry Pi 3, Raspberry Pi OS.
Bahasa pemrograman penggunakan Python. Backend menggunakan flask, backup data menggunakan SQLite.

### Cara Instalasi

### Installing PyBlueZ from sources

Installing PyBluez
==================

PyBluez can be installed on GNU/Linux, Windows and macOS systems.

.. note:: Before you install **PyBluez** please install the dependencies required for
		  your system as described in the sections below.

**Installing PyBluez using pip**

Open a terminal (command prompt on Windows) and enter
::

	pip install pybluez

Run main.py menggunakan `sudo python3 main.py

## MQTT Topics

| Topic | Description |
| ----- | --- |
| mqtt/pub/data | Send Data from Forwarder to MQTT Broker |
| mqtt/sub/command | Receive Command from MQTT Broker |
| mqtt/pub/online | Online Notification |
| mqtt/pub/offline | Offline Notification |
| + | Wildcard Subscribe |

 
