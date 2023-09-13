# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.


MENU = 'Добро пожаловать в банкомат Python \nДоступные операции: \n \
1. Пополнение счета\n \
2. Снятие денежных средств\n \
3. История совершённых операций\n \
4. Выход'

CLS = "\033[H\033[J"

def menu():
    print(CLS)
    print(MENU)
    account["action"] = int(input("Введите номер нужной операции: "))

def replenishment():
    print(CLS)
    print("Пополнение возможно только купюрами наминалом 50 у.е.")
    volume = float(input("Введите необходимое количество купюр: "))
    if account["balance"] > 5_000_000:
        account["balance"] -= account["balance"]*0.10
    account["balance"] += volume*50
    if account["operation"]%3 == 0 and account["balance"] > 0:
        account["balance"] += account["balance"]*0.03

def withdrawal():
    print(CLS)
    print("Снятие возможно только купюрами наминалом 50 у.е.")
    number = float(input("Введите необходимое количество купюр: "))
    if account["balance"] > 5_000_000:
        account["balance"] -= account["balance"]*0.10
    if account["balance"] < number*50:
        print("На Вашем счёте не достаточно денежных средств")
        return
    if number*0.015 < 30:
        account["balance"] -= number*50+30
    elif number*0.015 >= 30 and number*0.015 < 600:
        account["balance"] -= number*50+number*50*0.015
    elif number*0.015 >= 600:
        account["balance"] -= number*50
    if account["operation"]%3 == 0 and account["balance"] > 0:
        account["balance"] += account["balance"]*0.03

def balance():
    print(CLS)
    print('Операция выполнена успешно ')
    print(f'Ваш баланс: {account["balance"]}')
    input('Нажмите ввод для возврата в меню ')

def error():
    print(CLS)
    print(f'{account["action"]} данная операция невозможна. Выберите доступную операцию из списка')
    input('Нажмите ввод для возврата в меню ')

def history():
    print(CLS)
    print(*log, sep="\n")
    input('Нажмите ввод для возврата в меню ')

account = { "balance":0.0, "operation":0, "action":0 }
log = list()

while(account["action"]!=3):
    match account["action"]:
        case 0:
            menu()
        case 1:
            account["operation"] += 1
            replenishment()
            log.append(account.copy())
            balance()
            account["action"] = 0
        case 2:
            account["operation"] += 1
            withdrawal()
            log.append(account.copy())
            balance()
            account["action"] = 0
        case 3:
            history()
            account["action"] = 0
        case _:
            error()
            account["action"] = 0




