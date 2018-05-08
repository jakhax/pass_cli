import os,sys; sys.path.insert(0, os.path.abspath('..'))
import unittest
import  pass_cli.config
from  pass_cli.session_check import SessionCheck
from pass_cli.csv_file import Data_Operator
crypto_extention= pass_cli.config.DEFAULT["crypto_extention"]
users_dir= pass_cli.config.DEFAULT['users_dir']

class Test_session(unittest.TestCase):
    def setUp(self):
        '''
        set up tests
        '''
        self.username="test"
        self.master_pass="password"
        self.data_file='../users/'+self.username+".csv"
        self.crypt_file='../users/'+crypto_extention+self.username+".csv"
    
    def tearDown(self):
        '''
        Tear down test
        '''
        if self.username+".csv" in os.listdir(users_dir):
            os.remove(self.data_file)
        if crypto_extention+self.username+".csv" in os.listdir(users_dir):
            os.remove(self.crypt_file)

    def test_user_exists(self):
        '''
        Test for existing users
        '''
        self.assertEqual(False,SessionCheck(self.username).check_if_user_exists())
        Data_Operator(self.data_file).writeit()
        self.assertEqual(True,SessionCheck(self.username).check_if_user_exists())

