# Basketball Team Stats Tool

This Python application is designed to manage and display statistics for basketball teams and their players.

## Features

- Displays a menu of basketball teams
- Shows detailed statistics for a selected team including:
   - Total number of players
   - Number of experienced and inexperienced players
   - Average height of the team
   - List of players on the team
   - List of guardians for all players on the team
- Evenly distributes players across teams based on experience

## Files

- `app.py`: The main script that runs the application
- `constants.py`: Contains constant data such as player information and team names
- `functions.py`: Contains utility functions for data processing

## How to Use

1. Run the `app.py` script
2. You will be presented with a menu of basketball teams
3. Enter the number corresponding to the team you want to view
4. The application will display detailed statistics for the selected team
5. Press Enter to return to the main menu or exit the application

## Functions

The application uses several helper functions to process and display data:

- `make_height_integer()`: Converts player heights to integers
- `make_experience_boolean()`: Converts player experience to boolean values
- `make_guardians_list()`: Ensures guardians are stored as lists
- `sort_for_experience()`: Sorts players based on their experience
- `distribute_list_items_equally()`: Evenly distributes players across teams

## Data Structure

Player data is stored as a list of dictionaries, where each dictionary represents a player with the following keys:
- `name`: Player's name
- `guardians`: List of player's guardians
- `experience`: Boolean indicating if the player is experienced
- `height`: Player's height in inches

Team data is stored as a dictionary, where keys are team names and values are lists of player dictionaries.

## Requirements

- Python 3.x

## Running the Application

To run the application, navigate to the directory containing the script and run: