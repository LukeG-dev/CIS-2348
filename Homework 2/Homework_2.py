#  Luke Gilin 1216992
#  Homework 2
import datetime
from datetime import date

#  get Current date
current_date = date.today()
#  define day for while loop
day = ''
#  define dates list
dates = []
#  Lookup Dictionary for valid months
months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
          'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
#  Get filename from user
filename = input()

#  Open file
with open(filename, 'r') as openfile:
    # main loop, gets input, checks if they are valid and adds to date list
    while day != '-1':
        day = str(openfile.readline())
        #  replaces comma with nothing in input string
        day = day.replace(',', '')
        #  phrases input string into temporary list
        this_day = day.split()
        #  Checks if the input month is valid then assigns it a numeric value from the dictionary
        if this_day[0] in months:
            month_num = months[this_day[0]]
            #  creates date object from input string for comparison with current_date
            formatted_date = datetime.date(int(this_day[2]), month_num, int(this_day[1]))
            #  reformat input string to have correct formatting for the united states
            us_formatted_date = '{month}/{day}/{year}'.format(month=month_num, day=this_day[1], year=this_day[2])
            #  compares date object with current_date and if the date object is larger
            #  adds the United States formatted date to list
            if formatted_date > current_date:
                dates.append(us_formatted_date)
#  Prints valid date List to file as long as it has more than one value
if len(dates) > 0:
    with open('parsedDates.txt', 'w') as output_file:
        for i in range(len(dates)):
            output_file.write(dates[i])
            output_file.write('\n')



