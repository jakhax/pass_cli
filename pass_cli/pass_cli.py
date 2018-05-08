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

@cli.command(help="Log in to an already existing account")
@click.option('--name', prompt='Username',help="Username for password manager account")
@click.password_option(help="Master password to decrypt / encrypt password files")
def login(name,password):
    '''
    Log in to an already existing account
    '''
    session_data=SessionCheck(name).get_user_session()
    if session_data==True:
        return click.echo(click.style("Account  name {} is already logged in".format(name), bg='red', fg='white'))
    if type(session_data)==ValueError:
        return click.echo(click.style("Account  name {} does not  exist".format(name), bg='red', fg='white'))
    elif not session_data:
        session_state=pass_cli.manage_users.User_Account(name,password).login() 
        if session_state==True:
            return click.echo(click.style("Account  name {} has been successfully logged in".format(name), bg='green', fg='white'))
        elif type(session_state)== ValueError:
            return click.echo(click.style("Wrong password given for account name: {}".format(name), bg='red', fg='white'))
        else:
            return click.echo(click.style("Unable to log into account name: {}".format(name), bg='red', fg='white'))
    else:
        return click.echo(click.style("Unable to log into account name: {}".format(name), bg='red', fg='white'))

@cli.command(help="Log out of an already existing account")
@click.option('--name', prompt='Username',help="Username for password manager account")
@click.password_option(help="Master password to decrypt / encrypt password files")
def logout(name,password):
    '''
    Log out of an already existing account
    '''
    session_data=SessionCheck(name).get_user_session()
    if session_data==True:
        session_state=pass_cli.manage_users.User_Account(name,password).logout()
        if session_state==False:
            return click.echo(click.style("Unable to log out account name: {}".format(name), bg='red', fg='white'))
        else:
            return click.echo(click.style("Account  name {} has been successfully logged out".format(name), bg='green', fg='white'))
    elif session_data==False:
        return click.echo(click.style("Account name: {} is already logged out".format(name), bg='red', fg='white'))
    else:
        return click.echo(click.style("Unable to log out account name: {}".format(name), bg='red', fg='white'))

@cli.command(help="Log out of an already existing account")
@click.option('--name', prompt='Username',help="Username for password manager account")
@click.option('-r', '--random', is_flag=True, help="Randomly generate password")
def add_cred(name,random):
    session_data=SessionCheck(name).get_user_session()
    if session_data==True:
        click.echo(click.style("Warning: duplicate names may errors during a search Enter unique credential names",fg="red"))
        cred_name=click.prompt("Unique credential name", type=str)
        cred_login=click.prompt("Enter credential login/username:", type=str)
        if random==True:
            rand_length = click.prompt("Enter length of random password:", type=int)
            rand_str=CSRNG(rand_length).hex_osrandom()
            User_Creds(name).add([cred_name,cred_login,rand_str])
            return click.echo(click.style("Credentials successfully added", bg='green', fg='white'))
        else:
            web_pass=getpass("Enter credential password:")
            web_pass2=getpass("Confirm credential password:")
            if web_pass !=web_pass2:
                return click.echo(click.style("Passwords do not match try again", bg='red', fg='white'))
            User_Creds(name).add([cred_name,cred_login,web_pass])
            return click.echo(click.style("Credentials successfully added", bg='green', fg='white'))

    if type(session_data)==ValueError:
        return click.echo(click.style("Account  name {} does not  exist".format(name), bg='red', fg='white'))
    elif session_data==False:
        return click.echo(click.style("Account name: {} is logged out".format(name), bg='red', fg='white'))

@cli.command(help="Search for user data and copy password to clip board")
# @click.option('-s', '--show', is_flag=False, help="show passwords in clear text")
@click.option('--username', prompt='Username',help="Username for password manager account")
def search(username):
    session_data=SessionCheck(username).get_user_session()
    if session_data==True:
        credentials=User_Creds(username).get_creds()
        if len(credentials)>=1:
            table = Table(
                pass_cli.config.fieldnames,'rst',
                colors=pass_cli.config.colors,
                hidden=[pass_cli.config.fieldnames[2]]
            )
            click.echo(table.render(credentials))
            if click.confirm('Do you want to get password of any of the displayed sites?'):
                cred_name=click.prompt("Unique credential name", type=str)
                search_data=User_Creds(username).get_creds()
                search_pass=''
                for row in search_data:
                    if row[pass_cli.config.fieldnames[0]]==cred_name:
                        search_pass=row[pass_cli.config.fieldnames[2]]
                        break
                if search_pass:
                    pyperclip.copy(search_pass)
                    return click.echo(click.style("Found password for  {}..password copied to clipboard".format(cred_name), bg='green', fg='white'))
                else:
                    return click.echo(click.style("Did not Find password for  {}".format(cred_name), bg='red', fg='white'))
        elif len(credentials)<1:
            return click.echo(click.style("Empty data for account name: {}".format(username), bg='red', fg='white'))
        else:
            return click.echo(click.style("Unable to display credentials", bg='red', fg='white'))
    if type(session_data)==ValueError:
        return click.echo(click.style("Account  name {} does not  exist".format(username), bg='red', fg='white'))
    elif session_data==False:
        return click.echo(click.style("Account name: {} is logged out".format(username), bg='red', fg='white'))


if __name__=="__main__":
    cli()
