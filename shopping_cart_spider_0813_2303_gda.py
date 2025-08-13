# 代码生成时间: 2025-08-13 23:03:07
#!/usr/bin/env python

"""
Shopping Cart Spider - A Scrapy Framework based shopping cart program.
This program simulates a basic shopping cart functionality using Scrapy.
"""

import scrapy
from scrapy.exceptions import DropItem

class ShoppingCartItem:
    """Shopping Cart Item model."""
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"<ShoppingCartItem(item_id={self.item_id}, name={self.name}, price={self.price}, quantity={self.quantity})>"

class ShoppingCart:
    """Shopping Cart model."""
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the cart."""
        if not isinstance(item, ShoppingCartItem):
            raise ValueError("Item must be an instance of ShoppingCartItem")
        for cart_item in self.items:
            if cart_item.item_id == item.item_id:
                cart_item.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item(self, item_id):
        """Remove an item from the cart."""
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                return
        raise ValueError("Item not found in the cart")

    def update_quantity(self, item_id, quantity):
        """Update the quantity of an item in the cart."""
        for item in self.items:
            if item.item_id == item_id:
                if quantity < 1:
                    item.quantity = 1
                else:
                    item.quantity = quantity
                return
        raise ValueError("Item not found in the cart")

    def calculate_total(self):
        """Calculate the total price of all items in the cart."""
        total = sum(item.price * item.quantity for item in self.items)
        return total

    def __repr__(self):
        return f"<ShoppingCart(items={self.items})>"

class ShoppingCartSpider(scrapy.Spider):
    """Scrapy Spider for simulating shopping cart."""
    name = "shopping_cart"
    allowed_domains = []
    start_urls = []

    def process_item(self, item, spider):
        """Process the item and add it to the shopping cart."""
        try:
            # Create a ShoppingCartItem instance
            cart_item = ShoppingCartItem(
                item_id=item['item_id'],
                name=item['name'],
                price=item['price'],
                quantity=item['quantity'],
            )
            # Add the item to the shopping cart
            self.cart.add_item(cart_item)
            return item
        except KeyError as e:
            raise DropItem(f"Missing field in item: {e}")

    def start_requests(self):
        """Start the spider and initiate the shopping cart."""
        self.cart = ShoppingCart()
        yield scrapy.Request(url="http://example.com/shop", callback=self.parse)

    def parse(self, response):
        """Parse the page and yield the item data."""
        # This is a placeholder for the actual parsing logic
        # It should extract item data and yield it
        items = [
            {'item_id': '1', 'name': 'Item 1', 'price': 10.99, 'quantity': 1},
            {'item_id': '2', 'name': 'Item 2', 'price': 9.99, 'quantity': 2},
        ]
        for item in items:
            yield item

# Usage example:
if __name__ == "__main__":
    # Create a ShoppingCartSpider instance and start the spider
    cart_spider = ShoppingCartSpider()
    cart_spider.start_requests()
    # Process items and update the shopping cart
    for item in cart_spider.process_item:
        print(item)
    # Print the total price of all items in the cart
    print(f"Total price: ${cart_spider.cart.calculate_total()}")