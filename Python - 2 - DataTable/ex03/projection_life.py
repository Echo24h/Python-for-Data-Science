import matplotlib.pyplot as plt
from load_csv import load


def draw_compare_life_expectancy_gdp(year: int = 1900):
    """
    Draws a scatter plot comparing life expectancy and GDP
    for a given year.

    Args:
        year (int): The year for which to compare the data.

    Returns:
        None
    """
    year = str(year)
    dataset1 = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    dataset2 = load("life_expectancy_years.csv")

    if dataset1 is not None and dataset2 is not None:

        data1 = dataset1[year]
        data2 = dataset2[year]
        plt.scatter(data1, data2)
        plt.xscale('log')
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.title(year)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.show()


if __name__ == "__main__":
    draw_compare_life_expectancy_gdp(1900)
