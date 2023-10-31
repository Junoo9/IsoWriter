# ISO Writer

## Introduction

This Python script provides a simple graphical user interface (GUI) for burning ISO images to a selected target drive. It utilizes the Tkinter library for the GUI, the filedialog library for file picking, and the pyudev library for listing available drives. Additionally, the `dd` command is used to perform the ISO burning operation.

## Usage

### Prerequisites

Before using the ISO Writer, make sure you have the following dependencies installed on your Linux machine:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- pyudev (install with `pip install pyudev`)

### Running the Script

1. Clone or download this repository to your local machine.
git clone https://github.com/Junoo9/IsoWriter.git


2. Open a terminal and navigate to the script's directory:
cd /path/to/IsoWriter


3. Run the script using Python:
python main.py


This will launch the GUI window.

### Using the GUI

- **Select ISO Image**: Click the "Browse" button to select the ISO image file you want to burn.

- **List Drives**: Click the "List Drives" button to view the available drives.

- **Select Target Drive**: Choose a drive from the list or manually enter the device path into the entry field.

- **Burn ISO**: Click the "Burn ISO" button to initiate the burning process. You may be prompted to enter your sudo password since it requires superuser privileges to write to the drive.

- **Result**: The outcome of the burning process will be displayed in the result label at the bottom of the window.

## Important Notes

- Exercise caution when using this script, especially when selecting the target drive. Writing to the wrong drive can lead to data loss.
- This script is intended for Linux-based systems and has been tested on Ubuntu. While it may work on other Linux distributions, it's essential to be familiar with your system's device naming conventions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The script was created by Charbel Rahme.
- Special thanks to the open-source community for the libraries and tools used in this project.

Feel free to modify and improve this README as needed for your project.

