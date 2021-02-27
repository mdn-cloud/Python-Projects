"""
Project name - CST8333ProjectByMuktaDebnath
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
CST8333-351- Assignment 02
Student No.: 040950904


Description: This script allows the user to interact with the program and
displays console-based menu and accepts user input i.e. business or persistence
to perform requested tasks depending on the user input. This script needed to
install and import 'pyinputplus' to run the script.

The sys import allows to use the sys.exit command to quit/logout
of the application.
"""

import sys
from collections import namedtuple
import pandas as pd
import pyinputplus
from BusinessLogic import dataService
from Data.datesetPath import DatasetPath
from Persistence import dataAccess


res_list = []
response = ""


def validate_response():
    """
    This function displays menu on screen and accepts user input by checking validation.

    """
    global response
    menu = Menu()
    menu.print_menu()
    response = pyinputplus.inputNum("\nSelect Option: ", '>', min=1, lessThan=10)
    handle_response(response)


def data_not_loaded(user_resp):
    """

    This function alerts user that CSV dataset is to be loaded before performing
    any of the console-based menu operations. This function triggers when
    AttributeError arises.
    @param user_resp: User input for a menu item.
    @type user_resp: int

    """
    print("\n Load data before accessing other menu items. Press 1 to continue...\n")
    validate_response()


def handle_response(user_response):
    """
    this function takes the input and assists user to select the layer (persistence or business) depending on the
    user input
    :param user_response:
    :type user_response: int
    """
    try:
        if user_response == 1:
            dataAccess.reload()
            validate_response()

        elif user_response == 2 and len(dataAccess.records) != 0:
            dataService.writeToFile(DatasetPath.new_dataset)
            validate_response()

        elif user_response == 3 and len(dataAccess.records) != 0:
            response_one = pyinputplus.inputNum(
                "\nEnter one index number to view [0 to " + str(len(dataAccess.records) - 1) + "]: ",
                '>', min=0, lessThan=len(dataAccess.records))
            print("\nHere is the record with index number " + str(response_one) + "\n")
            dataService.showOneRecord(response_one)
            validate_response()

        elif user_response == 4 and len(dataAccess.records) != 0:
            response_total = pyinputplus.inputNum("How many records you want to print? [1 to " +
                                                  str(len(dataAccess.records)) + "]: ", '>', min=1,
                                                  lessThan=(len(dataAccess.records) + 1))
            print("\nChoose the index numbers of row to print.")
            for i in range(response_total):
                response_multi = pyinputplus.inputNum("No. " + str(i + 1) + " row [0 to " +
                                                      str(len(dataAccess.records) - 1) + "]: ", '>', min=0,
                                                      lessThan=len(dataAccess.records))
                res_list.append(response_multi)

            print("\nYour selected  " + str(response_total) + " records are: \n")

            for i in res_list:
                dataService.showMultipleRecords(i)

            res_list.clear()

            validate_response()

        elif user_response == 5 and len(dataAccess.records) != 0:
            dataService.showAllRecords()
            validate_response()

        elif user_response == 6 and len(dataAccess.records) != 0:
            prid = pyinputplus.inputNum("Province id (number): ")
            pname_en = pyinputplus.inputStr("Province name in English: ", "N/A")
            pname_fr = pyinputplus.inputStr("Province name in French: ", "N/A")
            idate = pyinputplus.inputRegex(r'\d{2}/\d{2}/\d{4}', prompt='Date (MM/DD/YYYY): ')
            inumconf = pyinputplus.inputNum("Number of conf (number): ")
            inumprob = pyinputplus.inputNum("Number of prob (number): ")
            deaths = pyinputplus.inputNum("Number of deaths (number): ")
            inumtotal = pyinputplus.inputNum("Number of total (number): ")
            inumtoday = pyinputplus.inputNum("Number of today (number): ")
            iratetotal = pyinputplus.inputFloat("Total rate (number): ")
            new_record = {'pruid': prid, 'prname': pname_en, 'prnameFR': pname_fr, 'date': idate, 'numconf': inumconf,
                          'numprob': inumprob, 'numdeaths': deaths, 'numtotal': inumtotal, 'numtoday': inumtoday,
                          'ratetotal': iratetotal}
            dataService.addRecord(new_record)
            new_record_index = (len(dataAccess.records) - 1)
            print("\nThe new record has been created below:")
            print(dataAccess.records[new_record_index])
            pd_df = pd.DataFrame(dataAccess.records)
            print(pd_df.loc[[new_record_index]])
            validate_response()

        elif user_response == 7 and len(dataAccess.records) != 0:
            response_update = pyinputplus.inputNum("\nGive the index of the record to update [0 to "
                                                   + str(len(dataAccess.records) - 1) + "]: ", '>', min=0,
                                                   lessThan=len(dataAccess.records))
            print("\nThis is the record with index of " + str(response_update) + "\n")
            dataService.updateRecord(response_update)
            validate_response()

        elif user_response == 8 and len(dataAccess.records) != 0:
            response_del = pyinputplus.inputNum("\nGive the index of the record to delete [0 to  "
                                                + str(len(dataAccess.records) - 1) + "]: ", '>', min=0,
                                                lessThan=len(dataAccess.records))
            print("\nThe deleted record is:\n")
            pd_df = pd.DataFrame(dataAccess.records)
            print(pd_df.loc[[response_del]])
            dataService.delete_record(response_del)
            print("\nThe index number " + str(response_del) + " has deleted.\n")
            validate_response()

        elif user_response == 9:
            print("exit")
            sys.exit()

    except AttributeError:
        data_not_loaded(user_response)


class Menu:
    """
    This class allows the user to interact with the program. It displays menu system and accepts user inputs after
    validation and redirects user to the business or persistence layer to perform requested tasks based on user input.
    """

    response = 0

    Option = namedtuple('Option', 'label')
    _separator = "~" * 45
    _options = {1: Option("Reload 100 records"), 2: Option("Create a new file and save records to the file"),
                3: Option("Print one record"), 4: Option("Print multiple records"),
                5: Option("Print all saved records"), 6: Option("Create a new record"),
                7: Option("Update a record from the file"), 8: Option("Delete a record from the file"),
                9: Option("Exit")}

    def print_header(self):
        """
        This method will print student info and and the options that user can see and select them from the list
        @param self: The instance of the class.
        """
        dataAccess.printName()
        print("\n Please Select Option from the list below: \n{0}".format(self._separator))

    def print_menu(self):
        """

        This method outputs main menu on display with 9 options
        for the user to select from.
        @param self: The instance of the class.
        """

        self.print_header()
        for option in sorted(self._options.keys()):
            print("{0} {1}".format(option, self._options[option].label))
