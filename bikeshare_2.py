import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city are you interested in? Chicago, New York City, or Washington?: ").lower().replace(" ",
                                                                                                                  "_")
        if city == "chicago" or city == "new_york_city" or city == "washington":
            break
        else:
            print("Please type in the correct city.")

    # get user input for month (all, january, february, ... , june)
    months = [
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'november',
        'december'
    ]
    while True:
        month = input("Which month are you interested in?: ").lower()
        if month in months or month == "all":
            break
        else:
            print("Please spell out the correct month (ex: January) or type all for the whole year.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_of_week = [
        'sunday',
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday'
    ]
    while True:
        day = input("Please type in the day of the week you are interested in or type all: ").lower()
        if day in day_of_week or day == 'all':
            break
        else:
            print("Please enter the correct day or type all.")

    print('-' * 40)
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

    df = pd.read_csv(city + '.csv')

    # The following with covert the Start Time and End Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], errors='coerce')
    df['End Time'] = pd.to_datetime(df['End Time'], errors='coerce')

    # I need to create columns for Month, Day and Start Hour
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour

    # I need to filter the data for month and for day
    month_filtered = (df['Month'] == month.capitalize())
    day_filtered = (df['Day'] == day.capitalize())

    # I need to apply the filters to the dataframes
    if month != 'all' and day != 'all':
        return df[month_filtered & day_filtered]
    else:
        return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month:", df['Month'].mode()[0])
    # display the most common day of week
    print("The most common day of the week:", df['Day'].mode()[0])
    # display the most common start hour
    print("The most common start hour is:", df['Start Hour'].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# def station_stats(df):
#     """Displays statistics on the most popular stations and trip."""
#
#     print('\nCalculating The Most Popular Stations and Trip...\n')
#     start_time = time.time()
#
#     # display most commonly used start station
#
#     # display most commonly used end station
#
#     # display most frequent combination of start station and end station trip
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-' * 40)
#
#
# def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""
#
#     print('\nCalculating Trip Duration...\n')
#     start_time = time.time()
#
#     # display total travel time
#
#     # display mean travel time
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-' * 40)
#
#
# def user_stats(df):
#     """Displays statistics on bikeshare users."""
#
#     print('\nCalculating User Stats...\n')
#     start_time = time.time()
#
#     # Display counts of user types
#
#     # Display counts of gender
#
#     # Display earliest, most recent, and most common year of birth
#
#     print("\nThis took %s seconds." % (time.time() - start_time))
#     print('-' * 40)
#
#
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
