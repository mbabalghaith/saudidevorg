from tkinter import *
from tkinter import ttk
from tkinter import messagebox            #ملاحظة , الكود اشتغل معي في  IDLE ,في pycharm لم يظهر لي خطا ولكن لم تظهر النوافذ
from random import randint                 # كان بالامكان افضل من كذا ولكن لظروف عملي .. 

window = Tk()
window.geometry('708x556+400+100')  #تحديد طول وعرض النافذة ومكان ظهورها
window.title('Tic Tac Toe')
window.configure(background='blue')  #لون خلفية نافذى اللعب , لم تظهر في جهازي ولكن ظهرت في جهاز آخر !!
player1 = 1     #هنا متغير يحدد دور اي لاعب 1 يعني اللاعب الاول و2 يعني اللاعب الثاني

p1 = [] #لستة للاعب الاول راح تضاف  فيها اماكن اللعب اللي يختارها الاعب

p2 = [] #لستة للاعب الثاني

draw = 0 #متغير عشان يحسب كم لعبة انلعبت الين يووصل الى 9 مرات وماحد فاز معناته تعادل


def mainwin():
    # هذي الدالة تفتح شاشة صغيرة اول مايشتغل البرنامح وفيها سؤال للاعب يختار كم لاعب
    global mwin
    mwin = Tk()
    mwin.title('Tic Tac Toe')
    mwin.geometry('250x200+600+300')
    mwin.resizable(False, False)
    window.state('withdrawn') #هذي النافذة الرئيسية اللي فيها الازرار , في البداية تكون مخفية بهذا الامر
    # الليبل يعرض الرسالة والازرار الي تحت يحدد كم لاعب من خلال ضغطك لاي زر راح يستدعي دالة بلاي مع قيمة هذي القيمة هي اللي تحدد اذا يلعب مع لاعب ثاني او الكمبيوتر
    Label(mwin, text='How many players?').pack()
    ttk.Button(mwin, text='2 Players', command=lambda: play(1)).pack()

    ttk.Button(mwin, text='1 Player', command=lambda: play(2)).pack()


# --------------------------------------------------
def play(opp): #قيمة المتغير اخذناها من الدالة الي فوق وهي اختيار اللاعب مع مين يلعب
    global window

    window.resizable(False, False)  # تمنع اليوزر من تغيير حجم النافذة
    mwin.state('withdrawn')
    window.state('normal')
    window.title('Tic Tac Toe  PLAYER 1 (X)  ')
    global p1 #عرفناها فوق ورجعت عرفتها هنا قلوبال , وفضيتها تحت عشان لو اللاعب يبي يلعب مرة ثانية تتصفر
    global p2
    p1 = []
    p2 = []
    global but1
    global but2
    global but3
    global but4
    global but5
    global but6
    global but7
    global but8
    global but9
    global draw
    global player1
    player1 = 1
    draw = 0
    # buttons

    #هنا عرفنا الازرار ومكان ظهورها عن طريق row & column واذا ضغطتها تستدعي دالة تطلب قيمتين الاولى هي ID وهو مكان لعب اللاعب والثانية هي قيمة الخصم (1 لاعب ثاني , 2 كمبيوتر)
    but1 = ttk.Button(window, text='')
    but1.grid(row=0, column=0, sticky='snew', ipadx=80, ipady=80)
    but1.config(command=lambda: buttonclick(1, opp))

    but2 = ttk.Button(window, text='')
    but2.grid(row=0, column=1, sticky='snew', ipadx=80, ipady=80)
    but2.config(command=lambda: buttonclick(2, opp))

    but3 = ttk.Button(window, text='')
    but3.grid(row=0, column=2, sticky='snew', ipadx=80, ipady=80)
    but3.config(command=lambda: buttonclick(3, opp))

    but4 = ttk.Button(window, text='')
    but4.grid(row=1, column=0, sticky='snew', ipadx=80, ipady=80)
    but4.config(command=lambda: buttonclick(4, opp))

    but5 = ttk.Button(window, text='')
    but5.grid(row=1, column=1, sticky='snew', ipadx=80, ipady=80)
    but5.config(command=lambda: buttonclick(5, opp))

    but6 = ttk.Button(window, text='')
    but6.grid(row=1, column=2, sticky='snew', ipadx=80, ipady=80)
    but6.config(command=lambda: buttonclick(6, opp))

    but7 = ttk.Button(window, text='')
    but7.grid(row=2, column=0, sticky='snew', ipadx=80, ipady=80)
    but7.config(command=lambda: buttonclick(7, opp))

    but8 = ttk.Button(window, text='')
    but8.grid(row=2, column=1, sticky='snew', ipadx=80, ipady=80)
    but8.config(command=lambda: buttonclick(8, opp))

    but9 = ttk.Button(window, text='')
    but9.grid(row=2, column=2, sticky='snew', ipadx=80, ipady=80)
    but9.config(command=lambda: buttonclick(9, opp))


