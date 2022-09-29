# 判断病人是否付钱 返回结果

is_pay = False

def pay():
    # 付钱
    global is_pay  # 标记is_pay为全局变量，才会去修改上面定义的is_pay
    is_pay = True
    return is_pay

def get_medicine(is_pay):
    if is_pay == True:
        print('支付完成，请取药')
        return '药物'
    else:
        print('尚未支付')
        return None

get_medicine(is_pay)
pay()
medicine = get_medicine(is_pay)
print(medicine)

