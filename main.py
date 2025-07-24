class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

users = []

def register(username, timestamp):
    for user in users:
        if user.name == username:
            return 'Duplicate User!'

    users.append(User(username, 100))
    return 'Registered Successfully'

def deposit(username, amount, timestamp):
    for user in users:
        if user.name == username:
            user.money += amount
            return user.money
    return 'No Such User Found!'

def get_balance(username, timestamp):
    idx = -1
    for i, user in enumerate(users):
        if user.name == username:
            idx = i
            break
    else:
        return 'No Such User Found!'

    if users[idx].money < 10:
        return 'Not Enough Fund!'

    users[idx].money -= 10
    return users[idx].money

n = int(input())

for i in range(n):
    query = input().split()

    if query[0] == 'REGISTER':
        print(register(query[1], query[2]))

    elif query[0] == 'DEPOSIT':
        print(deposit(query[1], int(query[2]), query[3]))

    else:
        print(get_balance(query[1], query[2]))
