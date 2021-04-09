"""
Project name - Search records based on multiple columns at same time
Programming Language Research Project
CST8333-351- Assignment 04
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
Student No.: 040950904

Description: This is the starting point of the project where my code will execute. In this script I imported my
persistence and presentation classes to execute and print in the console for user use.

"""
from datetime import datetime
from Presentation.menu import validate_response
from Persistence.dataAccess import *
from Data.datesetPath import *


def main():
    """
    this function loads the datafile first time in a list and call other functions from different layers
    to display all the user input.
    :return:
    """
    today = datetime.now()
    print("\n>>>>>>>> The last execution on: ", today, "<<<<<<<<")
    read_dataset(DatasetPath.covid19canada)
    validate_response()


if __name__ == '__main__':
    main()
