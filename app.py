import streamlit as st
import pandas as pd
import gspread
from ucitaj import ucitaj_podatke

# Učitavanje podataka
SHEET_URL = st.secrets["sheet_url"]
SHEET_NAME = "filmovi"
df, worksheet = ucitaj_podatke(SHEET_URL, SHEET_NAME)

df["GODINA"] = pd.to_numeric(df["GODINA"], errors="coerce")
df["OCJENA"] = pd.to_numeric(df["OCJENA"], errors="coerce")

# Prikaz postojećih filmova
st.title("Moji omiljeni filmovi")
st.subheader("Trenutni popis filmova")
st.dataframe(df)

# Dodavanje filma
st.subheader("Dodaj novi film")
naslov = st.text_input("NASLOV")
godina = st.number_input("GODINA", step=1, format="%d")
zanr = st.text_input("ŽANR")
ocjena = st.slider("OCJENA", 1, 10)

if st.button("Dodaj film"):
    if naslov and zanr:
        worksheet.append_row([naslov, int(godina), zanr, int(ocjena)])
        st.success("Film je uspješno dodan! Osvježite stranicu da vidite promjene.")
    else:
        st.warning("Unesite NASLOV i ŽANR.")

# Pretraživanje
st.subheader("Pretraži filmove")
filtrirani = df.copy()

zanr_filt = st.text_input("Pretraži po žanru")
godina_filt = st.number_input("Pretraži po godini", step=1, format="%d", value=0)

if zanr_filt:
    filtrirani = filtrirani[filtrirani["ŽANR"].str.contains(zanr_filt, case=False, na=False)]
if godina_filt:
    filtrirani = filtrirani[filtrirani["GODINA"] == int(godina_filt)]

st.dataframe(filtrirani)

# Brisanje filma
st.subheader("Izbriši film")
filmovi_opcije = df.apply(lambda r: f"{r['NASLOV']} ({r['GODINA']})", axis=1).tolist()
film_za_brisanje = st.selectbox("Odaberi film za brisanje", filmovi_opcije)

if st.button("Izbriši film"):
    for idx, row in df.iterrows():
        if f"{row['NASLOV']} ({row['GODINA']})" == film_za_brisanje:
            try:
                worksheet.delete_rows(idx + 2)  # header + zero-index
                st.success("Film izbrisan! Ručno osvježite stranicu za prikaz promjena.")
            except gspread.exceptions.APIError:
                st.error("Ne mogu obrisati red. Provjerite dopuštenja ili Google Sheets API.")
            break

# Top 3
st.subheader("TOP 3 FILMA")
top3 = df.sort_values(by="OCJENA", ascending=False).head(3)
st.table(top3)
