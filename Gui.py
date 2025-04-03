from tkinter import *

# criando classe da interface gráfica
class Gui():
    """ Classe da Interface Gráfica
    """
    xpad = 5
    ypad = 3
    widthentry = 30

    # Criando Janela do Programa
    window = Tk()
    window.wm_title("PYSQL versão 1.0")

    # Definição das variáveis que recebem os dados inseridos pelo user
    txtNome = StringVar()
    txtSobrenome = StringVar()
    txtEmail = StringVar()
    txtCPF = StringVar() 

    # Criando Objetos que farão parte da janela
    lblNome = Label(window,text="Nome")
    lblSobrenome = Label(window,text="Sobrenome")
    lblEmail = Label(window,text="Email")
    lblCPF = Label(window,text="CPF")

    entNome = Entry(window,textvariable=txtNome,width=widthentry)
    entSobrenome = Entry(window,textvariable=txtSobrenome,width=widthentry)
    entEmail = Entry(window,textvariable=txtEmail,width=widthentry)
    entCPF = Entry(window,textvariable=txtCPF,width=widthentry)

    listClientes = Listbox(window,width=100)
    scrollClientes = Scrollbar(window)

    btnViewAll = Button(window,text="Ver Todos")
    btnBuscar = Button(window,text="Buscar")
    btnInserir = Button(window,text="Inserir")
    btnUpdate = Button(window,text="Atualizar Selecionados")
    btnDel = Button(window,text="Deletar Selecionados")
    btnClose = Button(window,text="Fechar")

    # ajustando os objetos na grid da janela

    lblNome.grid(row=0,column=0)
    lblSobrenome.grid(row=1,column=0)
    lblEmail.grid(row=2,column=0)
    lblCPF.grid(row=3,column=0)

    entNome.grid(row=0,column=1,padx=50,pady=50)
    entSobrenome.grid(row=1,column=1)
    entEmail.grid(row=2,column=1)
    entCPF.grid(row=3,column=1)

    listClientes.grid(row=0,column=2,rowspan=10)
    scrollClientes.grid(row=0,column=6,rowspan=10)

    btnViewAll.grid(row=4,column=0,columnspan=2)
    btnBuscar.grid(row=5,column=0,columnspan=2)
    btnInserir.grid(row=6,column=0,columnspan=2)
    btnUpdate.grid(row=7,column=0,columnspan=2)
    btnDel.grid(row=8,column=0,columnspan=2)
    btnClose.grid(row=9,column=0,columnspan=2)

    # união da scrollbar com a listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    # adicionar a aparencia à interface
    for child in window.winfo_children():
        widgetClass = child.__class__.__name__
        if widgetClass == "Button":
            child.grid_configure(sticky="WE",padx=xpad,pady=ypad)
        elif widgetClass == "Listbox":
            child.grid_configure(sticky="NS",padx=0,pady=0)
        elif widgetClass == "Scrollbar":
            child.grid_configure(sticky="NS",padx=0,pady=0)
        else:
            child.grid_configure(sticky="N",padx=xpad,pady=ypad)

    def run(self):
        Gui.window.mainloop()