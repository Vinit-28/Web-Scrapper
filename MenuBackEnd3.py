from MenuBackEnd1 import configure_documents, GetDocument, SetResultTextBoxData, Thread
from MenuBackEnd2 import  BeautifulSoup, SearchingTagsWithRelatedNames, showerror, ShowTags, GetSearchBar, CloseNavigateAndSearchBar
from tkinter import *


##---------- Making Global Variables ----------##
ModificationBar = False




##---------- Function to Get Error if Result is False otherwise Success ----------##
def GetErrorOrSuccess(Result,dictionary):
    if Result:
        SetResultTextBoxData(DocType = 'DuplicateDocument',Data = str(dictionary['SoupObject']))
        showerror('Succession','Changes Applied successfully!!')
        try:
            dictionary['temprary_window'].destroy()
        except:
            pass
        configure_documents(screen_object = dictionary['root_screen'],DocType = 'DuplicateDocument')

    else:
        showerror('Show Error','Error While Making Changes')

##---------- END of this Function ----------##


##---------- Function to GetChangeType for Experiments ----------##
def GetModificationType():
    ChangeType = []
    thread = Thread(target=TagforChanges, args=(ChangeType,))
    thread.start()
    thread.join()
    try:
        return ChangeType[0]
    except:
        return ''

##---------- END of this Function ----------##



##---------- Function to Provide Tag Choices to MakeChanges----------##
def TagforChanges(ChangeType):

    screen = Tk()

    screen.geometry('350x160')

    screen.title('Choose Option')

    Label(screen, text='Choose an Option to Make\nChanges to Tag ...', font=('default', 10, 'bold')).place(x=70,y=20)

    def ReturnDoctype(string):
        nonlocal ChangeType
        ChangeType.append(string)
        screen.destroy()

    Button(screen, text='Apply to First Tag', fg='red', bg='white', activeforeground='white', activebackground='red',command=lambda: ReturnDoctype('FirstTag')).place(x=15, y=120)
    Button(screen, text='Apply to all Tags', fg='blue', bg='white', activeforeground='white',activebackground='blue', command=lambda: ReturnDoctype('AllTags')).place(x=180, y=120)
    Button(screen, text='Choose Tag/Tags', fg='green', bg='white', activeforeground='white',activebackground='green', command=lambda: ReturnDoctype('ChooseTags')).place(x=100, y=75)

    screen.mainloop()
##---------- END of this Function ----------##


##---------- Function to GetSoupObject ----------##
def GetSoupObject(DocumentName):
    Document = GetDocument(DocType = DocumentName)
    try:
        SoupObject = BeautifulSoup(Document.get('0.1',END),'html.parser',multi_valued_attributes = None)
    except:
        SoupObject = BeautifulSoup(Document,'html.parser',multi_valued_attributes = None)

    return SoupObject

##---------- END of this Function ----------##



##---------- Function to GetModificationWindow----------##
def GetModificationWindow(root,function,dictionary,Question1,Question2):
    TemperaryRoot = Toplevel(root)
    TemperaryRoot.geometry('360x230')
    TemperaryRoot.title('Modification Window')

    Canvas(TemperaryRoot,bg = 'lightgray',width = 350,height = 220).place(x=0,y=0)

    Label(TemperaryRoot, text = 'Modification Bar',width = 40, height = 2, fg = 'white', bg = 'purple').place(x=17,y=10)

    Label(TemperaryRoot, text = Question1,fg = 'black',bg = 'lightgray').place(x=20,y=80)

    Label(TemperaryRoot, text = Question2,fg = 'black',bg = 'lightgray').place(x=20,y=120)

    Answer1 = StringVar()
    Answer2 = StringVar()

    Entry(TemperaryRoot, textvariable = Answer1, width = 17).place(x=185,y=78)
    Entry(TemperaryRoot, textvariable = Answer2, width = 17).place(x=185,y=118)

    def ToCallNextFunction():
        nonlocal dictionary
        try :
            if dictionary['Aim'] == 'DeleteAttribute' and dictionary['ModificationType'] != 'ChooseTags':
                dictionary['TagName'] = Answer1.get()

            elif dictionary['Aim'] == 'DeleteAttribute' and dictionary['ModificationType'] == 'ChooseTags':
                dictionary['Indexes'] = str(Answer1.get()).split(',')


        except:
            pass
        dictionary.update({'temprary_window': TemperaryRoot,'Answer1' : Answer1.get(),'Answer2' : Answer2.get()})
        function(dictionary = dictionary)

    Button(TemperaryRoot, text = 'Apply Changes', fg = 'white', bg = 'blue', activeforeground = 'blue', activebackground = 'white',command = ToCallNextFunction).place(x=115,y=185)

    TemperaryRoot.mainloop()

