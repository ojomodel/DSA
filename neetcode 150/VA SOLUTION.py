def anagrams(s1, s2):
    countS, countT = {}, {}  # this is a hashmap
    for i in range(len(s1)):
        countS[s1[i]] = countS.get(s1[i], 0) + 1  # if key does not exist in hashmap return 0
        countT[s2[i]] = countS.get(s2[i], 0) + 1
        """
        so the countS.get(s1[i], 0) its really .get(key, default=None) it gets the value of the key and
        if there is no value of the key in our case it does not set it to NONE, since we did (s[i], 0) 
        it sets the value of the key to 0 but we have + 1 outside of the parenthesis so it 0 + 1 which 
        is 1 so the value of the keybecomes 1 if they key DOES NOT EXIST but if the key exists, it just 
        adds 1 to it, the 0 only APPLIES WHEN THE KEY DOES NOT EXIST. but if the key EXIST it does not 
        apply it just adds + 1 to the value of the key
        """
        # chatgpt words
        # .get(key, default) returns the value for key if it exists; otherwise it returns default (0        here).
        # Then we add 1 and assign it back into the dict under that key.
        # So: first time a character appears -> 0 + 1 = 1
        # otherwise -> existing_count + 1
        for c in countS:  # so if looping thru a dict you are looping thru the KEYS
            if countS[c] != countT[c]:  # now when you put the keys as the index they return the value
                return False  # code is comparing the values for both list and if they do not match its false
        # todo