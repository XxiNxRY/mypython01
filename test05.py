# คำสั่งรับค่าข้อความ string ทางแป้นพิมพ์ ใช่ฟังก์ชัน input()



fullname = input('ป้อนชื่อคุณ: ')
year_born = input('ป้อนปีเกิดคุณ: ')
print('----------------')
print(f'สวัสดีคุณ {fullname}')
print(f'คุณเกิดในปี {year_born} ตอนนี้คุณมีอายุ {2568 - int(year_born)} ')
print('----------------')
# ใช้ ,
print('----------------')
print('สวัสดีคุณ',fullname)
print('คุณเกิดในปี',year_born ,'ตอนนี้คุณมีอายุ',2568 - int(year_born))
# ใช้ + 
print('----------------')
print('สวัสดีคุณ '+fullname)
print('คุณเกิดในปี '+year_born +' ตอนนี้คุณมีอายุ '+str(2568 - int(year_born)))
# ใช้ format()
print('----------------')
print('สวัสดีคุณ {}'.format(fullname))
print(' คุณเกิดในปี {}'.format(year_born) +' ตอนนี้คุณมีอายุ {}'.format(2568 - int(year_born)))