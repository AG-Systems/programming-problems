class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote in magazine:
            return True
        if len(ransomNote) > len(magazine):
            return False
        counter = 0
        container1 = list(ransomNote)
        container2 = list(magazine)
        for x in range(0,len(container2)):
            for z in range(0,len(container1)):
                try:
                    if container1[z] == container2[x]:
                        del container1[z]
                        del container2[x]
                except:
                    print("")
        if len(container1) == 0 or container1[0] in container2:
            return True
        else:
            return False
             
        
