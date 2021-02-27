"""
Project name - CST8333ProjectByMuktaDebnath
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
CST8333-351- Assignment 02
Student No.: 040950904

Description: This Script will Open and read a CSV file. The pandas and the pyinputplus module installed within the
Python environment to analysis the data and other requirements.

"""

import pandas as pd
import pyinputplus
from Persistence import dataAccess


def showOneRecord(record):
    """
    This method pass an int type index of a single row that entered by the user
    :param record: Indicate the index of the recorded element.
    :type record: int
    """
    pd_df = pd.DataFrame(dataAccess.records)
    print(pd_df.iloc[[record]])


def showAllRecords():
    """
    This method read the records from the dataset by implementing DaraFrame module and display the saved data
    :return:
    """

    pd_df = pd.DataFrame(dataAccess.records)
    print(pd_df)


def showMultipleRecords(rec_list):
    """
    This function takes a data structure (list) of multiple indexes
    of the stored record, entered by the user, as its parameter
    and outputs specific records of data on screen.

    :param rec_list: Multiple indexes of stored data elements.
    :type rec_list: list
    """

    pd_df = pd.DataFrame(dataAccess.records)
    print(pd_df.iloc[[rec_list]])


def writeToFile(file_name):
    """
    This function uses pandas dataframe and to read records from a
    simple data structure and then writes saved data from memory to
    a new CSV file.
    :param file_name: Course dataset in CSV format.
    :type file_name: str
    """

    pd_df = pd.DataFrame(dataAccess.records)
    pd_df.to_csv(file_name, index=False, header=True)
    print("\n A new CSV file 'new_dataset.csv' is successfully created from the list.")


def delete_record(delete_index):
    """
    This function takes an index of the stored record, entered by
    the user, as its parameter and deletes that specific record
    of data.

    :param delete_index: Index of a stored data element.
    :type delete_index: int
    """

    dataAccess.records.pop(delete_index)


def addRecord(add_row):
    """
    this function will take a record of single row where the user will input all the columns information
    and add to the dataset.
    Append object to the end of the list.

    :param add_row:  Single row of record data
    :type add_row: list
    """

    dataAccess.records.append(add_row)


def updateRecord(update_index):
    """
    This function takes an index of the stored record, entered by
    the user, as its parameter and updates a specific column value
    of a row in the record of data by allowing user to enter new value.

    :param update_index: Index of a stored data element.
    :type update_index: int
    """
    new_value = ""
    pd_df = pd.DataFrame(dataAccess.records)
    print(pd_df.loc[[update_index]])
    response_col = pyinputplus.inputRegex(r'^[0-9]$', prompt="\nInput the column number to update [0 to 9]: ")
    if int(response_col) == 0:
        new_value = pyinputplus.inputNum("Input province id (number): ")
    elif int(response_col) == 1:
        new_value = pyinputplus.inputStr("Input province name in English: ", "N/A")
    elif int(response_col) == 2:
        new_value = pyinputplus.inputStr("Input province name in French: ", "N/A")
    elif int(response_col) == 3:
        new_value = pyinputplus.inputRegex(r'\d{2}/\d{2}/\d{4}', prompt='Input date (MM/DD/YYYY): ')
    elif int(response_col) == 4:
        new_value = pyinputplus.inputNum("Input no. of conf (number): ")
    elif int(response_col) == 5:
        new_value = pyinputplus.inputNum("Input no. of prob (number): ")
    elif int(response_col) == 6:
        new_value = pyinputplus.inputNum("Input no. of deaths (number): ")
    elif int(response_col) == 7:
        new_value = pyinputplus.inputNum("Input no. of total (number): ")
    elif int(response_col) == 8:
        new_value = pyinputplus.inputNum("Input no. of today (number):")
    elif int(response_col) == 9:
        new_value = pyinputplus.inputFloat("Input total rate (number):")

    dataAccess.records[update_index][dataAccess.colNames[int(response_col)]] = new_value
    print("\n'" + dataAccess.colNames[int(response_col)] + "' Column number " + str(update_index) + " has updated:\n")
    pd_df = pd.DataFrame(dataAccess.records)
    print(pd_df.loc[[update_index]])