def buttonclick(id, opp):
    global player1        #مع كل ضغطة زر راح يستدعي هذي الدالة
    global p1
    global p2
    global draw
    if player1 == 1:   #هذا المتغير عرفناه فوق وهو يحدد دور اي لاعب , اذا كان واحد معناه اللاعب الاول ويستدعي دالة ويرسل لها X وهو رمز اللاعب الاول وid وهو مكان لعبه
        setlayout(id, 'X')
        p1.append(id)
        window.title('Tic Tac Toe   PLAYER2 (O)   ') #طبعا بعد مايلعب اللاعب الاول راح يغير العنوان
        #print ('p1:{}'.format(p1)) #اذا حاب تشوف كيف يجمع ارقام اللعب في اللستة
        player1 += 1            #هنا يزيد 1 عشان يصير دور اللاعب الثاني
        draw += 1
        if draw != 9: #المتغير اللي عرفناه فوق عشان يعرف نتيجة التعادل , لايساوي 9 وهو عدد مرات اللعب كاملة
            checkwinner(opp) #دالة للتاكد من وجود فايز نستدعيها بعد كل مرة لعب مع رقم الخصم
            if opp == 2: #هنا نستفيد من رقم الخصم , فوق قلنا له اذا كان 1 يعني لاعب ثاني واذا 2 معناته كمبيوتر
                checkwinner(opp)
                autoplay(opp) #دالة للعب الكمبيوتر, يروح للدالة ويسوي عملياته ويرجع للدالة هذي وقيمة player 2 ف ينفذ الكود اللي تحت


    elif player1 == 2:
        setlayout(id, 'O')
        p2.append(id)
        window.title('Tic Tac Toe   PLAYER1 (X) ')
        #print ('p2:{}'.format(p2))
        player1 -= 1
        draw += 1
    checkwinner(opp)

def setlayout(id, playersmb):        #هذي الدالة تاخذ متغيرين id وهو مكان لعب الاعب والثاني وهو رمز اللاعب شوف الدالة الي فوقها
    if id == 1:
        but1.config(text=playersmb)  #في كل مرة تضغط على زر اللعب تجي للدالة تسوي حاجتين الاولى تكتب رمز اللعب على الزر , الثانية تخلي الزر disable عشان ماتضغط عليه مرة ثانية
        but1.state(['disabled'])
    elif id == 2:
        but2.config(text=playersmb)
        but2.state(['disabled'])
    elif id == 3:
        but3.config(text=playersmb)
        but3.state(['disabled'])
    elif id == 4:
        but4.config(text=playersmb)
        but4.state(['disabled'])
    elif id == 5:
        but5.config(text=playersmb)
        but5.state(['disabled'])
    elif id == 6:
        but6.config(text=playersmb)
        but6.state(['disabled'])
    elif id == 7:
        but7.config(text=playersmb)
        but7.state(['disabled'])
    elif id == 8:
        but8.config(text=playersmb)
        but8.state(['disabled'])
    elif id == 9:
        but9.config(text=playersmb)
        but9.state(['disabled'])

#-------------------------------------------------------------------

