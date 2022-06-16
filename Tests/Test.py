# General methods for test files, last edited 6/11/2022
import sys

# Print a line of stars
def stars(endstr="\n"):
    print("*************************", end=endstr)

# Print out seperators for individual tests
def swText(string):
    stars()
    print(string)
    stars("\n\n")

# Print out seperators for test files
def header(string):
    stars("")
    stars("")
    stars()
    print(string)
    stars("")
    stars("")
    stars("\n\n")

# Print the value of either a single item or an entire array
# NOTE: This function ends with a newline
def printValue(value):
    if type(value) == list:
        print("[", end="")
        length = len(value)
        if length == 0:
            print("]")
        for i in range(length):
            print(f"{value[i]}", end="")
            if i < length - 1:
                print(", ", end="")
            else:
                print("]")
    else:
        print(str(value))

# Print out the comparison, works for both arrays and single items
def equalsPrint(provDesc, foundDesc, typeDesc, provided, found):
    print(f"{provDesc} {typeDesc}: ", end="")
    printValue(provided)
    print(f"{foundDesc} {typeDesc}: ", end="")
    printValue(found)

# Determines if the two entries are equivilant
def assertEquals(provDesc, foundDesc, typeDesc, provided, found):
    ok = provided == found
    equalsPrint(provDesc, foundDesc, typeDesc, provided, found)
    print(f"Equal? {'Yes' if ok else 'No'}\n")
    return ok
