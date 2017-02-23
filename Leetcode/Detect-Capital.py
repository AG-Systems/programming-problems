class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        firstchar = False
        counter = 0
        for x in xrange(len(word)):
            if word[x].isupper():
                if word[x].isupper() and x == 0:
                    firstchar = True
                    counter += 1
                else:
                    counter += 1
        if counter == 0 or counter == len(word):
            return True
        if counter == 1 and firstchar:
            return True
        else:
            return False
            
                
