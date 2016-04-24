Hardware Projects
#################

:slug: hardware
:menulabel: Hardware
:url: hardware
:sortorder: 2

GPIBUSB Adpater
---------------

**Languages**: C

**Platform**: Microchip PIC18F4520

**Source Code**:
`Firmware <https://www.github.com/Galvant/gpibusb-firmware>`__
`Circuit Board <https://www.github.com/Galvant/gpibusb-pcb>`__
`Bootloader <https://www.github.com/Galvant/gpibusb-bootloader>`__
`Documentation <https://www.github.com/Galvant/gpibusb-documentation>`__

**About**: This project was borne out of my frustration with proprietary GPIB to USB adapters. They typically require large driver downloads and very specific operating system and programming language combinations. Fet up with their high prices, I decided to create my own. The current version uses a Microchip PIC 18F4520 8-bit microcontroller for the main protocol conversion, an FTDI 230X for USB-to-Serial conversion, and the proper TI GPIB line driver ICs to interface the micro with the bus.

antiAFK
-------

**Languages**: Arduino Wiring

**Platform**: ATMega32u4

**Source Code**:
`Firmware <https://www.github.com/Galvant/antiafk_firmware>`__
`Circuit Board <https://www.github.com/Galvant/antiafk-pcb>`__

**About**: The antiAFK in simply a small USB-enabled dongle which acts like an HID keyboard. The main purpose and motivation behind this project was to have a small device which could be inserted into a computer's USB port to provide psudorandom keypresses to help prevent automatic logging out of online connected video games. These keypress events occur based on a stored period and variance, have a randomized press duration, and the key is chosen from a stored set (default is WASD and space). Settings are configurable through a virtual serial interface and are stored in the microcontroller EEPROM.

USB Wrapper
-----------

**Source Code**:
`Circuit Board <https://www.github.com/Galvant/usb_wrapper-pcb>`__

**About**: Connecting personal USB enabled devices to unknown ports can present a problem. Perhaps you want to connect your cell phone to a friends computer to charge it, but don't want their OS to start trying to interact with your phone. Or maybe you're trying to plug into an untrusted power source, such as a power adapter at an airport.

The USB Wrapper helps with the above by severing the USB data lines and only allowing the power lines to connect through. This ensures that no data information can be transferred between the power source and your device. This helps against known attacks such as juice jacking: http://krebsonsecurity.com/2011/08/beware-of-juice-jacking/

The USB Wrapper also addresses the problem where legitimate USB chargers use the data lines to communicate to the device how much power they are capable of sourcing. Different manufacturers do this differently, but thankfully most have agreed on one way. My solution is to use slider switches allowing emulation of whatever standard you'd like.

**Features**:

- Disconnects USB data lines between the host and device, preventing attacks such as "juice jacking" and keeps trusted computers from trying to sync
- Slider switches which allow you to tell your device what kind of charger is connected. Select from dedicated charger port, Sony, open circuit, and four different Apple chargers; 500mA, 1A, 2.1A, and 2.5A.
- USB-B and USB-micro-B connectors on the power side
- USB-A on the device side