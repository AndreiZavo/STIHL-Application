##########################################################
#
#   BY: Zavorodnic Andrei
#   V: 1.4
#
#########################################################
import os
import subprocess
import sys
from openpyxl import Workbook
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QPropertyAnimation, QSortFilterProxyModel
import pandas as pd
from Backend.Domain.Client import Client
from Backend.Repository import FileRepository
from Backend.Service import Service
from Backend.Validations import Valid
from ClientsTableView import TableModel
from PDF_py import PDF_Generator
from Backend.Domain.Date import Date
from Backend.Exceptions import ValidException, RepositoryException
from Run_UI.Run_Error_Window import ErrorWindow
from ui_MainWindow import *

WINDOW_SIZE = 0

path_to_script = sys.argv[0]
path_to_script_dir = os.path.dirname(os.path.abspath(path_to_script))

width_display, height_display = pyautogui.size()

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"  # command for scaling


# os.environ["QT_DEVICE_PIXEL_RATIO"] = "1"     # command for scaling


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.first_client_added = True
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.__repository = None
        self.__service = None

        # Hide the preformed toolbar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set window icon
        self.setWindowIcon(QtGui.QIcon(":/Icons/Icons/Stihl_Server_IconToolBar.svg"))
        # Set window title
        self.setWindowTitle("STIHL Server")

        # Set actions for buttons
        self.connect_futures()

        # set default page
        self.ui.containerPages.setCurrentWidget(self.ui.HomeWWidget)

        # Set action for left click mouse for moving the window
        def move_window(e):
            if self.isMaximized() is False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        # set on what elements the move_window applies
        self.ui.topbar_menu.mouseMoveEvent = move_window
        self.ui.titleLabel.mouseMoveEvent = move_window

        # set window size grip for bottom right corner
        QSizeGrip(self.ui.size_grip)

        # hide confirmation massages
        self.ui.confirmationLabel.startFadeOut()
        self.ui.confirmDeletionLabel.startFadeOut()
        self.ui.confirmFileLabel.startFadeOut()

        self.show()

    """ Function sets actions for buttons """

    def connect_futures(self):
        # minimize the window
        self.ui.minimazeButton.clicked.connect(lambda: self.showMinimized())
        # maximize the window
        self.ui.maximazeButton.clicked.connect(lambda: self.
                                               restore_or_maximize_window())
        # close the window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        # extend the left side menu
        self.ui.slideMenuButton.clicked.connect(lambda: self.slideLeftMenu())
        # navigate to home page
        self.ui.homeButton.clicked.connect(lambda: self.ui.containerPages.setPage1())
        # navigate to search page
        self.ui.listButton.clicked.connect(lambda: self.set_listen_tab())
        # navigate to add page
        self.ui.addButton.clicked.connect(lambda: self.set_add_tab())
        # navigate to delete page
        self.ui.removeButton.clicked.connect(lambda: self.set_remove_tab())
        # navigate to view client page
        self.ui.ViewClientButton.clicked.connect(lambda: self.ui.containerPages.setPage3())
        # navigate to choose table page
        self.ui.chooseTablePushButton.clicked.connect(lambda: self.set_choose_tab())

        # make full row selection in search, in client's table
        self.ui.clientsDataTableView.clicked.connect(lambda: self.show_view_button())
        # close slide menu for when page is accessed
        self.ui.homeButton.clicked.connect(lambda: self.close_slide_menu_if_opened())
        self.ui.listButton.clicked.connect(lambda: self.close_slide_menu_if_opened())
        self.ui.addButton.clicked.connect(lambda: self.close_slide_menu_if_opened())
        self.ui.removeButton.clicked.connect(lambda: self.close_slide_menu_if_opened())
        # add a client
        self.ui.addLineEdit.returnPressed.connect(lambda: self.add_client_to_data_base())
        self.ui.addPushBUtton.clicked.connect(lambda: self.add_client_to_data_base())
        self.ui.quitPushButton.clicked.connect(lambda: self.empty_add_input())
        # remove a client
        self.ui.removetableView.clicked.connect(lambda: self.view_clicked())
        self.ui.removePushButton.clicked.connect(lambda: self.remove_client())
        self.ui.quitPushButton_2.clicked.connect(lambda: self.empty_remove_input())
        # search a client
        self.ui.clientsDataTableView.clicked.connect(lambda: self.show_view_button())
        self.ui.ViewClientButton.clicked.connect(lambda: self.show_client())
        self.ui.alphabeticalOrderRadioButton.clicked.connect(lambda: self.sort_by_name())
        self.ui.oldDateOrderRadioButton.clicked.connect(lambda: self.sort_by_old_date())
        self.ui.recentDateOrderRadioButton.clicked.connect(lambda: self.sort_by_recent_date())
        # view a client
        self.ui.PrintButton.clicked.connect(lambda: self.print_client())
        # choose an database file
        self.ui.toolPushButton.clicked.connect(lambda: self.choose_file())
        self.ui.OKButton.clicked.connect(lambda: self.change_table())

    '''Function sets the choose tab as the current one and hides confirmation messages'''

    def set_choose_tab(self):
        self.ui.containerPages.setPage6()
        self.ui.confirmFileLabel.setVisible(False)

    '''Function sets the add tab as the current one and hides confirmation messages'''

    def set_add_tab(self):
        self.ui.containerPages.setPage4()
        self.ui.confirmationLabel.setVisible(False)

    @staticmethod
    def create_table_file_name(table_name):
        if not os.path.exists(table_name):
            workbook = Workbook(table_name)
            workbook.save(table_name)
            workbook.close()
        return table_name

    ''' Function changes excel table to use for the application'''

    def change_table(self):
        validator = Valid()
        path = self.ui.choosePathLineEdit.text()
        if path == '':
            ErrorWindow('Nu a fost selectat niciun fisier.')
        try:
            validator.validate_file(path)
            self.__repository = FileRepository(self.create_table_file_name(path), Client.read_from_file,
                                               Client.write_to_file)
            self.__service = Service(self.__repository)

            self.populate_table()
            self.populate_remove_table()

            self.ui.choosePathLineEdit.setText("")
            self.ui.confirmFileLabel.setStyleSheet(u"font-size: 60px;\n")
            self.ui.confirmFileLabel.setVisible(True)
            self.ui.confirmFileLabel.startAnimation()

        except ValidException:
            self.ui.choosePathLineEdit.setText("")
            ErrorWindow('Fisierul ales nu este corespunzator.<p align=\"center\">Fisierul trebuie sa contina pe fiecare rand un nume,</p>'
                        '<p align=\"center\">urmat de un id, o data de creare si o data de expirare</p>')

    ''' Function opens a choose file window letting user to select the desired file '''

    def choose_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', '', 'Excel Files (*.xlsx)')
        self.ui.choosePathLineEdit.setText(file_name[0])

    ''' Function sets sorting to be by recent date '''

    def sort_by_recent_date(self):
        self.ui.clientsDataTableView.sortByColumn(2, Qt.DescendingOrder)

    ''' Function sets sorting to be by old date'''

    def sort_by_old_date(self):
        self.ui.clientsDataTableView.sortByColumn(2, Qt.AscendingOrder)

    ''' Function sets sorting to be by name'''

    def sort_by_name(self):
        self.ui.clientsDataTableView.sortByColumn(0, Qt.AscendingOrder)

    ''' Function generates a pdf according to the data selected'''

    def print_client(self):
        index = self.ui.clientsDataTableView.selectionModel().currentIndex()
        name = index.sibling(index.row(), 0).data()
        id = index.sibling(index.row(), 1).data()
        creation_date = index.sibling(index.row(), 2).data()
        expiration_date = index.sibling(index.row(), 3).data()
        pdf = PDF_Generator.generate_pdf(name, id, creation_date, expiration_date)
        subprocess.Popen([path_to_script_dir + '\PDFs\\' + pdf.name + '.pdf'], shell=True)

    ''' Function shows client in another window '''

    def show_client(self):
        self.ui.containerPages.setCurrentWidget(self.ui.ViewClientWidget)
        self.ui.ViewClientButton.setVisible(False)

        index = self.ui.clientsDataTableView.selectionModel().currentIndex()
        name = index.sibling(index.row(), 0).data()
        id = index.sibling(index.row(), 1).data()
        creation_date = index.sibling(index.row(), 2).data()
        expiration_date = index.sibling(index.row(), 3).data()

        self.ui.nameLineEdit.setText(name)
        self.ui.IdLineEdit.setText(id)
        self.ui.creationDateLineEdit.setText(creation_date)
        self.ui.expirationDateLineEdit.setText(expiration_date)

        self.validate_client(expiration_date)

    """ Function validates if the current day is bigger then the expiration date """

    def validate_client(self, expiration):
        expiration_date = expiration.split('-')
        year = int(expiration_date[0])
        month = int(expiration_date[1])
        day = int(expiration_date[2])
        date_to_check = Date(year, month, day)
        current_date = Date.generate_current_date()
        if current_date > date_to_check:
            self.ui.Valid_InvalidLabel.setText('Client Invalid')
        else:
            self.ui.Valid_InvalidLabel.setText('Client Valid')

    ''' Hide the View button and make window principal window'''

    def set_listen_tab(self):
        self.ui.containerPages.setPage2()
        self.ui.clientsDataTableView.clearSelection()
        self.ui.ViewClientButton.setVisible(False)

        self.ui.alphabeticalOrderRadioButton.setAutoExclusive(False)
        self.ui.recentDateOrderRadioButton.setAutoExclusive(False)
        self.ui.oldDateOrderRadioButton.setAutoExclusive(False)

        self.ui.recentDateOrderRadioButton.setChecked(False)
        self.ui.oldDateOrderRadioButton.setChecked(False)
        self.ui.alphabeticalOrderRadioButton.setChecked(False)

        self.ui.alphabeticalOrderRadioButton.setAutoExclusive(True)
        self.ui.recentDateOrderRadioButton.setAutoExclusive(True)
        self.ui.oldDateOrderRadioButton.setAutoExclusive(True)

        self.ui.clientsDataTableView.sortByColumn(2, Qt.AscendingOrder)

    ''' Function shows View button '''

    def show_view_button(self):
        self.ui.ViewClientButton.setVisible(True)

    ''' Function deletes text from remove-client search bar'''

    def empty_remove_input(self):
        self.ui.removeSearchbarLineEdit.setText("")

    ''' Function hides the remove and quit buttons and refreshes the remove table view'''

    def set_remove_tab(self):
        self.ui.containerPages.setPage5()
        self.ui.removePushButton.setVisible(False)
        self.ui.quitPushButton_2.setVisible(False)
        self.ui.confirmDeletionLabel.setVisible(False)
        self.ui.removetableView.clearSelection()

    ''' Function populate removeTableView table with the new data'''

    def populate_remove_table(self):
        data = pd.DataFrame(self.__service.repository,
                            columns=['Nume', 'ID', 'Creat la', 'Expiră la'])
        self.ui.remove_model = TableModel(data)
        self.ui.remove_filter_proxy_model = QSortFilterProxyModel()
        self.ui.remove_filter_proxy_model.setSourceModel(self.ui.remove_model)
        self.ui.remove_filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.ui.remove_filter_proxy_model.setFilterKeyColumn(-1)

        self.ui.removetableView.setModel(self.ui.remove_filter_proxy_model)

        self.ui.removeSearchbarLineEdit.textChanged.connect(self.ui.remove_filter_proxy_model.setFilterRegExp)

    @staticmethod
    def removes_file_from_folder(file_name, file_directory):
        for parent, dir_names, filenames in os.walk(file_directory):
            for fn in filenames:
                if fn == file_name:
                    os.remove(os.path.join(parent, fn))

    ''' Function removes client from database and hides remove and quit button after that'''

    def remove_client(self):
        index = self.ui.removetableView.currentIndex()
        name_to_remove = index.sibling(index.row(), 0).data()
        id_to_remove = index.sibling(index.row(), 1).data()
        self.__service.remove_client(name_to_remove, id_to_remove)  # removes client from database

        self.removes_file_from_folder(name_to_remove + ".pdf", "PDFs")  # removes pdf file with client name

        self.removes_file_from_folder(name_to_remove + ".png", "Barcodes")  # removes barcode png file with client name

        self.populate_table()
        self.populate_remove_table()

        self.ui.removeSearchbarLineEdit.setText("")

        self.ui.confirmDeletionLabel.setStyleSheet(u"font-size: 60px;\n")
        self.ui.confirmDeletionLabel.setVisible(True)
        self.ui.confirmDeletionLabel.startAnimation()

        self.ui.removePushButton.setVisible(False)
        self.ui.quitPushButton_2.setVisible(False)

    ''' Function makes row selection in remove table regardless of pressed cell'''

    def view_clicked(self):
        self.ui.removePushButton.setVisible(True)
        self.ui.quitPushButton_2.setVisible(True)

    ''' Function empties the text line edit '''

    def empty_add_input(self):
        self.ui.addLineEdit.setText("")

    ''' Function fills again the table with the new clients '''

    def populate_table(self):
        pass
        data = pd.DataFrame(self.__service.repository,
                            columns=['Nume', 'ID', 'Creat la', 'Expiră la'])
        self.ui.model = TableModel(data)
        # filter proxy model
        self.ui.filter_proxy_model = QSortFilterProxyModel()
        self.ui.filter_proxy_model.setSourceModel(self.ui.model)
        self.ui.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.ui.filter_proxy_model.setFilterKeyColumn(-1)  # -1 is for searching in all columns

        self.ui.clientsDataTableView.setModel(self.ui.filter_proxy_model)

        self.ui.searchbarLineEdit.textChanged.connect(self.ui.filter_proxy_model.setFilterRegExp)

    def set_confirmation_message(self, message):
        self.ui.confirmationLabel.setText(message)
        self.ui.confirmationLabel.setStyleSheet(u"font-size: 60px;\n")
        self.ui.confirmationLabel.setVisible(True)
        self.ui.confirmationLabel.startAnimation()

    ''' Function adds client to database '''

    def add_client_to_data_base(self):
        name_to_add = self.ui.addLineEdit.text()
        try:
            if self.__service is None:
                self.set_confirmation_message('Nu a fost niciun tabel selectat')
            else:
                self.__service.add_client(name_to_add)
                self.set_confirmation_message('Clientul a fost adaugat cu succes')
        except ValidException:
            ErrorWindow(
                'Inputul introdus nu este comform modului de procesare al programului. < / p > < p align =\"center\">La introducerea unui nou client, utilizatorul trebuie s\u0103 insereze un nou nume</p><p align=\"center\">compus din nume \u0219i prenume(sau prenume \u0219i nume) fiecare cu majuscul\u0103,</p><p align=\"center\">av\u00e2nd un spa\u021biu \u00eentre ele.'
            )
        except RepositoryException:
            self.add_client_to_data_base()

        self.empty_add_input()
        self.populate_table()
        self.populate_remove_table()

    ''' Function closes slide menu after the user accesses a page from the extended menu  '''

    def close_slide_menu_if_opened(self):
        width = self.ui.left_side_menu.width()
        if width == round(width_display / 10):
            newWidth = round(width_display / 18.82)
            self.ui.homeButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.listButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.addButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.removeButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.chooseTablePushButton.setText(QCoreApplication.translate("Main", u"", None))

            # Animate the transition
            self.animation = QPropertyAnimation(self.ui.left_side_menu,
                                                b"minimumWidth")
            self.animation.setDuration(250)
            self.animation.setStartValue(width)  # Start value is the current menu width
            self.animation.setEndValue(newWidth)  # end value is the new menu width
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    """ Function changes the size of window accordingly to the action needed """

    def restore_or_maximize_window(self):
        global WINDOW_SIZE
        win_status = WINDOW_SIZE
        if win_status == 0:  # if window is minimized
            WINDOW_SIZE = 1  # set the flag
            self.showMaximized()  # maximize window
            self.ui.maximazeButton.setIcon(QtGui.QIcon(u":/Icons/Icons/Maximaze-Icon.svg"))
        else:  # if window is maximized
            WINDOW_SIZE = 0
            self.showNormal()  # show predefined size of window
            self.ui.maximazeButton.setIcon(QtGui.QIcon(u":/Icons/Icons/MaximazeButton_2.svg"))

    """ Function sets events to the window """

    def mousePressEvent(self, event):
        # get current position of the mouse
        self.clickPosition = event.globalPos()

    """ Function extends to the left the buttons menu """

    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_side_menu.width()
        # If minimized
        if width == round(width_display / 18.82):
            # Expand menu
            newWidth = round(width_display / 10)
            self.ui.homeButton.setText(QCoreApplication.translate("Main", u"     Acas\u0103", None))
            self.ui.listButton.setText(QCoreApplication.translate("Main", u"     Caut\u0103", None))
            self.ui.addButton.setText(QCoreApplication.translate("Main", u"     Adaug\u0103", None))
            self.ui.removeButton.setText(QCoreApplication.translate("Main", u"    \u0218terge", None))
            self.ui.chooseTablePushButton.setText(QCoreApplication.translate("Main", u"     Fi\u0219ier", None))
        # If maximized
        else:
            # Restore menu
            newWidth = round(width_display / 18.82)
            self.ui.homeButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.listButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.addButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.removeButton.setText(QCoreApplication.translate("Main", u"", None))
            self.ui.chooseTablePushButton.setText(QCoreApplication.translate("Main", u"", None))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_side_menu,
                                            b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)  # Start value is the current menu width
        self.animation.setEndValue(newWidth)  # end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
