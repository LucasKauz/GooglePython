#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    print 'Hello there', repeat(sys.argv[1],True)
    
    # Convers\xc3o de tipos
    pi = 3.14
    ##text = 'The value of pi is ' + pi      ## NO, does not work
    text = 'The value of pi is '  + str(pi)  ## yes
    print text


    raw = r'this\t\n and that' # O r a frenta de string indica para o python interpreta-la literalmente
    print raw     ## this\t\n and that

    multi = """It was the best of times.
    It was the worst of times."""

    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """Returns the string s repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s +', '+ s +', '+ s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result

if __name__ == '__main__':
    main()
