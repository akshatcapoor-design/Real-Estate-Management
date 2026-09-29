# Real Estate Management System

## Project Description

This is a simple console-based Python program to manage property records. The user can add, view, search, update and delete properties from a menu shown in the terminal. The property data is saved in a JSON file, so it stays saved even after the program is closed. I made this project as a first-year B.Tech CSE student to practice basic Python concepts.

## Problem Statement

Property details are often written in notebooks or spread across different files, which makes it hard to find a property quickly or update its details. This project is a small program that keeps all property records in one place and lets the user manage them easily.

## Objectives

- To store basic property details in an organised way
- To add, view, search, update and delete property records
- To save the data in a file so it is not lost when the program closes
- To practice functions, lists, dictionaries, loops, conditions and file handling in Python
- To split the program into separate files so the code is easy to read

## Features

- **Add Property** - enter the details of a new property. The program checks that numbers are entered correctly and does not allow two properties with the same ID.
- **View All Properties** - shows all saved properties in a list.
- **Update Property** - find a property by its ID and change its details. Fields can be left blank to keep the old value.
- **Delete Property** - remove a property using its ID.
- **Search Properties** - search using a keyword. It looks in both the title and the location (not case sensitive).
- **File Storage** - all properties are saved in `properties.json`.

Each property stores:

| Field | Description |
|-------|-------------|
| ID | Property ID (whole number) |
| Title | Name or short title of the property |
| Location | Area or city of the property |
| Price | Price of the property |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Area | Area in square feet |

## Technologies Used

- Python 3
- `json` and `os` modules (built into Python)
- Git and GitHub for version control

No external libraries are needed.

## How the Program Works

The project is divided into separate files, and each file does one job:

| File | Purpose |
|------|---------|
| `main.py` | Shows the menu and calls the other functions |
| `connect.py` | Creates the data file, loads data from it and saves data to it |
| `add.py` | Adds a new property |
| `view.py` | Shows all properties |
| `update.py` | Updates an existing property |
| `delete.py` | Deletes a property |
| `search.py` | Searches properties by keyword |

Working:

1. When the program starts, `main.py` calls `create_table()` which creates an empty `properties.json` file if it does not exist yet.
2. A menu is shown inside a `while` loop and the user enters a choice from 1 to 6.
3. Depending on the choice, the matching function is called.
4. Properties are stored as dictionaries inside a list. The list is read from the JSON file each time it is needed and written back after a change.
5. If the user enters something wrong (like text instead of a number, or an ID that does not exist), a message is shown instead of the program crashing.
6. The menu keeps repeating until the user chooses option 6 (Exit).

## How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository:
   ```
   git clone <your-repository-link>
   ```
3. Open a terminal in the project folder (all the `.py` files must be in the same folder).
4. Run:
   ```
   python main.py
   ```
5. Follow the menu on the screen.

`properties.json` will be created automatically the first time you run the program.

## Sample Usage

```
=== Real Estate Management System ===
1. Add Property
2. View All Properties
3. Update Property
4. Delete Property
5. Search Properties
6. Exit
Enter your choice: 1
Enter ID of the property: 1
Enter property title: Green Villa
Enter location: Indore
Enter price: 5000000
Enter number of bedrooms: 3
Enter number of bathrooms: 2
Enter area in square feet: 1500
Property added successfully.

Enter your choice: 2

All Properties:
ID | Title | Location | Price | Bedrooms | Bathrooms | Area
-----------------------------------------------------------------
1 | Green Villa | Indore | $5,000,000.00 | 3 | 2 | 1500.0 sq ft

Enter your choice: 5
Enter search keyword (location/title): indore

Search Results:
ID: 1, Title: Green Villa, Location: Indore, Price: $5,000,000.00, Bedrooms: 3, Bathrooms: 2, Area: 1500.0 sq ft
```

## Testing

I have tested the program manually (there are no automated tests yet). Some things I tried:

- Adding a property and checking that it appears in "View All Properties"
- Adding a property with an ID that already exists (shows an error message)
- Entering text where a number is needed (shows an error message)
- Updating only one field and leaving the others blank
- Searching with a keyword that has no match
- Deleting an ID that does not exist
- Closing the program and running it again to check that the data is still saved

## Future Improvements

- Add more property details that are not in the program yet, like property type (flat, house, plot), owner name and availability status (available/sold)
- Stop the user from entering negative values or empty titles/locations (right now these are not checked)
- Search by price range, number of bedrooms, etc.
- Sort properties by price
- Add unit tests
- Add a login system
- Make a GUI version of the program

## Author

Akshat Capoor
B.Tech CSE, 1st Year
VIT Bhopal
Registration No: 26BCE10267
