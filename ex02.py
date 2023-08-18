# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import time


class CashMachine:

    def __init__(self):
        self._balance = 0
        self._number_operations = 0
        self._money_commission = 0
        self._history_operations = []

    def _print_history_operation(self):
        '''Печатает историю операций по счету'''

        print('\n')
        for number, value in enumerate(self._history_operations, 1):
            print(f'{number}. {value}')

    def _refill_withdraw(self, mode):
        '''Функция изменения счета в зависимости от режима работы - снятие/пополнение'''

        self.money_commission = 0 + self._money_commission

        while True:
            self.money = int(input('Введите сумму (кратную 50): '))
            if self.money % 50 == 0:
                break
            else:
                print('Повторите попытку')

        if self._number_operations == 3:
            self.money_commission += 0.03

        match mode:
            case 1:
                self.money_value = (self.money - (self.money * self.money_commission))
                self._balance += self.money_value
                self._history_operations.append(f'Пополнение баланса +{self.money_value}')
                self._number_operations += 1
            case 2:
                if self.money > self._balance:
                    print('Ошибочная операция!')
                if self.money * (0.015 + self.money_commission) <= 30:
                    self.money_value = (self.money + 30)
                    self._balance -= self.money_value
                    self._history_operations.append(f'Снятие средств -{self.money_value}')
                elif self.money * (0.015 + self.money_commission) >= 600:
                    self.money_value = (self.money + 600)
                    self._balance -= self.money_value
                    self._history_operations.append(f'Снятие средств -{self.money_value}')
                else:
                    self.money_value = (self.money + (self.money * (0.015 + self.money_commission)))
                    self._balance -= self.money_value
                    self._history_operations.append(f'Снятие средств -{self.money_value}')
                self._number_operations += 1


test = CashMachine()

while True:
    print(f'\nВведите номер операции:\n'
          '1. Пополнить счет\n'
          '2. Снять деньги\n'
          '3. Показать баланс\n'
          '4. История операций\n'
          '5. Выйти\n')

    mode = int(input('Введите номер операции: '))

    if test._balance >= 5_000_000:
        test.money_commission = 10

    match mode:
        case 1:
            test._refill_withdraw(mode)
        case 2:
            if test._balance != 0:
                test._refill_withdraw(mode)
            else:
                print('Нулевой баланс!')
        case 3:
            print(f'\nВаш баланс: {test._balance}')
            time.sleep(2)
        case 4:
            test._print_history_operation()
            time.sleep(2)
        case 5:
            break