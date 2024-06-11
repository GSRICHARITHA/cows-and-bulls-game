import random
def generate_unique_digit_number():
    digits = list(range(10))
    random.shuffle(digits)
    number = digits[:4]
    # Ensure the first digit is not zero to maintain the 4-digit number
    while number[0] == 0:
        random.shuffle(digits)
        number = digits[:4]
    return int("".join(map(str, number)))
def getDigits(num):
    return [int(x) for x in str(num)]
def noDuplicates(num): 
    num_li = getDigits(num) 
    if len(num_li) == len(set(num_li)): 
        return True
    else: 
        return False
def guessing_the_number(number,guess):
    bull_cow = [0,0]
    # converting numbers into list 
    num_li=getDigits(number) 
    guess_li=getDigits(guess)
    for i in range(0,4):
        if num_li[i]==guess_li[i]:
            bull_cow[0]+=1
    for j in range(0,4):
        if guess_li[j] in num_li:
            bull_cow[1]+=1
    return bull_cow
number = generate_unique_digit_number()
#print("secret num =",number)
tries=int(input("Enter number of tries you need :"))
while tries>0:
    guess=int(input("Enter your guess :"))
    if guess < 1000 or guess > 9999: 
        print("Enter 4 digit number only! Try again!") 
    elif not noDuplicates(guess): 
        print("Number should not have repeated digits. Try again.") 
        continue
    bull_cow = guessing_the_number(number,guess) 
    print(f"{bull_cow[0]} bulls, {bull_cow[1]-bull_cow[0]} cows") 
    tries -=1
    if bull_cow[0] == 4: 
        print("You guessed right!") 
        break
print(f"You ran out of tries. Number was {number}")