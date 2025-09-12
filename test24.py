# คำสั่ง Break, Continue
# break ใน Loop ทำงานเมื่อใดจบ Loop ทันที
# continue ใน Loop ทำงานเมื่อใดจบ Loop แค่รอบนั้นทันทีให้ไปรอบต่อไปเลย

for aa in range(5) :
    if aa == 2 :
        break
    print(aa, 'Hello')

print('-------------------')
for aa in range(5) :
    if aa == 2 :
        continue
    print(aa, 'Hello...')