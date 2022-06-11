# General methods for test files, last edited 6/8/2022
import sys
def stars():
    print("*************************")

def starsln():
    stars()
    print("")

def swText(string):
    stars()
    print(string)
    starsln()

def equalsPrint(provDesc, foundDesc, typeDesc, provided, found):
    print(f"{provDesc} {typeDesc}: {str(provided)}\n{foundDesc} {typeDesc}: {str(found)}")

def assertEquals(provDesc, foundDesc, typeDesc, provided, found):
    ok = provided == found
    equalsPrint(provDesc, foundDesc, typeDesc, provided, found)
    print(f"Equal? {'Yes' if ok else 'No'}\n")
    return ok
