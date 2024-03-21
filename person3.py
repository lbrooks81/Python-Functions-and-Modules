def build_person(first_name: str, last_name: str, age: int=None) -> dict:
    """Returns a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

musician = build_person('derek', 'shulman')
print(musician)

