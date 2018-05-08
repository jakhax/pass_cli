logo='''

 ██▓███      ▄▄▄           ██████      ██████        ▄████▄      ██▓        ██▓
▓██░  ██▒   ▒████▄       ▒██    ▒    ▒██    ▒       ▒██▀ ▀█     ▓██▒       ▓██▒
▓██░ ██▓▒   ▒██  ▀█▄     ░ ▓██▄      ░ ▓██▄         ▒▓█    ▄    ▒██░       ▒██▒
▒██▄█▓▒ ▒   ░██▄▄▄▄██      ▒   ██▒     ▒   ██▒      ▒▓▓▄ ▄██▒   ▒██░       ░██░
▒██▒ ░  ░    ▓█   ▓██▒   ▒██████▒▒   ▒██████▒▒      ▒ ▓███▀ ░   ░██████▒   ░██░
▒▓▒░ ░  ░    ▒▒   ▓▒█░   ▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░      ░ ░▒ ▒  ░   ░ ▒░▓  ░   ░▓
░▒ ░          ▒   ▒▒ ░   ░ ░▒  ░ ░   ░ ░▒  ░ ░        ░  ▒      ░ ░ ▒  ░    ▒ ░
░░            ░   ▒      ░  ░  ░     ░  ░  ░        ░             ░ ░       ▒ ░
                  ░  ░         ░           ░        ░ ░             ░  ░    ░
                                                    ░

'''
DEFAULT = {
    'users_dir':'../users/',
    'crypto_extention':'crypt.',
    'genpass_pattern': r'[a-z]{10} [-_+=*&%$#]{10} [A-Z]{10}',
    'table_format': 'fancy_grid',
    'headers': ['name', 'login', 'password', 'comment'],
    'colors': {'name': 'yellow', 'login': 'green'},
    'copy_timeout': 0,
    'hidden': ['password'],
    'hidden_string': u'********'}
terminate_warning='''
    Warning Account will be terminated!!!
    Please confirm that you have a back up of your credentials before you continue
    Hint: use the export command to store an encrypted back up of your Account
                that you can decrypt using Hexcrypt
                '''
fieldnames=["name","login","password"]
colors= {'name': 'yellow', 'login': 'green'}