import hashlib
import binascii
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os,sys

class Cipher:
    def __init__(self,file,key):
        self.file=file
        self.key=key

    def encrypt(self):
            try:
                salt=Random.new().read(16)
                con_key=self.get_conkey()
                key2=binascii.hexlify(hashlib.pbkdf2_hmac('sha256',self.key.encode('utf-8'),salt,100000,16))
                chunksize = 64*1024
                if not os.path.exists(self.file):
                    return FileNotFoundError("File Does not Exist")
                outputFile =os.path.join(os.path.dirname(self.file), "crypt."+os.path.basename(self.file))
                filesize = str(os.path.getsize(self.file)).zfill(16)
                IV=Random.new().read(16)
                encryptor = AES.new(key2, AES.MODE_CBC, IV)
                with open(self.file, 'rb') as infile:
                        with open(outputFile, 'wb') as outfile:
                                outfile.write(filesize.encode('utf-8'))
                                outfile.write(IV)
                                outfile.write(con_key)
                                outfile.write(salt)
                                while True:
                                        chunk = infile.read(chunksize)
                                        if len(chunk) == 0:
                                                break
                                        elif len(chunk) % 16 != 0:
                                                chunk += b' ' * (16 - (len(chunk) % 16))
                                        outfile.write(encryptor.encrypt(chunk))
                os.remove(self.file)
                return "successfully Encrypted"

            except Exception as err:
                return 'An error occured:%s'%err

    def decrypt(self):
            try:
                chunksize = 64*1024
                if not os.path.exists(self.file):
                    return FileNotFoundError("File Does not Exist")
                q=os.path.basename(self.file)
                con_key=self.get_conkey()
                outputFile =os.path.join(os.path.dirname(self.file), q[6:])
                with open(self.file, 'rb') as infile:
                        filesize = infile.read(16)
                        IV = infile.read(16)
                        con_key2=infile.read(32)
                        salt=infile.read(16)
                        if con_key!=con_key2:
                            return ValueError('ERROR: Wrong self.key selected for %s'%q)
                        else:
                            key2=binascii.hexlify(hashlib.pbkdf2_hmac('sha256',self.key.encode('utf-8'),salt,100000,16))
                            decryptor = AES.new(key2, AES.MODE_CBC, IV)
                            with open(outputFile, 'wb') as outfile:
                                    while True:
                                            chunk = infile.read(chunksize)
                                            if len(chunk) == 0:
                                                    break
                                            outfile.write(decryptor.decrypt(chunk))
                                    outfile.truncate(int(filesize))
                os.remove(self.file)
                return "successfully Decrypted"
            except Exception as err:
                return 'An error occured:%s'%err

    def get_conkey(self):
            if type(self.key)!=str: return TypeError("Expected a string as a key")
            hasher = SHA256.new(self.key.encode('utf-8'))
            return hasher.digest()
    
