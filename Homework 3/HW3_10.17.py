# Luke Gilin 1216992

class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0):
        self.item_name = str(item_name)
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)
        self.price = self.item_price * self.item_quantity
    def print_item_cost(self):

        print('{item} {quan} @ ${value:.0f} = ${price:.0f}'.format(item=self.item_name, quan=self.item_quantity,
                                                           value=self.item_price, price=self.price))


if __name__ == '__main__':
    print('Item 1')
    itemOneName = input('Enter the item name:\n')
    itemOnePrice = float(input('Enter the item price:\n'))
    itemOneQuan = int(input('Enter the item quantity:\n\n'))

    itemOne = ItemToPurchase(itemOneName, itemOnePrice, itemOneQuan)

    print('Item 2')
    itemTwoName = input('Enter the item name:\n')
    itemTwoPrice = float(input('Enter the item price:\n'))
    itemTwoQuan = int(input('Enter the item quantity:\n\n'))

    itemTwo = ItemToPurchase(itemTwoName, itemTwoPrice, itemTwoQuan)

    print('TOTAL COST')
    itemOne.print_item_cost()
    itemTwo.print_item_cost()

    total = itemOne.price + itemTwo.price
    print()
    print('Total: ${total:.0f}'.format(total=total))
