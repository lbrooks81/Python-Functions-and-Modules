def print_models(unprinted_designs : list, completed_models : list) -> None:
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design : str = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models : list) -> None:
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
  