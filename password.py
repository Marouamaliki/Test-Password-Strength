import string

password=""

upper_case=any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case=any([1 if c in string.ascii_lowercase else 0 for c in password])
special=any([1 if c in string.punctuation else 0 for c in password])
digits=any([1 if c in string.digits else 0 for c in password])

characters =[upper_case,lower_case,special,digits]
score=0
length=len(password)


with open("commonpass.txt", "r") as file:
  passwordList = file.read().splitlines()

if password in passwordList:
    print("password was found in a common list . score 0/7")
    exit()

if length>8:
    score+=1
if length>12:
    score+=1
if length>17:
    score+=1
if length>20:
    score+=1
print(f"password length is {str(length)},adding {str(score)} points!")

if sum(characters)>1:
    score+=1
if sum(characters)>2:
    score+=1
if sum(characters)>3:
    score+=1
print(f"Password has {str(sum(characters))} different character types, adding {str(sum(characters)-1)}")

if score <4:
    print(f"the password is quite weak!S Score : {str(score)}/7")
elif score==4:
    print(f"The password is ok! : Score {str(score)}/7")
elif 4<score<6:
    print(f"The password is pretty good! Score {str(score)}/7 ")
else:
    print(f"The password is strong! Score {str(score)}/7")
