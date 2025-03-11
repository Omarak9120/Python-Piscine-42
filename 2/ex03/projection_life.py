from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads and visualizes the correlation between Gross National Product (GNP)
    and life expectancy in the year 1900 using a scatter plot.
    """
    certified_42 = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_data = load(certified_42)
    life_expectancy_data = load("life_expectancy_years.csv")
    year_1900_column = '1900'
    gnp_1900 = income_data[year_1900_column]
    life_expectancy_1900 = life_expectancy_data[year_1900_column]

    plt.figure(figsize=(10, 6))
    plt.scatter(gnp_1900, life_expectancy_1900)
    plt.title("Year 1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
