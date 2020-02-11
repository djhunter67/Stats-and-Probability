#!/usr/bin/env python3.7
'''
Christerpher Hunter
2020 FEB 08
EEE 350 HW 02

'''
# Importing a seperate script I made that has to be in the same directory as this script
# or this script will not work
#
import simulation_station

# The P[E] error of each individual bit is wrong
#
error = 0.01

# The number of bits per data packet
#
# @bits = input("Enter the number of bits per packet: ")
bits = 100

# The 'X' number of packets that contrain 100 bits each
#
#BasePackets = input("Enter the number of data packets: ")
BasePackets = 10_000

# The iteration of the remaining 100 bits
#
I = [0, 1, 2, 3]

# The difference percentage array
#
diff_err = [0, 1, 2, 3, 4]

# The Probability of that number of wrong bits, or errors
#
P = [0, 1, 2, 3]

# The number of packets with zero errors
#
P[0] = simulation_station.ErrProb((int(bits)-I[0]), I[0], error)
print("\nThe probability that the " + str(bits) +
      " bits per packet have zero errors is", round(P[0], 3))

# The number of packets one with error
#
P[1] = simulation_station.ErrProb((int(bits)-I[1]), I[1], error)
print("\nThe probability that the " + str(bits) +
      " bits per packet have one error is", round(P[1], 3))

# The number of packets with two errors
#
P[2] = simulation_station.ErrProb((int(bits) - I[2]), I[2], error)
print("\nThe probability that the " + str(bits) +
      " bits per packet have two errors is", round(P[2], 3))

# The number of packets with three errors
#
P[3] = simulation_station.ErrProb((int(bits) - I[3]), I[3], error)
print("\nThe probability that the " + str(bits) +
      " bits per packet have three errors is", round(P[3], 3))

# The proabability of a packet being decoded correctly
#
PC = P[0] + P[1] + P[2] + P[3]
print("\nThe probability that a packet is correctly decoded is", PC)

# The number of those 10,000 packets that have zero errors in their 100 bits
#
ZeroError = simulation_station.packets(int(BasePackets), P[0])
print("\nThe number of the " + str(BasePackets) + " packets that have " +
      str(I[0]) + " errors in their " + str(bits) + " bits is", ZeroError)

# The number of those 10,000 packets that have one error in their 100 bits
#
OneError = simulation_station.packets(int(BasePackets), P[1])
print("\nThe number of the " + str(BasePackets) + " packets that have " +
      str(I[1]) + " error in their " + str(bits) + " bits is", OneError)

# The number of those 10,000 packets that have two errors in their 100 bits
#
TwoError = simulation_station.packets(int(BasePackets), P[2])
print("\nThe number of the " + str(BasePackets) + " packets that have " +
      str(I[2]) + " errors in their " + str(bits) + " bits is", TwoError)

# The number of those 10,000 packets that have three errors in their 100 bits
#
ThreeError = simulation_station.packets(int(BasePackets), P[3])
print("\nThe number of the " + str(BasePackets) + " packets that have " +
      str(I[3]) + " errors in their " + str(bits) + " bits is", ThreeError)

# The number of packets that were correctly decoded
#
Correctly_coded = simulation_station.packets(int(BasePackets), PC)
print("\nThe number of the " + str(BasePackets) +
      " packets that have been decoded correctly is", Correctly_coded)

# Dictionary used to store and present the theoretical and simulation probabilites
#
theoretical_value = {
    "0-theo": P[0],
    "1-theo": P[1],
    "2-theo": P[2],
    "3-theo": P[3],
    "corr-theo": PC
}

simulated_value = {
    "0-sim": round((ZeroError/float(BasePackets)), 4),
    "1-sim": round((OneError/float(BasePackets)), 4),
    "2-sim": round((TwoError/float(BasePackets)), 4),
    "3-sim": round((ThreeError/float(BasePackets)), 4),
    "corr-sim": round((Correctly_coded/float(BasePackets)), 4)
}

# The percentage difference between the theoretical and simulated values
#
diff_err[0] = simulation_station.percent_compare(
    theoretical_value["0-theo"], simulated_value["0-sim"])
print("\nThe percent difference between the theoretical " +
      str(round(P[0], 4)) + " and simulated " + str(simulated_value["0-sim"]) + " error: ", diff_err[0], "%")

diff_err[1] = simulation_station.percent_compare(
    theoretical_value["1-theo"], simulated_value["1-sim"])
print("\nThe percent difference between the theoretical " +
      str(round(P[1], 4)) + " and simulated " + str(simulated_value["1-sim"]) + " error: ", diff_err[1], "%")

diff_err[2] = simulation_station.percent_compare(
    theoretical_value["2-theo"], simulated_value["2-sim"])
print("\nThe percent difference between the theoretical " +
      str(round(P[2], 4)) + " and simulated " + str(simulated_value["2-sim"]) + " error: ", diff_err[2], "%")

diff_err[3] = simulation_station.percent_compare(
    theoretical_value["3-theo"], simulated_value["3-sim"])
print("\nThe percent difference between the theoretical " +
      str(round(P[3], 4)) + " and simulated " + str(simulated_value["3-sim"]) + " error: ", diff_err[3], "%")

diff_err[4] = simulation_station.percent_compare(
    theoretical_value["corr-theo"], simulated_value["corr-sim"])
print("\nThe percent difference between the theoretical " + str(round(PC, 4)) +
      " and simulated " + str(simulated_value["corr-sim"]) + " error: ", diff_err[4], "%")

''' END OF FILE '''
