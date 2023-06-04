import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities = ['chicago','new york city','washington']
        city = input("\n Would you like to view data for Chicago, New York City, or Washington? \n").lower()
        if city in cities:
            break
        else:
            print("\n Please enter a valid city name")


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ['January','February','March','April','June','May','None']
        month = input("\n Which month? January, February, March, April, May, or June? Type 'None' for no month filter.\n").title()
        if month in months:
            break
        else:
            print("\n Please enter a valid month")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','None']
        day = input("\n Which day? Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday? Type 'None' for no day filter.\n").title()
        if day in days:
            break
        else:
            print("\n Please enter a valid day.")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time  to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month
    if month != 'None':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+ 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'None':
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        day = days.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f"\n The most popular month is: {popular_month}")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"\n The most popular day is: {popular_day}\n(Where Sun:1,Mon:2,Tue:3 etc.)")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"\n The most popular start hour is: {popular_hour}")

    #Prints time taken to run inputs
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print("\n The most popular start station is: {}".format(com_start_station))

    # TO DO: display most commonly used end station
    com_end_station = df['End Station'].mode()[0]
    print("\n The most popular end station is: {}".format(com_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    com_stations= df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"\n The most frequent start and end station trip combination is: {com_stations}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration=df['Trip Duration'].sum()
    # Minute duration in seconds
    minute, second = divmod(total_duration, 60)
    # Hour duration in minutes
    hour, minute = divmod(minute, 60)

    print(f"\n Total trip duration is: {hour} hour(s), {minute} minute(s) and {second} second(s).")

    # TO DO: display mean travel time
    mean_duration=round(df['Trip Duration'].mean())
    # Minute duration in seconds
    mean_minute, mean_second = divmod(mean_duration, 60)
    # Hour duration in minutes
    mean_hour, mean_minute = divmod(mean_minute, 60)
    print(f"\n The average trip duration is {mean_hour} hour(s), {mean_minute} minute(s) and {mean_second} second(s).")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print("Gender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_byr = int(df['Birth Year'].min())
        print("\n The earliest birth year is:",earliest_byr)
        recent_byr = int(df['Birth Year'].max())
        print("\n The most recent birth is:",recent_byr)
        common_byr = int(df['Birth Year'].mode()[0])
        print("\n The most common birth year is:",common_byr)
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data in increments of 5 rows"""

    i = 0
    raw = input("\n Would you like to view 5 rows of raw data? Type 'yes' or 'no' \n").lower()
    pd.set_option('display.max_columns',200)

    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i:i+5])

            raw = input("\n Would you like to view more data? Type 'yes' or 'no'\n").lower()
            i += 5
        else:
            raw = input("\n Your input is invalid. Please enter only 'yes' or 'no'\n")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
