import tkinter as tk
import json

window = tk.Tk()
window.geometry('900x700')


def autoFindPersonByName(ch):
    ch = ch.get()
    customers = open("test.json", "r", encoding='utf-8')
    customers = json.load(customers)
    personName = ''
    personId = 0
    for customer in customers:
        if ch.lower() in customer['name'].lower():
            personName = customer['name']
            personId = customer['id']
            person = tk.Button(frame_top, text=str(customer['name']), width=25,
                               command=lambda: autoFillPerson(idP=int(personId), nameP=str(personName)))
            person.place(x=75, y=70)


def autoFindPersonById(n):
    ch = n.get()
    customers = open("test.json", "r", encoding='utf-8')
    customers = json.load(customers)
    personName = ''
    personId = 0
    for customer in customers:
        print(ch, customer['id'], ch == customer['id'])
        if int(ch) == customer['id']:
            personName = customer['name']
            personId = customer['id']
            person = tk.Button(frame_top, text=str(customer['name']), width=25,
                               command=lambda: autoFillPerson(idP=int(personId), nameP=str(personName)))
            person.place(x=75, y=70)


def autoFillPerson(idP, nameP):
    print(nameP)
    Id.delete(0, 500)
    name.delete(0, 500)
    Id.insert(0, idP)
    name.insert(0, nameP)


def writehandler(nameP='', dateP='', serviceP='', priceP=0, discountP=0):
    customers = open("test.json", "r", encoding='utf-8')
    customers = json.load(customers)
    new = {
        "id": 1,
        "name": nameP,
        "services": [
            {
                "date": dateP,
                "service": serviceP,
                "cost": priceP,
                "sale": discountP,
            }
        ],
        "nvisits": 1
    }
    fieldsFilled = True
    for i in new:
        if not new[i]:
            fieldsFilled = False
    if fieldsFilled:
        newExist = False
        for customer in customers:
            if new['name'] == customer['name']:
                newExist = True

        if not newExist:
            new['id'] = int(customers[-1]['id']) + 1
            customers.append(new)
        else:
            for customer in customers:
                if customer['name'] == new['name']:
                    customer['services'].append(new['services'][0])
                    customer['nvisits'] += 1

        with open("test.json", "w", encoding='utf-8') as fh:
            json.dump(customers, fh)
        f = open('customers.txt', 'w', encoding='utf-8')
        for c in customers:
            f.write(str(c) + '\n')
        f.close()
        Id.delete(0, 1000)
        name.delete(0, len(nameP))
        date.delete(0, len(dateP))
        service.delete(0, len(serviceP))
        price.delete(0, 1000)
        discount.delete(0, 1000)
    else:
        info['text'] = 'Какое то поле не заполнено'


frame_top = tk.Frame(window, bg='#9BA2D6', bd=5)
frame_top.place(relx=0, rely=0, relwidth=1, relheight=0.5)

frame_bottom = tk.Frame(window, bg='#5C6BDB', bd=5)
frame_bottom.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

write = tk.Label(frame_top, text='Записать', bg='#ffb700', font=60)
write.pack(anchor="n")

num = tk.IntVar()
num.trace("w", lambda names, index, mode, n=num: autoFindPersonById(n))
writeId = tk.Label(frame_top, text='ID', bg='#1AEBE7', font=40)
writeId.place(x=10, y=25)
Id = tk.Entry(frame_top, bg='white', font=40, width=5, textvariable=num)
Id.place(x=10, y=50)

char = tk.StringVar()
char.trace("w", lambda names, index, mode, ch=char: autoFindPersonByName(ch))
writeN = tk.Label(frame_top, text='Имя Фамилия', bg='#1AEBE7', font=40)
writeN.place(x=75, y=25)
name = tk.Entry(frame_top, bg='white', font=40, width=25, textvariable=char)
name.place(x=75, y=50)

writeD = tk.Label(frame_top, text='Дата', bg='#1AEBE7', font=40)
writeD.place(x=310, y=25)
date = tk.Entry(frame_top, bg='white', font=40, width=10)
date.place(x=310, y=50)

writeS = tk.Label(frame_top, text='Услуга', bg='#1AEBE7', font=40)
writeS.place(x=410, y=25)
service = tk.Entry(frame_top, bg='white', font=40, width=50)
service.place(x=410, y=50)

writeP = tk.Label(frame_top, text='Цена', bg='#1AEBE7', font=40)
writeP.place(x=10, y=100)
price = tk.Entry(frame_top, bg='white', font=40)
price.place(x=10, y=125)

writeD = tk.Label(frame_top, text='Сумма скидки', bg='#1AEBE7', font=40)
writeD.place(x=300, y=100)
discount = tk.Entry(frame_top, bg='white', font=40)
discount.place(x=300, y=125)

btn = tk.Button(frame_top, text='Записать', command=lambda: writehandler(nameP=name.get(), dateP=date.get(),
                                                                         serviceP=service.get(),
                                                                         priceP=int(price.get()),
                                                                         discountP=int(discount.get())))
btn.place(x=10, y=175)

info = tk.Label(frame_top, text='', bg='red', font=40)
info.place(x=420, y=200)


####################################################

def moneyCounter():
    customers = open("test.json", "r", encoding='utf-8')
    customers = json.load(customers)
    sum = 0
    visits = 0
    for e in customers:
        for i in e['services']:
            sum += i['cost']
    for e in customers:
        visits += e['nvisits']
    infoSum['text'] = str(sum) + ' рублей за все время'
    infoCust['text'] = str(visits) + ' посещений за все время'


def moreInfo(_id):
    extraWindow = tk.Tk()
    extraWindow.geometry('600x500')
    inframe = tk.Frame(extraWindow, bg='#6EEBA4', bd=5)
    inframe.place(relx=0, rely=0, relwidth=1, relheight=1)
    customers = open("test.json", "r", encoding='utf-8')
    customers = json.load(customers)
    for e in customers:
        if _id == e['id']:
            sum = 0
            for i in e['services']:
                sum += i['cost']
            nameLine = tk.Label(inframe, text='Имя: ' + e['name'], bg='white', font=40)
            nameLine.place(x=10, y=10)
            visitsLine = tk.Label(inframe, text='Посещений: ' + str(e['nvisits']), bg='white', font=30)
            visitsLine.place(x=120, y=10)
            wasteLine = tk.Label(inframe, text='Всего трат: ' + str(sum), bg='white', font=30)
            wasteLine.place(x=250, y=10)
            lbox = tk.Listbox(inframe, width=80, font=20)
            lbox.place(x=10, y=40)
            for c in e['services']:
                line = c['date'] + ' ' + c['service'] + ' Стоимость: ' + str(c['cost']) + ' Скидка: ' + str(c['sale'])
                lbox.insert(0, str(line))



def findHandler():
    customers = open("test.json", "r", encoding='utf-8')
    customers = json.load(customers)
    findof = find.get()
    findof = findof.lower()
    found = ''
    foundId = 0
    for e in customers:
        if findof in e['name'].lower():
            found = e['name'] + " Посещений всего: " + " " + str(e['nvisits'])
            foundId = e['id']
            btn = tk.Button(frame_bottom, bg='#6EEBA4', text='Расширенная информация', command=lambda: moreInfo(foundId))
            btn.place(x=300, y=130)
    infoFind['text'] = found


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
