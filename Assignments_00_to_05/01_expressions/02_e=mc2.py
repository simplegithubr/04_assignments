
C: int = 299792458
def main():
    mass_in_kg : float = float(input("Enter kills of mass: "))

     # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_of_joules : float = mass_in_kg * (C**2)
    # Display work to the user
    print(" e = m * c^2")
    print(" m = " + str(mass_in_kg) + " kg ")
    print(" c = " + str(C) + " m/s ")
    print(str(energy_of_joules) + " joules_of_energy! ")

if __name__ == "__main__":
    main()

