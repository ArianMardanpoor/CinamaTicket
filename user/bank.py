#! usr/bin/python3
from random import randint 
from user import User


class Bank(User):
    user_data = [] 
    def __init__(self, balance: int = 10_000, card_pass: int = 1234, cvv2: int = None):
        super().__init__()
        cv2 =randint(1000, 10000)
        self.cvv2 = cv2
        self._balance = balance
        self._card_pass = card_pass
    @property
    def balance1(self):
        """The balance property."""
        return self._balance

    @balance1.setter
    def balance1(self, value):
        pass
    
    def add(self, amount: int):
        if amount>0:
            self._balance += amount
        else:
            print("Something Went Wrong!....")
    
    def sub(self, amount: int):
        if amount > 0 and (self._balance - amount >= 10000):
            self._balance -= amount
        else:
            print("Something Went Wrong!....")    
    
    def transfer(self,other: "Bank", amount: int):
        self.sub(amount + 600)
        other.add(amount)   
        
    @property
    def card_pass1(self):
        """getter for card password but it's just created to complete getter and setter for password and it not gonna use!"""
        return self._card_pass
    
    @card_pass1.setter
    def card_pass1(self, value):
        """setter for card password"""
        self._card_pass = value
    
    def cvv2(self):
        return self.cvv2
    
    @classmethod
    def max(cls):
        return max(account_balance for account in cls.__accounts)


class Wallet(Bank):
    

    def __init__(self, wallet_balance : int = 0, item : list = [], subscription : int = 0,number_purchases : int = 0):
        super().__init__()
        self._wallet_balance = wallet_balance
        self.item = item
        self.subscription = subscription
        self.number_purchases = number_purchases
    @property
    def wallet_balance1(self):
        """The wallet_balance property."""
        return self._wallet_balance

    @wallet_balance1.setter
    def wallet_balance1(self, value):
        self._wallet_balance = value


    def add_w(self, amount: int):
        if amount>0:
            self._wallet_balance += amount
        else:
            print("Something Went Wrong!....")
    
    def sub_w(self, amount: int):
        if value > 0 and (self._wallet_balance - value >= 10000):
            self._wallet_balance -= amount
        else:
            print("Something Went Wrong!....")
    
    def to_dict(self):
        return {
            "username": f"{self._username}",
            "id" :f"{self.id}",
            "phone_number": f"{self.phone_number}",
            "birthday": f"{self.birthday1}",
            "password": f"{self.password1}",
            "balance": f"{self._balance}",
            "cvv2": f"{self.cvv2}",
            "card_pass": f"{self.card_pass1}",
            "wallet_balance" : f"{self._wallet_balance}",
            "time" : f"{self.time}"
        }
    
    def save_data(self):
        Bank.user_data.append(self.to_dict())
     
    def __str__(self) -> str:
        """returning the information of the user"""
        return f"*your username --> {self._username} \n*your phone_number --> {self.phone_number} \n*your id --> {self.id} \n*your birthday --> {self.birthday1} \n*your cvv2 --> {self.cvv2} \n*your registration time --> {self.time}"
    
    def __str1__(self) -> str:
        """returning the information of the bank account"""
        return f"\n*your balance --> {self._balance}\n*your wallet_balance --> {self._wallet_balance}" 

    def Bronze(self, value):
        pass

    def Silver(self, value):
        if (self.number_purchases <= 3):
            self._wallet_balance += (value/5)

    def Gold(self, value):
        one_month_later = self.time + timedelta(days=30)
        if datetime.now() != one_month_later:
            self._wallet_balance += (2 * value/2)
            self.item.append("Energy drink")
        

