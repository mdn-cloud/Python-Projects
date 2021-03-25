"""
Project name - Oracle 12c Database Connectivity
Programming Language Research Project
CST8333-351- Assignment 03
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
Student No.: 040950904

Description: Read, store and reload the entire covid19-modified dataset. Output the
recorded data on screen and write saved data from memory to a new CSV file.
It also stores 4632 rows of data into a simple data structure, list. It then loads
all 34458 records of data to Oracle Database table. It displays to the console all
4632 records from Oracle database. It also reloads records to the Oracle database
and writes to a new CSV file from database table.
"""

import sys
from csv import DictReader

import BusinessLogic.oracleDBconnector
from Data.datesetPath import DatasetPath

records = []
col_names = ""
records_dict = []


def read_dataset(file_name):
    """
    This function takes a CSV file as its parameter and creates a
    record object. It opens and reads the CSV dataset. It stores
    all the records to the Oracle Database into a simple data structure and in a list.

    :param file_name: Course dataset in CSV format.
    :type file_name: str
    """
    global records
    global col_names
    global records_dict
    try:
        """'r' indicating that the passing file will open as read mode"""
        with open(file_name, 'r') as read_file:
            """ passing the readFile to DictReader() and assigned to dictR """
            dictR = DictReader(read_file)

            """Variable colNames will store the column names"""
            col_names = ""
            col_names = dictR.fieldnames

            """The variable will store 4632 record of the dataset"""
            records = []
            records = [next(dictR) for x in range(4632)]

    except FileNotFoundError:
        print("File not found! Please check the file name and location.")
        sys.exit()


def print_header():
    """
    This function displays column headers.
    """

    print("\n************************************************************************************")
    print(col_names[0], col_names[1], col_names[2], col_names[3], col_names[4], col_names[5], col_names[6],
          col_names[7], col_names[8], col_names[9])
    print("*************************************************************************************")


def printDataset():
    """
     This function displays the records.
    """

    for row in records:
        print(row[col_names[0]], row[col_names[1]], row[col_names[2]], row[col_names[3]],
              row[col_names[4]], row[col_names[5]], row[col_names[6]], row[col_names[7]],
              row[col_names[8]], row[col_names[9]])


def printName():
    """
    This function will print my name and student number on the console.
    """

    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%% Student Name: Mukta Debnath, Student No.: 040950904  %%")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


def reload():
    """
    This function reloads 4632 rows of data from CSV file into the Oracle DB table.
    """
    print("It will take 6-10 seconds to load whole dataset to oracle DB. Loading......")
    BusinessLogic.oracleDBconnector.insert_to_oracle()
    print("\nReloaded 4632 records to oracle DB from covid19-Modified.csv dataset.\n")


class DataAccess:
    """
    DataAccess class allows the user to take a CSV file and create a record object, open
    and read the CSV dataset. It stores 4632 rows of data to Oracle DB, print in console,
    reloads, and writes saved data from Oracle DB.

    records (list): The list to store data from CSV dataset.
    col_names (list): The list to store names of the columns of dataset.
    records_dict (list): The dictionary to store data from CSV dataset.
    """

    records = []
    col_names = []
    records_dict = []

    if __name__ == "__main__":
        read_dataset(DatasetPath.covid19canada)
        print_header()
        printDataset()
        printName()
