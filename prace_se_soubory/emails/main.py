# zadání - https://www.youtube.com/watch?v=OdndwYnCJCU&list=PLQ8x_VWW6AkuCxxIi2fMjBP4u-U5rTMO1&index=16
with open("Input/general_letter.txt") as letter_file:
    letter = letter_file.read()

with open("Input/names.txt", mode="r") as names_file:
    list_of_names = names_file.readlines()
    for name in list_of_names:
        name = name.strip()
        letter_text = letter.replace("[name]", name)
        with open(f"Output/{name}_mas_dopis.txt", mode="w") as final_letter:
            final_letter.write(letter_text)
