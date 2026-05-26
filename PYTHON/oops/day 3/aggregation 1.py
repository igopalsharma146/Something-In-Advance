# aggregation relationship in OOPs
class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def edit_profile(self, new_name,new_city,new_pincode,new_state):
        self.name = new_name
        self.address.change_address(new_city, new_pincode, new_state)
class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
        
    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state
        
# creating an address object
address = Address("Bangalore", 560001, "Karnataka")

# creating a customer object with the address object
customer = Customer("John Doe","Male",address)

# accessing the city of the customer's address through the customer object
print(f"The customer lives in {customer.address.city}.")

# editing the customer's profile
customer.edit_profile("Jane Doe", "Mumbai", 400001, "Maharashtra")
# accessing the updated city of the customer's address through the customer object
print(f"After editing the profile, the customer lives in {customer.address.city}.")