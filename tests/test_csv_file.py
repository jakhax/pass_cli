import os,sys; sys.path.insert(0, os.path.abspath('..'))

import pass_cli.csv_file as csv_file
import unittest,csv
from binascii import hexlify

class Test_csv_file(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.test_file="test_csv.csv"
        self.invalid_file=hexlify(os.urandom(5))
        self.correct_test_data={"name":"github","login":"von rossum","password":"password"}
        self.wrong_test_data=["github","von rossum","password","facebook","rossum@mail.com"]

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        if os.path.exists(self.test_file): os.remove(self.test_file)

    def test_readit_invalid_filepath(self):
        '''
        Test for behaviour of the readit method when parsed with an invalid filename
        '''
        self.assertEqual(FileNotFoundError,type(csv_file.Data_Operator(self.invalid_file).readit()))

    def test_writeit_invalid_data(self):
        '''
        Test behaviour of writeit method when parsed with invalid Data_Operator
        '''
        self.assertEqual(ValueError,type(csv_file.Data_Operator(self.test_file).writeit(self.wrong_test_data)))

    def test_readit_method(self):
        '''
        Test that correct data is read from a csv file in the correct format using DictReader
        '''
        with open(self.test_file,'a') as my_csv_file:
            fieldnames=["name","login","password"]
            csv_writer=csv.DictWriter(my_csv_file,fieldnames=fieldnames)
            csv_writer.writeheader()
            for i in range(5):
                csv_writer.writerow(self.correct_test_data)
        self.assertEqual([self.correct_test_data]*5,csv_file.Data_Operator(self.test_file).readit())

    def test_editit_method(self):
        '''
        Test that correct data is written to the CSV file in the correct table_format
        '''
        csv_file.Data_Operator(self.test_file).editit([self.correct_test_data])
        with open(self.test_file,'r') as my_csv_file:
            csv_reader=csv.DictReader(my_csv_file)
            test_data=[i for i in csv_reader]
            test_pass=test_data[0]["password"]
        self.assertEqual("password",test_pass)

if __name__=="__main__":
    unittest.main()
