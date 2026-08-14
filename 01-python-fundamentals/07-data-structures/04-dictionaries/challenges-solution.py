def main():
    # Initial inventory
    inventory = {
        "apple": 10,
        "banana": 5,
        "orange": 8,
        "grape": 3
    }
    
    print("Initial Inventory:")
    for item, count in inventory.items():
        print(f"- {item}: {count}")
        
    while True:
        if not inventory:
            print("\nInventory is completely empty!")
            break
            
        sell_item = input("\nEnter item to sell (or 'exit' to quit): ").strip().lower()
        if sell_item == 'exit':
            break
            
        if sell_item in inventory:
            try:
                quantity_str = input(f"Enter quantity of {sell_item} to sell: ").strip()
                quantity = int(quantity_str)
                if quantity <= 0:
                    print("Error: Quantity must be positive.")
                    continue
                
                if quantity > inventory[sell_item]:
                    print(f"Error: Not enough stock. Only {inventory[sell_item]} available.")
                else:
                    inventory[sell_item] -= quantity
                    print(f"Successfully sold {quantity} {sell_item}(s).")
                    
                    if inventory[sell_item] == 0:
                        print(f"Alert: {sell_item} is now out of stock and has been removed from inventory.")
                        del inventory[sell_item]
            except ValueError:
                print("Error: Invalid quantity. Please enter an integer.")
        else:
            print(f"Error: '{sell_item}' does not exist in inventory.")

if __name__ == "__main__":
    main()
