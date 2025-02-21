# virtual environment makes isolated environment to different version of any pip versions
# to create a virtual environment to run any other version of python or panadas version
# first we make folder and open in terminal like Pycharm
# then run the following commands to specify which version you want to run
# python -m venv (folder name)
# (folder name)\Scripts\Activate.ps1 # for powershell
# (folder name)\Scripts\activate for cmd
# pip install pandas==version(e.g. 1.5.0)
# deactivate (for accessing our global version)

# touch main.py # is used to create file directly in file with powershell

# pip freeze # gives all packages install in python virtual installment
# pip freeze > requirement.txt # gives you a text file of all packages same as above but not list this time text file

# pip install -r requirement.txt # gives other programmer direct download all ve package at once


# for checking version directly write py --version

# Set-ExecutionPolicy Unrestricted -Scope Process Please change it for requirement