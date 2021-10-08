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
        return self.items.pop(0)

    def show_queue(self):
        # print(self.items)
        return self.items


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):

        scoops = int(scoops)
        self.flavors = flavor
        self.scoops = scoops
        self.customer = customer
        if scoops < 1 and scoops > 3:
            print("please choose the right scoops")
            return
        if flavor not in self.flavors:
            print("Sorry we don't have this", flavor)
            return
        else:
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.show_queue(order)
            print("Order created!")

        self.orders.enqueue((customer, flavor, scoops))
        print(f"Order created for customer!!")

    def show_all_orders(self):
        for order in self.orders.dequeue():
            print("All Pending Ice Cream Orders: \n Customer:", order.self.customer,
                  "--", "Flavor:", order.self.flavor, "--", "Scoops:", order.self.scoops)
   # def next_order(self):


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
