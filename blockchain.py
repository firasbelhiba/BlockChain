blockchain = []


def get_last_blockchain_value():
    return blockchain[-1]


def get_transaction_value():
    user_input = float(input('Please enter your transaction amount :'))
    return user_input


def add_value(transaction_amount, last_transaction=[1]):
    blockchain.append([last_transaction, transaction_amount])


def get_user_choice():
    user_input = input('Your choice :')
    return user_input


# Output the blockchain list to the console
def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)


tx_amount = get_transaction_value()
add_value(tx_amount)

while True:
    print('Please choose an option')
    print('1:Add a new transaction value')
    print('2:Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    else:
        print_blockchain_elements()

print('Done !')
