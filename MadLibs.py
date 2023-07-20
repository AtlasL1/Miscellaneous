# Build a Program
# Mad Libs: Mad Libs Game Online

# IMPORTING PACKAGES
import random

# PROMPTS USER TO ANSWER GAME INVITATION
def invitation():
    print()
    print('Hallo!')
    print('My name is Bing Wen.')
    print()
    print("I'm all alone here. Can you play a game with me?")
    yes_or_no = input('[Yes / No]: ')
    return yes_or_no
yes_or_no = invitation()

# PROMPTS USER TO ENTER NAME
def get_name():
    if yes_or_no == "Yes":
        print()
        name_input = input('What is your name, kind stranger? \nName: ')
        return name_input
name_input = get_name()

# EXPLAINS MAD LIBS
def explain():
    if yes_or_no == "Yes":
        print()
        print("Let's play my favourite game, Mad Libs! ")
        print()
        print('Do you know what Mad Libs is, {}?'.format(name_input))
        do_you_know = input('[Yes / No]: ')
        if do_you_know == "Yes":
            print()
            print("Alright, let's play!")
        elif do_you_know == "No":
            print()
            print("No worries, I'll explain it to you!")
            print()
            print("I will start by asking you to provide a list of words of specific types, such as nouns, \n"
                  "verbs or adjectives without telling you the context of the story. \n\n"
                  "Once all the words are gathered, I will insert them into a pre-written story, with the \n"
                  "chosen words filling in the blanks. The resulting story is often funny because it's unexpected!")
            print()
            print("Let's play, shall we?")
            shall_we = input('[Yes / No]: ')
            if shall_we == "No":
                print()
                print('Alright.')
                print('Thanks for stopping by, still!')
                print('I hope I see you again.')
explain()

# GET WORD INPUTS FROM USER
def word_input():
    print()
    print("Let's start the game!")
    print()
    place1 = input('Enter a place: ')
    place2 = input('Enter another place: ')
    name = input('Enter a name: ')
    adj = input('Enter an adjective: ')
    verb = input('Enter a verb: ')
    mood = input('Enter a mood: ')
    object_or_animal = input('Enter an object or animal: ')
    return place1, place2, name, adj, verb, mood, object_or_animal
place1, place2, name, adj, verb, mood, object_or_animal = word_input()

# LIST OF RANDOM STORIES
def random_story():
    random_stories = [
        f"There's a {place1} in {place2}! {name}, a {adj}-looking girl is {verb} there. She seems \n"
        f"to be very {mood}, but {object_or_animal} is welcoming her!",

        f"In the {place1} there is a {place2}. {name} is a {adj} {object_or_animal} who loves to \n"
        f"{verb}. He is always in a {mood} mood.",

        f"The path in {place1} is very {adj}. The path in {place2} is owned by {name}. He does not \n"
        f"like {object_or_animal}. Now he is feeling very {mood} because he has to {verb}.",

        f"{name} does not know what he is doing. {place1} is not for {object_or_animal}. {place2} \n"
        f"is not for {object_or_animal} too. {place1} and {place2} is for very {adj} {object_or_animal}. \n"
        f"{name} is very {mood}!",

        f"{object_or_animal}, very dangerous when they have a {object_or_animal} fight. Especially \n"
        f"{name}. He is most {adj} of the bunch. He comes from {place1}. {place1} is very scary \n"
        f"for {object_or_animal} from {place2}. Beware! He is currently very {mood}!"
    ]

    story = random.choice(random_stories)
    return story

# SHOWS THE COMPLETED STORY
def show():
    print()
    story = random_story()
    print(story)
show()

# THANK YOU AND GOODBYE NOTE FOR CONTENTED ACCEPTION
def bye():
    print()
    print('Ha-ha!')
    print('That was very funny, I loved it!')
    print('Thank you so much for playing with me, {}!'.format(name_input))
    print("Let's meet again next time. I hope I see you soon!")
bye()

# THANK YOU AND GOODBYE NOTE FOR REJECTION
def no():
    if yes_or_no == "No":
        print()
        print('Alright.')
        print('Thanks for stopping by, still!')
        print('I hope I see you again.')
no()