from threading import Thread
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showerror
from bs4 import BeautifulSoup
from tkinter.messagebox import askyesno
import requests
import os


##---------- MAking Some Global Variables ----------##
Original_Saved_FileName = Duplicate_Saved_FileName = Result_Saved_FileName = ''
Original_Fg = 'NavyBlue'
Duplicate_Fg = 'Red'
Result_Fg = 'Black'
Original_Bg = Result_Bg = Duplicate_Bg = 'LightBlue'


StructureType = 'Normal'
Vertical_ScrollBar = Horizontal_ScrollBar = False

Original_TextBox = '\nSorry!!!!  No Original Document to Show !!!!!\n\n\n--------------------------------------------\n\nMethods to Get an Original Document : \n\n\n----------First Method----------\n\n1. Go to "File" tab\n2. Click on "Open Html Document" Option\n3. Select an HTML Document\n\n\n----------Second Method----------\n\n1.Click on the "File" tab\n2.Click on "Open URL Bar" option\n3.Enter the URL and get the HTML Document of the Specified Page\n\n\n--------------------------------------------'
Duplicate_TextBox = '\nSorry!!!!  No Duplicate Document to Show !!!!!\n\n\n--------------------------------------------\n\nSteps to Get an Duplicate Document : \n\n1.Go to "File" tab\n2.Click on "Duplicate the Original" Option\n3.Enjoy Manipulating the Code Without Damaging the Original Code.\n\n--------------------------------------------'
Result_TextBox = '\nSorry!!!! No Result to Show!!!!!!!!!'


ForeGround = ('Red','Green','Blue','Yellow','Pink','White','Purple','NavyBlue','LightBlue','LightGreen','Brown','Black')
BackGround = ('Red','Green','Blue','Yellow','Pink','White','Purple','NavyBlue','LightBlue','LightGreen','Brown')
SelectedForeGround = SelectedBackGround = ThemeDocument = ''



