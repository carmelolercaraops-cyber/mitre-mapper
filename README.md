# 🎯 mitre-mapper V1.0

**MITRE Mapper** è un tool CLI sviluppato in Python che cerca corrispondenze tra parole chiave o indizi di sicurezza forniti dall'utente e gli oggetti del framework MITRE ATT&CK Enterprise.

Il tool scarica e utilizza il database JSON ufficiale di MITRE ATT&CK, esclude gli elementi deprecati o revocati e restituisce i risultati più pertinenti insieme al relativo ID e alla tattica ATT&CK.


## 🚀 Caratteristiche principali

* Mappa automatica degli indizi: Inserisci una o più parole chiave (es. mimikatz, pass the hash) per trovare la corrispondenza più pertinente.
* Aggiornamento del Database: Gestione locale del database MITRE con opzione di aggiornamento forzato tramite linea di comando.
* Filtraggio degli oggetti non validi: esclude automaticamente gli elementi deprecati o revocati.
* Output strutturato a colori: Report chiaro e leggibile direttamente nel terminale.

---

## ⚙️ Requisiti

* Python 3.x (il tool utilizza esclusivamente librerie standard integrate come urllib, json, os, argparse, sys e re).

---

## 📥 Installazione

Clona il repository nella tua macchina locale usando l'URL corretto:

git clone https://github.com/carmelolercaraops-cyber/mitre-mapper.git

Entra nella cartella del progetto appena clonata:

cd mitre-mapper

Rendi eseguibile lo script (opzionale, su sistemi Unix/Linux):

chmod +x mitre-mapper.py

---

## 💡 Utilizzo

Puoi passare direttamente gli indizi come argomenti da riga di comando:

python3 mitre-mapper.py "mimikatz" "pass the hash"

### Opzioni disponibili:
* -u o --update: Forza il download e l'aggiornamento del database ufficiale MITRE ATT&CK (mitre_database_reale.json).

Esempio di aggiornamento forzato:

python3 mitre-mapper.py --update

---

## 🛠️ Come funziona

1. Database
   Alla prima esecuzione il tool scarica il dataset JSON
   ufficiale MITRE ATT&CK e lo salva localmente.

2. Matching e scoring
   Gli input dell'utente vengono normalizzati e confrontati
   con nomi e descrizioni degli oggetti ATT&CK.
   I risultati vengono ordinati in base alla rilevanza.

3. Output
   Il tool mostra nel terminale i risultati più pertinenti,
   includendo tipologia, nome, ID ATT&CK e tattica associata.


---

## 🤝 Contributi
I contributi sono benvenuti! Sentiti libero di aprire una Pull Request o segnalare un Issue per suggerire miglioramenti.

---

## 📜 Licenza
Questo progetto è distribuito sotto licenza [MIT](LICENSE).
