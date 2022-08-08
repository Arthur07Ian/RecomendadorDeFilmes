from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# Cores e fontes -------------------------------------------------------
co_bg = '#262626'
co_nav = '#171717'
fon_padrao = ('Arial 10')


# Configs da janela ----------------------------------------------------
janela = Tk()
janela.title('Recomendador de Filmes')
janela.config(bg=co_bg)
style = ttk.Style()

style.theme_create( "my_theme", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] }},
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": co_bg },
            "map":       {"background": [("selected", co_bg)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("my_theme")
style.configure('TNotebook.Tab', foreground='white')
style.configure('TNotebook', background=co_nav, borderwidth=0)


# Variaveis de mudança e imagens --------------------------------------------------
check1_var = IntVar()
check2_var = IntVar()
check3_var = IntVar()

check1_var2 = IntVar()
check2_var2 = IntVar()
check3_var2 = IntVar()


img_logo = Image.open('logo.png')
img_logo = img_logo.resize((30, 30), Image.ANTIALIAS)
img_logo = ImageTk.PhotoImage(img_logo)

img_filme1 = Image.open('Ultimato.png')
img_filme1 = img_filme1.resize((30, 40), Image.ANTIALIAS)
img_filme1 = ImageTk.PhotoImage(img_filme1)

img_filme2 = Image.open('v&f.png')
img_filme2 = img_filme2.resize((30,40), Image.ANTIALIAS)
img_filme2 = ImageTk.PhotoImage(img_filme2)

img_filme3 = Image.open('godzilla.png')
img_filme3 = img_filme3.resize((30,40), Image.ANTIALIAS)
img_filme3 = ImageTk.PhotoImage(img_filme3)


# Funções -----------------------------------------------------------------
txt_user1 = 'Usuário 1, para você recomendamos: '
txt_user2 = 'Usuário 2, para você recomendamos: '
enviou1 = False
enviou2 = False

txt_filme1 = ''
txt_filme2 = ''
txt_filme3 = ''

txt2_filme1 = ''
txt2_filme2 = ''
txt2_filme3 = ''

end = False

def comparar2():
    global txt2_filme1
    global txt2_filme2
    global txt2_filme3
    global enviou2

    if check1_var.get() == 1 and check1_var2.get() == 0:
        txt2_filme1 += 'Avengers'
    if check2_var.get() == 1 and check2_var2.get() == 0:
        txt2_filme2 += 'Velozes e Furiosos'
    if check3_var.get() == 1 and check3_var2.get() == 0:
        txt2_filme3 += 'Godzilla'
    enviou2 = True
    botao2_enviar.config(state=DISABLED)



def comparar1():
    global txt_filme1 
    global txt_filme2 
    global txt_filme3 
    global enviou1

    if check1_var.get() == 0 and check1_var2.get() == 1:
        txt_filme1 += 'Avengers'
    if check2_var.get() == 0 and check2_var2.get() == 1:
        txt_filme2 += 'Velozes e Furiosos'
    if check3_var.get() == 0 and check3_var2.get() == 1:
        txt_filme3 += 'Godzilla'
    enviou1 = True
    botao_enviar.config(state=DISABLED)

def end_app():
    if enviou1 == True and enviou2 == True:

        label1_resposta.grid(row=4, column=0, columnspan=2, rowspan=4, sticky='w')

        if check1_var.get() == 0 and check1_var2.get() == 1:
            Label(frame_baixo1, width=45, height=1, padx=10, text=txt_filme1, bg=co_bg, fg='white', font=('Arial 12 bold'), anchor='nw').grid()
        if check2_var.get() == 0 and check2_var2.get() == 1:
            Label(frame_baixo1, width=45, height=1, padx=10, text=txt_filme2, bg=co_bg, fg='white', font=('Arial 12 bold'), anchor='nw').grid()
        if check3_var.get() == 0 and check3_var2.get() == 1:
            Label(frame_baixo1, width=45, height=1, padx=10, text=txt_filme3, bg=co_bg, fg='white', font=('Arial 12 bold'), anchor='nw').grid()

        
        label2_resposta.grid(row=4, column=0, columnspan=2, rowspan=4, sticky='w')

        if check1_var.get() == 1 and check1_var2.get() == 0:
            Label(frame_baixo2, width=45, height=1, padx=10, text=txt2_filme1, bg=co_bg, fg='white', font=('Arial 12 bold'), anchor='nw').grid()
        if check2_var.get() == 1 and check2_var2.get() == 0:
            Label(frame_baixo2, width=45, height=1, padx=10, text=txt2_filme2, bg=co_bg, fg='white', font=('Arial 12 bold'), anchor='nw').grid()
        if check3_var.get() == 1 and check3_var2.get() == 0:
            Label(frame_baixo2, width=45, height=1, padx=10, text=txt2_filme3, bg=co_bg, fg='white', font=('Arial 12 bold'), anchor='nw').grid()


def botao1():
    comparar1()
    end_app()

def botao2():
    comparar2()
    end_app()



# Notebooks ---------------------------------------------------------------
notebook = ttk.Notebook(janela, width=604)
notebook.grid(row=1, column=0, columnspan=2)


# Frames ---------------------------------------------------------------
frame_cima = Frame(janela, width=400, height=40, relief='raised', bg=co_nav)
frame_cima.grid(row=0, column=0)

frame_baixo1 = Frame(notebook, width=587, height=260, relief='flat', bg=co_bg)
frame_baixo1.pack(fill='both', expand=True)

frame_baixo2 = Frame(notebook, width=587, height=260, relief='flat', bg=co_bg)
frame_baixo2.pack(fill='both', expand=True)

notebook.add(frame_baixo1, text='Usuario 1')
notebook.add(frame_baixo2, text='Usuario 2')

# Widgets nav ----------------------------------------------------------------
label_logo = Label(frame_cima, image=img_logo)
label_logo.grid(row=0, column=0)

label_titulo = Label(frame_cima, width=39, height=1, padx=10, text='Recomendador de Filmes', font=('Ivy 17 bold'), relief='flat', bg=co_nav, fg='white', anchor='w')
label_titulo.grid(row=0, column=1, columnspan=2)

# Widgets main1 -------------------------------------------------------------------
label_qualassistiu = Label(frame_baixo1, width=45, height=1, padx=10, text='Qual desses Filmes você assistiu?', bg=co_bg, fg='white', font=('Ivy 15'), anchor='w')
label_qualassistiu.grid(row=0, column=0, columnspan=2, sticky='w')

check_filme1 = Checkbutton(frame_baixo1,padx=15, pady=15, text='Avengers',font=('Arial 20'),image=img_filme1,compound='left', variable=check1_var, fg='white', bg=co_bg, onvalue=1, offvalue=0, activebackground=co_bg, activeforeground='white', selectcolor='black')
check_filme1.grid(row=1, column=0, sticky='w')

check_filme2 = Checkbutton(frame_baixo1,padx=15, pady=15, text='Velozes e Furiosos',font=('Arial 20'),image=img_filme2,compound='left', variable=check2_var, fg='white', bg=co_bg, onvalue=1, offvalue=0, activebackground=co_bg, activeforeground='white', selectcolor='black')
check_filme2.grid(row=2, column=0, sticky='w')

check_filme3 = Checkbutton(frame_baixo1,padx=15, pady=15, text='Godzilla',font=('Arial 20'),image=img_filme3,compound='left', variable=check3_var, fg='white', bg=co_bg, onvalue=1, offvalue=0, activebackground=co_bg, activeforeground='white', selectcolor='black')
check_filme3.grid(row=3, column=0, sticky='w')

botao_enviar = Button(frame_baixo1, width=15, height=1, text='Enviar', command=botao1)
botao_enviar.grid(row=1, column=1, rowspan=3)

label1_resposta = Label(frame_baixo1, width=45, height=1, padx=10, text=txt_user1, bg=co_bg, fg='white', font=('Arial 11 bold'), anchor='w')


# Widgets main2 ---------------------------------------------------------------------
label2_qualassistiu = Label(frame_baixo2, width=45, height=1, padx=10, text='Qual desses Filmes você assistiu?', bg=co_bg, fg='white', font=('Ivy 15'), anchor='w')
label2_qualassistiu.grid(row=0, column=0, columnspan=2, sticky='w')

check2_filme1 = Checkbutton(frame_baixo2,padx=15, pady=15, text='Avengers',font=('Arial 20'),image=img_filme1,compound='left', variable=check1_var2, fg='white', bg=co_bg, onvalue=1, offvalue=0, activebackground=co_bg, activeforeground='white', selectcolor='black')
check2_filme1.grid(row=1, column=0, sticky='w')

check2_filme2 = Checkbutton(frame_baixo2,padx=15, pady=15, text='Velozes e Furiosos',font=('Arial 20'),image=img_filme2,compound='left', variable=check2_var2, fg='white', bg=co_bg, onvalue=1, offvalue=0, activebackground=co_bg, activeforeground='white', selectcolor='black')
check2_filme2.grid(row=2, column=0, sticky='w')

check2_filme3 = Checkbutton(frame_baixo2,padx=15, pady=15, text='Godzilla',font=('Arial 20'),image=img_filme3,compound='left', variable=check3_var2, fg='white', bg=co_bg, onvalue=1, offvalue=0, activebackground=co_bg, activeforeground='white', selectcolor='black')
check2_filme3.grid(row=3, column=0, sticky='w')

botao2_enviar = Button(frame_baixo2, width=15, height=1, text='Enviar', command=botao2)
botao2_enviar.grid(row=1, column=1, rowspan=3)

label2_resposta = Label(frame_baixo2, width=45, height=1, padx=10, text=txt_user2, bg=co_bg, fg='white', font=('Arial 11 bold'), anchor='w')



#-----------------------------------------------------------------------
janela.mainloop()