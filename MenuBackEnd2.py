from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror
from bs4 import BeautifulSoup
from MenuBackEnd1 import configure_documents, GetDocumentName, GetDocument, SetResultTextBoxData, AddWhiteSpaces
import re


##---------- Making Global Variables ----------##
SearchBar = NavigateBar = False
TagNames_TagValues = {'OriginalDocument' : '', 'DuplicateDocument' : '', 'ExperimentResult' : ''}
SearchHistory = []


##---------- Function to GetSoupObject----------##
def GetSoupObject():
    DocType = GetDocumentName()
    Document = GetDocument(DocType=DocType)
    try:
        SoupObject = BeautifulSoup(Document.get('0.1',END),'html.parser',multi_valued_attributes = None)
    except:
        SoupObject = BeautifulSoup(Document,'html.parser',multi_valued_attributes = None)
    return SoupObject

##---------- END of this Function ----------##



##---------- Function to ConfigureSearchTags(1. SearchMenu)----------##
def ConfigureSearchTags(screen_object):
    SoupObject = GetSoupObject()
    SearchingItem = GetSearchBar(screen_object = screen_object, Question = 'Enter TagName : ',BarType = 'Searching')
    Button(screen_object, text = 'Search', bd = 0, fg = 'white', bg = 'blue',activeforeground = 'blue',activebackground = 'white',command = lambda: GetTagsSearched(screen_object = screen_object, StringToFind = SearchingItem.get(), SoupObject = SoupObject)).place(x=910,y=6)

##---------- END of this Function ----------##


##---------- Function to GetFocus in a text/Entry Widget----------##
def GetFocus(event,Widget):
    Widget.focus_set()

##---------- END of this Function ----------##



##---------- Function to GetSearchBar or NavigateBar on the screen----------##
def GetSearchBar(screen_object, Question, BarType):
    global SearchBar, NavigateBar, SearchHistory, SearchingItem

    if SearchBar or NavigateBar:
        CloseNavigateAndSearchBar(screen_object = screen_object, BarType = BarType)

    Label(screen_object, text = Question).place(x=580, y=8)

    SearchingItem = Combobox(screen_object,value = SearchHistory)
    SearchingItem.place(x=710,y=6)
    SearchingItem.bind('<Enter>',lambda event: GetFocus(event = event,Widget = SearchingItem))

    if BarType == 'Searching':
        SearchBar = True
    else:
        NavigateBar = True
    return SearchingItem

##---------- END of this Function ----------##


##---------- Function to AddSearchHistory----------##
def AddSearchHistory(ThingToAdd):
    global SearchHistory
    if ThingToAdd not in SearchHistory:
        SearchHistory.append(ThingToAdd)

##---------- END of this Function ----------##



##---------- Function to CLose NavigationBar or SearchBar----------##
def CloseNavigateAndSearchBar(screen_object, BarType):
    global NavigateBar, SearchBar
    if BarType == 'Navigation':
        if NavigateBar:
            Label(screen_object, text = '                                                                                                                ',bg= 'lightgray',font = ('arial',15,'bold')).place(x=580,y=6)
            Label(screen_object, text='                       ',bd = 0, fg='black', bg='black', font=('arial',19,'bold')).place(x=50, y=630)
            NavigateBar = False
        else:
            showerror('Show Error', 'There is no NavigationBar available')

    elif BarType == 'Searching':
        if SearchBar:
            Label(screen_object, text = '                                                                                                                ',bg= 'lightgray',font = ('arial',15,'bold')).place(x=580,y=6)
            SearchBar = False
        else:
            showerror('Show Error', 'There is no Searchbar available')

##---------- END of this Function ----------##



##---------- Function to GetTagsSearched----------##
def GetTagsSearched(screen_object, StringToFind, SoupObject):
    Result = '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n'
    if StringToFind == '':
        for item in SoupObject.findAll():
            Result += str(item) + '\n'
    else:
        for item in SoupObject.findAll(StringToFind):
            Result += str(item) + '\n'
    if Result == '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n':
        showerror('Show Error','No Match Found!!!')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = StringToFind)
        configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')

##---------- END of this Function ----------##


