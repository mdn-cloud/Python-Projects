"""
Project name - Oracle 12c Database Connectivity
Programming Language Research Project
CST8333-351- Assignment 03
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
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
import pyinputplus
from BusinessLogic import dataService, oracleDBconnector
from Data.datesetPath import DatasetPath
from Persistence import dataAccess

res_list = []
response = ""


def validate_response():
    """
    This function displays menu on the screen and accepts user input by checking proper validations.

    """
    global response
    menu = Menu()
    menu.print_menu()
    response = pyinputplus.inputNum("\nPlease select Options from the list: ", '>', min=1, lessThan=10)
    handle_response(response)


def data_not_loaded(user_resp):
    """

    This function alerts user that CSV dataset is to be loaded before performing
    any of the console-based menu operations. This function triggers when
    AttributeError arises.
    @param user_resp: User input for a menu item.
    @type user_resp: int

    """
    print("\n Please load data before accessing other menu items. Press 1 to continue.....\n")
    validate_response()


def handle_response(user_response):
    """
    This function takes the user input and assists user to select the layer (persistence or business) depending on the
    user input
    :param user_response:
    :type user_response: int
    """

    try:
        if user_response == 1:
            dataAccess.reload()
            validate_response()
        # elif user_response == 2 and oracleDBconnector.count_records_number_from_oracle() > 0:
        elif user_response == 2:
            dataService.writeToFile(DatasetPath.new_dataset)
            validate_response()
        # elif user_response == 3 and oracleDBconnector.count_records_number_from_oracle() > 0:
        elif user_response == 3:
            one_res = pyinputplus.inputNum(
                "\nEnter the index number to view [0 to " + str(oracleDBconnector.count_records_number_from_oracle()-1)
                + "]: ", '>', min=0, lessThan=int(int(oracleDBconnector.count_records_number_from_oracle())))
            print("\nHere is the record with index number " + str(one_res) + "\n")
            dataService.showOneRecord(one_res)
            validate_response()

        elif user_response == 4 and oracleDBconnector.count_records_number_from_oracle() > 0:
            total_res = pyinputplus.inputNum("How many records you want to print? [1 to " + str(
                oracleDBconnector.count_records_number_from_oracle()) + "]: ", '>', min=1, lessThan=(
                    oracleDBconnector.count_records_number_from_oracle() + 1))
            print("\nChoose the index numbers of row to print.")
            for i in range(total_res):
                response_multi = pyinputplus.inputNum("No. " + str(i + 1) + " row [0 to " + str(
                    oracleDBconnector.count_records_number_from_oracle() - 1) + "]: ", '>', min=0, lessThan=int(
                    int(oracleDBconnector.count_records_number_from_oracle())))
                res_list.append(response_multi)
            print("\nYour selected  " + str(total_res) + " records are: \n")
            dataService.showMultipleRecords(res_list)
            res_list.clear()
            validate_response()

        elif user_response == 5 and oracleDBconnector.count_records_number_from_oracle() > 0:
            dataService.showAllRecords()
            validate_response()

        elif user_response == 6 and oracleDBconnector.count_records_number_from_oracle() > 0:
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
            new_record = {'pruid': prid, 'prname': pname_en, 'prnameFR': pname_fr, 'sdate': idate, 'numconf': inumconf,
                          'numprob': inumprob, 'numdeaths': deaths, 'numtotal': inumtotal, 'numtoday': inumtoday,
                          'ratetotal': iratetotal}
            dataService.addRecord(new_record)
            validate_response()
        # elif user_response == 7 and oracleDBconnector.count_records_number_from_oracle() > 0:
        elif user_response == 7:
            res_to_update = pyinputplus.inputNum("\nPlease enter the index# of the record to update [0 to " + str(
                oracleDBconnector.get_last_index_from_oracle()) + "]: ", '>', min=0, lessThan=int(
                int(oracleDBconnector.get_last_index_from_oracle()) + int(1)))
            oracleDBconnector.read_one_record_from_oracle(res_to_update)
            print('\nPlease enter the new values for the record:')
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
            dataService.updateRecord(prid, pname_en, pname_fr, idate, inumconf, inumprob, deaths, inumtotal,
                                     inumtoday, iratetotal, res_to_update)
        # elif user_response == 8 and oracleDBconnector.count_records_number_from_oracle() > 0:
        elif user_response == 8:
            res_to_del = pyinputplus.inputNum("\nPlease enter the index# of the record to delete [0 to  " + str(
                oracleDBconnector.get_last_index_from_oracle()) + "]: ", '>', min=0, lessThan=int(
                int(oracleDBconnector.get_last_index_from_oracle()) + int(1)))
            oracleDBconnector.read_one_record_from_oracle(res_to_del)
            dataService.delete_record(res_to_del)
            validate_response()

        elif user_response == 9:
            print("exit")
            sys.exit()

    except AttributeError:
        data_not_loaded(user_response)


class Menu:
    """
    This class is to interact user with the program. It displays menu system and accepts user inputs after
    validation and redirects user to the business or persistence layer to perform requested tasks based on user input.
    """

    response = 0

    Option = namedtuple('Option', 'label')
    _separator = "~" * 45
    _options = {1: Option("Reload All Covid records"), 2: Option("Write all saved records to a new file"),
                3: Option("Print one record from Oracle DB"), 4: Option("Print multiple records from Oracle DB"),
                5: Option("Print all saved records from the DB"), 6: Option("Create a new record to the file"),
                7: Option("Update a record from the DB"), 8: Option("Delete a record from the file in the DB"),
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

        This method outputs a menu on the console with 9 options
        for the user to select from.
        @param self: The instance of the class.
        """

        self.print_header()
        for option in sorted(self._options.keys()):
            print("{0} {1}".format(option, self._options[option].label))
