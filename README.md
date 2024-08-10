# Coffee Shop Time Tracker

## Overview

The Coffee Shop Time Tracker is a simple Python application designed to manage clients in a coffee shop environment. This program allows you to add and remove clients, while keeping track of the duration each client spends in the shop. It's a useful tool for coffee shop owners or managers who want to monitor client activity and improve service efficiency.

## Features

- **Add Client**: Add a new client to the coffee shop.
- **Remove Client**: Remove a client and log the time they spent in the shop.
- **Display Current Clients**: View a list of all current clients along with the duration of their stay.
- **User-Friendly Interface**: Simple command-line interface for easy interaction.

## Installation

To run the Coffee Shop Time Tracker, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

### Steps to Run

1. **Clone the Repository**: If you have Git installed, you can clone this repository using:
   ```bash
   git clone <repository-url>

Or download the ZIP file and extract it.
Navigate to the Project Directory:
bash
cd coffee-shop-time-tracker

Run the Application:
bash
python coffee_shop_time_tracker.py

Usage
Once the application is running, you will see a menu with the following options:
Add Client: Input the name of the client you want to add.
Remove Client: Input the name of the client you want to remove. The application will display how long the client stayed.
Display Current Clients: View a list of all clients currently in the shop along with their duration.
Exit: Close the application.
Example Interaction
text
1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 1
Enter client name: Alice
Added client Alice

Code Structure
Client Class: Represents a client in the coffee shop, tracks their name, start time, and end time.
CoffeeShop Class: Manages the collection of clients, allowing for adding, removing, and displaying clients.
Main Function: The entry point of the application that handles user input and interactions.
Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments
Thanks to the Python community for their ongoing support and resources that made this project possible.
