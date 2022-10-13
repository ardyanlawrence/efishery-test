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

For experimental Bluetooth Low Energy support (only for Linux platform -
for additional dependencies please take look at:
`ble-dependencies <https://github.com/oscaracena/pygattlib/blob/master/DEPENDS>`_)
::

    pip install pybluez[ble]

 
