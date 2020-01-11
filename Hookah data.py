from tkinter import *
from tkinter import ttk
import os, time


root = Tk()
root.title('Hookah Keeper - Beta')
root.geometry('800x700+280+5')
root.resizable(False, True)

frameH = Frame(root, width=800, height=1000, bg='#1b1b1b')
frameH.place(x=-2, y=-1)

img1 = PhotoImage(file='hookah background 2 + logo.gif')
img = Label(frameH, image=img1, width=800, height=700)
img.place(x=-2, y=-1)

hookah_data = open("hookah_data.txt", "a")

data = ttk.Entry(frameH, width=20)
data.place(x=29, y=100)

btn_data = ttk.Button(frameH, text='ok', width=4)
btn_data.bind('<Button-1>', lambda event: hookah_data.write('\n\n' + data.get() + '\n' + 'стол' + '\t' + 'подача' + '\t' + 'уголь'
                                                            + '\t' + 'конец' + '\t' + 'цена' + '\t' + 'вид'))
btn_data.place(x=160, y=98)

stol = ttk.Entry(frameH, width=6)
podacha = ttk.Entry(frameH, width=11)
cena = ttk.Entry(frameH, width=7)
vid = ttk.Entry(frameH, width=16)
stol.place(x=29, y=335)
podacha.place(x=87, y=335)
cena.place(x=328, y=335)
vid.place(x=387, y=335)

kaliki = 0
perezabivki = 0
kassa = 0


def btn_CE(stol, podacha, cena, vid):
    global kassa
    kassa += cena
    label(frameH, str(kassa) + ' р.', 100, 165)

    global kaliki
    kaliki += 1
    label(frameH, str(kaliki) + ' шт.', 320, 165)

    if vid == 'перезабивка':
        global perezabivki
        perezabivki += 1
    label(frameH, str(perezabivki) + ' шт.', 320, 203)

    zp = 5 * kaliki - 5 * perezabivki
    label(frameH, str(zp) + ' р.', 100, 203)

    def list_create(stol, podacha, cena, vid):
        stol_ = Label(frameH, text=stol, bg='#333', fg='#fff', font='arial 11')
        stol_.place(x=28, y=410 + 30 * (kaliki - 1))

        podacha_ = Label(frameH, text=podacha, bg='#333', fg='#fff', font='arial 11')
        podacha_.place(x=88, y=410 + 30 * (kaliki - 1))

        c = Checkbutton(frameH, variable=IntVar(), bg='#1b1b1b')
        c.place(x=540, y=410 + 30 * (kaliki - 1))
        c2 = Checkbutton(frameH, variable=IntVar(), bg='#1b1b1b')
        c2.place(x=640, y=410 + 30 * (kaliki - 1))
        global h_p, m_p, h_u, m_u, h_k, m_k
        h_p, m_p = int(podacha[0] + podacha[1]), int(podacha[3] + podacha[4])
        m_u = m_p + 35
        if m_u > 59:
            h_u = h_p + 1
            m_u -= 60
        else:
            h_u = h_p

        h_k = h_u + 1
        m_k = m_u + 15
        if m_k > 59:
            h_k = h_k + 1
            m_k -= 60
        if h_u == 24: h_u = 0
        elif h_u == 25: h_u = 1
        elif h_u == 26: h_u = 2
        if h_k == 24: h_k = 0
        elif h_k == 25: h_k = 1
        elif h_k == 26: h_k = 2
        ugol = str(h_u) + ' ' + str(m_u)
        konec = str(h_k) + ' ' + str(m_k)

        label(frameH, ugol, 168, 410 + 30 * (kaliki - 1))
        label(frameH, konec, 248, 410 + 30 * (kaliki - 1))
        label(frameH, cena, 328, 410 + 30 * (kaliki - 1))
        label(frameH, vid, 398, 410 + 30 * (kaliki - 1))

    list_create(stol, podacha, cena, vid)

    hookah_data.write('\n' + str(stol) + '\t' + str(h_p) + ':' + str(m_p) + '\t' + str(h_u) + ':' + str(m_u)
                      + '\t' + str(h_k) + ':' + str(m_k) + '\t' + str(cena) + ' р.' + '\t' + str(vid))


def label(frame, textL, xL, yL):
    nameL = Label(frame, text=textL, bg='#333', fg='#fff', font='arial 11')
    nameL.place(x=xL, y=yL)


btnCE = ttk.Button(frameH, text='добавить заказ', width=80)
btnCE.bind('<Button-1>', lambda event: btn_CE(int(stol.get()),
                                              str(podacha.get()),
                                              int(cena.get()),
                                              str(vid.get())))

btnCE.place(x=28, y=370)

#  itog = '\n' + 'кол-во кальянов: ' + str(kaliki) + '\n' + 'из них перезабивки: ' + str(perezabivki) + '\n' + 'касса: ' + str(kassa) + 'р.' + '\n' + 'з/п: ' + str(5 * kaliki - 5 * perezabivki) + 'р.'
#  hookah_data.write(itog)
btn_otchet = ttk.Button(frameH, text='сохранить отчёт', width=40)
btn_otchet.bind('<Button-1>', lambda event: hookah_data.close())

btn_otchet.place(x=28+500, y=370)

time1 = ''
clock = Label(frameH, bg='#333', fg='#fff', font='arial 16')
clock.place(x=215, y=98)


def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


tick()

root.mainloop()
