MERCURY_GRAVITY = 0.376
VANUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATRUN_GRAVITY = 1.081
URVERS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
ERTH_GRAVITY = 1.0

def main():
    erth_wight = float(input("Enter your weight on Earth: "))
    planet = input("Enter the planet you want to know your weight on : ")
    planet = planet.capitalize()

    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VANUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATRUN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URVERS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY

    planet_weight = erth_wight * gravity_constant
    round_weight = round(planet_weight, 2)

    print("The equivalent weight on " + planet + ":"+ ":" + str(round_weight) )

if __name__ == "__main__":
    main()

        