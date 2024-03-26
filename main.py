

with open("Input/Letters/starting_letter.txt") as blueprint:
    list_blueprint = blueprint.read()

with open("Input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

for name in names:
    name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as letter:
        new_letter = list_blueprint.replace("[name]", name)
        letter.write(new_letter)

