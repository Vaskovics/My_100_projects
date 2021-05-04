import pandas
data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}

word = list(input("Enter a word:").upper())
result = [code for letter in word for (key, code) in data_dict.items() if letter == key]
print(result)
