sales = float(input('please input your sales:'))

while sales >= 0:
    if sales <1000 :
        bonus = sales * 0.1
        print(f'your bonus is : {bonus:.2f}')
    else:
        bonus = sales * 0.15
        print(f'your bonus is : {bonus:.2f}')
    sales = float(input('please input your sales:'))
