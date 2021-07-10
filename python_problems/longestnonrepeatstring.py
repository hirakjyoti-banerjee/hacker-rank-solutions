#PRINT THE LONGEST NON-REPEATED SUBSRTING FROM AN INPUT STRING
class Solution(object):

    def lengthOfLongestSubstring(self,str):
        str_len = len(str)
        #print(str_len)

        if str_len <= 1:
            print("The longest substring is :", str)
            return

        maxlen = 0
        st = 0 #start of current substring
        start = 0 #start of maximum length start string
        pos = {}
        pos[str[0]] = 0

        for i in range(1,str_len):
            if st == 0 and i == str_len - 1 and str[i] not in pos:
                maxlen = str_len

            if str[i] not in pos:
                pos[str[i]] = i
            else:
                if pos[str[i]] >= st:
                    currlen = i - st
                    if maxlen < currlen:
                        maxlen = currlen
                        start = st
                    st = pos[str[i]] + 1
                pos[str[i]] = i
            print("i-st: ", i-st)
            if maxlen <= i - st:
                print("!!!")
                maxlen = i - st + 1
                start = st

            print("i: ", i)
            print("st: ", st)
            print("start: ", start)
            print("str[i]: ", str[i])
            print("pos: ", pos)
            print("#",maxlen)

        print(pos)
        print("The longest substring is :",str[start: start + maxlen])
        return


instr = input("Enter string: ")
input_str = Solution()
input_str.lengthOfLongestSubstring(instr)