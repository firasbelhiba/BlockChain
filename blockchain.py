blockchain = []
open_trnasaction = []
owner = 'Firas Belhiba'

# Returns the last value of the blockchain


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def get_transaction_value():
    transaction_recipient = input('Enter the recipient of the transaction')
    transaction_amount = float(input('Please enter your transaction amount :'))
    return transaction_recipient, transaction_amount


def add_transaction(recipient, sender=owner, amount=1.0):
    # Transaction dictionnary
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_trnasaction.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    block = {
        'previous_hash': 'XXX',
        'index': len(blockchain),
        'transaction': open_trnasaction
    }
    blockchain.append(block)


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
        else:
            print('-' * 20)


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


waiting_input = True

while waiting_input:
    print('Please choose an option')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('x: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        transaction_data = get_transaction_value()
        recipient, amount = transaction_data
        add_transaction(recipient, amount=amount)
        print(open_trnasaction)
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'x':
        waiting_input = False
    else:
        print('Invalid input , please pick a valid choice !')
    if not verify_blockchain():
        print_blockchain_elements()
        print('There is a missmatch in the blockchain')
        break
else:
    print('User left!')

print('Thank you for your contribution and goodbye')
