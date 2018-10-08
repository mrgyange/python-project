# filename      : Matamorosa_e1.py
# author        : Marge Angela P. Matamorosa
# description :  This is a python program that prints
#                    the contents of a dictionary in a specific format


message = "I am {}.\n" + "My spirit animal is {},\n" + \
            "because {}.\n" + \
            "When not in school, I love to {}.\n" + \
            "I dream of being a/an {} in the future."




data = {"Name" : "Marge Angela Pilapil Matamorosa",
        "spirit_animal" : "Dog", 
        "reason" : "dogs shows service and loyalty generously to others", 
        "hobby" : "sleep", 
        "profession" : "Psychologist"}

print(message.format(data["Name"], data["spirit_animal"], data["reason"], data["hobby"], data["profession"]))