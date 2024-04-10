import streamlit as st
from liste_marketplaces import filtrer_marketplaces, charger_donnees

data = charger_donnees("data_marketplaces.xlsx")

st.title("Trouvez votre marketplace idéale 🎯")
st.markdown("Vous allez pouvoir savoir quelles sont les marketplaces qui répondent le plus à vos produits.")

# Sélection de la catégorie
option = st.selectbox("Sélectionnez votre catégorie correspondante", 
                      ("Maison & Habitat", "Mode & Chaussures", "Bébé & Enfants", "Sport",'Beauté & Santé',"DIY & Jardin"))
st.write("Catégorie sélectionnée :", option)

# Options de panier moyen en fonction de la catégorie
paniers_moyens_options = {
    'Maison & Habitat': ["0-499", "500-999", "1000-1499", "1500+"],
    'Mode & Chaussures': ["0-49", "50-99", "100-199", "200+"],
    'Bébé & Enfants': ["0-99", "100-199", "200-499", "500+"],
    'Sport': ["0-49", "50-140", "150-299", "300+"],
    'Beauté & Santé': ["0-99", "100-199", "200-499", "500+"],
    "DIY & Jardin": ["0-499", "500-999", "1000-1499", "1500+"]
}

# Sélection du panier moyen
options_panier_moyen = paniers_moyens_options[option]
option_2 = st.selectbox('Choisissez votre panier moyen :', options_panier_moyen).strip()
st.write("Prix moyen sélectionné :", option_2)

# Fonction de conversion du panier moyen
def convertir_panier_moyen(categorie, tranche_selectionnee):
    
    if categorie == 'Maison & Habitat':
        tranches = {
            "0-499": 1,
            "500-999": 2,
            "1000-1499": 3,
            "1500+": 4
        }
        
    elif categorie == 'Mode & Chaussures':
        tranches = {
            "0-49":1,
            "50-99":2,
            "100-199":3,
            "200+":4,
        }
        
    elif categorie == "Sport":
        tranches = {
        "0-49":1,
        "50-140":2,
        "150-299":3,
        "300+":4
        }

    elif categorie == "Bébé & Enfants":
        tranches = {
            "0-99":1,
            "100-199":2,
            "200-499":3,
            "500+":4
        }
        
    elif categorie == "Beauté & Santé":
        tranches = {
            "0-99":1,
            "100-199":2,
            "200-499":3,
            "500+":4
        }
        
    elif categorie == "DIY & Jardin":
        tranches = {
            "0-499":1,
            "500-999": 2,
            "1000-1499": 3,
            "1500+": 4
        }
        
    else:
        tranches = {}
    return tranches.get(tranche_selectionnee, 0)  # Utilisez 0 comme valeur par défaut si la tranche n'est pas trouvée

# Utilisez la fonction de conversion pour obtenir le panier moyen
panier_moyen = convertir_panier_moyen(option, option_2)


# Sélection du type de marketplace
option_3 = st.selectbox("Sélectionnez le type de marketplace que vous voulez", 
                        ["Marketplaces Généralistes", "Marketplaces Spécialisées", "Un mixte des deux"])

# Conversion de l'option sélectionnée pour le type de marketplace
if option_3 == "Marketplaces Généralistes":
    type_marketplaces = (1, 2)
elif option_3 == "Marketplaces Spécialisées":
    type_marketplaces = (3, 4)
elif option_3 == "Un mixte des deux":
    type_marketplaces = (1, 2, 3, 4)
else:
    type_marketplaces = (0,)  # Utiliser un tuple même pour une seule valeur pour isin

# Conversion de la tranche de panier moyen en segment
segment = convertir_panier_moyen(option, option_2)

# Appel de filtrer_marketplaces avec les paramètres ajustés
if st.button('Filtrer les marketplaces'):
    resultat = filtrer_marketplaces(option, segment, type_marketplaces, data)
        # Vérifier si le résultat est vide
    if len(resultat) == 0:
        # Afficher un message indiquant qu'aucun résultat n'a été trouvé
        st.write("Aucune marketplace ne correspond à vos critères de sélection.")
    else:
        # Afficher les résultats si le DataFrame n'est pas vide
        st.write('Marketplaces filtrées selon vos critères :')
        st.write(resultat.to_html(index=False), unsafe_allow_html=True)

