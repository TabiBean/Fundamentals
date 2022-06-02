class Queue:
    def __init__(self): #creates box object
        self.item = []

    def size(self):#item length
        return len(self.item)

    def enqueue(self, item): #push to the queue-rear
        self.item.append(item)

    def dequeue(self): #remove from the queue-front
        if self.size == 0:#are items in the object
            return None
        return self.item.pop(0)#take out first item

    def show_queue(self):
        print(self.item)#prints list of objects

#First In First Out
class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops): #dequeue-remove-front
        
        if flavor in self.flavors and (scoops <= 3 and scoops >= 1):
            item = {"Customer": customer, "Flavor": flavor, "Scoops": scoops}
            print("Order created!")
            return self.orders.enqueue(item)

        if flavor in self.flavors:
            return flavor
        else:
            print("Sorry, we don't have that flavor.")

        if 1<= scoops <= 3:
            print("Choose between 1-3 scoops")
        else:
            return scoops 

    def show_all_orders(self): #show_queue
        print("All Pending Ice Cream Order Orders:")
        for x in self.orders.item:
            print("Customer:", x["Customer"], "---", "Order:", x["Flavor"], "---", "Scoops:", x["Scoops"])

    def next_order(self): #enqueue
        print("Next Order Up!")
        self.orders.dequeue()

        print("All Pending Ice Cream Orders:")
        self.orders.show_queue()
 
            

 # Test Cases
shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()

    