##---------- Function to Configure/Load Documents ----------##
def configure_documents(screen_object, DocType):

    global Original_TextBox, Duplicate_TextBox, Result_TextBox, StructureType

    # Canvas(screen_object, width=1366, height=768, bg='black').place(x=0, y=0)
    # Canvas(screen_object, width=1366, height=35, bg='lightgray').place(x=0, y=0)

    if DocType == 'OriginalDocument':
        try:
            if StructureType == 'Normal':
                text_to_show = BeautifulSoup(Original_TextBox.get('0.1', 'end-1c'), 'html.parser')
            else:
                text_to_show = BeautifulSoup(Original_TextBox.get('0.1','end-1c'), 'html.parser').prettify()
        except:
            text_to_show = BeautifulSoup(Original_TextBox, 'html.parser').prettify()

        fg = Original_Fg
        bg = Original_Bg
        Button(screen_object, text='Original Document', fg='black', bg='lightgreen', activebackground='lightgreen',bd=0).place(x=15, y=4)

        Button(screen_object, text='Duplicate Document', fg='black', bg='lightgray', activebackground='lightblue',bd = 0, command = lambda: configure_documents(screen_object = screen_object, DocType = 'DuplicateDocument')).place(x=200, y=4)

        Button(screen_object, text='Experiment Results', fg='black', bg='lightgray', activebackground='lightblue',bd=0, command = lambda: configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')).place(x=385, y=4)

    elif DocType == 'DuplicateDocument':
        try:
            if StructureType == "Normal":
                text_to_show = BeautifulSoup(Duplicate_TextBox.get('0.1','end-1c'), 'html.parser')
            else:
                text_to_show = BeautifulSoup(Duplicate_TextBox.get('0.1','end-1c'), 'html.parser').prettify()
        except:
            text_to_show = str(Duplicate_TextBox)

        fg = Duplicate_Fg
        bg = Duplicate_Bg

        Button(screen_object, text='Original Document', fg='black', bg='lightgray', activebackground='lightblue',bd=0, command = lambda: configure_documents(screen_object = screen_object, DocType = 'OriginalDocument')).place(x=15, y=4)

        Button(screen_object, text='Duplicate Document', fg='black', bg='lightgreen', activebackground='lightgreen',bd=0).place(x=200, y=4)

        Button(screen_object, text='Experiment Results', fg='black', bg='lightgray', activebackground='lightblue',bd=0, command = lambda: configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')).place(x=385, y=4)

    else:
        try:
            text_to_show = str(Result_TextBox.get('0.1',END))
        except:
            text_to_show = str(Result_TextBox)
        fg = Result_Fg
        bg = Result_Bg

        Button(screen_object, text='Original Document', fg='black', bg='lightgray', activebackground='lightblue',bd=0, command = lambda: configure_documents(screen_object = screen_object, DocType = 'OriginalDocument')).place(x=15, y=4)

        Button(screen_object, text='Duplicate Document', fg='black', bg='lightgray', activebackground='lightblue',bd=0, command = lambda: configure_documents(screen_object = screen_object, DocType = 'DuplicateDocument')).place(x=200, y=4)

        Button(screen_object, text = 'Experiment Results', fg = 'black', bg = 'lightgreen', activebackground = 'lightgreen', bd = 0).place(x=385, y=4)

    try:
        global Vertical_ScrollBar, Horizontal_ScrollBar
        Vertical_ScrollBar.destroy()
        Horizontal_ScrollBar.destroy()
    except:
        pass

    Vertical_ScrollBar = Scrollbar(screen_object, orient=VERTICAL, width = 15)
    Vertical_ScrollBar.pack(side=RIGHT, fill=Y, padx=50, pady=80)

    Horizontal_ScrollBar = Scrollbar(screen_object, orient = HORIZONTAL, width = 15)
    Horizontal_ScrollBar.pack(side = BOTTOM, fill = X, padx = 350, pady=10)


    if DocType == 'ExperimentResult_Documentation':
        TextBox = Text(screen_object, bd=0, width=127, height=30, selectbackground='pink', bg=bg, fg=fg, wrap='word',yscrollcommand=Vertical_ScrollBar.set, xscrollcommand=Horizontal_ScrollBar.set)

        TextBox.place(x=120, y=90)
        position = ''
        index = 0
        for character in text_to_show:
            if character == '\n':
                break
            else:
                position += character
                index += 1

        TextBox.insert(END, str(text_to_show[index:]))
        TextBox.see(position)

    else:
        TextBox = Text(screen_object, bd = 0, width = 127, height = 30, selectbackground = 'pink', bg = bg, fg = fg, wrap = 'none', yscrollcommand = Vertical_ScrollBar.set, xscrollcommand = Horizontal_ScrollBar.set)

        TextBox.place(x=120, y=90)

        TextBox.insert(END, str(text_to_show))

    if DocType != 'DuplicateDocument':
        TextBox.config(state = DISABLED)
        if DocType == 'OriginalDocument':
            Original_TextBox = TextBox
        else:
            Result_TextBox = TextBox

    else:
        Duplicate_TextBox = TextBox

    Vertical_ScrollBar.config(command = TextBox.yview)
    Horizontal_ScrollBar.config(command = TextBox.xview)

##---------- END of this Function ----------##



##---------- Function to GetTextBoxData----------##
def GetDocument(DocType):
    if DocType == 'OriginalDocument':
        return Original_TextBox
    elif DocType == 'DuplicateDocument':
        return Duplicate_TextBox
    elif DocType == 'ExperimentResult':
        return Result_TextBox
    elif DocType == 'All':
        return Original_TextBox, Duplicate_TextBox, Result_TextBox

##---------- END of this Function ----------##



##---------- Function to give Data to ResultTextBox----------##
def SetResultTextBoxData(DocType,Data):
    global Result_TextBox,Duplicate_TextBox
    if DocType == 'DuplicateDocument':
        Duplicate_TextBox = Data
    elif DocType == 'ExperimentResult':
        Result_TextBox = Data
##---------- END of this Function ----------##



##---------- Function to OpenHtmlDocument(1. File Menu) Manually----------##
def Open_HTML_Document(screen_object):
    try:
        global Original_Saved_FileName, Duplicate_Saved_FileName, Result_Saved_FileName
        Original_Saved_FileName = Duplicate_Saved_FileName = Result_Saved_FileName = ''
        filename = askopenfile(initialdir='/home', title='Select an HTML Document',filetypes=(("HTML Documents", "*.html"),))

        with open(filename.name,'r') as f:
            global Original_TextBox
            Original_TextBox = str(f.read())
        configure_documents(screen_object = screen_object, DocType = 'OriginalDocument')
    except:
        pass
##---------- END of this Function ----------##



##---------- Function to Duplicate_the_Original(3. File Menu) ----------##
def Duplicate_the_Original(screen_object):
    global Duplicate_TextBox, Original_TextBox

    Duplicate_TextBox = Original_TextBox
    configure_documents(screen_object = screen_object, DocType = 'DuplicateDocument')

##---------- END of this Function ----------##



##---------- Function to Process Saving of Files (All Save Menus comes under this function) ----------##
def To_Process_Saving_of_Files(ThingtoSave, signal):

    global Duplicate_TextBox, Original_TextBox, Result_TextBox
    global Duplicate_Saved_FileName, Original_Saved_FileName, Result_Saved_FileName

    if ThingtoSave == 'Original' :
        try:
            Original_Saved_FileName = GetFileSaved(FileName = Original_Saved_FileName, ContentTOSave = str(Original_TextBox.get('0.1', 'end-1c')), Signal = signal)
        except:
            Original_Saved_FileName = GetFileSaved(FileName = Original_Saved_FileName, ContentTOSave = Original_TextBox, Signal = signal)

    elif ThingtoSave == 'Duplicate' :
        try:
            Duplicate_Saved_FileName = GetFileSaved(FileName = Duplicate_Saved_FileName, ContentTOSave = str(Duplicate_TextBox.get('0.1', END)), Signal = signal)
        except:
            Duplicate_Saved_FileName = GetFileSaved(FileName = Duplicate_Saved_FileName, ContentTOSave = Duplicate_TextBox, Signal = signal)

    else:
        try:
            Result_Saved_FileName =  GetFileSaved(FileName = Result_Saved_FileName, ContentTOSave = str(Result_TextBox.get('0.1', END)), Signal = signal)
        except:
            Result_Saved_FileName = GetFileSaved(FileName = Result_Saved_FileName, ContentTOSave = Result_TextBox, Signal = signal)

##---------- END of this Function ----------##




##---------- Function to Finish Saving Work ----------##
def GetFileSaved(FileName, ContentTOSave, Signal):

    if FileName != "" and Signal == 'Save':
        with open(FileName,mode='w') as f:
            f.write(ContentTOSave)
        return FileName
    else:
        try:
            SavedFileObject = asksaveasfile(initialdir = '/home', mode = 'w', filetypes = (("HTML Documents","*.html"),))
            SavedFileObject.write(ContentTOSave)
            SavedFileObject.close()
            return SavedFileObject.name
        except:
            return ''

##---------- END of this Function ----------##



##---------- Function to Restart the Application (8. FileMenu) ----------##
def BackToOrigin(screen_object):
    global Duplicate_TextBox, Original_TextBox, Result_TextBox
    signal = askyesno(title = 'Sensitive Decision',message = "It will lead to remove all your document's data and will restart application agian.\n\n Do You Want to Proceed ?")

    if signal:
        Original_TextBox = '\nSorry!!!!  No Original Document to Show !!!!!\n\n\n--------------------------------------------\n\nMethods to Get an Original Document : \n\n\n----------First Method----------\n\n1. Go to "File" tab\n2. Click on "Open Html Document" Option\n3. Select an HTML Document\n\n\n----------Second Method----------\n\n1.Click on the "File" tab\n2.Click on "Open URL Bar" option\n3.Enter the URL and get the HTML Document of the Specified Page\n\n\n--------------------------------------------'
        Duplicate_TextBox = '\nSorry!!!!  No Duplicate Document to Show !!!!!\n\n\n--------------------------------------------\n\nSteps to Get an Duplicate Document : \n\n1.Go to "File" tab\n2.Click on "Duplicate the Original" Option\n3.Enjoy Manipulating the Code Without Damaging the Original Code.\n\n--------------------------------------------'
        Result_TextBox = '\nSorry!!!! No Result to Show!!!!!!!!!'

        configure_documents(screen_object = screen_object, DocType = 'OriginalDocument')

##---------- END of this Function ----------##


##---------- Function to GETURLBar(2. FileMenu)----------##
def GetURLBar(screen_object):

    screen = Toplevel(screen_object)
    screen.title('Web Scrapper')
    screen.geometry('350x200')

    Canvas(screen, bg= 'lightgray', width = 350, height = 200).place(x = 0, y = 0 )

    Label(screen,text = 'URL Bar', fg = 'white', bg = 'purple', width = 40).place(x=12,y=10)

    Label(screen, text = 'Enter URL  :  ', bg = 'lightgray' ).place(x=45,y=80)

    URL_Input = StringVar()

    Entry(screen, text = URL_Input, width = 20).place(x=135, y=78)

    Button(screen, text = 'Get Content', fg = 'blue', bg = 'white', command = lambda: GetContent(root_screen = screen_object, top_screen = screen, URL = str(URL_Input.get())) ).place(x=135,y=155)

    screen.mainloop()

##---------- END of this Function ----------##


##---------- Function to GetContent of page specified by its URL ----------##
def GetContent(root_screen, top_screen, URL):
    error = ''
    try:
        response = requests.get(url = URL, timeout = (3,3))
        global Original_TextBox
        Original_TextBox = str(response.text)
    except requests.exceptions.Timeout:
        error = 'Timeout Error'
    except requests.exceptions.ConnectionError:
        error = 'Connection Error'
    except requests.exceptions.MissingSchema:
        error = 'Invalid URL'
    except requests.exceptions.HTTPError:
        error = 'HTTP Error'

    if error != '':
        Label(top_screen, text= error + '  .........', fg='red', bg='lightgray').place(x=130, y=120)
    else:
        Label(top_screen, text= 'Connected Successfully !!!                       ', fg='green', bg='lightgray').place(x=130, y=120)
        def DestroyCurrentScreen():
            top_screen.destroy()
            configure_documents(screen_object=root_screen, DocType='OriginalDocument')

        Button(top_screen, text='Show Content', fg='blue', bg='white',command = DestroyCurrentScreen ).place(x=135, y=155)

##---------- END of this Function ----------##


##---------- Function to change StructureType (Used-to in View tab)----------##
def ChangeStructureType(screen_object, NewStructureType):
    global StructureType

    if StructureType != NewStructureType:
        StructureType = NewStructureType
        configure_documents(screen_object = screen_object, DocType = 'OriginalDocument')

##---------- END of this Function ----------##


##---------- Function to GetDocumentName for Experiments----------##
def GetDocumentName():
    name_lst = []
    thread = Thread(target = DocumentForExperiment, args = (name_lst, ))
    thread.start()
    thread.join()
    try:
        return name_lst[0]
    except:
        return ''
##---------- END of this Function ----------##


##---------- Function to Provide Document Choices for Experiments----------##
def DocumentForExperiment(name_lst):

    screen = Tk()

    screen.geometry('350x160')

    screen.title('Choose Document')

    Label(screen,text = 'Choose a Document - Type\nfor Operation ...', font=('default',10,'bold')).place(x=70,y=20)

    def ReturnDoctype(string):
        nonlocal name_lst
        name_lst.append(string)
        screen.destroy()

    Button(screen, text = 'Original Document',fg = 'red',bg = 'white',activeforeground = 'white',activebackground = 'red', command =lambda: ReturnDoctype('OriginalDocument')).place(x=15,y=120)
    Button(screen, text = 'Duplicate Document',fg = 'blue',bg = 'white',activeforeground = 'white',activebackground = 'blue', command =lambda: ReturnDoctype('DuplicateDocument')).place(x=180,y=120)
    Button(screen, text = 'Experiment Results',fg = 'green',bg = 'white',activeforeground = 'white',activebackground = 'green', command =lambda: ReturnDoctype('ExperimentResult')).place(x=100,y=75)

    screen.mainloop()
##---------- END of this Function ----------##


##---------- Function to ExtractTags from SoupObject or HTML DOcument----------##
def GetTagList(SoupObject):
    tagset = set()
    for tag in SoupObject.findAll():
        tagset.add(tag.name)
    return list(tagset)
##---------- END of this Function ----------##


##---------- Function to ConfigureTagList(3. ViewMenu)----------##
def ConfigureTagList(screen_object):
    global Original_TextBox, Duplicate_TextBox, Result_TextBox
    DocType = GetDocumentName()
    if DocType == 'OriginalDocument':
        TextBoxObject = Original_TextBox
    elif DocType == 'DuplicateDocument':
        TextBoxObject = Duplicate_TextBox
    elif DocType == 'ExperimentResult':
        TextBoxObject = Result_TextBox
    else:
        return

    try:
        SoupObject = BeautifulSoup(TextBoxObject.get('0.1', 'end-1c'), 'html.parser')
        Result_TextBox = '\n\t\t\t\t--------------- Tags available in the Documents --------------- \n\n\n'
        taglist = GetTagList(SoupObject = SoupObject)
        for tag in taglist:
            if not '/' in tag:
                PreTag = AddWhiteSpaces(length = len(str('<' + tag + '>')), maxlength = 19, string = str('<' + tag + '>'))
                PostTag = '          </' + tag + '>\n'
                Result_TextBox += PreTag + PostTag
        configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')
        # print(len(tagset))
    except:
        return
##---------- END of this Function ----------##


##---------- Function to AddWhiteSpaces to strings----------##
def AddWhiteSpaces(length, maxlength, string):
    while length < maxlength:
        string += ' '
        length+=1
    return string
##---------- END of this Function ----------##


##---------- Function to Get Text Used in the Document (4. ViewMenu)----------##
def ConfigureDocumentText(screen_object):
    global Result_TextBox
    DocType = GetDocumentName()
    if DocType == 'OriginalDocument':
        TextBoxObject = Original_TextBox
    elif DocType == 'DuplicateDocument':
        TextBoxObject = Duplicate_TextBox
    elif DocType == 'ExperimentResult':
        TextBoxObject = Result_TextBox
    else:
        return

    try:
        SoupObject = BeautifulSoup(TextBoxObject.get('0.1','end-1c'),'html.parser')
        Result_TextBox = '\n\t\t\t\t--------------- Text available in the Document --------------- \n\n\n' + SoupObject.get_text()
    except:
        Result_TextBox = '\n\t\t\t\t--------------- Text available in the Document --------------- \n\n\n' + TextBoxObject

    configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')

##---------- END of this Function ----------##


##---------- Function to Get Comments Used in the Document(5. ViewMenu)----------##
def ConfigureComments(screen_object):
    global Result_TextBox
    DocType = GetDocumentName()
    if DocType == 'OriginalDocument':
        TextBoxObject = Original_TextBox
    elif DocType == 'DuplicateDocument':
        TextBoxObject = Duplicate_TextBox
    elif DocType == 'ExperimentResult':
        TextBoxObject = Result_TextBox
    else:
        return

    try:
        SoupObject = BeautifulSoup(TextBoxObject.get('0.1',END),'html.parser')
        Result_TextBox = '\n\t\t\t\t--------------- Comments Used in the Document --------------- \n\n\n'
        for tagB in SoupObject.findAll('b'):
            Result_TextBox += tagB.string
    except:
        print('exception')
        Result_TextBox = '\n\t\t\t\t--------------- Comments Used in the Document --------------- \n\n\n' + TextBoxObject

    configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')

##---------- END of this Function ----------##



##---------- Function to Run a File in Browser( Open In Browser Menu)----------##
def OpenFileInBrowser(screen_object):
    global Original_Saved_FileName, Duplicate_Saved_FileName, Result_Saved_FileName
    global Original_TextBoxnal, Duplicate_TextBox, Result_TextBox
    DocumentName = GetDocumentName()
    filename = ''
    if DocumentName == '':
        return None

    elif DocumentName == 'OriginalDocument':
        try:
            Original_Saved_FileName = GetFileSaved(FileName = Original_Saved_FileName, ContentTOSave=Original_TextBox.get('0.1', END), Signal='Save')
        except:
            Original_Saved_FileName = GetFileSaved(FileName = Original_Saved_FileName, ContentTOSave=Original_TextBox, Signal='Save')

        filename = Original_Saved_FileName

    elif DocumentName == 'DuplicateDocument':
        try:
            Duplicate_Saved_FileName = GetFileSaved(FileName = Duplicate_Saved_FileName, ContentTOSave = Duplicate_TextBox.get('0.1', END), Signal='Save')
        except:
            Duplicate_Saved_FileName = GetFileSaved(FileName = Duplicate_Saved_FileName, ContentTOSave=Duplicate_TextBox, Signal='Save')

        filename = Duplicate_Saved_FileName

    elif DocumentName == 'ExperimentResult':
        try:
            Result_Saved_FileName = GetFileSaved(FileName = Result_Saved_FileName, ContentTOSave=Result_TextBox.get('0.1', END), Signal='Save')
        except:
            Result_Saved_FileName = GetFileSaved(FileName = Result_Saved_FileName, ContentTOSave=Result_TextBox, Signal='Save')

        filename = Result_Saved_FileName

    try:
        os.system('xdg-open ' + filename)
    except:
        showerror('Show Error','Error While Opening the File !!!')

##---------- END of this Function ----------##



##---------- Function to ApplyChanges to Existing Theme defined by the User ----------##
def ApplyChanges():
    global SelectedBackGround,SelectedForeGround, ThemeDocument, Original_Fg, Original_Bg, Duplicate_Fg, Duplicate_Bg, Result_Fg, Result_Bg

    Signal = False
    try:
        if SelectedBackGround.get() == '' or SelectedForeGround.get() == '':
            showerror('Show Error',"Color field could not be empty!!")

        elif SelectedBackGround.get() == SelectedForeGround.get():
            showerror('Show Error',"Foreground and Background\n  color could not be Same.....")

        elif ThemeDocument == 'OriginalDocument':
            if SelectedForeGround.get() == Original_Fg and SelectedBackGround.get() == Original_Bg :
                showerror('Show Error','New Theme could not be same as Existing Theme')

            else:
                print(Original_Fg,Original_Bg)
                print(SelectedForeGround.get(),SelectedBackGround.get())
                Original_Fg = SelectedForeGround.get()
                Original_Bg = SelectedBackGround.get()
                Signal = True

        elif ThemeDocument == 'DuplicateDocument':
            if SelectedForeGround.get() == Duplicate_Fg and SelectedBackGround.get() == Duplicate_Bg:
                showerror('Show Error', 'New Theme could not be same as Existing Theme')

            else:
                Duplicate_Fg = SelectedForeGround.get()
                Duplicate_Bg = SelectedBackGround.get()
                Signal = True

        elif ThemeDocument == 'ExperimentResult':
            if SelectedForeGround.get() == Result_Fg and SelectedBackGround.get() == Result_Bg:
                showerror('Show Error', 'New Theme could not be same as Existing Theme')

            else:
                Result_Fg = SelectedForeGround.get()
                Result_Bg = SelectedBackGround.get()
                Signal = True

    except:
        pass

    if Signal:
        showerror('Succession','Changes Applied Successfully !!!')

##---------- END of this Function ----------##



##---------- Function to Show Available Document Themes to User ----------##
def ShowingAvailable_DocumentThemes(DocType, ThemeScreen):

    global SelectedBackGround,SelectedForeGround,ThemeDocument,Original_Fg,Original_Bg,Duplicate_Fg,Duplicate_Bg,Result_Fg,Result_Bg
    ThemeDocument = DocType
    bg = fg = ''
    Label(ThemeScreen,text = '                          \n                       \n                      ',fg = 'black', bg = 'white', font = ('default',15,'bold')).place(x=210,y=155)

    if DocType == 'OriginalDocument':
        fg = Original_Fg
        bg = Original_Bg
        Button(ThemeScreen, text='Original Document ', fg='blue', bg='lightgray',activeforeground = 'blue',font=('default', 8, 'bold'), command=lambda: '').place(x=35,y=100)
        Button(ThemeScreen, text='Duplicate Document', fg='red', bg='white',activeforeground = 'red', font=('default', 8, 'bold'),command=lambda: ShowingAvailable_DocumentThemes(DocType='DuplicateDocument', ThemeScreen=ThemeScreen)).place(x=35,y=170)
        Button(ThemeScreen, text='Resultant Document', fg='green', bg='white',activeforeground = 'green', font=('default', 8, 'bold'),command=lambda: ShowingAvailable_DocumentThemes(DocType='ExperimentResult', ThemeScreen=ThemeScreen)).place(x=35, y=240)

    elif DocType == 'DuplicateDocument':
        fg = Duplicate_Fg
        bg = Duplicate_Bg
        Button(ThemeScreen, text='Original Document ', fg='blue', bg='white', activeforeground='blue',font=('default', 8, 'bold'),command=lambda: ShowingAvailable_DocumentThemes(DocType='OriginalDocument', ThemeScreen=ThemeScreen)).place(x=35, y=100)
        Button(ThemeScreen, text='Duplicate Document', fg='red', bg='lightgray',activeforeground = 'red', font=('default', 8, 'bold'), command=lambda: '').place(x=35,y=170)
        Button(ThemeScreen, text='Resultant Document', fg='green', bg='white',activeforeground = 'green', font=('default', 8, 'bold'),command=lambda: ShowingAvailable_DocumentThemes(DocType='ExperimentResult', ThemeScreen=ThemeScreen)).place(x=35, y=240)

    elif DocType == 'ExperimentResult':
        fg = Result_Fg
        bg = Result_Bg
        Button(ThemeScreen, text='Original Document ', fg='blue', bg='white', activeforeground='blue',font=('default', 8, 'bold'),command=lambda: ShowingAvailable_DocumentThemes(DocType='OriginalDocument', ThemeScreen=ThemeScreen)).place(x=35, y=100)
        Button(ThemeScreen, text='Duplicate Document', fg='red', bg='white',activeforeground = 'red', font=('default', 8, 'bold'),command=lambda: ShowingAvailable_DocumentThemes(DocType='DuplicateDocument', ThemeScreen=ThemeScreen)).place(x=35,y=170)
        Button(ThemeScreen, text='Resultant Document', fg='green', bg='lightgray',activeforeground = 'green', font=('default', 8, 'bold'),command = lambda :'').place(x=35,y=240)


    Label(ThemeScreen,text = 'Select ForeGround : ',fg = 'black', bg = 'white').place(x=210,y=105)

    SelectedForeGround = Combobox(ThemeScreen,value = ForeGround,width = 15)
    SelectedForeGround.place(x=230,y=150)
    SelectedForeGround.set(fg)

    Label(ThemeScreen,text = 'Select BackGround : ',fg = 'black', bg = 'white').place(x=210,y=205)

    SelectedBackGround = Combobox(ThemeScreen,value = BackGround,width = 15)
    SelectedBackGround.place(x=230,y=250)
    SelectedBackGround.set(bg)

    Button(ThemeScreen,text = 'Apply Changes',bd =0, fg = 'blue',bg = 'white',command = ApplyChanges).place(x=270,y=340)


##---------- END of this Function ----------##



##---------- Function to GetThemeWindow( ThemeMenu )----------##
def GetThemeWindow(screen_object):

    ThemeScreen = Toplevel(screen_object)

    ThemeScreen.geometry('420x380')
    ThemeScreen.title('Theme Window')

    Canvas(ThemeScreen,bg= 'white',width=420,height=380).place(x=1,y=0)


    Canvas(ThemeScreen,width = 1,height = 290,bg='black').place(x=200,y=30)
    Canvas(ThemeScreen,width = 1,height = 290,bg='black').place(x=20,y=30)
    Canvas(ThemeScreen,width = 1,height = 290,bg='black').place(x=395,y=30)


    Canvas(ThemeScreen,width = 375,height = 1,bg='black').place(x=20,y=30)
    Canvas(ThemeScreen,width = 375,height = 1,bg='black').place(x=20,y=70)
    Canvas(ThemeScreen,width = 375,height = 1,bg='black').place(x=20,y=320)



    Label(ThemeScreen,text = 'Document Types   ',fg = 'black',bg= 'white').place(x=50,y=40)
    Label(ThemeScreen,text = 'Document Colors',fg = 'black',bg= 'white').place(x=240,y=40)

    Label(ThemeScreen,text = 'Please Select a Document\n first to change foreground\n and BackGround colors ...',fg = 'black', bg = 'white').place(x=210,y=155)


    Button(ThemeScreen,text = 'Original Document ',fg = 'blue',bg='white',activeforeground = 'blue', font=('default',8,'bold'),command = lambda : ShowingAvailable_DocumentThemes(DocType = 'OriginalDocument',ThemeScreen = ThemeScreen)).place(x=35,y=100)
    Button(ThemeScreen,text = 'Duplicate Document',fg = 'red',bg='white',activeforeground = 'red',font=('default',8,'bold'),command = lambda : ShowingAvailable_DocumentThemes(DocType = 'DuplicateDocument',ThemeScreen = ThemeScreen)).place(x=35,y=170)
    Button(ThemeScreen,text = 'Resultant Document',fg = 'green',bg='white',activeforeground = 'green',font=('default',8,'bold'),command = lambda : ShowingAvailable_DocumentThemes(DocType = 'ExperimentResult',ThemeScreen = ThemeScreen)).place(x=35,y=240)



    Button(ThemeScreen,text = 'Close',bd =0, fg = 'red',bg = 'white',command = ThemeScreen.destroy).place(x=20,y=340)
    Button(ThemeScreen,text = 'Apply Changes',bd =0, fg = 'white',bg = 'lightblue',activeforeground = 'white',activebackground = 'lightblue').place(x=270,y=340)

    ThemeScreen.mainloop()

##---------- END of this Function ----------##
