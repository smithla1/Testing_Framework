# Team 3 CSCI 362 Project
### Authors: Logan Smith, Brielen Beamon, Scott White

This is an automated testing framework designed to verify the proper function of
the Sugar Labs source code.

Our project is centered around [Sugar Labs](https://en.wikipedia.org/wiki/Sugar_Labs), a free and open source software project
that focuses on allowing people around the world to learn more about the world
around them. Sugar Labs is a spin off of One [Laptop Per Child](http://one.laptop.org), constituting a
simple Linux-based operating system. It is used to give disadvantaged populations
an opportunity to interact with a simple computer system.

Our goals in designing this testing framework was to verify the Sugar Labs source code functioned
correctly. In addition, this testing framework provides a way to verify that recent code changes
caused no unexpected bugs or failures elsewhere in the project.

For more detailed information about this project, please view the project [final report](Team_3_finalReport.pdf)

## Using the Framework
This automated testing framework was designed to be used on a Linux operating system. To use this 
automated testing framework no additional dependencies will be required. Simply download the repository
and navigate to the TestAutomation directory. Then, from within the TestAutomation directory, you may
invoke the automated testing framework with the following command:
```
./scripts/runAllTests.py
```
This script, runAllTests.py, will parse through a folder containing test cases and verify that the software
passes each test case. The results will be aggregated and displayed to the user. Again, for more detailed
information about this project, please view our [final report](Team_3_finalReport.pdf).
