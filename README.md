# RFID Reader dengan Python

Dokumentasi ini menjelaskan cara membaca kartu RFID menggunakan modul RFID RC522 dan Raspberry Pi dengan Python.

## Persyaratan

- Raspberry Pi (dengan Raspbian terinstall)
- Modul RFID RC522
- Perpustakaan Python:
  - `RPi.GPIO`
  - `mfrc522`

## Instalasi

1. **Update sistem**:
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

2. **Install Python dan pip**:
    ```bash
    sudo apt-get install python3 python3-pip
    ```

3. **Install library RPi.GPIO**:
    ```bash
    sudo pip3 install RPi.GPIO
    ```

4. **Install library mfrc522**:
    ```bash
    sudo pip3 install mfrc522
    ```

## Wiring

Sambungkan modul RFID RC522 ke Raspberry Pi sebagai berikut:

| Pin RC522 | Pin Raspberry Pi |
|-----------|------------------|
| SDA       | GPIO 8 (Pin 24)   |
| SCK       | GPIO 11 (Pin 23)  |
| MOSI      | GPIO 10 (Pin 19)  |
| MISO      | GPIO 9 (Pin 21)   |
| IRQ       | Tidak digunakan   |
| GND       | Ground (Pin 6)    |
| RST       | GPIO 25 (Pin 22)  |
| 3.3V      | 3.3V (Pin 1)      |

## Cara Kerja

Kode Python di bawah ini akan membaca data dari kartu RFID yang ditempelkan pada reader RC522. Data yang dibaca termasuk ID unik dari kartu dan teks yang tersimpan dalam kartu.

```python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

# Setup
reader = SimpleMFRC522()

try:
    print("Arahkan kartu RFID ke reader")
    id, text = reader.read()
    print(f"ID: {id}")
    print(f"Teks: {text}")
finally:
    GPIO.cleanup()
