"""
Things to discuss:
1. Review init and class attribute
   a. Class attribute and modifying the class attribute
   b. Negative balance raising ValueError()
2. __str__
3. withdraw()/deposit()
4. transfer
   a. isinstance()
   b. transfer_to()
5. Class inheritance examples
"""


class Account:
    total_account_no = 0  # class attribute. Counts number of generated instances

    def __init__(self, category: str, balance: float = 0):
        self.category_ = category
        if balance < 0:
            # check balance before assignment, program stops if negative
            raise ValueError("Balance cannot be negative")
        self.balance_ = balance

        Account.total_account_no += 1  # mutate class attribute, note it's assigned to Account class and not self
        self.account_id_ = self.total_account_no  # generate account id number based on the current account counter

    def deposit(self, amount: float):
        print(f"..({self.category_}) Deposit {amount}")
        self.balance_ += amount

    def withdraw(self, amount: float):
        if amount > self.balance_:
            print(f"..({self.category_}) Withdrawal amount is larger than the current balance."
                  f" Not able to complete operation.")
        else:
            print(f"..({self.category_}) Withdrawn {amount} from account")
            self.balance_ -= amount

    def transfer_to(self, other, amount: float):
        if not isinstance(other, Account):  # isinstance(object, type) compares object with type 
            print(f"..({self.category_}) Transfer not possible as {other}"
                  f" is not an instance of {self.__class__.__name__} class.")
        else:
            self.withdraw(amount)
            other.deposit(amount)

    def __str__(self) -> str:
        return f"\n\tCategory: {self.category_}" \
               f"\n\tAccount no: {self.account_id_:04d}" \
               f"\n\tBalance: {self.balance_}"


class Food(Account):
    total_food_account_no = 0  # class attribute. Food class has it's own counter

    def __init__(self, balance: float = 0):
        super().__init__(category='food', balance=balance)
        Food.total_food_account_no += 1


class Games(Account):
    def __init__(self, balance: float = 0):
        super().__init__(category='games', balance=balance)

    def __str__(self):
        # overriding a build in method, which is executed by print(object), or str(object)
        return f"##############\n" \
               f"#    GAMES   #\n"\
               f"# A: {self.account_id_:07d} #\n" \
               f"# B: {self.balance_:07.2f} #\n" \
               f"##############"


#############################################################

# print('\n*** Negative balance error')
# fred_account = Account('food', -10)  # -> program stops with ValueError()

print('\n*** Creating accounts -> mutate class attribute...')
print(Account.total_account_no)  # -> 0
barney_food = Account('food')  # account_id = 1
tom_games = Account('games', 100)  # account_id = 2

print(Account.total_account_no)  # -> 2
bob_books = Account('books', 30)  # account_id =3

# You can access class attrubute either by referring to it through class itself or through instances
print(Account.total_account_no)  # -> 3
print(barney_food.total_account_no)  # -> 3
print(tom_games.total_account_no)  # -> 3

print('\n*** Deposit/withdraw transactions...')
barney_food.withdraw(10)  # -> prints below balance error message
barney_food.deposit(100)  # -> balance = 100
barney_food.withdraw(0.99)  # -> balance = 90.01
print(barney_food)

tom_games.withdraw(30)  # balance = 70
print(tom_games)

bob_books.deposit(100)  # balance = 130
bob_books.withdraw(80)  # balance = 50
print(bob_books)

print('\n*** isinstance(object, type)')
a_string, b_int, c_bool = 'a', 10, True
print(isinstance(a_string, str))    # -> True
print(isinstance(b_int, int))       # -> True
print(isinstance(c_bool, bool))     # -> True
print(isinstance(a_string, float))  # -> False

print('\n*** Books to Food transfer...')
bob_books.transfer_to(barney_food, 20)  # bob_books.balance = 30; barney_food.balance = 110.01

print('\n*** Bad transfer...')
dog = '"I am a string"'
tom_games.transfer_to(dog, 1)  # error message, no effect

# more accounts
account_4 = Account('food', 6000)
account_5 = Account('food', 10)
account_6 = Account('games')

print('\n*** Food class instances')
food_account_1 = Food(125)  # account_id = 7
food_account_2 = Food(99)  # account_id = 8
bob_books.transfer_to(food_account_2, 1)  # bob_books.balance = 29; food_account_2 = 100
food_account_1.transfer_to(tom_games, 24.50)  # food_account_1 = 100.50; tom_games = 94.50
food_account_1.transfer_to(dog, 1)  # error message, no effect

print(food_account_1)

print('\n*** Games class instance')
games_account_1 = Games(400)  # account_id = 9
account_10 = Account('books', 10)  # account_id = 10
print(games_account_1)

print('\n*** Total number of accounts')
print('All accounts: ', Account.total_account_no)  # -> 10
print('Food accounts: ', Food.total_food_account_no)  # -> 2