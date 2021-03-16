"""
Project name - CST8333ProjectByMuktaDebnath
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
CST8333-351- Assignment 03
Student No.: 040950904

Description: I will test a function by using the Unit Test framework. My tests will check:
* Function addRecord() to check create and add function is working or not
"""

import unittest
from BusinessLogic import dataService, oracleDBconnector
from Data import datesetPath
from Persistence import dataAccess


class UnitTestAssignment3(unittest.TestCase):

    def test_delete_record(self):
        """
        This method will test the function delete_record()
        :param self: the instance of the class
        """

        records_count_before_deletion = oracleDBconnector.count_records_number_from_oracle()
        dataService.delete_record(200)
        records_count_after_deletion = oracleDBconnector.count_records_number_from_oracle()
        self.assertNotEqual(records_count_before_deletion, records_count_after_deletion)
        dataAccess.printName()


if __name__ == '__main__':
    unittest.main()