##---------- END of this Function ----------##



##---------- Function to return essentials item in a dictionary----------##
def GetDictionary(screen_object):
    ModificationType = GetModificationType()
    SoupObject = GetSoupObject(DocumentName='DuplicateDocument')
    dictionary = {'root_screen': screen_object,
                  'SoupObject': SoupObject,
                  'ModificationType': ModificationType, }

    return dictionary

##---------- END of this Function ----------##



##---------- Function to configureRenameTags(1. ModificationMenu)----------##
def ConfigureRenameTags(screen_object):
    dictionary = GetDictionary(screen_object = screen_object)

    if dictionary['ModificationType'] == 'ChooseTags':
        SearchItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')
        Button(screen_object, text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: OnlySlectedTags(screen_object = screen_object,SoupObject = dictionary['SoupObject'],TagtoSearch = SearchItem.get(),ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to Rename that Tag/Tags -----------------\n\n\n\n",function = RenameSelectedTags,dictionary = dictionary)).place(x=910, y=6)

    elif dictionary['ModificationType'] == 'FirstTag' or dictionary['ModificationType'] == 'AllTags':
        GetModificationWindow(root = screen_object,function = RenameFirstAndAllTags,dictionary = dictionary,Question1 = 'Enter TagName : ', Question2 = 'Enter New TagName : ')


##---------- END of this Function ----------##



##---------- Function to Rename Tags Selected by the User----------##
def RenameSelectedTags(dictionary):
    NewTagName = GetSearchBar(screen_object = dictionary['root_screen'],Question = 'New TagName : ', BarType = 'Searching')

    def ApplyChanges():
        if NewTagName.get() == '':
            showerror('Show Error','Error While Applying Changes')
        else:
            SelectedTagNumbers = dictionary['TagNumbers'].split(',')
            index = 1

            for tag in dictionary['SoupObject'].findAll(dictionary['TagtoSearch']):
                if str(index) in SelectedTagNumbers:
                    tag.name = str(NewTagName.get())
                index += 1
            SetResultTextBoxData(DocType = 'DuplicateDocument',Data = str(dictionary['SoupObject']))
            configure_documents(screen_object = dictionary['root_screen'],DocType = 'DuplicateDocument')
            CloseNavigateAndSearchBar(screen_object = dictionary['root_screen'],BarType = 'Searching')
            showerror('Succession', 'Changes Applied Successfully!!')


    Button(dictionary['root_screen'], text='Apply Changes', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: ApplyChanges()).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to Execute another function when user chooses "Choose Tags" option----------##
def OnlySlectedTags(screen_object,SoupObject,TagtoSearch,ResultStartingLine,function,dictionary):
    signal, TagNumber, Result = ShowTags(screen_object = screen_object,SoupObject = SoupObject,TagtoSearch = TagtoSearch,ResultStartingLine = ResultStartingLine, BarType = 'Searching')

    if signal:
        def WhenBelowButtonPressed():
            TagNumbers = ''
            if not str(TagNumber.get()).endswith(','):
                TagNumbers = str(TagNumber.get()) + ','
            dictionary.update({'TagNumbers' : TagNumbers, 'TagtoSearch' : TagtoSearch})
            function(dictionary)

        Button(screen_object, text='Make Changes', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed()).place(x=910, y=6)

##---------- END of this Function ----------##


##---------- Function to apply changes to tags ## Things that the dictionary must have are: SoupObject,OldTagName,NewTagName,ModificationType ##----------##
def RenameFirstAndAllTags(dictionary):
    Result = False
    for tag in dictionary['SoupObject'].findAll(dictionary['Answer1']):
        if dictionary['ModificationType'] == 'FirstTag' and dictionary['Answer2'] != '':
            tag.name = dictionary['Answer2']
            Result = True
            break
        elif dictionary['ModificationType'] == 'AllTags' and dictionary['Answer2'] != '':
            tag.name = dictionary['Answer2']
            Result = True

    GetErrorOrSuccess(Result = Result,dictionary = dictionary)

##---------- END of this Function ----------##



##---------- Function to Configure Rename Tag's Attributes ----------##
def ConfigureRenameAttribute__RedefineVAlues(screen_object, Signal):
    dictionary = GetDictionary(screen_object = screen_object)

    if Signal == 'Rename':
        dictionary.update({'Aim' : 'Rename' , 'Question1': "Attribute's OldName : ", 'Question2': "Attribute's NewName : "})
    elif Signal == 'Redefine':
        dictionary.update({'Aim' : 'Redefine' , 'Question1': "Attribute's OldValue : ", 'Question2': "Attribute's NewValue : "})

    if dictionary['ModificationType'] == 'ChooseTags':
        SearchingItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')
        Button(dictionary['root_screen'], text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: RenameSelectedTagsAttributes__RedefineVAlues(StringTOFind = SearchingItem.get(),function = RenameTagsAttributes__RedefineVAlues,dictionary = dictionary,Modify = 'Other')).place(x=910, y=6)

    elif dictionary['ModificationType'] == 'FirstTag' or dictionary['ModificationType'] == 'AllTags':
        GetModificationWindow(root = screen_object,function = RenameTagsAttributes__RedefineVAlues,dictionary = dictionary,Question1 = dictionary['Question1'],Question2 = dictionary['Question2'])

##---------- END of this Function ----------##




##---------- Function to Rename only Selected Tag's Attributes ----------##
def RenameSelectedTagsAttributes__RedefineVAlues(StringTOFind,function,dictionary, Modify):
    SearchingTagsWithRelatedNames(screen_object = dictionary['root_screen'],StringToFind = StringTOFind,SoupObject = dictionary['SoupObject'],Signal = 'WithIndex')
    SearchingItem = GetSearchBar(screen_object = dictionary['root_screen'],Question = 'Enter TagNumber : ', BarType = 'Searching')

    def WhenBelowButtonPressed():
        dictionary.update({'Indexes' : str(SearchingItem.get()).split(','), 'TagName' : StringTOFind})
        if Modify == 'String':
            ModificationWindowForString(dictionary = dictionary,function = function)
        else:
            GetModificationWindow(root = dictionary['root_screen'],function = function,dictionary = dictionary,Question1 = dictionary['Question1'],Question2 = dictionary['Question2'])


    Button(dictionary['root_screen'], text='Make Changes', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed()).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to ConfigureDeleteAttributes( .) ModificationMenu)----------##
def ConfigureDeleteAttribue(screen_object):
    dictionary = GetDictionary(screen_object = screen_object)
    dictionary['Aim'] = 'DeleteAttribute'
    if dictionary['ModificationType'] != 'ChooseTags':
        GetModificationWindow(root = screen_object,function = RenameTagsAttributes__RedefineVAlues,dictionary = dictionary,Question1 = 'Enter TagName : ',Question2 = 'Enter Attribute Name : ')

    else:

        SearchingItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')

        def WhenBelowButtonPressed():
            SearchingTagsWithRelatedNames(screen_object = screen_object,StringToFind = SearchingItem.get(),SoupObject = dictionary['SoupObject'],Signal = 'WithIndex')
            dictionary['TagName'] = SearchingItem.get()
            GetModificationWindow(root=screen_object, function=RenameTagsAttributes__RedefineVAlues,dictionary=dictionary, Question1='Enter TagNumber : ',Question2='Enter Attribute Name : ')

        Button(screen_object, text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed()).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to ConfigureWrapTags( .) ModificationMenu)----------##
