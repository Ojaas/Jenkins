def get_product_info():
  """Prompts the user for product name and quantity and returns a dictionary."""
  product_name = input("What product are you looking for? ")
  while True:
    try:
      quantity = int(input("Enter the quantity: "))
      if quantity > 0:
        break
      else:
        print("Quantity must be a positive numbers.")
    except ValueError:
      print("Invalid input. Please enter a number.")
  return {"product": product_name, "quantity": quantity}

if __name__ == "__main__":
  product_info = get_product_info()
  print(f"You are looking for {product_info['quantity']} of {product_info['product']}.")
