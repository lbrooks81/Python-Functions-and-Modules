unprinted_designs : list = ['phone case', 'robot pendant', 'dodecahedron']
completed_models : list = []

while unprinted_designs:
    current_design : str = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

