import re
import unittest

def sumNums(fileName):
    total = 0
    #open the file
    hand = open(fileName)

    #loop through the lines
    for line in hand:

        line = line.rstrip()
        
        a = re.findall('([0-9]+)', line)
        if a != []:
            for nums in a:
                total += int(nums)
    print(total)
    return total
           
def countWord(fileName, word):

    
    wordList = []
    word_count = 0
   
    hand = open(fileName)
    
    for line in hand:
       #re.findall(r'\b' + word + r'b')
        words = re.findall(r'\b' + word + r'\b', line, flags = re.IGNORECASE)
        
        wordList = wordList + words
    word_count = len(wordList)
    print(word_count)
    return(word_count)

    


def listURLs(fileName):
    urls = []
    hand = open(fileName)

    for line in hand:
        line = line.rstrip()

        url = re.findall("w{3}\.[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9-.]+", line)
        if url != []:
            urls += url
        
    print(urls)
    return urls

sumNums("regex_sum_132198.txt")
countWord("regex_sum_132198.txt","computer")
listURLs("regex_sum_132198.txt")


class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)
