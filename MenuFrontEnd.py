from MenuBackEnd1 import *
from MenuBackEnd2 import *
from MenuBackEnd3 import *


##---------- Class to create MenuBar ----------##

class MenuBar():

    ##---------- Method to Create Menus/MenuBar ----------#
    def __init__(self ,screen_object ,fg = 'white' ,bg = 'black' ,active_bg = 'lightblue'):
        self.Menu_Bar = Menu(screen_object, fg = fg, bg = bg, activebackground = active_bg)

        screen_object.config(menu=self.Menu_Bar)

    ##---------- END of this Method ----------##


    ##---------- Method to Create FileMenu ----------##
    def FileMenu(self, screen_object):

        Inner_File_Menu = Menu(self.Menu_Bar, tearoff = False, fg = 'white', bg = 'black' , activebackground = 'orange')
        Inner_File_Menu.add_separator()

        Inner_File_Menu.add_command(label = '   Open HTML Document  ', command = lambda: Open_HTML_Document(screen_object = screen_object))
        Inner_File_Menu.add_command(label = '   Open URL Bar   ', command = lambda: GetURLBar(screen_object = screen_object))
        Inner_File_Menu.add_command(label = '   Duplicate the Original  ', command = lambda: Duplicate_the_Original(screen_object = screen_object))
        Inner_File_Menu.add_separator()

        Inner_File_Menu.add_command(label = '   Save Original as  ', command = lambda: To_Process_Saving_of_Files(ThingtoSave = 'Original', signal = 'Save as'))
        Inner_File_Menu.add_command(label='   Save Duplicate   ',command=lambda: To_Process_Saving_of_Files(ThingtoSave = 'Duplicate', signal = 'Save'))
        Inner_File_Menu.add_command(label='   Save Duplicate as  ',command=lambda: To_Process_Saving_of_Files(ThingtoSave = 'Duplicate', signal = 'Save as'))
        Inner_File_Menu.add_command(label='   Save Result as  ',command=lambda: To_Process_Saving_of_Files(ThingtoSave='Result',signal='Save as'))
        Inner_File_Menu.add_separator()

        Inner_File_Menu.add_command(label='   Back to Origin  ',command=lambda: BackToOrigin(screen_object = screen_object))

        Inner_File_Menu.add_command(label = '   Exit   ', command = quit)
        Inner_File_Menu.add_separator()

        self.Menu_Bar.add_cascade(label = '  File  ',menu = Inner_File_Menu)

    ##---------- END of this METHOD ----------##



    ##---------- Method to Create ViewMenu ----------##
    def ViewMenu(self, screen_object):
        Inner_View_Menu = Menu(self.Menu_Bar, tearoff=False, fg='white', bg='black', activebackground='orange')
        Inner_View_Menu.add_separator()

        Inner_View_Menu.add_command(label='   Normal Structure   ', command = lambda: ChangeStructureType(screen_object = screen_object, NewStructureType = 'Normal'))
        Inner_View_Menu.add_command(label='   Nested Structure   ', command = lambda: ChangeStructureType(screen_object = screen_object, NewStructureType = 'Nested'))
        Inner_View_Menu.add_separator()

        Inner_View_Menu.add_command(label="   Tags Used   ", command = lambda: ConfigureTagList(screen_object = screen_object))
        Inner_View_Menu.add_command(label="   Text Used   ", command = lambda: ConfigureDocumentText(screen_object = screen_object))
        Inner_View_Menu.add_command(label="   Comments Used   ", command = lambda: ConfigureComments(screen_object = screen_object))
        Inner_View_Menu.add_command(label="   Attributes and Values   ", command = lambda: ConfigureAttributesAndValues(screen_object = screen_object))
        Inner_View_Menu.add_separator()

        Inner_View_Menu.add_command(label="   View Only Tag names    ", command = lambda: ViewOnlyTagNames(screen_object = screen_object))
        Inner_View_Menu.add_command(label="   View Tags Content    ", command = lambda: ViewTagsContent(screen_object = screen_object))
        Inner_View_Menu.add_separator()

        Inner_View_Menu.add_command(label="   Quick Documentation    ", command = lambda: GetHelp(screen_object = screen_object, Position = '0.1'))
        Inner_View_Menu.add_separator()

        self.Menu_Bar.add_cascade(label='  View  ', menu=Inner_View_Menu)

    ##---------- END of this METHOD ----------##



    ##---------- Method to Create SearchMenu ----------##
    def SearchMenu(self, screen_object):
        Inner_Search_Menu = Menu(self.Menu_Bar, tearoff=False, fg='white', bg='black', activebackground='orange')
        Inner_Search_Menu.add_separator()

        Inner_Search_Menu.add_command(label='   Tags Using Exact Names   ', command = lambda: ConfigureSearchTags(screen_object = screen_object) )
        Inner_Search_Menu.add_command(label='   Tags Using Related Names   ', command = lambda: Configure_SearchingTagsWithRelatedNames(screen_object = screen_object))
        Inner_Search_Menu.add_command(label='   Tags Using Attributes   ', command = lambda: ConfigureSearchAttributes(screen_object = screen_object,signal = 'Tags&Attributes'))
        Inner_Search_Menu.add_command(label='   Tags Using Values   ', command = lambda: ConfigureTagsUsingValues(screen_object = screen_object))
        Inner_Search_Menu.add_command(label='   Tags Using Number  ', command = lambda: ConfigureTagsUsingNumber(screen_object = screen_object))
        Inner_Search_Menu.add_separator()

        Inner_Search_Menu.add_command(label='   Attributes Using Values   ', command = lambda: ConfigureSearchAttributes(screen_object = screen_object,signal = 'Attributes&Values'))
        Inner_Search_Menu.add_separator()

        Inner_Search_Menu.add_command(label='   Values Using Attributes   ', command = lambda: ConfigureSearchAttributes(screen_object = screen_object,signal = 'Values&Attributes'))
        Inner_Search_Menu.add_separator()

        Inner_Search_Menu.add_command(label='   Close SearchBar   ',command=lambda: CloseNavigateAndSearchBar(screen_object = screen_object,BarType = 'Searching'))
        Inner_Search_Menu.add_separator()

        self.Menu_Bar.add_cascade(label='  Search  ', menu=Inner_Search_Menu)

    ##---------- END of this METHOD ----------##



    ##---------- Method to Create NavigateMenu ----------##
    def NavigateMenu(self, screen_object):
        Inner_Navigate_Menu = Menu(self.Menu_Bar, tearoff=False, fg='white', bg='black', activebackground='orange')
        Inner_Navigate_Menu.add_separator()

        Inner_Navigate_Menu.add_command(label="   Tag's Parent   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Parent -----------------\n\n\n\n",Function = NavigateParentTag))
        Inner_Navigate_Menu.add_command(label="   Tag's Direct Child   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Child -----------------\n\n\n\n",Function = NavigateChildTag))
        Inner_Navigate_Menu.add_command(label="   Tag's Descendants   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Descendants -----------------\n\n\n\n",Function = NavigateDescendants))
        Inner_Navigate_Menu.add_command(label="   Tag's Next Sibling   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Next Siblings -----------------\n\n\n\n",Function = NavigateNextSiblings))
        Inner_Navigate_Menu.add_command(label="   Tag's Previous Sibling   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Previous Siblings -----------------\n\n\n\n",Function = NavigatePreviousSiblings))
        Inner_Navigate_Menu.add_separator()

        Inner_Navigate_Menu.add_command(label="   Tag's Next Elements   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Next Elements -----------------\n\n\n\n",Function = NavigateNextElements))
        Inner_Navigate_Menu.add_command(label="   Tag's Previous Elements   ", command = lambda: ConfigureNavigateRelatives(screen_object = screen_object, ResultStartingLine = "\n\t\t\t----------------- Enter TagNumber to find that Tag's Next Elements -----------------\n\n\n\n",Function = NavigatePreviousElements))
        Inner_Navigate_Menu.add_separator()

        Inner_Navigate_Menu.add_command(label="   Close NavigationBar   ", command = lambda: CloseNavigateAndSearchBar(screen_object = screen_object,BarType = 'Navigation'))
        Inner_Navigate_Menu.add_separator()


        self.Menu_Bar.add_cascade(label='  Navigate  ', menu=Inner_Navigate_Menu)

    ##---------- END of this METHOD ----------##



    ##---------- Method to Create ModificationMenu ----------##
    def ModifyMenu(self, screen_object):
        Inner_Modify_Menu = Menu(self.Menu_Bar, tearoff=False, fg='white', bg='black', activebackground='orange')
        Inner_Modify_Menu.add_separator()

        Inner_Modify_Menu.add_command(label='   Modify Tag Names   ', command = lambda: ConfigureRenameTags(screen_object = screen_object))
        Inner_Modify_Menu.add_command(label="   Modify Attribute Names   ", command = lambda: ConfigureRenameAttribute__RedefineVAlues(screen_object = screen_object,Signal = 'Rename'))
        Inner_Modify_Menu.add_command(label="   Modify Values   ", command = lambda: ConfigureRenameAttribute__RedefineVAlues(screen_object = screen_object,Signal = 'Redefine'))
        Inner_Modify_Menu.add_command(label="   Modify String   ", command = lambda: ConfigureChangeString(screen_object,AIM = 'Modify'))
        Inner_Modify_Menu.add_separator()

        Inner_Modify_Menu.add_command(label="   Delete a Tag   ", command = lambda: ConfigureDeleteTag(screen_object = screen_object,AIM = 'DeleteTag'))
        Inner_Modify_Menu.add_command(label="   Delete Tag's Elements   ", command = lambda: ConfigureDeleteTag(screen_object = screen_object,AIM = 'DeleteElements'))
        Inner_Modify_Menu.add_command(label="   Delete Tag's Attributes   ", command = lambda: ConfigureDeleteAttribue(screen_object = screen_object))
        Inner_Modify_Menu.add_separator()

        Inner_Modify_Menu.add_command(label="   Wrap Tags   ", command = lambda: ConfigureWrapTags(screen_object = screen_object,AIM = 'WrapTag'))
        Inner_Modify_Menu.add_command(label="   Wrap Strings   ", command = lambda: ConfigureWrapStrings(screen_object = screen_object,AIM = 'Wrap'))
        Inner_Modify_Menu.add_command(label="   Unwrap Tags   ", command = lambda: ConfigureWrapTags(screen_object = screen_object,AIM = 'UnwrapTag'))
        Inner_Modify_Menu.add_command(label="   Unwrap Strings   ", command = lambda: ConfigureWrapStrings(screen_object = screen_object,AIM = 'Unwrap'))
        Inner_Modify_Menu.add_separator()


        self.Menu_Bar.add_cascade(label='  Modification  ', menu=Inner_Modify_Menu)

    ##---------- END of this METHOD ----------##



    ##---------- Method to Create RunCodeInBrowser ----------##
    def OpenInBrowser(self, screen_object):

        self.Menu_Bar.add_command(label = '  Open In Browser  ',command = lambda :OpenFileInBrowser(screen_object = screen_object))

    ##---------- END of this METHOD ----------##


    ##---------- Method to Create HelpMenu ----------##
    def ThemeMenu(self, screen_object):
        self.Menu_Bar.add_command(label='  Themes  ',command=lambda: GetThemeWindow(screen_object = screen_object))


    ##---------- Method to Create HelpMenu ----------##
    def HelpMenu(self, screen_object):
        Inner_Help_Menu = Menu(self.Menu_Bar, tearoff=False, fg='white', bg='black', activebackground='orange')
        Inner_Help_Menu.add_separator()

        Inner_Help_Menu.add_command(label = '   Regarding File   ',command = lambda: GetHelp(screen_object = screen_object, Position = '7.0'))
        Inner_Help_Menu.add_separator()

        Inner_Help_Menu.add_command(label = '   Regarding View   ',command = lambda: GetHelp(screen_object = screen_object, Position = '56.0'))
        Inner_Help_Menu.add_command(label = '   Regarding Search   ',command = lambda: GetHelp(screen_object = screen_object, Position = '101.0'))
        Inner_Help_Menu.add_separator()

        Inner_Help_Menu.add_command(label = '   Regarding Navigation   ',command = lambda: GetHelp(screen_object = screen_object, Position = '147.0'))
        Inner_Help_Menu.add_command(label = '   Regarding Modification   ',command = lambda: GetHelp(screen_object = screen_object, Position = '197.0'))
        Inner_Help_Menu.add_separator()

        Inner_Help_Menu.add_command(label = '   Regarding Open In Browser   ',command = lambda: GetHelp(screen_object = screen_object, Position = '273.0'))
        Inner_Help_Menu.add_command(label = '   Regarding Themes   ',command = lambda: GetHelp(screen_object = screen_object, Position = '273.0'))
        Inner_Help_Menu.add_separator()

        self.Menu_Bar.add_cascade(label='  Get Help  ', menu=Inner_Help_Menu)

    ##---------- END of this METHOD ----------##


##---------- END of Class "MenuBar" ----------##




def gui():

    screen = Tk()

    screen.geometry('1366x768')

    menubar = MenuBar(screen_object = screen)
    menubar.FileMenu(screen_object = screen)
    menubar.ViewMenu(screen_object = screen)
    menubar.SearchMenu(screen_object = screen)
    menubar.NavigateMenu(screen_object = screen)
    menubar.ModifyMenu(screen_object = screen)

    Canvas(screen,width = 1366, height = 50, bg = 'black').place(x=0,y=0)

    # Button(screen, text='Search', bd=0, fg='white', bg='blue').place(x=910, y=6)

    screen.mainloop()


# gui()