def ConfigureWrapTags(screen_object, AIM):
    dictionary = GetDictionary(screen_object = screen_object)
    dictionary['Aim'] = AIM
    if dictionary['ModificationType'] != 'ChooseTags':
        if AIM == 'WrapTag':
            GetModificationWindow(root = screen_object,function = RenameTagsAttributes__RedefineVAlues,dictionary = dictionary,Question1 = 'Wrapped with  : ',Question2 = 'Tag To be Wrapped : ')

        elif AIM == 'UnwrapTag':
            GetModificationWindow(root = screen_object,function = RenameTagsAttributes__RedefineVAlues,dictionary = dictionary,Question1 = 'Outer TagName : ',Question2 ='Inner TagName : ')

    else:

        SearchingItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')

        def WhenBelowButtonPressed(Value):
            nonlocal dictionary

            if Value == 0:
                SearchingTagsWithRelatedNames(screen_object = screen_object,StringToFind = SearchingItem.get(),SoupObject = dictionary['SoupObject'],Signal = 'WithIndex')
                dictionary['TagName'] = SearchingItem.get()
                TagIndexes = GetSearchBar(screen_object=screen_object, Question='Enter TagNumber : ', BarType='Searching')

                if AIM == 'WrapTag':
                    Button(screen_object, text='Wrap Tags', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed(Value = TagIndexes)).place(x=910, y=6)
                elif AIM == 'UnwrapTag':
                    Button(screen_object, text='Unwrap Tags', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed(Value = TagIndexes)).place(x=910, y=6)

            else:

                dictionary['Indexes'] = str(Value.get()).split(',')
                if AIM == 'WrapTag':
                    GetModificationWindow(root=screen_object, function=RenameTagsAttributes__RedefineVAlues,dictionary=dictionary, Question1='Wrapped with  : ',Question2='Tag To be Wrapped : ')

                elif AIM == 'UnwrapTag':
                    GetModificationWindow(root=screen_object, function=RenameTagsAttributes__RedefineVAlues,dictionary=dictionary, Question1='Outer TagName : ',Question2='Inner TagName : ')


        Button(screen_object, text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed(Value = 0)).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to Rename Tag's Attributes ----------##