def autoplay(opp):  #هذي دالة اللعب العشوائ (مافيها اي ذكاء اصطناعي ولكن الكمبيوتر يلعب :))
    global p1
    global p2

    cells = []     #لستة عشان نحط فيها الاماكن المتاحة للعب
    for cel in range(9): #في المجال من صفر الى 8
        if (not (cel + 1 in p1) and not (cel + 1 in p2)): #يشيك اذا الرقم موجود في لستة p1  ولستة p2  وهي زي ماقلنا ارقام اماكن اللعب
            cells.append(cel + 1)  #اذا موموجودة في اللستةp1 & p2 يضيفها في اللستة الفاضية اللي سويناها

    rnd = randint(0, len(cells) - 1) #دالة تنشئ رقم عشوائي من 1 الى طول اللستة
    buttonclick(cells[rnd], opp) #هنا نستدعي الدالة الي فوق ونعطيها قيمة id هي الرقم العشوائي في اللستة cells

#--------------------------------------------------------------------------

def checkwinner(opp):
    winner = 0 #متغير لتحديد الفايز
    global draw
    if ((1 in p1) and (2 in p1) and (3 in p1)): #شروط حالات الفوز في اللعبة , P1 اللستة حق اللاعب الاول , نقوله لا تواجدت الارقام التالية في اللستة معناته هو الفايز , الارقام هي امكان لعب اللاعب ومثلها في p2
        winner = 1

    if ((1 in p2) and (2 in p2) and (3 in p2)):
        winner = 2

    if ((4 in p1) and (5 in p1) and (6 in p1)):
        winner = 1

    if ((4 in p2) and (5 in p2) and (6 in p2)):
        winner = 2

    if ((7 in p1) and (8 in p1) and (9 in p1)):
        winner = 1

    if ((7 in p2) and (8 in p2) and (9 in p2)):
        winner = 2

    if ((1 in p1) and (5 in p1) and (9 in p1)):
        winner = 1

    if ((1 in p2) and (5 in p2) and (9 in p2)):
        winner = 2

    if ((3 in p1) and (5 in p1) and (7 in p1)):
        winner = 1

    if ((3 in p2) and (5 in p2) and (7 in p2)):
        winner = 2


    if ((1 in p1) and (4 in p1) and (7 in p1)):
        winner = 1


    if ((1 in p2) and (4 in p2) and (7 in p2)):
        winner = 2

    if ((2 in p1) and (5 in p1) and (8 in p1)):
        winner = 1

    if ((2 in p2) and (5 in p2) and (8 in p2)):
        winner = 2

    if ((3 in p1) and (6 in p1) and (9 in p1)):
        winner = 1

    if ((3 in p2) and (6 in p2) and (9 in p2)):
        winner = 2

    if winner == 1: #بعد مايشيك على شروط الفوز كلها اذا فيه فايز راح يكون للمتغير قيمة 1 للفايز الاول و2 للفايز الثاني وفي كل مرة لعب راح يفحص اذا فيه فايز او لا
        messagebox.showinfo(title='There is winner :)', message='Player 1 is winner')
        endgame() #اذا فيه فايز راح يستدعي دالة نهاية اللعب
        sys.exit()
    if winner == 2:
        messagebox.showinfo(title='There is winner :)', message='Player 2  is winner')
        endgame()
        sys.exit()
    if draw == 9: #عدد مرات اللعب اذا وصلت 9 زي ماكتبت فوق يجي يشيك اذا فيه فاز واذا مافي معناته تعادل
        messagebox.showinfo(title='Game Over', message='The final result is draw')
        endgame()
        sys.exit()

#-------------------------------------------------------------------------------


def endgame():
    but1.state(['disabled'])
    but2.state(['disabled'])                #دالة نهاية اللعبة يغير حالة الازرار الى dis ويطلع لك رسالة هل تريد اللعب مرة اخرى
    but3.state(['disabled'])
    but4.state(['disabled'])
    but5.state(['disabled'])
    but6.state(['disabled'])
    but7.state(['disabled'])
    but8.state(['disabled'])
    but9.state(['disabled'])
    if messagebox.askyesno('Question', 'Do you want play again?') == True:
        mainwin() #في حالة الجواب ب yes يستدعي الدالة الاولى
    else:
        window.destroy() #اذا الجواب لا ينهي النافذى الاولى والثانية وينهي اللعب
        mwin.destroy()
        sys.exit()


mainwin()

