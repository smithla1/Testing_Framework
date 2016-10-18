#!/usr/bin/env python

"""
    This python script will run all the test cases associated with this
    project.
    
    To do so, it will adhere to the following steps:
    1.  Look in the child directory of the residing directory's parent 
        directory (../testCases).
    2.  The script will then parse the each test case (using the helper
        script 'testCaseParser.py'), determining the inputs to use and
        the expected outcome.
    3.  The results of each individual test case will be stored in the
        directory '../temp'. This directory will be cleared of any 
        contents before the test cases are run.
    4.  The results in '../temp' will be compiled into a html file,
        'testReport.html'. 
    
"""

import subprocess
import os
import imp
import progressBar
import runTestCase
import testCaseParser

# Preserve current directory
starting_path = os.getcwd()

# Navigate to directory containing test cases
os.chdir("../testCases")

# Gather the name of each test case into a list
#   Gather a string containing filenames with ls
#   Split the string on newline characters
#   Remove the extraneous last element in the resulting list ('')
testCaseNames = subprocess.check_output(['ls']).split('\n')[:-1]

# Create the testReport that will be further modified to create a final document
# detailing the results of each test case
reportGeneration = (
    "<!DOCTYPE html>                        "
    "    <html>                             "
    "    <head>                             "
    "    <style>                            "
    "    table {                            "
    "        font-family: arial, sans-serif;"
    "        border-collapse: collapse;     "
    "        width: 100%;                   "
    "    }                                  "
    "    td, th {                           "
    "        border: 1px solid #dddddd;     "
    "        text-align: left;              "
    "        padding: 8px;                  "
    "    }                                  "
    "    tr:nth-child(even) {               "
    "        background-color: #dddddd;     "
    "    }                                  "
    "    </style>                           "
    "    </head>                            "
    "    <body>                             "
    "    <table>                            "
    "    <caption>Testing Results</caption> "
    "       <tr>                            "
    "           <th>Test Case ID</th>       "
    "           <th>Tested Method</th>      "
    "           <th>Input</th>              "
    "           <th>Expected Output</th>    "
    "           <th>Actual Outcome</th>     "
    "           <th>Pass/Fail</th>          "
    )

# Initialize progress bar
progress_interval = 0.0
progressBar.update_progress(progress_interval)
progress_interval += 1.0

# Parse, execute, and document the result of each test case
for test in testCaseNames:
    # The runTestCase script will move to some directory. After running it, we
    # need to backtrack to the current directory (the one containing the test
    # cases) so runAllTests can continue running each script
    current_path = os.getcwd()
    
    # Gather the necessary information for the test case
    testCaseRequirements = testCaseParser.parseTestCase(test)
    
    # Run the test case and get the results with the provided input
    testCaseResult = runTestCase.runTestCase(testCaseRequirements[1:4])
    
    # Create a string containing the pertinent information
    link = ('<a href="file://{0}/testCase{1}.txt" target="_blank"'
                '>{1}</a>')
    test_passed = '<font color = "Green">Pass</font>'
    test_failed = '<font color = "Red">Fail</font>'
    
    current_result = ("<tr><td>"
        + str(link.format(current_path, testCaseRequirements[0])) + "</td><td>"
        + str(testCaseRequirements[2]) + "</td><td>"
        + str(testCaseRequirements[3]) + "</td><td>"
        + str(testCaseRequirements[4]) + "</td><td>"
        + str(testCaseResult) + "</td><td>"
        + (test_failed, test_passed)[eval(testCaseRequirements[4])==eval(str(testCaseResult))]
        + "</td></tr>")
    
    # Append the newly created string to the html file
    reportGeneration = reportGeneration + current_result
    
    # Return to the directory containing the testCases
    os.chdir(current_path)
    
    #Update progress bar
    progressBar.update_progress(progress_interval/len(testCaseNames))
    progress_interval += 1.0

# Return to starting path to simplify navigation to reports directory
os.chdir(starting_path)
os.chdir("../reports") 

# Finalize, write, and close resources for the testReport
reportGeneration = reportGeneration + "</table></body></html>"
output_file = open("testReport.html", "w")
output_file.write(reportGeneration)
output_file.close()

# Open the newly created file
subprocess.check_output(['xdg-open', 'testReport.html'])
