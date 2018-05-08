import os,sys; sys.path.insert(0, os.path.abspath('..'))

import unittest

from pass_cli.gen_rand import CSRNG

class Test_gen_rand(unittest.TestCase):
    def setUp(self):
        self.lengths=[1,42,233,78]
    
    def test_length_of_rand(self):
        for length in self.lengths:
            self.assertEqual(length,len(CSRNG(length).hex_osrandom()))


if __name__=="__main__":
    unittest.main()