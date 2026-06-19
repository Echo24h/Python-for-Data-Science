from os import error

import matplotlib.pyplot as plt
from load_csv import load


def draw_country_life(country: str):
    """
    Draw a line plot of the life expectancy of a country over the years.

    Args:
        country (str): The name of the country.

    Returns:
        None
    """

    dataset = load("life_expectancy_years.csv")

    if dataset is not None:

        country_data = dataset[dataset['country'] == country]
        years = list(country_data.columns[1:])
        life_expectancy = country_data.values.tolist()[0][1:]

        plt.plot(years, life_expectancy)
        plt.xticks(years[::40])
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        try:
            plt.show()
        except KeyboardInterrupt:
            print("Plotting interrupted by user.")
            exit(0)


if __name__ == "__main__":
    draw_country_life("Switzerland")
