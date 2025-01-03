import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input("Please enter the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Oh no! Invalid input. Try again please!")


    while True:
        month = input("Please enter the month (all, january, february, march, april, may, june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Oh no! Invalid input. Try again please!")

    while True:
        day = input('Please enter the day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Oh no! Invalid input. Try again please!')

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_index = months.index(month) + 1
        df = df[df['month'] == month_index]

    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['month'].mode()[0]
    print(f"The most common month is: {common_month}")

    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of the week is: {common_day}")

    common_month = df['month'].mode()[0]
    print(f"The most common month is: {common_month}")

    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of the week is: {common_day}")

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"The most common start hour is: {common_hour}:00")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    commonly_used_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {commonly_used_start_station}")

    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")

    commonly_used_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {commonly_used_start_station}")

    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")


    common_start_to_end_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"The most frequent trip is from: {common_start_to_end_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    counts_user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", counts_user_types)

    counts_user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", counts_user_types)


    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of Gender:\n", gender_counts)
    else:
        print("It looks like gender data is not available for this city.")

    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print(f"Earliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {recent_year}")
        print(f"Most common year of birth: {common_year}")
    else:
        print("Sorry! Looks like birth year data is not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon user request."""
    start_loc = 0
    while True:
        show_data = input("Would you like to see 5 lines of raw data? Enter yes or no: ").lower()
        if show_data == 'yes':
            print(df.iloc[start_loc:start_loc + 5])
            start_loc += 5
            if start_loc >= df.shape[0]:
                print("No more raw data to display.")
                break
        elif show_data == 'no':
            break
        else:
            print("Oh no! Invalid input. Try again please!")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)


        restart = input('\nLovely!!Would you like to restart? Please enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
