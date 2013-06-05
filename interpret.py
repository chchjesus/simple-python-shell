"""
Created on 12/12/2012

:author: Cody Harrington

This is a small Python interpreter that runs its own functions as commands.

To add a command, simply add a function and give it a docstring formatted
for Sphinx documentation, and a description of the syntax.
It should then be picked up.

Also, functions with two underscores preceding are special functions for the
interpreter, i.e. __executeCmd()

Python's code module could potentially be helpful here.
http://docs.python.org/2/library/code.html
"""
import types

# Uses a global dictionary as a token lookup table to fetch the references
# to the functions by using the string names they're stored under. This is
# very similar to how the Python interpreter works.
commands_ = {}

def commands(*args):
    """
    Syntax: commands
            commands cmd
            commands cmd0 cmd1 cmd2 ... cmdn
    
    Prints help on a particular command cmd. Multiple cmds can be given,
    separated by a space, and each of them will be printed.
    If cmd is not given, then all commands are printed.
    
    :param *args:
        The list of commands to print help for
    """
    # If no command is specified, print all of the available commands
    if len(args) <= 0:
        # Sets the list of commands which will be printed to every command
        args = commands_.keys()
    for cmd in args:
        if cmd in commands_.keys():
            print commands_[cmd].__name__
            print commands_[cmd].__doc__
        else:
            print("Command '{0}' does not exist.".format(cmd))
        
def leave():
    """
    Exits the interpreter.
    """
    raise KeyboardInterrupt

def __parseUserInput(userInput):
    """
    Parses the user input string and generates tokens from it for the command
    mapping
    
    :param userInput:
        The string with which to generate the tokens from
    :returns (token, args):
        A command token and arguments to be passed to the command function
    """
    tokenList = userInput.strip().split(' ')
    # Return the command token and any extra arguments
    return tokenList[0], tokenList[1:]
    
def __populateCommands():
    """
    Scans the global tokens dictionary returned from globals() and gets all 
    functions, storing them in the global commands dictionary.
    """
    globals_ = globals()

    for key in globals_.keys():
        # Copies the references to the actual functions into our global
        # commands dictionary which is acting as the token lookup table 
        if isinstance(globals_[key], types.FunctionType) and "__" not in key:
            # If the command fits the requirement, add it to the list
            commands_[key] = globals_[key]

def __main():
    """ Program entry point """
    # Fill the global token mapping dictionary with available commands_ based
    # on functions with an underscore at the end of their names.
    __populateCommands()
    
    try:
        while True:
            # Response needs to be cleared regularly
            response = ""
            userInput = ""
            # This is the main interpreter loop
            while userInput == "":
                userInput = raw_input("Enter command: ")   
            (token, args) = __parseUserInput(userInput)
            if token in commands_.keys():
                cmd = commands_[token]
                # If *args is empty, nothing is passed to cmd(*args)
                # Run the command and get the response 
                response = cmd(*args)
            else:
                print "Command '{0}' does not exist.".format(token)
            # Only print something, if there is something sensible to print
            if response not in ["", None]:
                print response
    finally:
        # Exit after any exception
        exit()

if __name__ == '__main__':
    __main()
