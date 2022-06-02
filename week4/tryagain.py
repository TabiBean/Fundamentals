class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        # removes the first item on the list at index 0
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops
        if (flavor in self.flavors) and (scoops in range(1, 4)):
            print("Order created!")
            order = {"customer": self.customer,
                     "flavor": self.flavor, "scoops": self.scoops}
            self.orders.enqueue(order)
        elif flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
        elif scoops not in range(1, 4):
            print("Choose between 1-3 scoops")

    def show_all_orders(self):
        Queue()
        print("All Pending Ice Cream Order Orders:")
        for dict in self.orders:
            print("Customer:", dict['customer'], "-- Flavor:",
                  dict['flavor'], "--Scoops:", dict['scoops'])

    def next_order(self):
        print("Next Order Up!")
        self.orders.dequeue()

        print("All Pending Ice Cream Orders:")
        self.orders.show_queue()


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()