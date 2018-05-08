import os,sys; sys.path.insert(0, os.path.abspath('..'))
import click
'''
local imports
'''

from pass_cli.crypt import Cipher
from  pass_cli.csv_file import Data_Operator
from  pass_cli.config import DEFAULT
from  pass_cli.config import fieldnames
from  pass_cli.session_check import SessionCheck
'''
Global variables declarations
'''
crypto_extention=DEFAULT["crypto_extention"]
users_dir=DEFAULT['users_dir']

class User_Creds:
    def __init__(self,username):
        self.username=username
        self.data_file='../users/'+self.username+".csv"
        

    def add(self,add_list):
        add_dict=dict(zip(fieldnames,add_list))
        Data_Operator(self.data_file).writeit(add_dict)
    
    def get_creds(self):
        return Data_Operator(self.data_file).readit()
    
    def edit(self,add_dict):
        return Data_Operator(self.data_file).editit(add_dict)


