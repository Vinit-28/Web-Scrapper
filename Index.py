from MenuFrontEnd import *
from tkinter import *
from MenuBackEnd1 import configure_documents
import os


##---------- Class to Start Applictaion ----------##
class WebScrapper:

    def __init__(self):
        pass

    ##---------- Method to GetScreen ----------##
    def get_screen(self):
        self.screen = Tk()

        self.screen.geometry('1366x768')
        self.screen.title('WEB -- SCRAPPER')

        self.get_menubars()
        self.get_file_pannel()

        self.screen.mainloop()

    ##---------- END of this  Method----------##

    ##---------- Method to GetFilePannel ----------##
    def get_file_pannel(self):
        Canvas(self.screen, width=1366, height=768, bg='black').place(x=0, y=0)
        Canvas(self.screen, width=1366, height=35, bg='lightgray').place(x=0, y=0)

        Button(self.screen, text='Original Document', fg='black', bg='lightgray', activebackground='lightblue', bd=0,
               command=lambda: configure_documents(screen_object=self.screen, DocType='OriginalDocument')).place(x=15,
                                                                                                                 y=4)
        Button(self.screen, text='Duplicate Document', fg='black', bg='lightgray', activebackground='lightblue', bd=0,
               command=lambda: configure_documents(screen_object=self.screen, DocType='DuplicateDocument')).place(x=200,
                                                                                                                  y=4)
        Button(self.screen, text='Experiment Results', fg='black', bg='lightgray', activebackground='lightblue', bd=0,
               command=lambda: configure_documents(screen_object=self.screen, DocType='ExperimentResult')).place(x=385,
                                                                                                                 y=4)

    ##---------- END of this Method----------##

    ##---------- Method to GetMenuBars ----------##
    def get_menubars(self):
        menubar = MenuBar(screen_object=self.screen)
        menubar.FileMenu(screen_object=self.screen)
        menubar.ViewMenu(screen_object=self.screen)
        menubar.SearchMenu(screen_object=self.screen)
        menubar.NavigateMenu(screen_object=self.screen)
        menubar.ModifyMenu(screen_object=self.screen)
        menubar.OpenInBrowser(screen_object=self.screen)
        menubar.ThemeMenu(screen_object=self.screen)
        menubar.HelpMenu(screen_object=self.screen)

    ##---------- END of this Method----------##

    ##---------- Method to StartApplication----------##
    def StartApplication(self):
        self.get_screen()

    ##---------- END of this Method ----------##


##---------- END of this Class----------##


if __name__ == '__main__':
    scrapper = WebScrapper()
    scrapper.StartApplication()
