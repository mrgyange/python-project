# filename      : Matamorosa_e2.py
# author        : Marge Angela P. Matamorosa
# description :  This is a python program that prints
#                the classifies a tropical cyclone
#                with respect to its sustained winds

import sys

# Read input from CLI
sustained_winds = sys.argv[1]

# Converts str sustained_winds to float
sustained_winds = float(sustained_winds)

# Compare sustained winds to preset range & Displays proper classification
if (sustained_winds >= 220.0) :
    print ("Super Typhoon")

elif(sustained_winds >= 118.0) :
    print ("Typhoon")

elif(sustained_winds >= 89.0) :
    print ("Severe Tropical Storm")

elif(sustained_winds >= 62.0) :
    print ("Tropical Storm")

else:
    print ("Tropical Depression")