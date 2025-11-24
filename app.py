import streamlit as st
import pandas as pd
#sad želimo uvesti funkciju iz ucitaj.py
from ucitaj import ucitaj_podatke

SHEET_URL=st.secrets["sheet_url"]
SHEET_NAME="filmovi"
df, worksheet=ucitaj_podatke(SHEET_URL, SHEET_NAME) #dt znaci dataframe
df["GODINA"]=pd.to_numeric(df["GODINA"]) #pretvaramo godine i ocjene u cijele brojeve
df["OCJENA"]=pd.to_numeric(df["OCJENA"])
st.title("Moji omiljeni filmovi")
st.subheader("Trenutni popis filmova")
st.dataframe(df)

st.subheader("Dodaj novi film")
naslov=st.text_input("Naslov")
godina=st.number_input("Godina",step=1, format="%d") #step=1, kad korisnik određuje godinu da može birati s popisa gdje su navedene jedna za drugom / %d znači da godina bude prikazana kao cijeli broj (bez decimalne točke)
zanr=st.text_input("Žanr")
ocjena=st.slider("Ocjena",1,10) #slider je klizač, 1,10 je raspon

if st.button("Dodaj film"):
    novi_red=[naslov,int(godina),zanr,ocjena]
    worksheet.append_row(novi_red)
    st.success("Film je uspješno dodan")
    st.rerun() #rerun automatski osvježi stranicu kad dodamo neš novo ili maknemo

st.subheader("Pretraži filmove")
filtrirani=df.copy() #ne zelimo da u originalnoj bazi filtrira, nego na app

žanr_filt=st.text_input("Pretraži po žanru")
godina_filt=st.number_input("Pretraži po godini",step=1,format="%d")

if žanr_filt:
    filtrirani=filtrirani[filtrirani["žanr"].str.contains(žanr_filt,case=False)] #ono što korisnik unese ako se nalazi među već unesenim žanrovima onda će se ispisati ti žanrovi
if godina_filt:
    filtrirani=filtrirani[filtrirani["Godina"]==int(godina_filt)]

st.dataframe(filtrirani)

filmovi_opcije=df.apply(lambda row: f"{row['Naslov'} ({row['Godina']})", axis=1).tolist()  #axis=1 znaci da ide red po red ova lambda funkcija / .tolist znaci da pretvori sve u listu
film_za_brisanje=st.selectbox("Odaberi film za brisanje", options=filmovi_opcije) #selectbox je padajuci izbornik

if st.button("Izbriši film"):
    for idx,row in df.iterrows():
        if f"{row['Naslov']} ({row['Godina']})"==film_za_brisanje:
            worksheet.delete_rows(idx+2) 
            st.success("Film je uspješno izbrisan")
            st.rerun()
st.subheader("TOP 3 FILMA")

top3=df.sort_values(by="Ocjena",ascending=False).head(3)
st.table(top3)


