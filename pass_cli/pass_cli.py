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

@cli.command(help='Create new credential to database')
@click.option('--name', prompt='Username',help="Username for password manager account")
@click.password_option(help="Master password to decrypt / encrypt password files")
def new_account(name,password):
    '''
    Handles user log in sessions
    '''
    if SessionCheck(name).check_if_user_exists():
        return click.echo(click.style("Account name: {} already exists".format(name), bg='red', fg='white'))
    if name.startswith(crypto_extention):
        return click.echo(click.style("Account name cannot start with a {}".format(crypto_extention), bg='red', fg='white'))
    pass_cli.manage_users.User_Account(name,password).create_account()
    return click.echo(click.style("Account name successfully created for {}".format(name), bg='green', fg='white'))

@cli.command(help='Delete Account From Pass Cli This will erase all your credentials virtually for good')
@click.option('--name', prompt='Username',help="Username for password manager account")
@click.password_option(help="Master password to decrypt / encrypt password files")
def terminate_account(name,password):
    '''
    Handles Deleting of a User Account
    '''
    click.echo(click.style("{}".format(pass_cli.config.terminate_warning),fg='white'))
    confirm_state=input("Enter (yes) if you wish to continue or any key to halt : ")
    if confirm_state!="yes": return click.echo(click.style("Process has been halted", bg='yellow', fg='white'))
    if  not SessionCheck(name).check_if_user_exists():
        return click.echo(click.style("Account name: {} does not  already exists".format(name), bg='red', fg='white'))
    if pass_cli.manage_users.User_Account(name,password).terminate_account():
        return click.echo(click.style("Account  name {} has been successfully terminated".format(name), bg='green', fg='white'))
    elif ValueError==type(pass_cli.manage_users.User_Account(name,password).terminate_account()):
        return click.echo(click.style("Wrong password given for account name: {}".format(name), bg='red', fg='white'))
    else:
        return click.echo(click.style("Unable to terminate account name: {}".format(name), bg='red', fg='white'))


if __name__=="__main__":
    cli()