def RenameTagsAttributes__RedefineVAlues(dictionary):
    Result = False
    index = 1
    Tag_list = []
    Attribute_list = []

    if dictionary['ModificationType'] == 'ChooseTags':

        for tag in dictionary['SoupObject'].findAll(re.compile(dictionary['TagName'])):

            if dictionary['Aim'] == 'WrapTag' and str(index) in dictionary['Indexes'] and tag.name == dictionary['Answer2']:
                Result = True
                Tag_list.append(tag)

            elif dictionary['Aim'] == 'UnwrapTag' and str(index) in dictionary['Indexes'] and tag.name == dictionary['Answer2']:
                Tag_list.append(tag)
                Result = True

            else:
                for attribute, value in tag.attrs.items():

                    if dictionary['Aim'] == 'DeleteAttribute' and str(index) in dictionary['Indexes'] and attribute == dictionary['Answer2']:
                        Result = True
                        Tag_list.append(tag)
                        Attribute_list.append(attribute)

                    elif dictionary['Aim'] == 'Rename' and str(index) in dictionary['Indexes'] and attribute == dictionary['Answer1']:
                        Result = True
                        tag[dictionary['Answer2']] = tag[dictionary['Answer1']]
                        del tag[dictionary['Answer1']]

                    elif dictionary['Aim'] == 'Redefine' and str(index) in dictionary['Indexes'] and value == dictionary['Answer1']:
                        Result = True
                        tag[attribute] = dictionary['Answer2']


            index += 1

    else:

        for tag in dictionary['SoupObject'].findAll():

            if dictionary['Aim'] == 'WrapTag' and tag.name == dictionary['Answer2']:
                Result = True
                Tag_list.append(tag)

            elif dictionary['Aim'] == 'UnwrapTag' and tag.name == dictionary['Answer2']:
                Tag_list.append(tag)
                Result = True

            else:
                for attribute, value in tag.attrs.items():

                    if dictionary['Aim'] == 'DeleteAttribute' and tag.name == dictionary['TagName'] and attribute == dictionary['Answer2']:
                        Result = True
                        Tag_list.append(tag)
                        Attribute_list.append(attribute)

                    elif dictionary['Aim'] == 'Rename' and attribute == dictionary['Answer1']:
                        Result = True
                        tag[dictionary['Answer2']] = tag[dictionary['Answer1']]
                        del tag[dictionary['Answer1']]

                    elif dictionary['Aim'] == 'Redefine' and value == dictionary['Answer1']:
                        Result = True
                        tag[attribute] = dictionary['Answer2']

            if Result and dictionary['ModificationType'] == 'FirstTag':
                break

    if dictionary['Aim'] == 'DeleteAttribute':
        index = 0
        for tag in Tag_list:
            del tag[Attribute_list[index]]
            index += 1

    elif dictionary['Aim'] == 'WrapTag':
        for tag in Tag_list:
            tag.wrap(dictionary['SoupObject'].new_tag(dictionary['Answer1']))

    elif dictionary['Aim'] == 'UnwrapTag':
        for tag in Tag_list:
            tag.parent.unwrap()

    GetErrorOrSuccess(Result = Result,dictionary = dictionary)

