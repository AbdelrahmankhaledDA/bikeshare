from re import X
import time
from turtle import circle
from matplotlib.pyplot import bar_label
import pandas as pd
import numpy as np

CITY_DATA = { "chicago": "chicago.csv",
              "new york city": "new_york_city.csv",
              "washington":"washington.csv",
              "nyc": "new_york_city.csv"}
months =["January", "February", "March", "April", "May", "June" ] 
days = ["Sturday" , "Sunday", "Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]             

def get_filters():
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city =input("Choose a city! chicago, new york city or washington ").lower()
        if city  in CITY_DATA.keys():
            break
        else:
            print("Plz Enter a valid input")
            
    while True :   
        month = input("Choose a month! january ..... june or all  ").title()
        
        if month in months or month =="All" :
            break
        else:
            print("Plz Enter a valid input")
            
    while True:    
        day = input("Choose a day!saturday ....... friday or all ").title()
        if day in days or day =="All":
            break
        else:
            print("Plz Enter a valid input")
           
    print('-'*40)
    return city, month , day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df.fillna(0)
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    

   
    if month != "All":
        month = months.index(month)+1
        df = df[df["month"] == month]

    
    if day != "All":
        df = df[df["day_of_week"] == day]
    return df




def time_stats(df):
   

    print("\nCalculating The Most Frequent Times of Travel...\n")
    start_time = time.time()

    # display the most common month
    mostmonth = df["month"].mode()
    print("The most common month is : {}".format(mostmonth))
    

    # display the most common day of week
    mostday = df["day_of_week"].mode()
    print("The most common day is : {}".format(mostday))

    # display the most common start hour
    moststart = df["Start Time"].mode()
    print("The most common start time is : {}".format(moststart))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    moststartstation = df["Start Station"].mode()
    print("The most common start station is : {}".format(moststartstation))

    # display most commonly used end station
    mostEndstation = df["End Station"].mode()
    print("The most common end station is : {}".format(mostEndstation))

    # display most frequent combination of start station and end station trip
    combstation = (df["Start Station" ]+ df["End Station"]).mode()
    print("The most common combination of start station is : {}".format(combstation))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totaltraveltime =df["Trip Duration"].sum()
    print("The total travel time is : {}".format(totaltraveltime))

    # display mean travel time
    averagetraveltime =df["Trip Duration"].mean()
    print("The average travel time is : {}".format(averagetraveltime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_type(df):
    print('\nCalculating User Stats...\n')
    countsofusertypes = df["User Type"].value_counts()
    print("The counts of user types is : {}".format(countsofusertypes))

def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    
    start_time = time.time()

    # Display counts of user types
    countsofusertypes = df["User Type"].value_counts()
    print("The counts of user types is : {}".format(countsofusertypes))
    # Display counts of gender
    countsofGender = df["Gender"].value_counts()
    print("The counts ofGender is : {}".format(countsofGender))
    # Display earliest, most recent, and most common year of birth
    earliest = df["Birth Year"].max()
    mostrecent = df["Birth Year"].min()
    mostcommon = df["Birth Year"].mode()
    print("The earliest is : {},The most recent is : {}, and most common is : {} year of birth".format(earliest , mostrecent , mostcommon ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw (df):
    i = 0
    x = "yes"
    while x == "yes":
       
       x = input("would U like to see some of the data?? ...... Type yes or no    ").lower 
       y= df.head(i+5)
       print(y)
       if x == "no" :
             break     
       x = input("Would Ulike to see some more??...... Type yes or no     ")
       i =+5

def main():
    while True:
        
        city, month , day = get_filters()
        df = load_data(city, month, day)
            

        if city == "washington" :
          time_stats(df)
          station_stats(df)
          trip_duration_stats(df)
          user_type(df)
          print( "There is no Gender or Birth year in this data set")
          raw(df)
        else :  
           time_stats(df)
           station_stats(df)
           trip_duration_stats(df)
           user_type(df)
           user_stats(df)
           raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
