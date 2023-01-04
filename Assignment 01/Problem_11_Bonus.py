#Question 11:
""" Nick and Jack are good friends and both are very good at numbers, they want to play a fun game to know
their understanding of numbers conversion into roman numerals. Nick will give a number N and Jack has to guess
the equivalent Roman Numeral.

Input Format : Input consists of single integer N

Constraints: 1 <= N <= 3999

Output : Print equivalent roman number in a single line.

Sample Input 1: 2085

Sample Output 1: MMLXXXV     """

#Defining Function
def main(nums) :
        while (nums > 0) :
            if (nums >= 1000) :
                print("M", end ="")
                nums = nums - 1000

            elif(nums >= 900) :
                print("CM", end ="")
                nums = nums - 900

            elif(nums >= 500) :
                print("D", end ="")
                nums = nums - 500

            elif(nums >= 400) :
                print("CD", end ="")
                nums = nums - 400

            elif(nums >= 100) :
                print("C", end ="")
                nums = nums - 100

            elif(nums >= 90) :
                print("XC", end ="")
                nums = nums - 90

            elif(nums >= 50) :
                print("L", end ="")
                nums = nums - 50

            elif(nums >= 40) :
                print("XL", end ="")
                nums = nums - 40

            elif(nums >= 10) :
                print("X", end ="")
                nums = nums - 10

            elif(nums >= 9) :
                print("IX", end ="")
                nums = nums - 9

            elif(nums >= 5) :
                print("V", end ="")
                nums = nums - 5

            elif(nums >= 4) :
                print("IV", end ="")
                nums = nums - 4

            elif(nums >= 1) :
                print("I", end ="")
                nums = nums - 1

#Taking Input:-
nums=int(input())
#Calling Function:-
main(nums)