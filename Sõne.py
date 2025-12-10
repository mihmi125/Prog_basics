first_name = "James"
last_name = "Bond"
full_name = f"{first_name} {last_name}"
self_description_sentence = f"My name is {last_name}, {full_name}."

cake = "vahukoormarjadtäidispõhi"

vahukoor = cake[0:8]
marjad = cake[8:14]
täidis = cake[14:20]
põhi = cake[20:]

print(vahukoor, marjad, täidis, põhi, sep="\n")

original_string = "Programming is fun!"

backwards = original_string[::-1]

every_other = original_string[0::2]

first_word = original_string.split()[0]
first_word_reversed = first_word[::-1]