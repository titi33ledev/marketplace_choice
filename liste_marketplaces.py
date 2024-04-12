#%%
import pandas as pd
#%%
data = pd.read_excel("data_marketplaces.xlsx")
#%%
def charger_donnees(chemin_fichier):
    df = pd.read_excel(chemin_fichier)
    # Supprimer les espaces superflus dans la colonne 'categorie'
    df['categorie'] = df['categorie'].str.strip()
    return df

data = charger_donnees("data_marketplaces.xlsx")
#%%
def filtrer_marketplaces(categorie,segment,type_marketplaces ,data):
    # Filtrer les marketplaces en fonction de la catégorie choisie
    marketplaces_filtrées = data[data["categorie"] == categorie]
    
    # Utiliser directement le segment fourni pour filtrer
    marketplaces_filtrées = marketplaces_filtrées[marketplaces_filtrées["segment_marketplaces"] == segment]

    # Filtrer en fonction du type de marketplace, si spécifié
    if type_marketplaces != (0,):  # S'assurer que le tuple pour aucun filtre est correct
        marketplaces_filtrées = marketplaces_filtrées[marketplaces_filtrées["types_marketplaces"].isin(type_marketplaces)]
    
    return marketplaces_filtrées[['categorie', 'marketplaces']]
