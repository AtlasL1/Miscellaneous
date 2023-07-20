# Build a Program
# Astronomy Gallery: Directory (About IMAG, Schedule, Docent Guides, Buggy Services)

# IMPORTING PACKAGES
from tabulate import tabulate

# PROMPTING THE USER TO ENTER THEIR NAME
def enter_name():
    print()
    print('Good day. ')
    name_input = input("Please enter your name: ")
    return name_input
user_name = enter_name()

# PRINTS WELCOME NOTE
def welcome_note():
    print()
    print('Welcome to the International Moving Astronomy Gallery 2023, {}! '.format(user_name))
    print('Kind note: If you filled in any of the information of what seems like a prank, it will be automatically \n'
          'dismissed. Thank you! ')
    print()
welcome_note()

# PRINTS AVAILABLE SERVICES
while True:
    def user_needs(selections):
        print(selections)
        print()
    user_needs(
        'Here are some available services we provide: '
        '\n1. About the International Moving Astronomy Gallery 2023 '
        '\n2. Schedule for Special Activities '
        '\n3. Docent Guide '
        '\n4. Buggy Service '
    )

# PROMPTS THE USER TO ENTER THEIR NEEDS
    def user_service():
        selection_input = input("What do you need? \n[1 / 2 / 3 / 4]: ")
        return selection_input
    selected = user_service()

    acceptable_selections = ["1", "2", "3", "4"]

# ERROR MESSAGE
    def error(error_message):
        if selected not in acceptable_selections:
            print()
            print(error_message)
    error('\nAn error has occured. Please try again. ')

# CHECKS INPUT VALIDATION
    def valid(valid_message):
        if selected in acceptable_selections:
            print()
    break

# BRINGS USER TO PAGE OF SELECTION 1
def about_gallery(about):
    if selected == "1":
        print()
        print('.........................................................................................')
        print()
        print('ABOUT THE INTERNATIONAL MOVING ASTRONOMY GALLERY 2023 \n')
        print(about)
about_gallery(
    'The International Moving ESCP Gallery (ESCP) is an organisation founded by a \n'
    'group of astronomy enthusiasts. First announcing its launch in October 2007, the ESCP \n'
    'has been going strong for 16 years. Our goal is to raise public awareness and interest \n'
    'among individuals about the universe beyond planet Earth. \n\n'
    'The vast reality outside ours is one far too bewildering to be fully comprehended. \n'
    'We aim to share our research and knowledge of this existing and expanding matter \n'
    'we all, as humans, forget to acknowledge due to our busy, yet microscopic lives. '
)

# TABULATE: SCHEDULE
schedule = [["8:00", "ESCP's Sun Model Building Contest - Individuals Under 18"],
            ["11:00", "ESCP's Sun Model Building Contest - Individuals Above 18"],
            ["15:00", "Introduction of ESCP 2023 from ESCP Founder"],
            ["17:00", "Short Film in ESCP Dome Theatre: Universal Galaxies"],
            ["21:00", "ESCP's Solar System Firework Show"]]

# BRINGS USER TO PAGE OF SELECTION 2
def full_schedule(schedule):
    if selected == "2":
        print()
        print('...................................................................................')
        print()
        print('SCHEDULE FOR SPECIAL ACTIVITIES OF THE INTERNATIONAL MOVING ASTRONOMY GALLERY 2023 \n')
        print(schedule)
full_schedule(tabulate(schedule, headers=["Time", "Activity"], tablefmt="grid"))

# TABULATE: DOCENT GUIDES
docent_guide_list = [["1", "Lim Bing Wen", "A 23-year-old Chinese astrophysicist from the Northern Region of \n"
                                           "Malaysia. An astronomy enthusiast since little, his current goal \n"
                                           "is to discover the existences of more planets and moons. "],
                     ["2", "Fang Song Yu", "A 26-year-old Chinese American meteorologist from Texas. He uses \n"
                                           "scientific principles to explain, understand, observe or forecast \n"
                                           "the earth's atmospheric phenomena. "],
                     ["3", "Lelioza Vandenberg", "A 22-year-old German science journalist from Berlin. She \n"
                                                 "reports news and other information about science to the \n"
                                                 "general public, specialising in astronomy. "],
                     ["4", "Axle Harrison", "A 25-year-old British astrophysicist from Nottingham. They study \n"
                                            "astronomical events and celestial bodies to learn more about the \n"
                                            "universe and how it was formed. "]]

# BRINGS USER TO PAGE OF SELECTION 3
def docent_guide(list):
    if selected == "3":
        print()
        print('....................................................................................................')
        print()
        print("LIST OF THE INTERNATIONAL MOVING ASTRONOMY GALLERY 2023'S DOCENT GUIDES AVAILABLE ")
        print(list)
        print('To hire a docent guide, please enter your information below. \n')
        while True:
            docent_guide_index = int(input('Docent guide No.: '))
            if docent_guide_index < 1 or docent_guide_index > 4:
                print('\nAn error has occured. \n'
                      'Please try again. \n')
            elif 1 <= docent_guide_index <= 4:
                current_location = input('\nYour current location: ')
                phone_number = input('\nPlease enter your phone number. \n (e.g. 0123456789) \nPhone number: ')
                print('\nYour request has been delivered successfully, {}. \n'
                      'Your docent guide should arrive in a few minutes. '.format(user_name))
                break
docent_guide(tabulate(docent_guide_list, headers=["No.", "Name", "About"], tablefmt="simple_grid"))

# BRINGS USER TO PAGE OF SELECTION 4
def buggy_service():
    if selected == "4":
        print()
        print('...................................................................................')
        print()
        print('BUGGY SERVICES OF THE INTERNATIONAL MOVING ASTRONOMY GALLERY 2023 ')
        print()
        print('We provide buggy services free of charge in building to facilitate access to destinations located \n'
              'beyond walking distance. Buggy services are also to help customers with special needs (Disabled, \n'
              'Pregnant Ladies, Senior Citizens, and Customers with Children). ')
        print()
        print('To book a buggy ride, please enter your information below. \n')
        while True:
            pax = int(input('Number of pax (1-6): '))
            if pax < 1 or pax > 6:
                print('\nOur buggy service is only for a minimum of 1 pax and a maximum of 6. \n'
                      'Please try again. \n')
            elif 1 <= pax <= 6:
                from_location = input('\nWhere from?: ')
                to_location = input('\nWhere to?: ')
                phone_number = input('\nPlease enter your phone number. \n (e.g. 0123456789) \nPhone number: ')
                print('\nYour ride has been booked successfully, {}. \n'
                      'Your driver should arrive in a few minutes. '.format(user_name))
                break
buggy_service()
