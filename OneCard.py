class Onecard: 
    def __init__(self, name:str, amt:float):
        self.name = name
        self.amt = amt

    def deposit(self, amt:float):
        self.amt += amt

    def canAfford(self, amt:float):
        return self.amt >= amt
    
    def spend(self, amt:float):
        if (self.canAfford(amt)):
            self.amt -= amt
        else:
            print("You don't have enough money in your card!")

def main():
    myCard: Onecard = Onecard("Yunxian", 1.0)
    print(myCard)
    print("This card belongs to", myCard.name)
    print(myCard.name, "has $", myCard.amt)
    print(myCard.canAfford(10))
    myCard.deposit(1.0)
    print(myCard.name, "has $", myCard.amt)

if __name__ == "__main__":
    main()