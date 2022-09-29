"""
ATM:
    属性：1.用户卡号，密码，余额集==>字典{215481:(123456,500)}
    功能：1.登录
         2.查询余额
         3.存款
         4.取款
         5.转账(拓展）

"""


class ATM:
    def __init__(self):
        self.card_data = {
            '000001': {'passwd': '123456', 'money': 1000},
            '000002': {'passwd': '111111', 'money': 4637},
            '000003': {'passwd': '222222', 'money': 4416},
            '000004': {'passwd': '333333', 'money': 4303},
        }

    def login(self):
        while True:
            print('ATM 登录界面')
            card = input('请输入卡号： ')
            for i in range(3):
                  passwd = input('请输入密码： ')
                  if passwd == self.card_data[card]['passwd']:
                      return card
                  elif i < 2:
                        print(f'密码有误，请重试, 错误{2-i}次后退出')
                  else:
                        print('重试次数过多，回到初始登录界面')

    def choose(self):
        print('1.查询余额')
        print('2.取款')
        print('3.存款')
        print('4.转账')
        print('5.退出')
        choice = input('请选择功能： ')
        return choice

    def show(self, card):
        print('查询余额')
        print(f"您的当前余额为: {self.card_data[card]['money']}元")

    def save(self, card):
        print('存款')
        save_money = int(input('请输入存款余额： '))
        self.card_data[card]['money'] += save_money
        print('存款成功')

    def draw(self, card):
        print('取款')
        for i in range(3):
            draw_money = int(input('请输入取款余额： '))
            if self.card_data[card]['money'] < draw_money:
                 print('账户余额不足，请重新输入')
            else:
                self.card_data[card]['money'] -= draw_money
                print('取款成功')
                break



if __name__ == '__main__':
    atm = ATM()
    while True:
          card = atm.login()
          while True:
               choice = atm.choose()
               if choice == '1':
                    atm.show(card)
               elif choice == '2':
                    atm.draw(card)
               elif choice == '3':
                    atm.save(card)
                    break

