#!/usr/bin/env python

"""
    This python file will run an individual test case.
    
    It requires a path to the file to be tested (from the project parent
    directory), a function to test, and arguments to be tested.
    
"""

import imp
import os
import re
import sys

def runTestCase( testCaseInfo ):
    
    # This will result in a filepath that will allow transversal from
    # the current directory to the directory containing the needed file
    filepath = "../../" + testCaseInfo[0]
    
    # This will create a path to the directory containing the needed files
    directorypath = re.sub(r"/[a-zA-Z_]*.py", "/", filepath)
    
    # Gather the full path name of the directory containing the needed
    # files and add them to sys.path
    # This is done to make sure that the imports needed by the desired
    # python file will be accessible.
    os.chdir(directorypath)
    sys.path.insert(0, os.getcwd())
    
    # Gather the name of the needed python file
    filename = testCaseInfo[0].split("/")[-1]
    
    # Import the needed python file
    foo = imp.load_source("test", filename)

    # Prepare to call the function by stripping its parenthesis and arguments
    funcName = re.sub(r"\([\d\D]*\)", "", testCaseInfo[1])
    
    # Prepare the arguments for using
    arguments = testCaseInfo[2].split(", ")
    try:
        arguments = [eval(i) for i in arguments]
    except ValueError:
        pass
    
    # Call the function with the arguments
    result = getattr(foo, funcName)(*arguments)
    
    return result
