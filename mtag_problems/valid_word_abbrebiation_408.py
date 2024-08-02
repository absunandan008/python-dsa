class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_ptr = 0
        word_ptr = 0

        #till both the pointers are less than actual length
        while abbr_ptr < len(abbr) and word_ptr < len(word):
            # if abbr pointer is a digit then check if it is leading,
            # if not then calculate the actual number
            # else return false for leading zeros
            if abbr[abbr_ptr].isdigit():
                if abbr[abbr_ptr] == '0':
                    return False
                curr_num = 0
                #calculating total digits
                while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                    curr_num = curr_num * 10 + int(abbr[abbr_ptr])
                    abbr_ptr +=1
                #adding current digit to pointer of word
                word_ptr += curr_num
            else:
                #if both current pointers are not pointing to same alphbet then something
                if abbr[abbr_ptr] != word[word_ptr]:
                    return False
                abbr_ptr += 1
                word_ptr += 1
        return abbr_ptr == len(abbr) and word_ptr == len(word)
