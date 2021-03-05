import random
guessesTaken = 0
print("Желаешь разбогатеть, друг? Как тебя зовут?")
name = input()
number = random.randint(1,20)
print("Ну тогда приступим?"+name+", я загадал число от одного до 20")
while guessesTaken < 3:
    print("Как ты думаешь, какое?") 
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken+1
    if guess < number:
        print("я загадал число больше твоего")
    if guess > number:
        print("я загадал число меньше твоего")
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Превосходно "+name+"! Ты угадал число с "+guessesTaken+" попытки. Твой выигрыш 600 золота.")
if guess != number:
    number = str(number)
    print("Жаль, но у тебя не осталось попыток. Я загадал число "+number+". Ты проиграл… я забираю у тебя 200 золота!")