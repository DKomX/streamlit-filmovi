prevedi na engleski word for word i isti format:

# streamlit-filmovi
# Aplikacija za upravljanje listom omiljenih filmova (Streamlit + Google Sheets)

# Opis projekta
  Ovo je Streamlit web aplikacija koja omogućuje pregled, dodavanje, filtriranje i brisanje filmova pohranjenih u Google Sheets dokumentu.
  Aplikacija koristi Google Sheets kao jednostavnu backend bazu podataka, dok Streamlit služi kao grafičko sučelje.
  Korisnik može:
    pogledati sve filmove iz tablice
    dodati novi film
    filtrirati filmove po žanru i godini
    izbrisati odabrani film
    pregledati TOP 3 filma prema ocjeni

# Tehnološki stack
  Python
  Streamlit (frontend)
  Pandas (obrada tablica)
  gspread (komunikacija s Google Sheets API-jem)
  Google Sheets (pohrana podataka)

# Struktura projekta
project/
│
├── app.py                # Glavna Streamlit aplikacija
├── ucitaj.py             # Modul za učitavanje podataka iz Google Sheetsa
│
├── requirements.txt      # Popis Python paketa
└── README.md             # Dokumentacija 

# Postavljanje Google Sheets API-ja

Aplikacija koristi Streamlitove secrets za sigurno spremanje podataka.
U .streamlit/secrets.toml datoteci mora biti:
    sheet_url = "URL_TVOJE_TABLICE"
    service_account = { ... JSON podaci ... }

Google Sheet mora imati sheet naziva:
    filmovi

Stupci moraju biti:
    NASLOV | GODINA | ŽANR | OCJENA

# Kako pokrenuti aplikaciju
    1. Instalirati pakete:
          pip install -r requirements.txt
    2. Kreirati .streamlit/secrets.toml.
    3. Pokrenuti Streamlit:
          streamlit run app.py

# Zahtjevi
Datoteka requirements.txt treba sadržavati barem:
    streamlit
    pandas
    gspread
    google-auth

# Napomene
Streamlit ne osvježava automatski podatke iz Google Sheetsa nakon unosa — potrebno je ručno osvježiti stranicu.
Google Sheets API ponekad ograničava broj zahvata; potrebno je imati dovoljno dopuštenja.
