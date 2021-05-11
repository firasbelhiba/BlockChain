blockchain = []

# Returns the last value of the blockchain


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    user_input = float(input('Please enter your transaction amount :'))
    return user_input


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_choice():
    user_input = input('Your choice :')
    return user_input


# Output the blockchain list to the console
def print_blockchain_elements():
    if len(blockchain) < 1:
        print('The blockchain is empty !')
    else:
        for block in blockchain:
            print('Outputting block')
            print(block)


# Verify if the blockchain is valid
def verify_blockchain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


while True:
    print('Please choose an option')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('x: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'x':
        break
    elif user_choice == 'h':
        print('success')
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print('Invalid input , please pick a valid choice !')
    if not verify_blockchain():
        print('There is a missmatch in the blockchain')
        break

print('Thank you for your contribution and goodbye')