##---------- END of this Function ----------##



##---------- Function to Remove characters from a String----------##
def RemoveCharacterFromString(String, DiscardThings):
    String1 = ''
    for character in String:
        if not character in DiscardThings:
            String1 = String1 + character

    return String1

##---------- END of this Function ----------##



##---------- Function to Get Contents of a Tag----------##
def GetThings(Tag,OldString,NewString):
    Things = []
    Signal = False
    OldString = RemoveCharacterFromString(String = OldString, DiscardThings = ['\n','\t',' '])
    for element in Tag.contents:
        if 'NavigableString' in str(type(element)) and RemoveCharacterFromString(String = str(element), DiscardThings=['\n', '\t', ' ']) == OldString:
                Things.append(NewString)
                Signal = True
        else:
            Things.append(element)

    return Things, Signal

##---------- END of this Function ----------##



##---------- Function to ConfigureChangeString(  . ModifyMenu)----------##
def ConfigureChangeString(screen_object, AIM):
    dictionary = {'root_screen': screen_object,
                  'SoupObject': GetSoupObject(DocumentName='DuplicateDocument'),
                  'AIM' : AIM }
    SearchItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')
    Button(screen_object, text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: RenameSelectedTagsAttributes__RedefineVAlues(StringTOFind = SearchItem.get(),function = ChangeRemoveString,dictionary = dictionary,Modify = 'String')).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function Change or Remove String of a Tag----------##
def ChangeRemoveString(dictionary):

    TagIndex = 1
    Signal = False
    for tag in dictionary['SoupObject'].findAll(re.compile(dictionary['TagName'])):

        if str(TagIndex) in dictionary['Indexes']:
            Things, Signal = GetThings(Tag = tag, OldString = dictionary['OldString'], NewString = dictionary['NewString'])

            tag.string = ''
            tag.string.insert_before(Things[0])
            index = 0

            for tagtoadd in range(1, len(Things)):
                NewTag = tag.contents[index]
                NewTag.insert_after(Things[tagtoadd])
                index += 1


    GetErrorOrSuccess(Result = Signal, dictionary = dictionary)

##---------- END of this Function ----------##



##---------- Function to get Modification Window to Change or Remove a Tag's String----------##
def ModificationWindowForString(dictionary, function):
    TempraryWindow = Toplevel(dictionary['root_screen'])
    dictionary['temprary_window'] = TempraryWindow
    TempraryWindow.geometry('350x300')
    dictionary['OldString'] = ''
    dictionary['NewString'] = ''

    TempraryWindow.title('Modification Window')
    Canvas(TempraryWindow, bg = 'lightgray',width = 350, height = 300).place(x=0,y=0)

    Label(TempraryWindow, text = 'Modification Bar', fg ='white', bg = 'purple',font = ('default',10,'bold'),width = 35).place(x=15,y=10)

    Label(TempraryWindow,text = 'Enter OldString : ',bg = 'lightgray').place(x=10,y=60)

    TextBox = Text(TempraryWindow, width = 35, height = 7)
    TextBox.place(x = 40,y=95)

    ##---------- Function to Go Back to Change Old String----------##
    def BACK():
        nonlocal TextBox,dictionary
        dictionary['NewString'] = TextBox.get('0.1',END)
        Label(TempraryWindow, text='Enter OldString : ', bg='lightgray').place(x=10, y=60)
        TextBox = Text(TempraryWindow, width=35, height=7)
        TextBox.place(x=40, y=95)
        TextBox.insert(END,dictionary['OldString'])
        Button(TempraryWindow, text=' Back ', fg='red', bg='white', activebackground='red', activeforeground='white',command = TempraryWindow.destroy).place(x=10, y=260)
        Button(TempraryWindow, text='Confirm String ', fg='blue', bg='white', activebackground='blue',activeforeground='white', command=lambda: WhenBelowButtonPressed(Signal='Confirm')).place(x=215, y=260)

    ##----------END of this Function----------##

    ##----------This function will execute when Below buttons will be pressed----------##
    def WhenBelowButtonPressed(Signal):
        nonlocal dictionary, TextBox
        if Signal == 'Confirm':
            dictionary['OldString'] = str(TextBox.get('0.1',END))
            Label(TempraryWindow, text='Enter NewString : ', bg='lightgray').place(x=10, y=60)
            TextBox = Text(TempraryWindow, width=35, height=7)
            TextBox.place(x=40, y=95)
            TextBox.insert(END, dictionary['NewString'])
            Button(TempraryWindow, text='Apply Changes', fg='green', bg='white', activebackground='green',activeforeground='white', command=lambda: WhenBelowButtonPressed(Signal='Apply Changes')).place(x=215,y=260)
            Button(TempraryWindow, text=' Back ', fg='red', bg='white', activebackground='red',activeforeground='white', command=lambda : BACK()).place(x=10, y=260)


        elif Signal == 'Apply Changes':
            dictionary['NewString'] = str(TextBox.get('0.1',END))
            function(dictionary = dictionary)

    ##----------END of this Function----------##


    Button(TempraryWindow, text = 'Confirm String', fg = 'blue', bg = 'white', activebackground = 'blue', activeforeground = 'white', command = lambda : WhenBelowButtonPressed(Signal = 'Confirm')).place(x=215, y=260)
    Button(TempraryWindow, text = ' Back ', fg = 'red', bg = 'white', activebackground = 'red', activeforeground = 'white', command = lambda : TempraryWindow.destroy).place(x=10, y=260)

    TempraryWindow.mainloop()

