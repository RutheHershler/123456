import io
import logging

logging.basicConfig(filename='card_log.log', level=logging.INFO)
logger = logging.getLogger("i enter card")

class card:

    COINS_VALUES={
        "quarters": 0.25,
        "dimes": 0.10,
        "half": 0.5,
        "shekels": 1.0
    }

    def __init__(self):
        """עודף"""
        self.surplus_get = 0
        """כסף שהתקבל"""
        self.money_received = 0
        self.cost=20

    def coins(self):
        """פונקצייה שמחשבת האם התקבל מספיק כסף"""
        self.money_received=self.COINS_VALUES["quarters"]*int(input("enter coins  quarters"))
        self.money_received+=self.COINS_VALUES["dimes"]*int(input("enter coins  dimes"))
        self.money_received+=self.COINS_VALUES["half"]*int(input("enter coins  half"))
        self.money_received+=self.COINS_VALUES["shekels"]*int(input("enter coins  shekels"))
        print(self.money_received)
        logger.info(self.money_received)
        print("cost card" ,self.cost)
        logger.info("cost card" ,self.cost)
        self.check(self.money_received)
        # return  self.money_received

    def check(self,price):
        if self.cost==price:
            return self.money_received
            # return True
        elif self.cost<price:
            self.surplus(price)
        else:
            print("you have less ",self.cost-price)
            # return False

    def surplus(self,price):
        """מחזירה את הסכום לעודף"""
        self.surplus_get=price-self.cost
        print(self.surplus_get)
        # if self.coins()==True and self.money_received>price:
        return self.surplus_get

    def print_card(self,name,time,date):
        newcard=open(f"C:/תכנות/שנה ב/PytonFinalPriject/cards/cardof{name}.txt" ,"w")
        newcard.write(f"האיחור של: שם{name} שעה:\n {time} תאריך :\n {date}  \n מחיר :{self.cost}\n סכום שהתקבל:{self.money_received}\n עודף ללקוח:{self.surplus_get} ")

