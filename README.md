# 🎯 mitre-mapper V1.0

**MITRE Mapper** è un tool a riga di comando (CLI) sviluppato in Python progettato per analizzare indizi, artefatti o parole chiave relative a un incidente di sicurezza e mapparli automaticamente sulle Tecniche, sui Tool e sui Malware del framework ufficiale MITRE ATT&CK.

Lo strumento scarica e utilizza il database JSON ufficiale enterprise-attack di MITRE, filtrando gli elementi deprecati o revocati e restituendo un report strutturato con relative tattiche e ID di riferimento.

---

## 🚀 Caratteristiche principali

* Mappa automatica degli indizi: Inserisci una o più parole chiave (es. mimikatz, pass the hash) per trovare la corrispondenza più pertinente.
* Aggiornamento del Database: Gestione locale del database MITRE con opzione di aggiornamento forzato tramite linea di comando.
* Filtri intelligenti: Esclude in automatico le voci deprecate o revocate per garantire risultati accurati e aggiornati.
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

1. Caching del Database: Alla prima esecuzione (o se richiesto tramite -u), il tool scarica il file JSON ufficiale dal repository GitHub di MITRE.
2. Analisi e Scoring: Il testo inserito viene suddiviso in parole chiave e confrontato con il nome e la descrizione di tecniche, tool e malware. Viene assegnato un punteggio di rilevanza per estrarre il miglior risultato possibile.
3. Report: Viene stampato un riepilogo indicando il tipo di riscontro (Tecnica o Strumento), l'ID ufficiale MITRE e la Kill Chain Phase (Tattica) associata.

---

## 🤝 Contributi
I contributi sono benvenuti! Sentiti libero di aprire una Pull Request o segnalare un Issue per suggerire miglioramenti.

---

## 📜 Licenza
Questo progetto è distribuito sotto licenza [MIT](LICENSE).
