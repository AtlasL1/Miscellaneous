# Build A Table of Contents
# ESCP Gallery

# IMPORTING PACKAGES
from tabulate import tabulate

# TABULATE: SOLAR SYSTEM
solar_system_list = [["0", "The Sun", "1. Structure \n2. Key Features \n3. Magnetosphere"],
                     ["1", "Mercury", "1. Structure \n2. Surface"],
                     ["2", "Venus", "1. Structure \n2. Surface, \n3. Atmosphere, \n4. Magnetosphere"],
                     ["3", "Earth", "1. Structure \n2. Size and Distance \n3. Orbit and Rotation \n4. Moon"],
                     ["4", "Mars", "1. Structure \n2. Surface \n3. Atmosphere \n4. Moons"],
                     ["5", "Jupiter", "1. Structure \n2. Surface \n3. Atmosphere \n4. Moons \n5. Rings"],
                     ["6", "Saturn", "1. Structure \n2. Surface \n3. Atmosphere \n5. Magnetosphere \n6. Rings \n7. Moons"],
                     ["7", "Uranus", "1. Structure \n2. Surface \n3. Atmosphere \n5. Magnetosphere \n6. Rings \n7. Moons \n8. Orbit and Rotation"],
                     ["8", "Neptune", "1. Structure \n2. Surface \n3. Atmosphere \n5. Magnetosphere \n6. Rings \n7. Moons"]]

# TABULATE: SUPERNOVAE
supernovae_list = [["0", "What Is A Supernova?"],
                   ["1", "Where Do Supernovae Take Place?"],
                   ["2", "What Causes A Supernova?"],
                   ["3", "Why Do Scientists Study Supernovae?"],
                   ["4", "How Do NASA Scientists Look for Supernovae?"]]

# TABULATE: NEBULAE
nebulae_list = [["0", "What is A Nebula?"],
                ["1", "Emission Nebulae"],
                ["2", "Planetary Nebulae"],
                ["3", "Supernova Remnants"],
                ["4", "Absorption Nebulae"]]

# TABULATE: MILKY WAY
milkyway_list = [["0", "What is the Milky Way?"],
                 ["1", "Does the Milky Way Have Two or Four Spiral Arms?"]]

# PRINTS TABLE OF SOLAR SYSTEM
def solar_system(topics):
    print()
    print('TOPICS COVERED BY THE IMAG')
    print()
    print('A) SOLAR SYSTEM')
    print(topics)
    print()
solar_system(tabulate(solar_system_list, headers=["No.", "Topic", "Sub-Topics"], tablefmt="simple_grid"))

# PRINTS TABLE OF SUPERNOVAE
def supernovae(topics):
    print()
    print('B) SUPERNOVAE')
    print(topics)
    print()
supernovae(tabulate(supernovae_list, headers=["No.", "Topic"], tablefmt="simple_grid"))

# PRINTS TABLE OF NEBULAE
def nebulae(topics):
    print()
    print('C) NEBULAE')
    print(topics)
    print()
nebulae(tabulate(nebulae_list, headers=["No.", "Topic"], tablefmt="simple_grid"))
