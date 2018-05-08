import os,sys; sys.path.insert(0, os.path.abspath('..'))
import click
'''
local imports
'''

from pass_cli.crypt import Cipher
from  pass_cli.csv_file import Data_Operator
from  pass_cli.config import DEFAULT
from  pass_cli.session_check import SessionCheck
'''
Global variables declarations
'''

crypto_extention=DEFAULT["crypto_extention"]
users_dir=DEFAULT['users_dir']

class User_Account:
    def __init__(self,username,password):
        self.username=username
        self.master_pass=password
        self.data_file='../users/'+self.username+".csv"
        self.crypt_file='../users/'+crypto_extention+self.username+".csv"

    def create_account(self):
        '''Create a new user csv file and encrypt it with the master password'''
        Data_Operator(self.data_file).writeit()
        Cipher(self.data_file,self.master_pass).encrypt()
        return True

    def terminate_account(self):
        if crypto_extention+self.username+".csv" in os.listdir(users_dir):
            if Cipher(self.crypt_file,self.master_pass).decrypt()=="successfully Decrypted":
                try:
                    os.remove(self.data_file)
                    return True
                except: return False
            elif ValueError==type(Cipher(self.data_file,self.master_pass).decrypt()):
                return ValueError("Wrong Password Given")
            else:
                return False

        elif self.username+".csv" in os.listdir(users_dir):
            try:
                os.remove(self.data_file)
                return True
            except: return False

    def login(self):
        '''
        Login User using the master password
        '''
        try:
            if Cipher(self.crypt_file,self.master_pass).decrypt()=="successfully Decrypted":
                return True
            elif ValueError==type(Cipher(self.data_file,self.master_pass).decrypt()):
                return ValueError("Wrong Password Given")
        except:
            return False

    def logout(self):
        '''
        Log out user and encrypt 
        '''
        try:
            return Cipher(self.data_file,self.master_pass).encrypt()
        except:
            return False
        


