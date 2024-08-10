import time

class Client:
    def __init__(self, name):
        self.name = name
        self.start_time = time.time()
        self.end_time = None

    def finish(self):
        self.end_time = time.time()

    def get_duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return time.time() - self.start_time

class CoffeeShop:
    def __init__(self):
        self.clients = {}

    def add_client(self, name):
        if name in self.clients:
            print(f"Client {name} is already in the coffee shop.")
        else:
            self.clients[name] = Client(name)
            print(f"Added client {name}")

    def remove_client(self, name):
        if name in self.clients:
            self.clients[name].finish()
            duration = self.clients[name].get_duration()
            print(f"Client {name} left after {duration:.2f} seconds")
            del self.clients[name]
        else:
            print(f"Client {name} is not in the coffee shop.")

    def display_current_clients(self):
        print("\nCurrent clients in the coffee shop:")
        for name, client in self.clients.items():
            duration = client.get_duration()
            print(f"{name}: {duration:.2f} seconds")

def main():
    coffee_shop = CoffeeShop()
    
    while True:
        print("\n1. Add client")
        print("2. Remove client")
        print("3. Display current clients")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter client name: ")
            coffee_shop.add_client(name)
        elif choice == '2':
            name = input("Enter client name: ")
            coffee_shop.remove_client(name)
        elif choice == '3':
            coffee_shop.display_current_clients()
        elif choice == '4':
            print("Thank you for using the Coffee Shop Time Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Example Output:

"""
1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 1
Enter client name: Alice
Added client Alice

1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 1
Enter client name: Bob
Added client Bob

1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 3

Current clients in the coffee shop:
Alice: 15.23 seconds
Bob: 8.75 seconds

1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 2
Enter client name: Alice
Client Alice left after 25.67 seconds

1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 3

Current clients in the coffee shop:
Bob: 35.12 seconds

1. Add client
2. Remove client
3. Display current clients
4. Exit
Enter your choice (1-4): 4
Thank you for using the Coffee Shop Time Tracker. Goodbye!
"""
