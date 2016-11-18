class Customer:
    __name = ""
    __age = ""
    __favorite_goods = None

    def __init__(self, name, age, goods):
        self.__name = name
        self.__age = age
        self.__favorite_goods = goods

    def check_age_restriction_of_good(self, good):
        if self.__favorite_goods[good] > self.__age:
            print(self.__name + " is too young to buy or do " + good + "!")
        else:
            print(self.__name + " can buy or do " + good + ".")


#fav_goods is a dictionary(sometimes called a map)
fav_goods = {"Tobacco" : 21, "Driving a Car" : 16, "Alcohol" : 21}
alice = Customer("Alice", 17, fav_goods)
alice.check_age_restriction_of_good("Tobacco")
