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

def assertEquals(provDesc, foundDesc, typeDesc, provided, found):
    ok = provided == found
    print(f"{provDesc} {typeDesc}: {provided}\n{foundDesc} {typeDesc}: {found}\n" +
          f"Equal? {'Yes' if ok else 'No'}\n")
    return ok
