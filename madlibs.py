print("Welcome to Madlibs! These are the madlibs available: \n 1. What happens when a unicorn poops? \n 2. Spring Garden \n 3. Spooky! \n 4. Apples")

madlibs= int(input("Select a number from 1-4: \n"))

game = 1

while game == 1:
    if madlibs==1:
        pluralnoun = input("Enter a plural noun: \n")
        adjective1 = input("Enter an adjective: \n")
        animal = input("Enter an animal(plural): \n")
        noun = input("Enter a noun: \n")
        adjective2 = input("Enter an adjective: \n")
        unicorn = f'Unicorns are not like other {pluralnoun}; they are {adjective1}. They look like {animal}, with {noun} for feet and a {adjective2} mane of hair. '
        print(unicorn)
    elif madlibs==2:
        noun1 = input("Enter a noun: \n")
        adjective = input("Enter an adjective: \n")
        noun2 = input("Enter a noun: \n")
        noun3 = input("Enter a noun: \n")
        spring = f'Planting a vegetable garden is not only fun it also helps save {noun1}. You will need a piece of {adjective} land. You may need a {noun2}, to keep the {noun3} out.'
        print(spring)
    elif madlibs==3:
        person1 = input("Enter a person name: \n")
        person2 = input("Enter a person name: \n")
        holiday = input("Enter a holiday: \n")
        verb = input("Enter a verb: \n")
        noun = input("Enter a noun: \n")
        verb2 = input("Enter a verb: \n")
        fruit = input("Enter a fruit: \n")
        spooky = f'{person1} and {person2} come out tonight! It is {holiday} and they are ready to {verb}. So watch your {noun} when {verb2} or treating, they want your {fruit}'
        print(spooky)
    elif madlibs==4:
        adjective = input("Enter an adjective: \n")
        verb = input("Enter a verb: \n")
        verb2 = input("Enter a verb: \n")
        person = input("Enter a person name: \n")
        fruit = input("Enter a fruit: \n")
        apple = f'Red, {adjective} apples! Today we are going to {verb} apples. I am going to {verb2} the most. My {person} and I are having a {fruit} picking contest this year.'
        print(apple)
    else:
        print('You did not select a valid number.')

    stop = input("Would you like to continue? (y/n): \n")

    if stop=='y':
        game = 1
        madlibs= int(input("Select a number from 1-4: \n"))
    else:
        game = 0




