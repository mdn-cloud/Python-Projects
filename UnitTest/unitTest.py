"""
Project name - Oracle 12c Database Connectivity
Programming Language Research Project
CST8333-351- Assignment 03
Professor's name: Mazin Abou-Seido
Author's name: Mukta Debnath
Student No.: 040950904

Description: I will test a function by using the Unit Test framework. My tests will check:
Function delete_record() to check the record delete from the database is working or not
"""

import unittest
from BusinessLogic import dataService, oracleDBconnector
from Persistence import dataAccess


class UnitTestAssignment3(unittest.TestCase):

    def test_delete_record(self):
        """
        This method will test to verify the delete_record() method
        :param self: the instance of the class
        """
        dataAccess.printName()
        records_count_before_deletion = oracleDBconnector.count_records_number_from_oracle()
        dataService.delete_record(10)
        records_count_after_deletion = oracleDBconnector.count_records_number_from_oracle()
        self.assertNotEqual(records_count_before_deletion, records_count_after_deletion)


if __name__ == '__main__':
    unittest.main()