##---------- Function to ConfigureSearchAttributes(2., 6., 7. SearchMenu)----------##
def ConfigureSearchAttributes(screen_object, signal):
    SoupObject = GetSoupObject()
    SearchingItem = GetSearchBar(screen_object = screen_object, Question = 'Enter Attribute : ',BarType = 'Searching')

    Button(screen_object, text = 'Search', bd = 0, fg = 'white', bg = 'blue',activeforeground = 'blue',activebackground = 'white',command = lambda: GetAttributeSearched(screen_object = screen_object, StringTofind = SearchingItem.get(), SoupObject = SoupObject, signal = signal)).place(x=910,y=6)

##---------- END of this Function ----------##


##---------- Function to GetAttributeSearched----------##
def GetAttributeSearched(screen_object, StringTofind, SoupObject, signal):

    Result = '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n'

    for tag in SoupObject.findAll():
        for attribute, value in tag.attrs.items():

            if signal == 'Tags&Attributes':
                if StringTofind == str(attribute) or StringTofind == '':
                    Result += str(tag) + '\n'
            elif signal == 'Values&Attributes':
                if StringTofind == str(attribute) or StringTofind == '':
                    Result += f"Attribute Name  :  {str(attribute)}          Attributes's Value  :  {str(value)}\n"
            elif signal == 'Attributes&Values':
                if StringTofind == str(value) or StringTofind == '':
                    Result += f"Attribute Name  :  {str(attribute)}          Attributes's Value  :  {str(value)}\n"

    if Result == '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n':
        showerror('Show Error','No Match Found!!!')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = StringTofind)
        configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')

##---------- END of this Function ----------##


##---------- Function to ConfigureTagsUsingNumber(5. SearchMenu)----------##
def ConfigureTagsUsingNumber(screen_object):
    SoupObject = GetSoupObject()
    SearchingItem = GetSearchBar(screen_object = screen_object,Question = 'Enter TagNumber : ',BarType = 'Searching')

    Button(screen_object, text='Search', bd=0, fg='white', bg='blue',activeforeground = 'blue',activebackground = 'white',command=lambda: GetNumberthTag(screen_object = screen_object,SoupObject = SoupObject,SearchingItem = SearchingItem.get())).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to get a Tag using Number----------##
def GetNumberthTag(screen_object, SoupObject, SearchingItem):
    if not SearchingItem.endswith(','):
        SearchingItem += ','
    SearchingIndexes = str(SearchingItem).split(',')
    Result = '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n'
    index = 1
    for tag in SoupObject.findAll():
        if str(index) in SearchingIndexes or SearchingItem == ',':
            Result += str(tag) + '\n'
        index+=1
    if Result == '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n':
        showerror('Show Error','No Match Found')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = SearchingItem)
        configure_documents(screen_object=screen_object, DocType='ExperimentResult')

##---------- END of this Function ----------##


##---------- Function to NavigateParentTag of a Normal Tag(5. SearchMenu)----------##
def NavigateParentTag(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'parent',PreviousResult = PreviousResult)

##---------- END of this Function ----------##



##---------- Function to NavigateChildTag of a Normal Tag(6. SearchMenu)----------##
def NavigateChildTag(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'direct child',PreviousResult = PreviousResult)

##---------- END of this Function ----------##


##---------- Function to NavigateDescendants of a Normal Tag(7. SearchMenu)----------##
def NavigateDescendants(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'descendants',PreviousResult = PreviousResult)

##---------- END of this Function ----------##


##---------- Function to NavigateNextSiblings of a Normal Tag(8. SearchMenu)----------##
def NavigateNextSiblings(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'next siblings',PreviousResult = PreviousResult)

##---------- END of this Function ----------##


##---------- Function to NavigatePreviousSiblings of a Normal Tag(9. SearchMenu)----------##
def NavigatePreviousSiblings(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'previous siblings',PreviousResult = PreviousResult)

##---------- END of this Function ----------##



##---------- Function to NavigateNextElements of a Normal Tag(10. SearchMenu)----------##
def NavigateNextElements(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'next elements',PreviousResult = PreviousResult)

##---------- END of this Function ----------##



##---------- Function to NavigateNextElements of a Normal Tag(7. NavigateMenu)----------##
def NavigatePreviousElements(screen_object, SoupObject, TagNumber, TagName, PreviousResult):
    NavigatingTagsRelatives(screen_object = screen_object, SoupObject = SoupObject, TagNumber = TagNumber, TagName = TagName, RelativeType = 'previous elements',PreviousResult = PreviousResult)

