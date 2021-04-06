"""
Project name - Oracle 12c Database Connectivity
Programming Language Research Project
CST8333-351- Assignment 03
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
Student No.: 040950904

Description: This Script will Open and read a CSV file. The pandas and the pyinputplus module installed within the
Python environment to analysis the data and other requirements.

"""

import pandas as pd
from BusinessLogic import oracleDBconnector
pd.set_option('display.max_columns', None)

df_ora = []
new_record = []


def showOneRecord(selected_index):
    """
    This method pass an int type index of a single row in DB that entered by the user to see
    :param selected_index: Indicate the index of the record in DB.
    :type selected_index: int
    """

    oracleDBconnector.read_one_record_from_oracle(selected_index)


def showAllRecords():
    """
    This method read the records from the DB by implementing DaraFrame module and display the saved data
    """
    oracleDBconnector.read_all_records_from_oracle()
    sort_df = oracleDBconnector.df_ora.sort_values(by=['index'])
    print(sort_df.to_string(index=False))


def showMultipleRecords(rec_list):
    """
    This function takes a data structure (list) of multiple indexes
    of the stored record, entered by the user, as its parameter
    and outputs specific records of data on screen.
    :param rec_list: Multiple indexes of stored data elements.
    :type rec_list: list
    """
    oracleDBconnector.read_all_records_from_oracle()
    sort_df = oracleDBconnector.df_ora.sort_values(by=['index'])
    format_df = sort_df.iloc[rec_list, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    print(format_df.to_string(index=False))
    rec_list.clear()


def writeToFile(file_name):
    """
    This function uses pandas dataframe and to read records from a
    simple data structure and then writes saved data from memory to
    a new CSV file.
    :param file_name: Course dataset in CSV format.
    :type file_name: str
    """
    oracleDBconnector.read_all_records_from_oracle()
    df_to_csv = pd.DataFrame(oracleDBconnector.df_ora)
    df_to_csv.to_csv(file_name, index=False, header=True)
    print("\n A new CSV file 'new_dataset.csv' is successfully created from the records stored in Oracle DB.")


def delete_record(delete_index):
    """
    This function takes an index of the stored record, entered by
    the user, as its parameter and deletes that specific record
    of data from the DB.
    :param delete_index: Index of a stored data element.
    :type delete_index: int
    """
    oracleDBconnector.delete_from_oracle(delete_index)


def addRecord(add_row):
    """
    this function will take a record of single row where the user will input all the columns information
    and add to the dataset in the DB.
    Append object to the end of the list.
    :param add_row:  Single row of record data1
    :type add_row: list
    """
    oracleDBconnector.add_a_record_to_oracle(add_row)


def updateRecord(id_u, pn_u, pnFR_u, dt_u, conf_u, prof_u, dth_u, total_u, today_u, rate_u, u_index):
    """
    This function update a record from the Database table based on the provided index number entered by
    the user.
    """
    oracleDBconnector.update_a_record_to_oracle(id_u, pn_u, pnFR_u, dt_u, conf_u, prof_u, dth_u, total_u, today_u,
                                                rate_u, u_index)
