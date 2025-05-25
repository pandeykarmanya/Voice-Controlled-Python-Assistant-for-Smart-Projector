# Voice-Controlled Python Assistant for Smart Projector

This Python project implements a voice-controlled assistant that can interact with an Arduino microcontroller to control a smart projector setup. It listens to voice commands and sends instructions to the Arduino via serial communication.

---

## HOW IT WORKS
The assistant continuously listens for your voice commands.

When you say "turn on presentation mode", it sends a command to the Arduino to activate connected devices.

Say "turn off" to deactivate presentation mode.

Say "quit" to exit the program gracefully.

## Features

- Uses **SpeechRecognition** to capture and interpret voice commands.
- Connects to Arduino over serial port.
- Supports commands like:
  - "Turn on presentation mode" — starts the presentation mode.
  - "Turn off" — shuts down presentation mode.
  - "Quit" — exits the assistant and closes connections.
- Provides voice feedback using the macOS `say` command.

---

## Requirements

- Python 3.x
- `speech_recognition` Python package (`pip install SpeechRecognition`)
- An Arduino connected via serial port (configured for your environment)
- macOS (or modify the `say()` function for other OS text-to-speech)

---

## Setup

1. **Connect your Arduino** to your computer and identify the serial port.
2. **Modify the serial port** in the script (`arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=9600, timeout=1)`) to match your device.
3. **Install Python dependencies**:

   ```bash
   pip install SpeechRecognition
