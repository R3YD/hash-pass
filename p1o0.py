import hashlib

startPass = '0000'
passHash = hash(startPass.encode())

def Start():
    passIsCorrect = False
    print('Введите пароль')
    while not passIsCorrect:
        userPass = input()
        userPassHash = hash(userPass.encode())
        if userPassHash != passHash:
            print('Пароль неверный, попробуйте еще раз')
        else:
            print('Пароль верный')
            passIsCorrect = True
    ProgramBody()
    
def ChangePassword():
    global passHash
    print('Введите новый пароль')
    newPass = input()
    passHash = hash(newPass.encode())
    Start()
    
def ProgramBody():
    print('Чтобы сменить пароль, введите 1')
    print('Чтобы деавторизоваться, введите 2')
    print('Чтобы закрыть программу, введите 3')
    choose = int(input())
    if choose == 1:
        ChangePassword()
    elif choose == 2:
        Start()
    elif choose == 3:
        exit()
    ProgramBody()

Start()
