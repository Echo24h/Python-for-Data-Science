import matplotlib.pyplot as plt
from load_csv import load
import matplotlib


matplotlib.use('TkAgg')

def draw_country_life(country: str):
    # Charger le fichier CSV
    dataset = load("life_expectancy_years.csv")

    if dataset is not None:
        # Filtrer les données pour obtenir les informations sur le pays de votre campus
        country_data = dataset[dataset['country'] == country]

        # Extraire les années et l'espérance de vie pour le pays donné
        years = list(country_data.columns[1:])
        life_expectancy = country_data.values.tolist()[0][1:]

        # Créer le graphique
        plt.plot(years, life_expectancy, marker='o', linestyle='-')
        plt.title(f"Life Expectancy in {country}")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy (Years)")
        plt.grid(True)
        plt.show(block=True)  # Modifier ici pour afficher de manière bloquante

# Appeler la fonction pour dessiner le graphique pour le pays de votre campus
draw_country_life("France")  # Remplacez "France" par le pays de votre campus
