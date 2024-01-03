from   forex_python.converter import CurrencyRates
import json
from datetime import datetime

c = CurrencyRates()


rate = c.get_rate('USD', 'EUR')
print(f"Taux de change USD vers EUR : {rate}")

def convertir_devise(montant, devise_source, devise_cible):
    try:
        taux = CurrencyRates().get_rate(devise_source, devise_cible)
        montant_converti = montant * taux
        return montant_converti
    except Exception as e:
        print(f"Erreur de conversion : {e}")
        return None


def charger_historique():
    try:
    
                with open('historique_conversions.json', 'r') as file:
    
                        return json.load(file)
    except FileNotFoundError:
    
      return []


def sauvegarder_historique(conversion):
     historique = charger_historique()
     conversion['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
     
     historique.append(conversion)
     with open('historique_conversions.json', 'w') as file:
       json.dump(historique, file, indent=2)

def afficher_historique():
    historique = charger_historique()

    if historique:
        print("Historique des conversions :")
        for conversion in historique:
            print(f"{conversion['date']} - {conversion['montant']} {conversion['devise_source']} en {conversion['devise_cible']} : {conversion['montant_converti']} {conversion['devise_cible']}")
    else:
        print("Aucun historique de conversions.")
if __name__ == "__main__":
    montant = float(input("Entrez le montant à convertir : "))
    devise_source = input("Entrez la devise source (par ex. USD) : ").upper() 
    devise_cible = input("Entrez la devise cible (par ex. EUR) : ").upper()

    montant_converti = convertir_devise(montant, devise_source, devise_cible)

    if montant_converti is not None:
        print(f"{montant} {devise_source} équivaut à {montant_converti} {devise_cible}")

        conversion = {
            'montant': montant,
            'devise_source': devise_source,
            'devise_cible': devise_cible,
            'montant_converti': montant_converti
        }
        sauvegarder_historique(conversion)

        afficher_historique()