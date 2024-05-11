# Assigning values to a variable 
'''
first_int = 4 
first_float = 3.1415 
second_float = 1.0 
complex_no = 2+4j 
first_string = 'hello'
second_string = 'world'
'''


# Extracting words from strings using slice 
'''
ex = 'Python is an interesting and useful language for numerical computing!'
ex_length = len(ex)

slice1 = ex[:6]
slice2 = ex[-1]
slice3 = ex[-10:-1]

print(slice1)
print(slice2)
print(slice3)
'''

# Create a list of states and population 
state_population = [['States', 'Taraba', 'Adamawa', 'Lagos', 'Abia', 'Abuja', 'Kano'], 
                    ['Population', 2000, 1000, 400, 5000, 2000, 300]]


states = state_population[0][:]
population = state_population[1][:]

# Print out states and population 
# print(states, end='\t\n')
# print(population, end='\t\n')

# Append additional number of states and population
# to the existing list
states.append('kaduna')
population.append(3000)

states.append('Jos')
population.append('5000')

states.append('Lagos')
population.append('3000')

# Delete Abia and Lagos State 
del states[4]
del population[4]

del states[-1]
del population[-1]

print(len(states), len(population))

#changing the population of a taraba state

population[1]=8000

print(states, end='\t\n')
print(population, end='\t\n')

# Chapter one Exercises complete