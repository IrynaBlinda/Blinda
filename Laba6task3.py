class Letter(str):
    def letter(self, s=""):
        counter = 0
        sym = [0]
        for i in s:
            if sym == i:
                counter += 1
            else:
                sym = i
                if counter == 3:
                    return True
        return False

s = Letter()
s.letter("Hello" = 3)
print(s.letter())

class Str(Letter):
    def letter_2(self, s):
        s = "Name or no name"
        s.find("Name")
        for i in s:
            if i in s:
                print("True")
            else:
                print("False")

    def Palindrome(self, r):
        r = "nalayalam"
        ans = Palindrome(r)
        if ans:
            print("True")
        else:
            print("False")
        return r == r[::-1]
r = Letter()




    
