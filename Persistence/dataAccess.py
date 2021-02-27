"""
Project name - CST8333ProjectByMuktaDebnath
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
CST8333-351- Assignment 02
Student No.: 040950904

Description: Read, store and reload 100 rows of dataset. Output the recorded data on screen and write
saved data from memory to a new CSV file.
We can run this script individually to see all the data from the dataset as this script deals with
File IO, this resides within the Persistence Layer.
This script requires that 'DictReader' and 'pandas' be installed within the Python
environment this script runs on.
"""

import sys
from csv import DictReader
from Data.datesetPath import DatasetPath
from BusinessLogic import dataService

records = []
colNames = ""
records_dict = []


def read_dataset(file_name):
    """
    This function takes a CSV file as its parameter and creates a
    record object. It opens and reads the CSV dataset. It stores
    100 rows of data into a simple data structure, list.

    :param file_name: Course dataset in CSV format.
    :type file_name: str
    """
    global records
    global colNames
    global records_dict
    try:
        """'r' indicating that the passing file will open as read mode"""
        with open(file_name, 'r') as readFile:
            """ passing the readFile to DictReader() and assigned to dictR """
            dictR = DictReader(readFile)

            """Variable colNames will store the column names"""
            colNames = ""
            colNames = dictR.fieldnames

            """The variable records will store 100 rows in a loop"""
            records = []
            records = [next(dictR) for x in range(100)]

    except FileNotFoundError:
        print("File not found! Check the file name and location.")
        sys.exit()


def print_header():
    """
    This function displays column headers on screen.
    """

    print("\n************************************************************************************")
    print(colNames[0], colNames[1], colNames[2], colNames[3], colNames[4],
          colNames[5], colNames[6], colNames[7], colNames[8], colNames[9])
    print("*************************************************************************************")


def printDataset():
    """
     This function displays the records on the screen.
    """

    for row in records:
        print(row[colNames[0]], row[colNames[1]], row[colNames[2]], row[colNames[3]],
              row[colNames[4]], row[colNames[5]], row[colNames[6]], row[colNames[7]],
              row[colNames[8]], row[colNames[9]])


def printName():
    """
    This function will print my name and student number on the console.
    """

    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%% Student Name: Mukta Debnath, Student No.: 040950904  %%")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


def reload():
    """
    This function reloads 100 rows of data from CSV file into a simple data
    structure, list.
    """

    read_dataset(DatasetPath.covid19_new)
    dataService.showAllRecords()
    print("\nReloaded 100 rows from covid19_new successfully\n")


class DataAccess:
    """
    DataAccess class allows the user to take a CSV file and create a record object, open and read the CSV dataset.
    It stores 100 rows of data, print in console, reloads, and writes saved data from memory to aCSV file.
        records (list): The list to store data from CSV dataset.
        colNames (list): The list to store names of the columns of dataset.
        records_dict (list): The dictionary to store data from CSV dataset.
    """

    records = []
    colNames = []
    records_dict = []

    if __name__ == "__main__":
        read_dataset(DatasetPath.covid19_new)
        print_header()
        printDataset()
        printName()
