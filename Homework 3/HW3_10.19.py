# Luke Gilin 1216992

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0, item_description='none'):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.item_description = item_description
        self.price = self.item_price * self.item_quantity
    def print_item_cost(self):

        print('{item} {quan} @ ${value:.0f} = ${price:.0f}'.format(item=self.item_name, quan=self.item_quantity,
                                                        value=self.item_price, price=self.price))

    def print_item_description(self, ItemToPurchase):
        print(self.item_description)

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        if item_name in self.cart_items:
            del self.cart_items[item_name]
        else:
            print('Item not found in cart. Nothing removed.')

    def modify_item(self, ItemToPurchase):
        if ItemToPurchase in self.cart_items:
            print("???")
        else:
            print('Item not found in cart. nothing modified.')
    def get_num_items_in_cart(self):
        return len(self.cart_items)
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total = total + item.price
        return total
    def print_total(self):
        print('')


    def print_menu(self, ShoppingCart):
        selection = ''
        while selection != 'q':
            if selection == 'q':
                exit()
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print("i - Output items' descriptions")
            print('o - Output shopping cart')
            print('q - Quit\n')
            selection = input('Choose an option:')

if __name__ == '__main__':
    c_name = input("Enter customer's name")
    c_date = input("Enter today's date:\n")



    print('Item 2')
    itemTwoName = input('Enter the item name:\n')
    itemTwoPrice = float(input('Enter the item price:\n'))
    itemTwoQuan = int(input('Enter the item quantity:\n\n'))

    itemTwo = ItemToPurchase(itemTwoName, itemTwoPrice, itemTwoQuan)

