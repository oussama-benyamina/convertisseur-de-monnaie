#Importation des Bibliothèques :

#Nous commençons par importer quelques bibliothèques nécessaires pour notre script, notamment celles pour la conversion des devises et le traitement des dates.
#Obtention de Toutes les Devises :

#Une fonction a été ajoutée pour obtenir une liste de toutes les devises disponibles. Cela permet à l'utilisateur de choisir n'importe quelle devise pour la conversion.
#Fonction de Conversion de Devises :

#Une fonction convertit un montant d'une devise source à une devise cible. Elle utilise la bibliothèque forex_python pour obtenir le taux de change.
#Gestion de l'Historique :

#Le script gère un historique des conversions. Il peut charger, sauvegarder et afficher cet historique.
#Partie Principale du Script :

#La partie principale permet à l'utilisateur d'entrer le montant, la devise source et la devise cible. 
# Il peut choisir parmi toutes les devises disponibles. La conversion est affichée, et l'historique est mis à jour et affiché.

from forex_python.converter import CurrencyRates
import json
from datetime import datetime

from moha import afficher_historique, sauvegarder_historique

def get_all_currencies():
    try:
        c = CurrencyRates()
        currencies = c.get_rates('USD')
        return list(currencies.keys())
    except Exception as e:
        print(f"Erreur lors de la récupération des devises : {e}")
        return None

def convertir_devise(montant, devise_source, devise_cible):
    try:
        taux = CurrencyRates().get_rate(devise_source, devise_cible)
        montant_converti = montant * taux
        return montant_converti
    except Exception as e:
        print(f"Erreur de conversion : {e}")
        return None

# ... (other functions remain the same)

if __name__ == "__main__":
    all_currencies = get_all_currencies()

    if all_currencies:
        print("Devises disponibles :", ', '.join(all_currencies))
        devise_source = input("Entrez la devise source : ").upper()
        devise_cible = input("Entrez la devise cible : ").upper()

        if devise_source not in all_currencies or devise_cible not in all_currencies:
            print("Devise source ou cible invalide.")
        else:
            montant = float(input("Entrez le montant à convertir : "))
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
    else:
        print("Aucune devise disponible.")
