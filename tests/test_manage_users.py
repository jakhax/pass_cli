import os,sys; sys.path.insert(0, os.path.abspath('..'))
import unittest


from pass_cli.manage_users import User_Account
from pass_cli.crypt import Cipher
from  pass_cli.config import DEFAULT
from  pass_cli.session_check import SessionCheck
from pass_cli.creds import Data_Operator
'''
Global variables declarations
'''
crypto_extention=DEFAULT["crypto_extention"]
users_dir=DEFAULT['users_dir']

class Test_manage_users(unittest.TestCase):
    def setUp(self):
        '''
        set up tests
        '''
        self.username="test"
        self.master_pass="password"
        self.data_file='../users/'+self.username+".csv"
        self.crypt_file='../users/'+crypto_extention+self.username+".csv"
    
    def tearDown(self):
        if self.username+".csv" in os.listdir(users_dir):
            os.remove(self.data_file)
        if crypto_extention+self.username+".csv" in os.listdir(users_dir):
            os.remove(self.crypt_file)

    def test_create_account(self):
        '''
        test for method creating new user account 
        '''
        status=User_Account(self.username,self.master_pass).create_account()
        self.assertEqual(True,status)
    


        



