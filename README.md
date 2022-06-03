# struct_project
This is a data project investigating percentage of female labour force participation in a country vs. the country's happiness index.

My program reads in two different files that I obtained from: https://www.kaggle.com/datasets/undp/human-development
* gender_inequality.csv
* world_happiness_ranking_2015.csv

The gender_inequality.csv file contains the following information: GII Rank, Country, Gender Inequality Index (GII), Maternal Mortality Ratio, Adolescent Birth Rate, Percent Representation in Parliament, Population with Secondary Education (Female), Population with Secondary Education (Male), Labour Force Participation Rate (Female), Labour Force Participation Rate (Male)
- Some countries are missing data, and the missing values are denoted with ".." within the csv file.
- Not all countries are represented.

The world_happiness_ranking_2015.csv file contains the following information: Country, Region, Happiness Rank, Happiness Score, Standard Error, Economy (GDP per Capita), Family, Health (Life Expectancy), Freedom, Trust (Government Corruption), Generosity, Dystopia Residual
- Some countries are missing data, and the missing values are denoted with "0" within the csv file.
- Not all countries are represented.

My program calculates the percentage of female labour force participation in a country (calculated based on info in the gender_inequality.csv), and compares it to a country's happiness index (found in world_happiness_ranking_2015.csv)
