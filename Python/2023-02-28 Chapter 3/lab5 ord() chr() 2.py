print("Evan Peres")
print("2/27/23")

print("")

v=input("what is the voltage in volts? ")
c=input("what is the current in milliAmps? ")
r=int(int(v)*1000/int(c))

print("")

print("V / I = R")
print(str(v) + "V / " + str(c) + "mA = " + str(r) + chr(937))
print("A circuit with a voltage of " + str(v) + "V and a current of " + str(c) + "mA will require a resistor of " + str(r) + chr(937))