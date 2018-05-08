import os,click,sys
import os,sys; sys.path.insert(0, os.path.abspath('..'))
from getpass import getpass
'''
local imports
'''
from pass_cli.crypt import Cipher
from  pass_cli.csv_file import Data_Operator
import pass_cli.config
from  pass_cli.session_check import SessionCheck
import pass_cli.manage_users
from pass_cli.creds import User_Creds
from  pass_cli.table import Table
from pass_cli.gen_rand import CSRNG
import pyperclip
'''
Global variables declarations
'''
crypto_extention=pass_cli.config.DEFAULT["crypto_extention"]
users_dir=pass_cli.config.DEFAULT['users_dir']
'''
Multi command init using command and group- nesting command line utilities
'''

@click.group()
@click.option('--username', default="jak")
def cli(username):
    '''
    Main CLI app
    '''
    click.echo(click.style(pass_cli.config.logo,fg="blue"))


if __name__=="__main__":
    cli()
