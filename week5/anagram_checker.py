from itertools import permutations

class AnagramChecker:
    def __init__(self):
        textfile = open('sowpods.txt','r').read()
        self.words2check1 = []
        self.words2check1.append(textfile)
        self.words2check = self.words2check1[0].split('\n')

    def is_valid_word(self,word):
      if word in self.words2check:
          print("Found it")
      else:
            print ("Not Found")

    def get_anagrams(self,word):
        temp = []
        letter_list = list(word)
        list_to_check = permutations(letter_list)
        for i in list_to_check:
            joined = (''.join(i))
            temp.append(joined)
            fin_list = []
        for item in temp :
            if item in self.words2check:
                fin_list.append(item)
                nfin_list=set(fin_list)
        print (nfin_list)



house = AnagramChecker()
house.get_anagrams("DOG")
