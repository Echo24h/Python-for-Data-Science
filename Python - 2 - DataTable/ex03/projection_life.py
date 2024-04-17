import matplotlib.pyplot as plt
from load_csv import load


def preprocess_population(pop_str):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string with or without
        the 'M' suffix for million.

    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)
    

def draw_compare_countries(country1: str, country2: str):
    """
    Draw a line plot of the population of two countries over the years.
    
    Args:
        country1 (str): The name of the first country.
        country2 (str): The name of the second country.
        
    Returns:
        None
    """

    dataset = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    
    if dataset is not None:
        
        country1_data = dataset[dataset['country'] == country1]
        country2_data = dataset[dataset['country'] == country2]
        
        years = [str(year) for year in range(1800, 2051)]
        country1_pop = country1_data[years].values.flatten()
        country2_pop = country2_data[years].values.flatten()
        
        country1_pop = [preprocess_population(pop) for pop in country1_pop]
        country2_pop = [preprocess_population(pop) for pop in country2_pop]
        
        plt.plot(years, country1_pop)
        plt.plot(years, country2_pop)
        plt.xticks(years[::40])
        plt.title("Population Projections")
        plt.legend([country1, country2], loc='lower right')
        max_pop = max(max(country1_pop), max(country2_pop))
        y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
        plt.xlabel("Year")
        plt.ylabel("Population")
        
        plt.show()


if __name__ == "__main__":
    draw_compare_countries("India", "China")