##---------- END of this Function ----------##



##---------- Function to Navigate a Tag's Relatives----------##
def NavigatingTagsRelatives(screen_object, SoupObject, TagNumber, TagName, RelativeType, PreviousResult):
    if not str(TagNumber).endswith(','):
        TagNumber += ','
    TagNumberList = str(TagNumber).split(',')
    index = 1
    signal = False
    Result = '\n\t\t\t\t--------------- Results that Matches to your Search ---------------\n\n\n\n'
    for tag in SoupObject.findAll(TagName):
        if str(index) in TagNumberList:

            if RelativeType == 'parent' and tag.parent != '\n':
                signal = True
                Result += f"\t********** Parent Tag of TagNumber : {index} **********\n\n{str(tag.parent)}"

            elif RelativeType == 'direct child':
                Result += f"\t********** Child Tag of TagNumber : {index} **********\n\n\n"
                ResultNumber = 1
                for child in tag.children:
                    if child != '\n':
                        Result += f"*****Child Number = {ResultNumber}*****\n" + str(child) +'\n\n'
                        signal = True
                        ResultNumber += 1


            elif RelativeType == 'descendants':
                Result += f"\t********** Descendant Tag/Tags of TagNumber : {index} **********\n\n\n"
                ResultNumber = 1
                for descendant in tag.descendants:
                    if descendant != '\n' and descendant != ',\n' and descendant != None:
                        Result += f"*****Descendant Number = {ResultNumber}*****\n" + str(descendant) +'\n\n'
                        signal = True
                        ResultNumber += 1


            elif RelativeType == 'next siblings':
                Result += f"\t**********  Next Sibling/Siblings of TagNumber : {index} **********\n\n\n"
                ResultNumber = 1
                for nextsibling in tag.next_siblings:
                    if nextsibling != None and nextsibling != '\n':
                        signal = True
                        Result += f"*****Sibling Number = {ResultNumber}*****\n" + str(nextsibling) +'\n\n'
                        ResultNumber += 1


            elif RelativeType == 'previous siblings':
                Result += f"\t**********  Previous Sibling/Siblings of TagNumber : {index} **********\n\n\n"
                ResultNumber = 1
                for previoussibling in tag.previous_siblings:
                    if previoussibling != None and previoussibling != '\n':
                        signal = True
                        Result += f"*****Sibling Number = {ResultNumber}*****\n" + str(previoussibling) +'\n\n'
                        ResultNumber += 1

            elif RelativeType == 'next elements':
                Result += f"\t**********  Next Element/Elements of TagNumber : {index} **********\n\n\n"
                ResultNumber = 1
                for nextelement in tag.next_elements:
                    if nextelement != None and nextelement != '\n':
                        signal = True
                        Result += f"*****Element Number = {ResultNumber}*****\n" + str(nextelement) +'\n\n'
                        ResultNumber += 1

            elif RelativeType == 'previous elements':
                Result += f"\t**********  Previous Element/Elements of TagNumber : {index} **********\n\n\n"
                ResultNumber = 1
                for previouselement in tag.previous_elements:
                    if previouselement != None and previouselement != '\n':
                        signal = True
                        Result += f"*****Element Number = {ResultNumber}*****\n" + str(previouselement) +'\n\n'
                        ResultNumber += 1

        index+=1

    Result += "\n\n"

    if not signal:
        showerror('Show Error','No Match Found')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = TagName)
        configure_documents(screen_object = screen_object, DocType = 'ExperimentResult')
        PreviousandActualResult(screen_object = screen_object,PreviousResult = PreviousResult,ActualResult = Result)
##---------- END of this Function ----------##



