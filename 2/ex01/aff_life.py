from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads life expectancy data, filters Lebanon's data, and plots a line graph.
    """
    dataset = load("life_expectancy_years.csv")
    beirut_data = dataset[dataset['country'] == 'Lebanon']
    years = beirut_data.columns[1:].to_numpy(dtype=int)
    life_expectancy = beirut_data.values[0][1:]

    plt.plot(years, life_expectancy, label='Lebanon')
    plt.title('Life Expectancy in Lebanon Over the Years')
    plt.xlabel('Year')
    plt.xticks(years[::40], rotation=45)
    plt.ylabel('Life Expectancy')
    plt.yticks(range(30, 101, 10))
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
