#  Luke Gilin
#  ID: 1216992
#  CIS 2348

import csv
import datetime
from datetime import date

if __name__ == '__main__':

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

    file_name = input('Enter input file name:\n')

    items = []
    data = []

    #  Gets initial data from file and passes it to an item object that is appended to a list
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file)
        for rows in csv_reader:
            data = rows[0:len(rows)]
            id = data[0]
            manufacturer = data[1]
            type = data[2]
            price = data[3]
            day = data[4]
            damage = data[5]
            items.append(Item(id, manufacturer, type, price, day, damage))

    #  Create List to store unsorted items in
    unsorted_list = []
    for i in items:
        data_list = i.list()
        unsorted_list.append(data_list)
    #  calls function to sort by manufacturer and assigns it to a new list
    sorted_list = sort_by_manufacturer(unsorted_list)

    #  writes sorted items to file
    with open('FullInventory.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i in sorted_list:
            data_list = i
            csv_writer.writerow(data_list)

    #  calls function to sort by price and assigns it to a new list
    sorted_list = sort_by_price(unsorted_list)

    with open('DamagedInventory.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for i in sorted_list:
            data_list = i
            #  Writes item to file if it's damage field = 'damaged'
            if data_list[5] == 'damaged':
                csv_writer.writerow(data_list)

    #  calls function to sort by type and assigns it to a new list
    sorted_list = sort_by_type(unsorted_list)

    for i in sorted_list:
        data_list = i
        x = 0
        with open(i[2] + 'Inventory.csv', 'w') as csv_file:

            csv_writer = csv.writer(csv_file)
            while x < i.count(i[2]):
                csv_writer.writerow(data_list)
                x += 1

    sorted_list = sort_by_date(unsorted_list)
    current_date = date.today()
    current_date = current_date.strftime("%d/%m/%Y")
    print(current_date)