##---------- Function to Show Previous and Actual Result----------##
def PreviousandActualResult(screen_object, PreviousResult, ActualResult):

    def GetResult(ResultType):
        if ResultType == 'Previous':
            Button(screen_object,text = '  Actual Result   ',fg = 'white', bg = 'purple',activeforeground = 'purple',activebackground = 'white', command = lambda: GetResult(ResultType = 'Actual')).place(x=50,y=630)
            SetResultTextBoxData(DocType = 'ExperimentResult',Data = PreviousResult)

        else:
            Button(screen_object,text = 'Previous Result ', fg='white', bg='purple',activeforeground = 'purple',activebackground = 'white',command=lambda: GetResult(ResultType='Previous')).place(x=50, y=630)
            SetResultTextBoxData(DocType = 'ExperimentResult',Data = ActualResult)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

    Button(screen_object, text='Previous Result ', fg='white', bg='purple',activeforeground = 'purple',activebackground = 'white',command=lambda: GetResult(ResultType='Previous')).place(x=50, y=630)

##---------- END of this Function ----------##



##---------- Function to ConfigureNavigateRelatives or it first asks a user a TagName whose relatives has to be search----------##
def ConfigureNavigateRelatives(screen_object, ResultStartingLine, Function):
    SoupObject = GetSoupObject()
    StringTofind = GetSearchBar(screen_object = screen_object, Question = 'Enter TagName : ',BarType = 'Navigation')

    def WhenBelowButtonPressed():
        signal, TagNumber, PreviousResult = ShowTags(screen_object=screen_object, SoupObject=SoupObject, TagtoSearch=StringTofind.get(), ResultStartingLine = ResultStartingLine, BarType = 'Navigation')

        if signal:
            Button(screen_object, text='Search', bd=0, fg='white', bg='blue',activeforeground = 'blue',activebackground = 'white', command=lambda: Function(screen_object = screen_object, SoupObject = SoupObject,TagNumber = TagNumber.get(), TagName = StringTofind.get(),PreviousResult = PreviousResult)).place(x=910, y=6)

    Button(screen_object, text='Search', bd=0, fg='white', bg='blue',activeforeground = 'blue',activebackground = 'white',command=lambda: WhenBelowButtonPressed()).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to Show Searched Tags on the screen----------##
def ShowTags(screen_object, SoupObject, TagtoSearch, ResultStartingLine, BarType):
    # Result = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Parent -----------------\n\n\n\n"
    Result = ResultStartingLine
    index = 1
    for tag in SoupObject.findAll(TagtoSearch):
        Result += str(index) + '.)   ' + str(tag) + '\n\n\n'
        index+=1
    if Result == ResultStartingLine:
        showerror('Show Error','No Match Found')
        return False,0,0
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = TagtoSearch)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')
        TagNumber = GetSearchBar(screen_object = screen_object,Question = 'Enter TagNumber : ',BarType = BarType)
        return True,TagNumber,Result

##---------- END of this Function ----------##


##---------- Function to Configure_Searching_Tags_Using_Related_Names(2. SearchMenu)----------##
def Configure_SearchingTagsWithRelatedNames(screen_object):
    SoupObject = GetSoupObject()
    StringToFind = GetSearchBar(screen_object = screen_object,Question = 'Enter TagName : ',BarType = 'Searching')
    Button(screen_object, text='Search', bd=0, fg='white', bg='blue',activeforeground = 'blue',activebackground = 'white',command=lambda: SearchingTagsWithRelatedNames(screen_object = screen_object,StringToFind = StringToFind.get(),SoupObject = SoupObject,Signal = 'WithoutIndex')).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to search tags using some related names enterd by the user----------##
def SearchingTagsWithRelatedNames(screen_object, StringToFind, SoupObject, Signal):
    Result = "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n\n"
    index = 1
    for tag in SoupObject.findAll(re.compile(StringToFind)):
        if Signal == 'WithIndex':
            Result += str(index) + '. )    ' + str(tag) + '\n\n\n'
        else:
            Result += str(tag) + '\n\n'
        index += 1
    if Result == "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n\n":
        showerror('Show Error','No Match Found')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = StringToFind)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

##---------- END of this Function ----------##



##---------- Function to ViewOnlyTagNames of a particular Document-Type(7. ViewMenu)----------##
def ViewOnlyTagNames(screen_object):
    DocType = GetDocumentName()
    Document = GetDocument(DocType = DocType)
    global TagNames_TagValues
    try:
        TagNames_TagValues[DocType] = str(Document.get('0.1',END))
    except:
        TagNames_TagValues[DocType] = str(Document)
    SoupObject = BeautifulSoup(TagNames_TagValues[DocType], 'html.parser')
    Result = "\n\t\t\t\t----------------- Results of Your Experiment -----------------\n\n\n\n"

    for tag in SoupObject.findAll():
        Result += tag.name + '\n\n'

    if Result == "\n\t\t\t\t----------------- Results of Your Experiment -----------------\n\n\n\n":
        showerror('Show Error','Error with Document Type')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

