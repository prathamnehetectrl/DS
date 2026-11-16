
# PART 1: PRODUCT NODE (GRAPH VERTEX)

class ProductNode:

    def __init__(self, name, price):
        self.name = name
        self.price = price

        # Stores direct references to neighbouring products
        self.neighbors = []

    # Connect another product to this product
    def add_neighbor(self, product_reference):

        if product_reference not in self.neighbors:
            self.neighbors.append(product_reference)



# PART 2: HASH TABLE NODE (LINKED LIST)

class HashNode:

    def __init__(self, key, value):
        self.key = key

        # Stores the actual ProductNode reference
        self.value = value

        # Points to the next node in case of collision
        self.next = None




# PART 3: CUSTOM HASH TABLE

class ProductDirectory:

    def __init__(self, size=20):
        self.size = size

        # Create an empty array of buckets
        self.table = [None] * size

    # Custom hash function
    def hash_function(self, key):

        hash_value = 0

        for character in key.lower():
            hash_value = hash_value * 31 + ord(character)

        return hash_value % self.size

    # Insert product into hash table
    def put(self, key, value):

        index = self.hash_function(key)

        new_node = HashNode(key.lower(), value)

        # If bucket is empty
        if self.table[index] is None:
            self.table[index] = new_node
            return

        current = self.table[index]

        # Handle collision using linked list
        while current:

            # Update if product already exists
            if current.key == key.lower():
                current.value = value
                return

            if current.next is None:
                current.next = new_node
                return

            current = current.next

    # Search product
    def get(self, key):

        index = self.hash_function(key)
        current = self.table[index]

        while current:

            if current.key == key.lower():
                return current.value

            current = current.next

        return None


    

# PART 4: RECOMMENDATION ENGINE

class RecommendationEngine:

    def __init__(self):
        self.directory = ProductDirectory()
        self.products = []

    # 1. ADD PRODUCT
    def add_product(self, name, price):

        # Check whether product already exists
        if self.directory.get(name) is not None:
            print("Product already exists!")
            return

        # Create product node
        product = ProductNode(name, price)

        # Store product in list
        self.products.append(product)

        # Store actual reference in custom hash table
        self.directory.put(name, product)

        print("Product added:", name)

    # 2. LINK TWO PRODUCTS
    def link_products(self, name1, name2):

        product1 = self.directory.get(name1)
        product2 = self.directory.get(name2)

        if product1 is None or product2 is None:
            print("Product not found!")
            return

        # Connect products bidirectionally
        product1.add_neighbor(product2)
        product2.add_neighbor(product1)

    # 3. GET DIRECT RECOMMENDATIONS
    def get_recommendations(self, name):

        product = self.directory.get(name)

        if product is None:
            print("Product not found!")
            return

        print("\nRecommendations for:", product.name)
        print("Path Length: 1")
        print("--------------------------------")

        if not product.neighbors:
            print("No recommendations available.")
            return

        for neighbor in product.neighbors:

            print(
                neighbor.name,
                "- Price: Rs.",
                neighbor.price
            )

    # 4. EXTENDED RECOMMENDATIONS USING BFS
    def get_extended_recommendations(self, name, max_depth=2):

        start = self.directory.get(name)

        if start is None:
            print("Product not found!")
            return

        # Track visited products
        visited = {start}

        # Queue stores product and depth
        queue = [(start, 0)]

        print("\nExtended Recommendations for:", start.name)
        print("Maximum Depth:", max_depth)
        print("--------------------------------")

        while queue:

            current, depth = queue.pop(0)

            # Stop at maximum depth
            if depth >= max_depth:
                continue

            # Visit neighboring products
            for neighbor in current.neighbors:

                if neighbor not in visited:

                    visited.add(neighbor)

                    print(
                        neighbor.name,
                        "- Depth:",
                        depth + 1,
                        "- Price: Rs.",
                        neighbor.price
                    )

                    queue.append((neighbor, depth + 1))




# PART 5: MAIN PROGRAM

# Create recommendation engine
engine = RecommendationEngine()

# Add 10 coffee products
engine.add_product("Espresso Machine", 15000)
engine.add_product("Coffee Grinder", 3500)
engine.add_product("Milk Frother", 1200)
engine.add_product("Coffee Beans", 800)
engine.add_product("Coffee Scale", 1500)
engine.add_product("French Press", 1000)
engine.add_product("Coffee Maker", 4000)
engine.add_product("Travel Mug", 600)
engine.add_product("Electric Kettle", 2000)
engine.add_product("Coffee Filter", 300)




# PART 6: CONNECT PRODUCTS USING GRAPH

engine.link_products("Espresso Machine", "Coffee Grinder")
engine.link_products("Espresso Machine", "Milk Frother")
engine.link_products("Espresso Machine", "Coffee Beans")
engine.link_products("Espresso Machine", "Coffee Scale")

engine.link_products("Coffee Grinder", "Coffee Beans")
engine.link_products("Coffee Grinder", "French Press")

engine.link_products("Milk Frother", "Coffee Maker")

engine.link_products("Coffee Maker", "Travel Mug")
engine.link_products("Coffee Maker", "Electric Kettle")

engine.link_products("French Press", "Coffee Filter")

engine.link_products("Electric Kettle", "Coffee Filter")

print("All products connected successfully!")





# PART 7: INTERACTIVE USER MENU

print("\n======================================")
print(" COFFEE PRODUCT RECOMMENDATION SYSTEM")
print("======================================")

while True:

    print("\n1. Direct Recommendations")
    print("2. Extended Recommendations (BFS)")
    print("3. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":

        name = input("Enter product name: ").strip()

        engine.get_recommendations(name)

    elif choice == "2":

        name = input("Enter product name: ").strip()

        engine.get_extended_recommendations(name, 2)

    elif choice == "3":

        print("Thank you for using our system!")
        break

    else:

        print("Invalid choice! Please try again.")

# BFS TEST
engine.get_extended_recommendations("Espresso Machine", 2)

