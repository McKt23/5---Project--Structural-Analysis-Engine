# Installation and Setup Guide

This document explains how to install and run the **Structural Analysis Engine** on your computer. The software provides two different ways to run: using a pre-packaged executable file (which requires no installation) or running directly from the Python source code.

## Option 1: Running the Executable (Recommended)

The easiest way to use the Structural Analysis Engine is to run the pre-built executable file. This method does not require you to install Python or any external libraries.

### Steps:
1. Extract the provided project archive (`.zip` or `.rar`) to a folder on your computer.
2. Open the extracted folder and locate the `Antigravity_Structural_Engine.exe` file.
3. Double-click the executable file to launch the application.
4. The user interface will open immediately, and you can start creating or importing your structural models.

*Note: Depending on your Windows security settings, you may receive a "Windows protected your PC" prompt. If this happens, click **More info** and then **Run anyway**.*

## Option 2: Running from Source Code

If you want to view the source code, run the unit tests, or modify the program, you can run the software directly using Python.

### Prerequisites:
- **Python 3.8 or higher** must be installed on your computer. You can download it from [python.org](https://www.python.org/).
- Ensure that you check the box **"Add Python to PATH"** during the Python installation process.

### Steps:

1. **Extract the Project Files**
   Extract the provided project archive to a folder of your choice.

2. **Open the Terminal**
   Open a Command Prompt or PowerShell window and navigate to the project folder. For example:
   ```bash
   cd "C:\Path\To\Extracted\Project"
   ```

3. **Install Required Libraries**
   The software relies on several external Python libraries for its graphical interface, matrix calculations, and plotting features. Install them by running:
   ```bash
   pip install -r requirements.txt
   ```
   *This command will automatically download and install `numpy`, `matplotlib`, `customtkinter`, `reportlab`, and other necessary dependencies.*

4. **Run the Application**
   Once the installation is complete, you can launch the software by running the main application script:
   ```bash
   python main.py
   ```

## Running the Verification Tests

The project includes an automated testing suite to verify the mathematical accuracy of the computational engine. If you are running the software from the source code, you can execute these tests.

1. Open your terminal in the main project directory.
2. Run the following command:
   ```bash
   python -m unittest discover -s tests -p "test_*.py" -v
   ```
3. The terminal will display the status of each test (e.g., thermal loads, support settlements, matrix assemblies). A status of `OK` indicates that all analytical verifications passed successfully.
