# WRITE YOUR FUNCTIONS HERE
# Q1
def get_pet_shop_name(pet_shop_list):
    return pet_shop_list["name"]
        
# Q2
def get_total_cash(pet_shop_list): 
    return pet_shop_list["admin"]["total_cash"]
    
# Q3
def add_or_remove_cash(pet_shop_list, amount_to_add):
    pet_shop_list["admin"]["total_cash"] += amount_to_add

# Q4
def add_or_remove_cash(pet_shop_list, amount_to_remove):
    pet_shop_list["admin"]["total_cash"] += amount_to_remove

# Q5
def get_pets_sold(pet_shop_list):
    return pet_shop_list["admin"]["pets_sold"]

# Q6
def increase_pets_sold(pet_shop_list, increase_amount):
    pet_shop_list["admin"]["pets_sold"] += increase_amount
   
# Q7   
def get_stock_count(pet_shop_list):
    for stock in pet_shop_list:
        stock_count = len(pet_shop_list["pets"])
        return stock_count

 # Q8  
def get_pets_by_breed(pet_shop_list, breed):
    breed_type = []
    for pet in pet_shop_list["pets"]:
        if pet["breed"] == breed:
            breed_type.append(pet)
    return breed_type

# Q9
def get_pets_by_breed_not_found(pet_shop_list, breed):
    for pet in pet_shop_list["pets"]:
        if pet["breed"] == breed:
            return pet

# Q10
def find_pet_by_name(pet_shop_list, pet_name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == pet_name:
            return pet

# Q11
    def find_pet_by_name(pet_shop_list, name):
        for pet in pet_shop_list["pets"]:
            if pet["name"] == name:
                return pet
            
# Q12
def remove_pet_by_name(pet_shop_list, pet_name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == pet_name:
            pet_shop_list["pets"].remove(pet)
            
# Q13
def add_pet_to_stock(pet_shop_list, new_pet):
    for pet in pet_shop_list["pets"]:
        pet_shop_list["pets"].append(new_pet)
        return new_pet
        
# Q14 
def get_customer_cash(customer):
    return customer["cash"]
 
# Q15
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# Q16
def get_customer_pet_count(customer):
    customer_pet_count = len(customer["pets"])
    return customer_pet_count

 
# Q17 
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
        