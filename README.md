Princeton Algorithms and Data Structures Course Assignments 
==================================================================
Description
-----------
This is my repository of solutions to the assignments of the Coursera 
Princeton Algorithms and Data Structures Course, the link to which
can be found [here](https://www.coursera.org/learn/algorithms-part1).
Within here is also my custom dynamic test suite generator written for another 
solution repo I have. If you want to use it, see installations instructions below:


Installation
------------
1. Clone the repo!

2. Navigate to the generated directory and within your terminal, run:

    `python3 -m venv env`
    
    if you haven't installed python virtual environments before, look up just that, then run:
    
    `pip install virtualenv`
    
    If you haven't installed pip, its a package manager for Python, so look it up and install :)
3. run:

    `source env/bin/activate`
    
    to activate your virtual environment. You should see a `(env)` in front of your terminal
    prompt now.
    
4. run:
    
    `pip install -r dependencies.txt`
    
    to install the dependencies for the test environment. 
    
5. Specify the source/root directory in your IDE. This is super important as Python needs a
    root directory so that it can import things correctly. 
    
    I use PyCharm Community Edition (I highly suggest you do the
    same for Python development) so to specify the source I go to Preferences -> Project -> 
    Project Structure and right click the top level of this git repo and check "Sources". The
    top level directory should now be blue or some such color depending on your IDE theme. 
    
6. Specify your SDK. This synchronizes your IDE with the virtual environment we created in step 3.
    
    in Pycharm, simply go to Preferences -> Project -> Project Interpreter and in the python interpreter
    dropdown select the Python source that lies in your virtual env directory. Mine is in 
    env/bin/python.
    
5. You're all set! :)