#!/usr/bin/env python

"""
    This python file is a helper script for the script runAllTest.py.
    This python file will parse a test case and return all the neccessary
    information to execute the test case.
    
    Args: filename: A name of a file to test
    Output: returnList: A list containing: the test ID number, the path to the
        file of concern, the the method to test, test inputs, and the expected
        output.
"""

from myExceptions import ImproperTestCaseSpecificationError

def parseTestCase( filename ):

    try:
        testCase = open(filename, 'r')
        
        returnList = []
        
        # Parse the testCase text file. Certain keywords will result in this
        # file collecting the following information: Test ID, filepath, the
        # method in the file to be tested, the inputs, and the expected
        # outcome(s). 
        #
        # It is important to note the current limitations. 
        # Any deviation from the keywords in the following conditional statements
        # will cause errors no all the necessary elements will be collected.
        # It is assumed that the elements being collected here will be passed
        # to the calling method. 
        # It is assumed that the filepath will be the path to the file from
        # the parent directory of this project.
        for line in testCase:
            if "Test Case ID: " in line:
                IDnumber = line.replace("\n", "").split("ID: ")[1]
                returnList.append(IDnumber)
            elif "Path to file: " in line:
                filepath = line.replace("\n", "").split("file: ")[1]
                returnList.append(filepath)
            elif "Method being tested: " in line:
                methodName = line.replace("\n", "").split("tested: ")[1]
                returnList.append(methodName)
            elif "arguments: " in line:
                inputs = line.replace("\n", "").split("arguments: ")[1]
                returnList.append(inputs)
            elif "outcome(s): " in line:
                outcomes = line.replace("\n", "").split("outcome(s): ")[1]
                returnList.append(outcomes)
        
        if len(returnList) != 5:
            raise ImproperTestCaseSpecificationError("Test case did not follow specification standards.")
        
        testCase.close()
        
        return returnList
    
    except Exception:
        raise ImproperTestCaseSpecificationError("Test case did not follow specification standards.")
    
    finally:
        testCase.close()
