import tkinter as tk

window = tk.Tk()
window.geometry('900x700')

def writehandler():
    f = open('customers.txt', 'a', encoding='utf-8')
    nameof = name.get()
    dateof = date.get()
    servof = service.get()
    priceof = price.get()
    discof = discount.get()
    if discof == 'да':
        priceof = round(float(priceof) * 0.9)
        priceof = str(priceof)
    a = [nameof, dateof, servof, priceof, discof]
    cani = 0
    for e in a:
        if e == '':
            info['text'] = 'Какое то поле не заполнено'
            cani = 0
        else:
            info['text'] = ''
            cani = 1
    if cani == 1:
        for e in a:
            if e == priceof:
                f.write('_' + str(e) + '*' + ' ')
            else:
                f.write(e + ' ')
        f.write('&' + '\n')
        f.close()
        cani = 0
        name.delete(0, len(nameof))
        date.delete(0, len(dateof))
        service.delete(0, len(servof))
        price.delete(0, len(priceof))
        discount.delete(0, len(discof))


frame_top = tk.Frame(window, bg='#9BA2D6', bd=5)
frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.5)

frame_bottom = tk.Frame(window, bg='#5C6BDB', bd=5)
frame_bottom.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

write = tk.Label(frame_top, text='Записать', bg='#ffb700', font=60)
write.pack(anchor="n")

writeN = tk.Label(frame_top, text='Имя Фамилия', bg='#1AEBE7', font=40)
writeN.place(x=10, y=25)
name = tk.Entry(frame_top, bg='white', font=40)
name.place(x=10, y=50)

writeD = tk.Label(frame_top, text='Дата', bg='#1AEBE7', font=40)
writeD.place(x=300, y=25)
date = tk.Entry(frame_top, bg='white', font=40)
date.place(x=300, y=50)

writeS = tk.Label(frame_top, text='Услуга', bg='#1AEBE7', font=40)
writeS.place(x=600, y=25)
service = tk.Entry(frame_top, bg='white', font=40)
service.place(x=600, y=50)

writeP = tk.Label(frame_top, text='Цена', bg='#1AEBE7', font=40)
writeP.place(x=10, y=100)
price = tk.Entry(frame_top, bg='white', font=40)
price.place(x=10, y=125)

writeD = tk.Label(frame_top, text='Скидка (да/нет)', bg='#1AEBE7', font=40)
writeD.place(x=300, y=100)
discount = tk.Entry(frame_top, bg='white', font=40)
discount.place(x=300, y=125)


btn = tk.Button(frame_top, text='Записать', command=writehandler)
btn.place(x=10, y=175)

info = tk.Label(frame_top, text='', bg='red', font=40)
info.place(x=420, y=200)

####################################################

def moneyCounter():
    f = open('customers.txt', 'rt', encoding='utf-8')
    s = f.read()
    check = 0
    sum = ''
    for i in s:
        if check == 1:
            sum = sum + i
        if i == '_':
            check = 1
        if i == '*':
            check = 0

    sum = sum.split('*')
    wholeSum = 0
    wholeCust = 0
    for e in sum:
        if e == '':
            break
        else:
            e = int(e)
            wholeSum = wholeSum + e
            wholeCust = wholeCust + 1
    infoSum['text'] = str(wholeSum) + ' рублей за все время'
    infoCust['text'] = str(wholeCust) + ' клиентов за все время'
    f.close()

def findHandler():
    f = open('customers.txt', 'rt', encoding='utf-8')
    s = f.read().lower()
    findof = find.get()
    findof = findof.lower()
    s = s.split('&')
    found = ''
    for e in s:
        if e.find(findof) > 0:
            found = found + e.replace('*', '').replace('_', '') + '\n'
    infoFind['text'] = found
    f.close()


btn = tk.Button(frame_bottom, text='Показать сумму', command=moneyCounter)
btn.place(x=10, y=10)
infoSum = tk.Label(frame_bottom, text='', bg='white', font=40)
infoSum.place(x=10, y=40)
infoCust = tk.Label(frame_bottom, text='', bg='white', font=40)
infoCust.place(x=10, y=70)

findS = tk.Label(frame_bottom, text='Найти по имени/дате', bg='#9ACAD6', font=40)
findS.place(x=300, y=10)
find = tk.Entry(frame_bottom, bg='white', font=40)
find.place(x=300, y=40)
btn = tk.Button(frame_bottom, text='Искать', command=findHandler)
btn.place(x=300, y=70)
infoFind = tk.Label(frame_bottom, text='', bg='white', font=40)
infoFind.place(x=300, y=100)

window.mainloop()