##---------- END of this Function ----------##



##---------- Function to Delete a Tag or its Contents/Elements----------##
def DeleteTag_Contents(screen_object,SoupObject,TagName,TagIndexes,ContentIndexes,AIM):
    TagContents = []
    index = 1
    Result = False
    for tag in SoupObject.findAll(re.compile(TagName)):
        if str(index) in TagIndexes:
            if AIM == 'DeleteTag':
                tag.extract()
            elif AIM == 'DeleteContents':
                for element in tag.contents:
                    if RemoveCharacterFromString(String=str(element), DiscardThings=['\n', ' ']) != '':
                        TagContents.append(element)
            Result = True
        index += 1


    if AIM == 'DeleteContents':
        for index in ContentIndexes:
            try:
                TagContents[int(index)-1].extract()
            except:
                pass
    dictionary = {'SoupObject':SoupObject,'root_screen':screen_object}
    print(Result)
    print(SoupObject)
    GetErrorOrSuccess(Result = Result,dictionary = dictionary)

##---------- END of this Function ----------##



##---------- Function to ShowTags With their Elements----------##
def ShowTagElements(screen_object,SoupObject,TagName,TagIndexes):
    GlobalIndex  = LocalIndex = 1
    tagindex = 1
    Result = "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n\n"

    for tag in SoupObject.findAll(re.compile(TagName)):
        if str(tagindex) in TagIndexes:
            LocalIndex = 1
            Result += f"\nTag Number : {tagindex}            Tag Name : <{tag.name}>\n\n\n"
            for element in tag.contents:
                if RemoveCharacterFromString(String = str(element),DiscardThings = ['\n',' ']) != '':
                    Result += f"-----Global Index : {GlobalIndex}   -----Local Index : {LocalIndex}\n\n{element}\n\n"
                    LocalIndex += 1
                    GlobalIndex += 1
            Result += '\n\n'
        tagindex += 1

    if Result == "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n\n":
        showerror('Show Error','No Match Found !!!')

    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')
        ContentIndexes = GetSearchBar(screen_object = screen_object,Question = 'Global Index : ',BarType = 'Searching')
        Button(screen_object, text='Delete', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white',command=lambda: DeleteTag_Contents(screen_object=screen_object, SoupObject=SoupObject,TagName=TagName,TagIndexes = TagIndexes, ContentIndexes = str(ContentIndexes.get()).split(','),AIM='DeleteContents')).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to ConfiguredeleteTags( .) ModificationMenu)----------##
def ConfigureDeleteTag(screen_object,AIM):
    SoupObject = GetSoupObject(DocumentName = 'DuplicateDocument')
    SearchingItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')


    ##---------- This Function will be executed when the below button pressed----------##
    def WhenBelowButtonPressed():
        SearchingTagsWithRelatedNames(screen_object=screen_object, StringToFind = SearchingItem.get(),SoupObject=SoupObject, Signal='WithIndex')
        TagIndexes = GetSearchBar(screen_object=screen_object, Question='Enter TagNumber : ', BarType='Searching')

        if AIM == 'DeleteTag':
            Button(screen_object, text='Delete', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: DeleteTag_Contents(screen_object = screen_object,SoupObject = SoupObject,TagName = SearchingItem.get(),TagIndexes = str(TagIndexes.get()).split(','),ContentIndexes = '',AIM = 'DeleteTag')).place(x=910, y=6)

        elif AIM == 'DeleteElements':
            Button(screen_object, text='Get Elements', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: ShowTagElements(screen_object = screen_object,SoupObject = SoupObject,TagName = SearchingItem.get(),TagIndexes = str(TagIndexes.get()).split(','))).place(x=910, y=6)

    ##---------- END of this Function ----------##


    Button(screen_object, text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed()).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function ConfigureWrapStrings( .) ModificationMenu)----------##
