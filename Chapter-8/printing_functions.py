def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# Simulate creating a 3D print from the design
		print("\tPrinting model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were completed. """
	print("\nThe following models have been printed:")	
	for completed_model in completed_models:
		print("\t" + completed_model)