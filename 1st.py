blockchain = [1]
def add_value():
    blockchain.append([blockchain[-1],234])
    print(blockchain)

print("Adding once...")
# Add once
add_value()

print("Adding multiple times...")
# Add more than once
add_value()
add_value()
add_value()

