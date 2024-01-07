# a file that performs a test for cap.py

import unittest # a library used to test
import cap  # a python file thats used to be tested

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text) # assign a variable for calling a functions or classes passing in something
        self.assertEqual(result, 'Python') # this does, is the result I'am getting from myscript the expected result

    # Here the unittest or this testing method is right however the code in cap.py has some issue so it will show there's a problem, to fix it i will update the cap.py
#    def test_multiple_words(self):
#        text = 'monty python'
#        result = cap.cap_text(text)
#        self.assertEqual(result, 'Monty Python')

    # to see the error uncomment the above function
    def test_multiple_words2(self):
        text = 'monty python'
        result = cap.cap_text2(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()