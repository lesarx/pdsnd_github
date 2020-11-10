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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = validate_input('In which city are you - Chicago, New York City or Washington? ', 1)

    # TO DO: get user input for month (all, january, february, ... , june)
    month = validate_input('What month? ', 2)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = validate_input('What day of the week? ', 3)

    print('-'*40)
    return city, month, day

#use a while loop to handle invalid inputs
def validate_input(input_str, input_type):
    while True:
        input_read=input(input_str).lower()
        try:
            if input_read in ['chicago', 'new york city', 'washington'] and input_type == 1:
                break
            elif input_read in ['all','january','february','march','april','may','june'] and input_type == 2:
                break
            elif input_read in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print('Invalid city input')
                if input_type == 2:
                    print('Invalid month input')
                if input_type == 3:
                    print('Invalid day input')
        except ValueError:
            print('Input Error')
    return input_read


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

    #load into DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #convert to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])

    #pull month, dow, & hour from start time column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month']==month]

    #filter by dow
    if day != 'all':
        df = df[df['day_of_week']==day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('Most Common Month: ', common_month)

    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].mode()[0]

    print('Most Common Day of the Week: ', common_dow)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]

    print('Most Commonly Used Start Station: ', common_start)


    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]

    print('Most Commonly Used End Station: ', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    group_field = df.groupby(['Start Station','End Station'])
    common_combo_station = group_field.size().sort_values(ascending=False).head(1)

    print('Most Common Combination Station Trip: ', common_combo_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()

    print('Total Travel Time: ', total_travel)


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()

    print('Mean Travel Time: ', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Counts:/n')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender - EDITED CODE TO REFLECT 'df' VS 'city' FOR VERSION 3 PROJECT SUBMISSION
    if df !='washington':
        print('Gender Statistics: ')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Year Statistics: /n')
        print('Earliest Birth Year: ')
        print(df['Birth Year'].min())

        print('Most Recent Birth Year: ')
        print(df['Birth Year'].max())

        print('Most Common Birth Year: ')
        print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    #FUNCTION TO DISPLAY RAW DATA AS PER V1 FEEDBACK

    start_loc = 0
    end_loc = 5

    display_raw = input("Do you want to see the raw data? ").lower()

    if display_raw == 'yes':
        while end_loc <= df.shape[0] - 1:
            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you wish to continue: ").lower()
            if end_display == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
