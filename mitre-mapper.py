#!/usr/bin/env python3
import urllib.request
import json
import os
import argparse
import sys
import re

C = '\033[96m'  # Ciano
G = '\033[92m'  # Verde
Y = '\033[93m'  # Giallo
R = '\033[91m'  # Rosso
W = '\033[0m'   # Reset

URL_MITRE = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"
CACHE_FILE = "mitre_database_reale.json"

def scarica_database():
    print(f"{Y}[*] Scaricamento del database ufficiale MITRE ATT&CK...{W}")
    try:
        urllib.request.urlretrieve(URL_MITRE, CACHE_FILE)
        print(f"{G}[+] Database aggiornato con successo!{W}\n")
    except Exception as e:
        print(f"{R}[!] Errore di connessione: {e}{W}")
        sys.exit(1)

def carica_dati(forza_aggiornamento=False):
    if forza_aggiornamento or not os.path.exists(CACHE_FILE):
        scarica_database()
    with open(CACHE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def cerca_miglior_risultato(dati, query):
    parole_chiave = [p.lower() for p in re.findall(r'\w+', query)]
    if not parole_chiave:
        return None

    candidati = []

    for obj in dati.get("objects", []):
        if obj.get("x_mitre_deprecated") or obj.get("revoked"):
            continue

        tipo = obj.get("type")
        if tipo in ["attack-pattern", "tool", "malware"]:
            nome = obj.get("name", "").lower()
            desc = obj.get("description", "").lower()
            
            punteggio = 0
            
            if query.lower() == nome:
                punteggio += 150
            elif query.lower() in nome:
                punteggio += 80

            for p in parole_chiave:
                if p in nome:
                    punteggio += 25
                if p in desc:
                    punteggio += 5
            
            if punteggio > 0:
                refs = obj.get("external_references", [])
                tech_id = next((r.get("external_id") for r in refs if r.get("source_name") in ["mitre-attack", "mitre-tool", "mitre-malware"]), "N/A")
                
                fasi = obj.get("kill_chain_phases", [])
                tattiche = [f.get("phase_name").replace("-", " ").title() for f in fasi]
                
                candidati.append({
                    "punteggio": punteggio,
                    "id": tech_id,
                    "nome": obj.get("name"),
                    "tipo": "Strumento/Tool" if tipo in ["tool", "malware"] else "Tecnica",
                    "tattiche": tattiche if tattiche else ["Execution / Lateral Movement"]
                })

    candidati.sort(key=lambda x: x["punteggio"], reverse=True)
    return candidati[0] if candidati else None

def main():
    parser = argparse.ArgumentParser(description="mitre-mapper V1.0 - Report Incidente")
    parser.add_argument("indizi", nargs="*", help="Indizi da cercare (es. mimikatz 'pass the hash')")
    parser.add_argument("-u", "--update", action="store_true", help="Forza l'aggiornamento del database MITRE")
    args = parser.parse_args()

    if not args.indizi and not args.update:
        parser.print_help()
        sys.exit(1)

    dati = carica_dati(args.update)
    
    if not args.indizi:
        sys.exit(0)

    print(f"{C}="*55)
    print(" 🎯 mitre-mapper V1.0 - REPORT INCIDENTE")
    print("="*55 + f"{W}\n")

    for indizio in args.indizi:
        risultato = cerca_miglior_risultato(dati, indizio)
        if risultato:
            tattica = ", ".join(risultato["tattiche"])
            print(f"{Y}Indizio cercato:{W} {indizio}")
            print(f" ┣━ {G}{risultato['tipo']}:{W} {risultato['nome']} ({risultato['id']})")
            print(f" ┗━ {C}Fase/Tattica:{W} {tattica}\n")
        else:
            print(f"{Y}Indizio:{W} {indizio}")
            print(f" ┗━ {R}Nessun riscontro trovato nel database.{W}\n")

if __name__ == "__main__":
    main()
