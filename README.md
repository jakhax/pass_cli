Pass Cli
===================

- - - -
Author: [Jack Ogina](https://github.com/jakhax)



[Pass Cli](https://github.com/jakhax/pass_cli.git)lets you manage
your login credentials from the terminal. Password files are saved into
[Advance Encryption Standard AES256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) encrypted files
using the user's master password as the encryption key. Only with the master password used to create the user account can one decrypt password files. If you want to know
more about how my cipher implementation works check out this repo [hexcrypt](https://github.com/jakhax/hexcrypt_aes256_encryption.git).

![Pass_cli console interface](https://imgur.com/8LVJdQF)

------------------------------------------------------------------------

## Main Features

+ [x] Console interface
+ [x] Manage multiple user accounts- add new and delete existing accounts
+ [x] Add, edit, remove credentials
+ [x] Copy passwords to clipboard
+ [x] List credentials as a table
+ [x] Colored output
+ [x] Search credentials by name
+ [x] Randomly generated credential passwords of a certain length
+ [x] Randomly generated strings of a certain length
+ [ ] Search with regular expression
+ [ ] Exporting Password Accounts to an encrypted text file
+ [ ] Importing Password from a previous account file.




## Installation
```bash
git clone https://github.com/jakhax/pass_cli.git && cd pass_cli
```
### Installing dependencies
```bash
pip install -r requirements.txt
```
The following libraries are required
* pycrypto==2.6.1
* pyperclip==1.5.7
* click==6.7
* PyYAML==3.12
* tabulate==0.8.2

### Running Tests
```bash
python -m unittest discover tests
```

### Running code
```bash
python pass_cli.pass_cli.py
```

## Quickstart

```bash
# Add a new user account by create a new credentials files, followed by a username and master password prompt. Command: `new_account` 
pass_cli new_account

# terminate an existing user account by deleting credentials files,authentication required if user is logged out. Command: `new_account` 
pass_cli terminate_account

# Log in to an existing user account. command: `login`
pass_cli login

# Log out of an existing logged in user account. command: `logout`
pass_cli logout

# add new credentials to a logged in user account,followed by a username prompt. Command: `add_cred`
pass_cli add_cred

# delete credentials of a logged in user account,followed by a username prompt. Command: `del_cred`
pass_cli del_cred

# search for  credentials of a logged in user account,followed by a username prompt. Displayed on a table like structure with hidden passes, a user can copy a pass to clip board. Command: `search`
pass_cli search

# edit credential password; followed by prompts for username and name of creds to edit. command: `update_pass`
pass_cli update_pass

```

## Tutorials

### 1) Creating user accounts and adding credentials

Pass cli credentials handles multiple logins for each name which groups credentials by name:

```bash
# create john account
#password will not be echoed
pass_cli new_account
Username: john
Password: ****
Repeat for confirmation: ****
Account name successfully created for user

# create a credential credential
passcli add_cred
Username: john
Warning: duplicate names may errors during a search Enter unique credential names
Unique credential name: facebook
Enter credential login/username:: johndoe
Enter credential password:
Confirm credential password:
Credentials successfully added

```
### 2) Logging in and out of a user account

Logging in enables you to be able to work with your credentials e.g coping passes, editing credentials and deleting credentials.
Logging out ensures that you file is encrypted and cannot be read until you log in.
Always log out after using the CLI app.

```bash
#logging in
Username: john
Password:
Repeat for confirmation:
Account  name john has been successfully logged in

#logging out
Username: john
Password:
Repeat for confirmation:
Account  name john has been successfully logged out
```

### 3) Listing and Searching credentials by name

You can list credentials or search for credentials using name:

```bash
#list and copy password to clip board
pass_cli search
Username: jak hax
========  ========  ==========
Name      Login     Password
========  ========  ==========
facebook  johndoe   *****
twitter   john_doe  *****
========  ========  ==========
Do you want to get password of any of the displayed sites? [y/N]: y
Unique credential name: twitter
Found password for  twitter..password copied to clipboard
```

### 4) Editing credential passwords

You can add edit a credential password

```bash
#editing credential password
Username: jak hax
========  ========  ==========
Name      Login     Password
========  ========  ==========
facebook  johndoe   *****
twitter   john_doe  *****
========  ========  ==========
Unique name of creds to edit: facebook
Enter credential password:
Confirm credential password:
Changed password for  facebook..password copied to clipboard
```

### 5) Deleting credentials and terminating user accounts
```bash
#Deleting credentials using name
Username: jak hax
========  ========  ==========
Name      Login     Password
========  ========  ==========
facebook  johndoe   *****
twitter   john_doe  *****
========  ========  ==========
Unique name of creds to delete: facebook
Confirm that you want to delete facebook [y/N]: y
Deleted creds for  facebook

#terminating a user account
Username: john
Password:
Repeat for confirmation:

    Warning Account will be terminated!!!
    Please confirm that you have a back up of your credentials before you continue
    Hint: use the export command to store an encrypted back up of your Account
                that you can decrypt using Hexcrypt

Enter (yes) if you wish to continue or any key to halt : yes
Account  name john has been successfully terminated
```

## How it works

### Encryption

Encryption is done with [AES256](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard). Take a look at [crypt.py](https://github.com/jakhax/pass_cli/pass_clie/crypt.py) module to know more. Specifically how the program is able to authenticate user log in /decryption sessions.

### Credentials Path

The default credentials files path is at `../users`. 
The credentials are stored in encrypted CSV files.
Each user has a csv file identified by their user-name.


### Credentials structure

Credentials are strored in the csv files in a dictionary format which is easy to read and write, the resultant CSV file is the encrypted using AES256.

```bash
# └── credential file
#     ├── name_header:name
#     ├── login_headeer: login
#     ├── password_
```

## Warning

This is an academic project with limited research hence this project at its current stage should not be used to secure serious passwords as suffers from the following but not limited to security purposes:
* The CSV files can be copied easily by an adversary as they are not hidden; though the encryption AES256 is pretty good and a bruteforce may be unsuccessful
* In an event the user forgets to log out an adversay can be able to obtain the password files in plain-text.
* The security method I have implemented on [crypt.py](https://github.com/jakhax/pass_cli/pass_clie/crypt.py) has not been examined in detail for security issues 

## Contributing

- Fork the repository [https://github.com/jakhax/pass_cli/fork](https://github.com/marcwebbie/pysswords/fork)
- Git clone [https://github.com/jakhax/pass_cli.git](https://github.com/jakhax/pass_cli.git) and make the changes.
- Write your tests on `tests/`
- If everything is OK. push your changes and make a pull request. ;)
- Examining the security implementation of [crypt.py](https://github.com/jakhax/pass_cli/pass_clie/crypt.py) and suggesting ways in which it could be comprosmised by creating issues.

## License ([MIT License](http://choosealicense.com/licenses/mit/))

This project is licensed under the MIT Open Source license, (c) [Jack ogina](https://github.com/jakhax)
