def main():
    mass = input("m: ")
    print(calculate_energy(mass))

def calculate_energy(mass):
    E = int(mass) *  300000000**2

    return E


if __name__=="__main__":
    main()