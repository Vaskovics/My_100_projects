PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, strip_name)
        with open(f"Output/ReadyToSend/{strip_name}_invitation.txt", "w") as invitation:
            invitation.write(new_letter)
