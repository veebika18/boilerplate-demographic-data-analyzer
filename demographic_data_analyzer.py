import pandas as pd
def calculate_demographic_data(print_data=True):
    df = pd.read_csv('adult.data.csv')
    # 1. Number of each race
    race_count = df['race'].value_counts()
    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    # 3. Percentage with Bachelors
    percentage_bachelors = round((df['education'].value_counts().get('Bachelors', 0) / len(df)) * 100, 1)
    # 4. Percentage with advanced education making >50K
    advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_advanced_edu_rich = round((len(df[advanced_edu & (df['salary'] == '>50K')]) / len(df[advanced_edu])) * 100, 1)
    # 5. Percentage without advanced education making >50K
    no_advanced_edu = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    percentage_no_advanced_edu_rich = round((len(df[no_advanced_edu & (df['salary'] == '>50K')]) / len(df[no_advanced_edu])) * 100, 1)
    # 6. Minimum hours worked per week
    min_work_hours = df['hours-per-week'].min()
    # 7. Percentage of rich among those who work minimum hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((len(min_workers[min_workers['salary'] == '>50K']) / len(min_workers)) * 100, 1)
    # 8. Country with highest percentage of people earning >50K
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_totals = df['native-country'].value_counts()
    highest_earning_country = (country_earnings / country_totals * 100).idxmax()
    highest_earning_country_percentage = round((country_earnings / country_totals * 100).max(), 1)
    # 9. Most popular occupation for those earning >50K in India
    india_occupations = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    top_india_occupation = india_occupations.value_counts().idxmax()
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {percentage_advanced_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {percentage_no_advanced_edu_rich}%")
        print(f"Minimum work hours: {min_work_hours}")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print(f"Country with highest percentage of rich: {highest_earning_country}")
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print(f"Top occupations in India: {top_india_occupation}")

    return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': percentage_advanced_edu_rich,
    'lower_education_rich': percentage_no_advanced_edu_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_india_occupation
}

