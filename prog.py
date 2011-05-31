
# Use appconsole.myprint instead of print and
# input = yield appconsole.output() instead of raw_input()
from appconsole import myprint, printoutput

def prog_gen(namn=""):

    while True:
        myprint("What's your name?")
        name = yield printoutput()
        myprint("Hello "+name+"!")
        myprint()

