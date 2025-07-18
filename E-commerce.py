class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    
    def get_details(self):
        return f"{self.name} - ${self.price:.2f}"
    
    def apply_discount(self, discount_percent):
        self.price = self.price * (1 - discount_percent / 100)
        return f"Applied {discount_percent}% discount to {self.name}"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product  # Composition: CartItem HAS a Product
        self.quantity = quantity
    
    def get_total_price(self):
        return self.product.price * self.quantity
    
    def get_item_details(self):
        return f"{self.product.name} x{self.quantity} = ${self.get_total_price():.2f}"

class Cart:
    def __init__(self):
        self.items = []  # Composition: Cart HAS CartItems
        self.discount_code = None
    
    def add_item(self, product, quantity=1):
        # Check if product already exists in cart
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                print(f"Updated {product.name} quantity to {item.quantity}")
                return
        
        # Add new item
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)
        print(f"Added {quantity} x {product.name} to cart")
    
    def remove_item(self, product_name):
        self.items = [item for item in self.items if item.product.name != product_name]
        print(f"Removed {product_name} from cart")
    
    def get_total(self):
        total = sum(item.get_total_price() for item in self.items)
        return total
    
    def display_cart(self):
        if not self.items:
            print("Cart is empty")
            return
        
        print("Shopping Cart:")
        print("-" * 30)
        for item in self.items:
            print(item.get_item_details())
        print("-" * 30)
        print(f"Total: ${self.get_total():.2f}")
    
    def apply_discount_code(self, code, discount_percent):
        self.discount_code = code
        discounted_total = self.get_total() * (1 - discount_percent / 100)
        print(f"Applied discount code '{code}': {discount_percent}% off")
        print(f"New total: ${discounted_total:.2f}")

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = Cart()  # Composition: User HAS a Cart
        self.order_history = []
    
    def add_to_cart(self, product, quantity=1):
        self.cart.add_item(product, quantity)
    
    def view_cart(self):
        print(f"{self.username}'s Cart:")
        self.cart.display_cart()
    
    def checkout(self):
        if not self.cart.items:
            print("Cannot checkout - cart is empty")
            return
        
        total = self.cart.get_total()
        # Create order (simplified)
        order = {
            'items': len(self.cart.items),
            'total': total,
            'status': 'completed'
        }
        self.order_history.append(order)
        
        print(f"Order placed successfully! Total: ${total:.2f}")
        self.cart.items = []  # Clear cart after checkout
    
    def view_order_history(self):
        print(f"{self.username}'s Order History:")
        if not self.order_history:
            print("No orders yet")
            return
        
        for i, order in enumerate(self.order_history, 1):
            print(f"Order {i}: {order['items']} items, ${order['total']:.2f}")

# Using the composition
# Create products
laptop = Product("Gaming Laptop", 1299.99, "High-performance gaming laptop")
mouse = Product("Wireless Mouse", 29.99, "Ergonomic wireless mouse")
keyboard = Product("Mechanical Keyboard", 89.99, "RGB mechanical keyboard")

# Create user
user = User("john_doe", "john@email.com")

# User adds items to cart
user.add_to_cart(laptop, 1)
user.add_to_cart(mouse, 2)
user.add_to_cart(keyboard, 1)

# View cart
user.view_cart()

# Apply discount
user.cart.apply_discount_code("SAVE10", 10)

# Checkout
user.checkout()

# View order history
user.view_order_history()