##---------- END of this Function ----------##



##---------- Function to ViewTagsContent of Particular Document-Type(8. ViewMenu)----------##
def ViewTagsContent(screen_object):
    DocType = GetDocumentName()
    global TagNames_TagValues
    try:
        if TagNames_TagValues[DocType] == '':
            showerror('Show Error','Error with Document Type')
        else:
            Result = TagNames_TagValues[DocType]
            SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
            configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

    except:
        pass
##---------- END of this Function ----------##



##---------- Function to View Attributes and their Corresponding Values used in the Document(6. ViewMenu)----------##
def ConfigureAttributesAndValues(screen_object):

    SoupObject = GetSoupObject()
    Result = "\n\t\t\t\t----------------- Results of Your Experiment -----------------\n\n\n"
    TagNumber = AttributeNumber = signal = 1

    for tag in SoupObject.findAll():

        Result += f"\n\nTag Number  =  {TagNumber}          Tag Name  =  {tag.name}\n"
        for attribute,value in tag.attrs.items():

            if AttributeNumber == 1:
                Result += f"\n            Attribute Number     Attribute Name     Attribute's Value\n"
                signal = 0
            Result += f"----------- {AddWhiteSpaces(length = len(str(AttributeNumber)),maxlength = 21,string = str(AttributeNumber))}{AddWhiteSpaces(length = len(str(attribute)),maxlength = 19,string = str(attribute))}{value}\n"
            AttributeNumber+=1

        if AttributeNumber == 1:
            Result += "\n########## No Attributes to Show ##########\n\n"

        AttributeNumber = 1
        TagNumber+=1

    if signal:
        showerror('Show Error','No Results to Show!!')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

##---------- END of this Function ----------##



##---------- Function to ConfigureTagsUsingValues(4. SearchMenu)----------##
def ConfigureTagsUsingValues(screen_object):
    SoupObject = GetSoupObject()
    StringToFind = GetSearchBar(screen_object = screen_object,Question = 'Enter Value : ',BarType = 'Searching')
    Button(screen_object, text='Search', bd=0, fg='white', bg='blue',activeforeground = 'blue',activebackground = 'white',command=lambda: GetTagsUsingValues(screen_object = screen_object,SoupObject = SoupObject,StringToFind = StringToFind.get())).place(x=910, y=6)

##---------- END of this Function ----------##



##---------- Function to Search Tags using their attribute's values----------##
def GetTagsUsingValues(screen_object, SoupObject, StringToFind):
    Result = "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n"
    TagNumber = 1
    for tag in SoupObject.findAll():
        ListOfValues = [tag.attrs[attribute] for attribute in tag.attrs]
        if StringToFind in ListOfValues:
            Result += f"\n\nTag Number  =  {TagNumber}          Tag Name  =  {tag.name}\n\n{str(tag)}\n"
        TagNumber+=1

    if Result == "\n\t\t\t----------------- Results that Matches to your Search -----------------\n\n\n":
        showerror('Show Error','No Results to Show')
    else:
        SetResultTextBoxData(DocType = 'ExperimentResult',Data = Result)
        AddSearchHistory(ThingToAdd = StringToFind)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult')

##---------- END of this Function ----------##



##---------- Function to GiveHelp to the User----------##
def GetHelp(screen_object, Position):

    try:
        HelpingContent = Position + "\n\n\t\t\t\t*************** WEB--SCRAPPER'S DOCUMENTATION ***************\n"

        with open('Documentation.txt','r') as f:
            HelpingContent += f.read()

        HelpingContent += "\n\n\t\t\t\t*************** END of DOCUMENTATION ***************\n"


        SetResultTextBoxData(DocType = 'ExperimentResult',Data = HelpingContent)
        configure_documents(screen_object = screen_object,DocType = 'ExperimentResult_Documentation')

    except:
        showerror('Show Error',"Sorry!!! We Can't Help You !!!  \n  Documentation File Missing  ")

##---------- END of this Function ----------##

