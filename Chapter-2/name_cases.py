# Try It Yourself
# 2-3 Personal Message
first_name = "Kenderson"
last_name = "Chang"
question = "would you like to learn some Python today?"
message = "Hello" + " " + first_name + ", " + question

print(message)

# 2-4 Name Cases
full_name = "Kenderson Chang"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# 2-5 Famous Quote
quote = 'Some anonymous person once said "You will continue to suffer if you have an emotional reaction to everything that is said to you. \nTrue power is sitting back and observing everything with logic; true power is restraint. \nIf words control you that means everyone else can control you; breathe and allow things to pass." \n\t-Anonymous'
print(quote)


# 2-6 Famous Quote 2
famous_person = "Anonymous"
message = "You will continue to suffer if you have an emotional reaction to everything that is said to you. \nTrue power is sitting back and observing everything with logic; true power is restraint. \nIf words control you that means everyone else can control you; breathe and allow things to pass."
print(message + " -" + famous_person)

# 2-7 Stripping Names
bigBaller1 = " Lonzo Ball"
bigBaller2 = "LiAngelo Ball "
bigBaller3 = " LaMelo Ball "
print(bigBaller1, bigBaller2, bigBaller3)

print(bigBaller1.lstrip(), bigBaller2.rstrip(), bigBaller3.strip())