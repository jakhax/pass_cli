
import os,sys; sys.path.insert(0, os.path.abspath('..'))

import  pass_cli.config

crypto_extention= pass_cli.config.DEFAULT["crypto_extention"]
users_dir= pass_cli.config.DEFAULT['users_dir']
class SessionCheck:
    def __init__(self,username):
        self.username=username

    def check_if_user_exists(self):
        if self.username+".csv" in os.listdir(users_dir) or crypto_extention+self.username+".csv" in os.listdir(users_dir) :
            return True
        else:return False


    def get_user_session(self):
        if self.username+".csv" in os.listdir(users_dir):
            return True
        elif crypto_extention+self.username+".csv" in os.listdir(users_dir):
            return False
        else:
            return ValueError("User does not exist")
