import os,sys; sys.path.insert(0, os.path.abspath('..'))
from pass_cli.crypt import Cipher
import unittest
from Crypto.Hash import SHA256
from binascii import hexlify

class TestCrypt(unittest.TestCase):

    def setUp(self):
        self.key="password"
        self.wrong_key="wrong password"
        self.testFile="testFile"
        self.crypted_file="crypt.testFile"
        self.fileNotExist=hexlify(os.urandom(10))
        with open(self.testFile,'w') as testFile:
            testFile.write("This is a Test File")

    def tearDown(self):
        if os.path.exists(self.testFile): os.remove(self.testFile)
        if os.path.exists(self.crypted_file): os.remove(self.crypted_file)


    def test_get_conkey_for_correct_data_type(self):
        self.keys=["password",78,5j,b"bin_data",0x13]
        for pass_key in self.keys:
            if type(pass_key)==str:
                self.assertEqual(SHA256.new(pass_key.encode()).digest(),Cipher("test.txt",pass_key).get_conkey())
            else:
                self.assertEqual(TypeError,type(Cipher("test.txt",pass_key).get_conkey()))

    def test_encrypt_for_invalid_file_path(self):
        #test for invalid file path or fileNotExist
        self.assertEqual(FileNotFoundError,type(Cipher(self.fileNotExist,self.key).encrypt()))

    def test_encrypt_for_successful_enc(self):
        #test for successful encryption
        with open(self.testFile,'w') as testFile:
            testFile.write("This is a Test File")
        self.assertEqual("successfully Encrypted",Cipher(self.testFile,self.key).encrypt())

    def test_decrypt_for_invalid_file_path(self):
            #test for invalid file path or fileNotExist
            self.assertEqual(FileNotFoundError,type(Cipher(self.fileNotExist,self.key).decrypt()))

    def test_decrypt_for_wrong_password(self):
            #test for wrong password
            with open(self.testFile,'w') as testFile:
                testFile.write("This is a Test File")
            Cipher(self.testFile,self.key).encrypt()
            self.assertEqual(ValueError,type(Cipher(self.crypted_file,self.wrong_key).decrypt()))

    def test_decrypt_for_correct_password(self):
            #test for correct password
            with open(self.testFile,'w') as testFile:
                testFile.write("This is a Test File")
            Cipher(self.testFile,self.key).encrypt()
            self.assertEqual("successfully Decrypted",Cipher(self.crypted_file,self.key).decrypt())

if __name__ == '__main__':
    unittest.main()