def ConfigureWrapStrings(screen_object,AIM):
    SoupObject = GetSoupObject(DocumentName = 'DuplicateDocument')
    dictionary = {'root_screen':screen_object,'SoupObject':SoupObject,'AIM':AIM}

    SearchingItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')

    def WhenBelowButtonPressed():
        nonlocal dictionary,SearchingItem
        SearchingTagsWithRelatedNames(screen_object = screen_object,StringToFind = SearchingItem.get(),SoupObject = SoupObject,Signal = 'WithIndex')
        dictionary['TagName'] =  SearchingItem.get()

        SearchingItem = GetSearchBar(screen_object=screen_object, Question='Enter TagNumber : ', BarType='Searching')

        Button(screen_object, text='Get String', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: ShowStrings(screen_object = screen_object,SoupObject = SoupObject,TagName = dictionary['TagName'],TagIndexes = str(SearchingItem.get()).split(','),dictionary = dictionary)).place(x=910, y=6)

    Button(screen_object, text='Search', bd=0, fg='white', bg='blue', activeforeground='blue',activebackground='white', command=lambda: WhenBelowButtonPressed()).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to WrapAndUnwrap Strings ----------##
def WrapStrings(dictionary):
    Result = False
    tagindex = globalindex = 1
    StringIndexes = str(dictionary['Answer1']).split(',')
    for tag in dictionary['SoupObject'].findAll(re.compile(dictionary['TagName'])):

        if str(tagindex) in dictionary['Indexes']:
            for element in tag.contents:

                if 'String' in str(type(element)) and str(globalindex) in StringIndexes:
                    if dictionary['AIM'] == 'Wrap':
                        element.wrap(dictionary['SoupObject'].new_tag(dictionary['Answer2']))
                        Result = True

                    elif dictionary['AIM'] == 'Unwrap':
                        ParentTag = element.parent
                        ParentTag.unwrap()
                        Result = True

                if 'String' in str(type(element)) :
                    globalindex += 1

        tagindex += 1

    GetErrorOrSuccess(Result = Result,dictionary = dictionary)

##---------- END of this Function ----------##



##---------- Function to ShowTags With their Elements----------##
def ShowStrings(screen_object,SoupObject,TagName,TagIndexes,dictionary):
    GlobalIndex  = LocalIndex = tagindex = 1
    Result = "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n\n"

    for tag in SoupObject.findAll(re.compile(TagName)):
        if str(tagindex) in TagIndexes:
            LocalIndex = 1
            Result += f"\nTag Number : {tagindex}            Tag Name : <{tag.name}>\n\n\n"
            for element in tag.contents:
                if 'String' in str(type(element)) and RemoveCharacterFromString(String = str(element),DiscardThings = ['\n',' ']) != '':
                    Result += f"-----Global Index : {GlobalIndex}   -----Local Index : {LocalIndex}\n\n{element}\n\n"
                    LocalIndex += 1
                    GlobalIndex += 1
            Result += '\n\n'
        tagindex += 1

    if Result == "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n\n":
        showerror('Show Error','No Match Found !!!')

    else:
        dictionary['Indexes'] = TagIndexes
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

        if dictionary['AIM'] == 'Wrap':
            GetModificationWindow(root = screen_object,function = WrapStrings,dictionary = dictionary,Question1 = 'Enter Global Index : ',Question2 = 'Wrapped With : ')

        elif dictionary['AIM'] == 'Unwrap':
            GetModificationWindow(root = screen_object,function = WrapStrings,dictionary = dictionary,Question1 = 'Enter Global Index : ',Question2 = 'Tag to be Unwrapped : ')

##---------- END of this Function ----------##

