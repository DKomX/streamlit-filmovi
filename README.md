# streamlit-filmovi
# Application for managing a list of favorite films (Streamlit + Google Sheets)

# Project description
This is a Streamlit web application that enables viewing, adding, filtering, and deleting films stored in a Google Sheets document.
The application uses Google Sheets as a simple backend database, while Streamlit serves as the graphical interface.
The user can:
  view all films from the table
  add a new film
  filter films by genre and year
  delete a selected film
  view TOP 3 films according to rating

# Technology stack
  Python
  Streamlit (frontend)
  Pandas (table processing)
  gspread (communication with Google Sheets API)
  Google Sheets (data storage)

# Project structure

project/
│
├── app.py # Main Streamlit application
├── ucitaj.py # Module for loading data from Google Sheets
│
├── requirements.txt # List of Python packages
└── README.md # Documentation

# Setting up Google Sheets API
The application uses Streamlit secrets for secure storage of data.

In the .streamlit/secrets.toml file there must be:
  sheet_url = "URL_OF_YOUR_SHEET"
  service_account = { ... JSON data ... }

The Google Sheet must have a sheet named:
  filmovi

Columns must be:
  NASLOV | GODINA | ŽANR | OCJENA

# How to run the application
1. Install packages:
      pip install -r requirements.txt
2. Create .streamlit/secrets.toml.
3. Run Streamlit:
      streamlit run app.py

# Requirements
The requirements.txt file must contain at least:
  streamlit
  pandas
  gspread
  google-auth

# Notes
Streamlit does not automatically refresh data from Google Sheets after entry — refreshing the page manually is required.
Google Sheets API sometimes limits the number of operations; sufficient permissions must be granted.
