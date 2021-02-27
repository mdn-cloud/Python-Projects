"""
Project name - CST8333ProjectByMuktaDebnath
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
CST8333-351- Assignment 02
Student No.: 040950904

Description: I will test a function by using the Unit Test framework. My tests will check:
* Function addRecord() to check create and add function is working or not
"""

import unittest
from BusinessLogic import dataService
from Data import datesetPath
from Persistence import dataAccess


class UnitTestAssignment2(unittest.TestCase):

    def test_create_record(self):
        """
        This method will test the function addRecord()
        :param self: the instance of the class
        """

        dataAccess.read_dataset(datesetPath.DatasetPath.covid19_new)
        list_length_before_addition = len(dataAccess.records)
        new_record = {'pruid': 2, 'prname': 'Ontario', 'prnameFR': 'Ontario', 'date': '01/01/2020', 'numconf': 5,
                      'numprob': 0, 'numdeaths': 0, 'numtotal': 5, 'numtoday': 0, 'ratetotal': 0.2}
        dataService.addRecord(new_record)
        list_length_after_addition = len(dataAccess.records)
        self.assertEqual((list_length_before_addition + 1), list_length_after_addition)
        dataAccess.printName()


if __name__ == '__main__':
    unittest.main()
