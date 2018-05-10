# Modifying a List in a Function

# Starting with some designs taht need to be printed
unprinted_designs = ['iphone x case', 'lungs', 'kidneys']
completed_models = []

# Simulate printing each design until none are left
# Move each design to completed_models after printing
while unprinted_designs:
	current_design = unprinted_designs.pop()
	# Simulate creating a 3D print from the design
	print("\tPrinting model: " + current_design)
	completed_models.append(current_design)

# Display all completed models
print("\n\tThe following models have been printed:")
for completed_model in completed_models:
	print("\t" + completed_model)