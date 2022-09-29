weight = float(input('请输入苹果的重量：'))
color = input('请输入苹果的颜色：')

if weight > 10:
    if color == '黄色':
        print('黄色大苹果')
    elif color == '红色':
        print('红色大苹果')
else:
    print('苹果太小，不要了')

    
