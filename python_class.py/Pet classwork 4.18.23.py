my_pet_1= 'pet'
my_pet_1_type = 'cat'
my_pet_1_noise = 'meow'
my_pet_1_full_name = 'Shuffles McSniff'


my_pet_2 = 'pet'
my_pet_2_type = 'cat'
my_pet_2_noise = 'meow'
my_pet_2_full_name = 'Snowpounce Flury

print(my_pet_1_noise)
print(my_pet_1_full_name)


#Class activity

class Sandwich:
    
    def __init__(self, ingredientA, ingredientB, ingredientC) : 
        self.ingredientA = ingredientA 
        self.ingredientB = ingredientB
        self.ingredientC = ingredientC

order = Sandwich('bread', 'meat', 'mayo,;')

print(order.ingredientA)
print(order.ingredientB)
print(order.ingredientC)