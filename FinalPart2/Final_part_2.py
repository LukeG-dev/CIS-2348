#  Luke Gilin
#  ID: 1216992
#  CIS 2348

import csv
import datetime
from datetime import date

if __name__ == '__main__':

    #  Class definition
    class Item:

        def __init__(self, item_id, fact_name, item_type, item_price, service_date, damaged=''):
            #  parameterized constructors
            self.item_id = item_id
            self.fact_name = fact_name
            self.item_type = item_type
            self.damaged = damaged
            self.item_price = item_price
            self.service_date = service_date

        def price_list(self, item_price):
            self.item_price = item_price

        def serviced(self, service_date):

            self.service_date = service_date

        def damaged(self, damaged):

            self.damaged = damaged

        def list(self):
            my_list = [self.item_id, self.fact_name, self.item_type, self.item_price, self.service_date, self.damaged]
            return my_list

    #  Sorts list by manufacturer
    def sort_by_manufacturer(sub_list):
        length = len(sub_list)
        for i in range(0, 1):
            for x in range(0, length - i - 1):
                if sub_list[x][1] > sub_list[x + 1][1]:
                    sort_by = sub_list[x]
                    sub_list[x] = sub_list[x + 1]
                    sub_list[x + 1] = sort_by
        return sub_list

    def sort_by_type(sub_list):
        sub_list.sort(key=lambda x: x[2])
        return sub_list

    def sort_by_price(sub_list):
        sub_list.sort(key=lambda x: x[3])
        return sub_list

    def sort_by_date(sub_list):
        sub_list.sort(key=lambda x: x[4])
        return sub_list

    def closest_price(lst, p):
        return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - p))]


#  Stores list of items
    items = []

#  Stores information needed during I/O operations
    ServiceDates = []
    ManufacturerList = []
    PriceList = []

#  Gets initial data from file and passes it to a separate list for each file
    with open('ManufacturerList.csv') as f1,  open('PriceList.csv') as f2, open('ServiceDatesList.csv') as f3:
        file_one = csv.reader(f1)
        file_two = csv.reader(f2)
        file_three = csv.reader(f3)
        for i in file_one:
            m_data = []
            m_data[0:4] = i[0:4]
            ManufacturerList.append(m_data)
        for i in file_two:
            p_data = []
            p_data[0:2] = i[0:2]
            PriceList.append(p_data)
        for i in file_three:
            s_data = []
            s_data[0:2] = i[0:2]
            ServiceDates.append(s_data)

#  Transfer information form file lists into a single item object
    for j in ManufacturerList:
        item_id = j[0]
        manufacturer = j[1]
        manufacturer = manufacturer.replace(' ', '')
        item_type = j[2]
        damage = j[3]
        for i in PriceList:
            if i[0] == item_id:
                price = int(i[1])
        for k in ServiceDates:
            if k[0] == item_id:
                day = k[1]
        tempItem = Item(item_id, manufacturer, item_type, price, day, damage)
        items.append(tempItem)

    #  Create List to store unsorted items in
    unsorted_list = []
    for i in items:
        data_list = i.list()
        unsorted_list.append(data_list)

    #  calls function to sort by manufacturer and assigns it to a new list
    sorted_list = sort_by_manufacturer(unsorted_list)

    #  Creates a list of item types and manufacturers to search though
    types = []
    manufacturers = []
    for i in unsorted_list:
        data_list = i
        types.append(data_list[2])
        manufacturers.append(data_list[1])

    #  Debug
    #  print(types)
    #  print(manufacturers)

    #  define type and manufacturer query for user input
    type_query = ''
    manufacturer_query = ''
    #  Ask for user input
    item_data = input('Enter one manufacturer and item type, separated by a comma:\n').split(sep=',')
    try:
        manufacturer_query = item_data[0]
        type_query = item_data[1]

    except IndexError:
        print('Invalid item information')

    #  Check if the user's item type and item manufacturer are in the respective list
    #  if returns false prints that the item isn't in inventory

    if type_query not in types and manufacturer_query not in manufacturers:
        print('No such item in inventory')

    #  converts string date to date object
    for i in sorted_list:
        data_list = i
        raw_date = i[4].split(sep='/')
        for x in range(0, len(raw_date)):
            raw_date[x] = int(raw_date[x])
        s_date = datetime.date(raw_date[2], raw_date[0], raw_date[1])
        i[4] = s_date

    #  sorts list by date object
    sorted_list = sort_by_date(sorted_list)
    #  Gets current date
    current_date = datetime.date.today()

    price_to_match = 0
    new_price_list = []

    while item_data[0] != 'q':
        #  define highest dollar value
        highest = 0

        #  Finds the highest dollar value that matches user input
        for i in sorted_list:
            data_list = i
            if type_query == data_list[2] and manufacturer_query == data_list[1] and data_list[5] != 'damaged'\
                    and data_list[4] > current_date and data_list[3] > highest:
                highest = data_list[3]

        #  Uses the highest dollar value and user input to search for item and print it
        #  Also assigns price to match as an optional operator if the user wants to enter another search
        for i in sorted_list:
            data_list = i
            if type_query == data_list[2] and manufacturer_query == data_list[1] and data_list[5] != 'damaged' \
                    and data_list[4] > current_date and data_list[3] == highest:
                price_to_match = int(data_list[3])
                print('Your item is: {ID} {fact} {type} ${price}'.format(ID=data_list[0], fact=data_list[1],
                                                                         type=data_list[2], price=data_list[3]))

        # Finds price closest to the previous item's price in the same type category from a separate manufacturer if
        # available
        for i in sorted_list:
            data_list = i
            if type_query == data_list[2] and manufacturer_query != data_list[1] and data_list[5] != 'damaged' \
                    and data_list[4] > current_date:
                new_price_list.append(int(i[3]))
        if len(item_data) > 1:
            next_price = closest_price(new_price_list, price_to_match)

        #  gives additional options from other manufacturers for the same item type
        for i in sorted_list:
            data_list = i
            if type_query == data_list[2] and manufacturer_query != data_list[1] and data_list[5] != 'damaged' \
                    and data_list[4] > current_date and data_list[3] == next_price:
                print('You may, also, consider: {ID} {fact} {type} ${price}'.format(ID=data_list[0], fact=data_list[1],
                                                                                    type=data_list[2],
                                                                                    price=data_list[3]))
        #  Request further user input
        item_data = input('Enter one manufacturer and item type, separated by a comma, type q to quit\n').split(sep=',')

        manufacturer_query = item_data[0]
        if len(item_data) > 1:
            type_query = item_data[1]

