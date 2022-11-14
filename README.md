# RFID-Jukebox
## Jukebox: Raspberry Pi, RFID, Spotify

This RFID Jukebox is a music player that uses an RFID module paired with a Raspberry Pi microprocessor to play music using Spotify! How does it work? Here's a breakdown:

- A Raspberry Pi is connected to an RFID scanner.
- RFID chips are programmed to contain track, playlist, album, or Spotify command info.
- The Raspberry Pi is integrated using Spotify's API and is enabled as a Spotify connect device
- When the pre-programmed RFID chips are tapped to the "Jukebox," it plays the corresponding songs!

This Jukebox does not require a screen to run; however, a certain file does need to be running when turned on in order to use. Currently, the file is accessed and ran through IDE using the connected touchscreen. However, I plan to create a GUI that will run upon starting the machine, and will add a fun effect to using the project! 

## Table of Contents

- Required materials
- Setting up the materials
- Configuring the device
- Spotify Integration
- Writing the code
- Finishing the project

## Required materials

These are the materials used to create the Jukebox. Some of these can be substituted for different versions and brands, but these are the exact ones that I used:

- Raspberry Pi 4 - https://www.canakit.com/raspberry-pi-4-extreme-kit.html
- RFID RC522 Module - https://a.co/d/8cnv7cw
- Female to Female Dupont wires - https://a.co/d/1a6E9Ke 
- Headphone Jack/USB Powered Speakers - https://www.amazon.com/dp/B005LW42MY?ref=ppx_pop_mob_ap_share 
- 7 Inch Touch Screen - https://www.amazon.com/dp/B071X8H5FB?ref=ppx_pop_mob_ap_share 
- RFID Chip Stickers - https://www.amazon.com/YARONGTECH-50pcs-MIFARE-Classic-adhesive-Sticker/dp/B01LZYOR7P?th=1

Something to note: I used a pre-sautered RFID module, but many of them do not come assembled. This is something to keep in mind when purchasing materials. 

## Setting up the materials
### Wiring the RFID module to the Raspberry Pi

First, we will need to connect the header pins of the RFID module to the Raspberry Pi. Note that the IRQ pin on the RFID module is not used. Here is a link that gives an easy to read pinout of the Raspberry Pi 4: https://pinout.xyz/

Use the female to female dupont wires to connect the RFID module to the Raspberry Pi. To keep track of where the wires are going, I recommend using a different color for each of the pins of the RFID module
| RFID Pins | Raspberry Pi Pins |
| ------ | ------ |
| SDA | Pin 24 (GPIO 8) |
| SCK | Pin 23 (GPIO 11) |
| MOSI | Pin 19 (GPIO 19) |
| MISO | Pin 21 (GPIO 9) |
| GND | Pin 6 (Ground) |
| RST | Pin 22 (GPIO 25) |
| 3.3V | Pin 1 (3.3V) |

### Connecting the other hardware

This is where I connected my speakers to the Raspberry Pi. I also will be using the Raspberry Pi headless, so I connected it to my monitor. 

## Configuring the device
If this is your first time using your Raspberry Pi, I recommend following a tutorial to set it up and turn it on. Once you have your Raspberry Pi set up, follow these steps to configure the device for our purposes. 

1. Run the following commands in the terminal to ensure that your device is up to date.

    ```sh
    sudo apt-get update
    sudo apt-get upgrade
    ```
2. Ensure compatibility with the RFID module by enabling SPI
a. Enter the following into the command line: 
    ```sh
    sudo raspi-config
    ```
    b. When the configuration menu opens, choose option menu 5 “Interfacing Options”
    c. Select “P4 SPI”
    d. When asked if you want to enable SPI interface select “Yes” 
    e. Once you see “The SPI interface is enabled” reboot your Raspberry Pi
	 ```sh
     sudo reboot
     ```
3. Install python, which is the language we will be using, as well as the following libraries that are used with the RFID module:
     ```sh
     sudo apt-get install python3-dev python3-pip
    sudo pip3 install spidev
    sudo pip3 install mfrc522
     ```


## Spotify Integration
## Writing the code
## Finishing the project
## Links and Credits
