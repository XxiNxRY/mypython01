# 2. have parameter no return

'''
def func_name(param1, param2, ...) :
    คำสั่ง
    คำสั่ง
    ......
'''

def showHi(your_name):
    print('--------------------')
    print(f'สวัสดี {your_name} !')
    print('--------------------')

def sumNumber(n1, n2):
    print('--------------------')
    print(f'ผลบวกของ {n1} และ {n2} คือ {n1 + n2}')
    print('--------------------')

    showHi('สมชาย') # ข้อมูลที่ส่งให้ parameter เรียกว่า argument
    showHi('สมหญิง')
    sumNumber(10, 20)
    showHi('Sombat')
    