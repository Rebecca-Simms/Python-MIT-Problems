
from string import punctuation
import re


class PhraseTrigger(object):
    def __init__(self, phrase):
        self.phrase = re.sub(r'[^\w\s]','',phrase.lower()).split()

    def is_phrase_in(self, text):
        self.text = re.sub(r'[^\w\s]',' ',text.lower()).split()
        #print(self.text)
        #print(self.phrase)

        count = 0
        count2 = 0

        for word in range(len(self.phrase)):
            #print(self.phrase[word])
            if self.phrase[word] in self.text:
                count += 1

        check =  ''.join(self.phrase)
        textcheck = ''.join(self.text)
        if check in textcheck:
            count2 += 1

        #print(count)
        #print(count2)
        if count == len(self.phrase) and count2 == 1:
            return True
        else:
            return False




# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        return(self.is_phrase_in(story.get_title()))


phrase = 'Purple Cow'
title0 = 'Purple! cow!!' #True
title1 = 'The purple cow is soft and cuddly.' #True
title2 =  'purple@#$%cow' #True
title3 = 'Did you see a purple     cow?' #True
title4 = 'The purple blob over there is a cow.' #False
title5 = 'Cow!!! Purple!!!' #False
title6 = 'purplecowpurplecowpurplecow' #False
title7 = 'I like poison dart frogs.' #False
title8 = 'Purple cows are cool!' #False

a = TitleTrigger(phrase)
print(a.is_phrase_in(title0))
print(a.is_phrase_in(title1))
print(a.is_phrase_in(title2))
print(a.is_phrase_in(title3))
print(a.is_phrase_in(title4))
print(a.is_phrase_in(title5))
print(a.is_phrase_in(title6))
print(a.is_phrase_in(title7))
print(a.is_phrase_in(title8))
