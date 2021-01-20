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
    while True :
        city=str(input('please choose city/s you want to analyze (chicago-new york city-washington)\nEnter the name of the city you want:').lower())
        if city not in CITY_DATA.keys() and city!='all':
            print('\nThe City not included in the data')
            continue
        break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=str(input('\n(Note:months are from january to june)\nplease Enter the name of the month to filter by, or "all" : ').lower())
        if month not in months and month!='all':
            print('\nThe month not included in the data')
            continue
        break  
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday' ,'Saturday']
        day=str(input('\nplease Enter the name of the day of week to filter by, or "all" : ')).title()
        if day not in days and day != 'All':
            print('\nThe name of the day not correct ')
            continue
        break   
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
    df = pd.DataFrame()
    if city == 'all':
        for cit in CITY_DATA :
            file = pd.read_csv(CITY_DATA[cit])
            df = df.append(file)
    else :
        df = pd.read_csv(CITY_DATA[city])
        
    # convert the Start Time column to datetime        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]
        
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
 

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month != 'all':
        print('you already choosed one month to analyze it\'s : ',month)
    else :
        most_common_month =df['month'].mode()
        print('the most common month is : ',most_common_month)

    # TO DO: display the most common day of week
    if day != 'All':
        print('you already choosed one day to analyze it\'s : ',day)
    else :
        most_common_day = df['day_of_week'].mode()
        print("the most common day is : %s " % (most_common_day))

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()
    print('the most common start hour is : ',most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()
    print('most commonly used start station is : ',most_commonly_used_start_station)

    # TO DO: display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()
    print('most commonly used end station is : ',most_commonly_used_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df['Start Station'and'End Station'].mode()
    print('most frequent combination of start station and end station trip is : ',most_frequent_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print('total travel time is ',total_travel_time,' minutes')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('mean travel time is ',mean_travel_time,' minutes') 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print('counts of user types is \n',counts_of_user_types)

    # TO DO: Display counts of gender
    try :
        counts_of_gender = df['Gender'].value_counts()
        print('counts of gender is \n',counts_of_gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        common = df['Birth Year'].mode()
        print('earliest is {}, most recent is {}, and most common year of birth {}'.format(earliest,recent,common))   
    except KeyError :
        print("\nthe genser and birth data not available for this city ")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def get_data(df):
    while True:
        get_data = input('\nWould you like to display the frist 5 rows of data ? Enter yes or no.\n').lower()
        if get_data == 'yes':
            print(df.head())
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        get_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
