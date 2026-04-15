# 1. Product catalog, its just a bunch of my test products
catalog = {
    "Bread": {"price": 2.50, "stock": 20},
    "Milk": {"price": 4.00, "stock": 15},
    "Eggs": {"price": 3.50, "stock": 12},
    "Cheese": {"price": 5.50, "stock": 10},
    "Rice": {"price": 15.00, "stock": 3},   # Low stock
    "Apples": {"price": 1.20, "stock": 30},
    "Chicken": {"price": 12.00, "stock": 8},
    "Coffee": {"price": 8.00, "stock": 4},  # Low stock
    "Sugar": {"price": 2.00, "stock": 25},
    "Water": {"price": 1.00, "stock": 50}
}

def POS_SYSTEM_MENU():
    while True: # Allows multiple transactions while function is #called
        cart = {}
        
        # checks if a item has a stock under 5 if so it makes a low #stock alert
        print("\n--- Low Stock Alerts ---")
        for item, info in catalog.items():
            if info['stock'] < 5:
                print(f"⚠️  ALERT: {item} is low ({info['stock']} left)")
       #options 
        while True:
            print("\n--- Main Menu ---")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. CHECKOUT")
            print("5. Exit Session")
            
            choice = input("\nSelect an option (1-5): ").strip()
            #if option is 1 it list all products and detail
            if choice == '1':
                print("\n--- Product List ---")
                for item, info in catalog.items():
                    status = "AVAILABLE" if info['stock'] > 0 else "OUT OF STOCK"
                    print(f"- {item:10} | Price: ${info['price']:>6.2f} | Stock: {info['stock']} [{status}]")
            #if option is 2 it adds a product to the cart along #with its quantity
            elif choice == '2':
                name = input("Enter product name: ").strip().capitalize()
                if name in catalog:
                    try: #how much of the item
                        qty = int(input(f"How many {name}s? "))
                        if qty <= 0:
                            print("Quantity must be greater than 0.")
                        elif catalog[name]['stock'] >= qty:
                            cart[name] = cart.get(name, 0) + qty
                            print(f"✅ Added {qty} {name}(s) to cart.")
                        else: #if the amount entered is above the #stock an error is displayed
                            print(f"❌ Error: Only {catalog[name]['stock']} available.")
                    except ValueError: #if any thing besides an #integer is entered
                        print("❌ Invalid quantity. Please enter a number.")
                else: #if the name of the product doesnt exist it #prints an error
                    print(f"❌ '{name}' not found in catalog. Check spelling/capitalization.")
            #if option 3 is selected it checks if there is anything #in cart if there isnt it gives an error otherwise #it displays
            elif choice == '3':
                if not cart:
                    print("Your cart is empty.")
                else:
                    print("\n--- Your Shopping Cart ---")
                    for item, qty in cart.items():
                        item_total = qty * catalog[item]['price']
                        print(f"{item:10} x{qty} @ ${catalog[item]['price']:.2f} = ${item_total:.2f}")
            
            elif choice == '4':
                # --- CHECKOUT LOGIC ---
                if not cart:
                    print("❌ CHECKOUT FAILED: You cannot checkout with an empty cart!")
                    continue
                
                # Calculations
                subtotal = sum(catalog[item]['price'] * qty for item, qty in cart.items())
                
                # Apply 5% discount if subtotal > $5000 
                #and applys 10% sales tax
                discount = 0
                if subtotal > 5000:
                    discount = subtotal * 0.05
                
                taxable_total = subtotal - discount
                tax = taxable_total * 0.10
                final_total = taxable_total + tax
                
                print(f"\n--- Order Summary ---")
                print(f"Subtotal:     ${subtotal:.2f}")
                if discount > 0:
                    print(f"Discount:    -${discount:.2f}")
                print(f"Sales Tax:    ${tax:.2f}")
                print(f"TOTAL DUE:    ${final_total:.2f}")
                
                # Payment Validation
                try:
                    paid = float(input("\nEnter amount received: $"))
                    if paid >= final_total:
                        change = paid - final_total
                        
                        # --- RECEIPT GENERATION ---
                        print("\n" + "*"*35)
                        print("        Best Buy Retail Store")
                        print("*"*35)
                        for item, qty in cart.items():
                            unit_p = catalog[item]['price']
                            print(f"{item:15} {qty}x @{unit_p:6.2f} = ${qty*unit_p:8.2f}")
                        print("-" * 35)
                        print(f"SUBTOTAL:          ${subtotal:10.2f}")
                        if discount > 0:
                            print(f"DISCOUNT:         -${discount:10.2f}")
                        print(f"TAX (10%):         ${tax:10.2f}")
                        print(f"GRAND TOTAL:       ${final_total:10.2f}")
                        print(f"CASH PAID:         ${paid:10.2f}")
                        print(f"CHANGE:            ${change:10.2f}")
                        print("*" * 35)
                        print("    THANK YOU FOR SHOPPING AT  Best Buy Retail Store!")
                        print("*" * 35)
                        
                        # Update Inventory
                        for item, qty in cart.items():
                            catalog[item]['stock'] -= qty
                        
                        break # Ends this transaction, goes back to start for next customer
                    else:
                        print(f"❌ Payment Insufficient! Need ${final_total - paid:.2f} more.")
                except ValueError:
                    print("❌ Invalid payment amount.")

            elif choice == '5':
                print("Closing system... Goodbye!")
                return

POS_SYSTEM_MENU()