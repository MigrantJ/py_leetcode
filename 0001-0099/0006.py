"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lol = []
        for i in range(numRows):
            lol.append([])
        rowtofill = 0
        dir = 1

        for c in s:
            lol[rowtofill].append(c)
            if numRows > 1:
                rowtofill = rowtofill + dir
            if rowtofill == len(lol) - 1 or rowtofill == 0:
                dir = dir * -1

        output = ""
        for l in lol:
            for c in l:
                output = output + c

        return str(output)
