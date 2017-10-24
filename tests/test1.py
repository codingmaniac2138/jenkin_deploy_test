import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

import xmlrunner
import unittest
print (os.getcwd())
from test_deploy import tt

class exampleTest(unittest.TestCase):

    def setUp(self):
        self.exampleClass = tt.Example()

    def tearDown(self):
        pass

    def testPlusSuccess(self):

        self.assertEqual(self.exampleClass.Plus(1,2),3)

   
if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output="./python_unittests_xml"))