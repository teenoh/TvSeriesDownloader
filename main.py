from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import qdarkstyle
import time
from pprint import pprint
from gui import Ui_MainWindow
from search import *


episode_links = {}

class Download(QThread):
    def __init__(self, series, season, episode_link):
        QThread.__init__(self)
        self.series = series
        self.season = season
        self.episode_link = episode_link

    def run(self):
        download_link = get_download_link(self.episode_link)
        
        download(download_link, self.series, self.season)
        
class Loading(QThread):
    def __init__(self):
        QThread.__init__(self)
        taskFinished = QtCore.pyqtSignal()

    def run(self):
        pass
        #while 1:
           
       #    self.taskFinished.emit()



class Teenoh(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        
        self.series_links = get_series_links()
        print(self.series_links)
        #self.ser_box.textEdited.connect(self.reset)
        self.valid_btn.clicked.connect(self.validate_series)
        self.sea_box.valueChanged.connect(self.update_episodes)
        self.download_btn.clicked.connect(self._download)
        self.reset()

    def get_links(self, series_link):
        self.episode_links = get_episodes_links(series_link)
        

    def validate_series(self):
        if self.ser_box.text() == '':
            QMessageBox.critical(self,"No Series",
                                       "You didn't enter any series.",
                                       QMessageBox.Ok)
            return
        
        self.series_entered = (self.ser_box.text()).lower()
        
        #checks if value entered in the series box is part of
        # a series name and corrects to the right name if true
        for i in self.series_links.keys():
            if self.series_entered in i:
                self.series_entered = i
                break 
        else:
            QMessageBox.critical(self,"Invalid Series",
                                       "Series not found!!!",
                                       QMessageBox.Ok)
            return
        
        #Gets the link of series entered
        ser_link = self.series_links[self.series_entered]

        
        
        self.get_links(ser_link)

        #sets text on series box to full series name
        self.ser_box.setText(self.series_entered)
        
        self.info_label.setText("Series Available")

        #loads the image url of the series entered
        self.webView.load(QUrl(get_series_image(ser_link))) 
            
        #Enables season and series combo box for use
        self.sea_box.setEnabled(True)
        self.epis_box.setEnabled(True)

        #sets season combo box to max length of season od the series
        self.sea_box.setMaximum(len(self.episode_links))
        
        self.update_episodes()

        #self.load_gif.taskFinished.connect(self.onFinish)
        
        self.download_btn.setEnabled(True)
        self.valid_btn.setEnabled(False)
        
    def reset(self):
        self.valid_btn.setEnabled(True)
        self.download_btn.setEnabled(False)
        self.sea_box.setEnabled(False)
        self.epis_box.setEnabled(False)


    def update_episodes(self):
        
        if self.sea_box.value() < 10 : 
            self.season_entered = "season 0" + \
                              str(self.sea_box.value())
        else: 
            self.season_entered = "season " + \
                          str(self.sea_box.value())

        pprint(self.episode_links)

        for i in episode_links.keys():
            if self.season_entered in i:
                self.season_entered = i
                break

        
        
        num_of_episodes = len(self.episode_links[self.season_entered])
        #sets episode combo box to max length of episodes based on season selected
        self.epis_box.setMaximum(num_of_episodes)


    def _download(self):
          
        if self.epis_box.value() < 10 : 
            self.episode_entered = "episode 0"+ str(self.epis_box.value())
        else: 
            self.episode_entered = "episode " + str(self.epis_box.value())
        

        for i in self.episode_links[self.season_entered]:
            if self.episode_entered in i.lower():
                self.episode_entered = i
                break

        
        episode_link = self.episode_links[self.season_entered][self.episode_entered]
        
        #download the series
        self.download_thread = Download(self.series_entered, self.season_entered,
                                episode_link)

        self.download_thread.start()


app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
dialog = Teenoh()

splash_image = QPixmap(".\images\splash-screen.jpg")
splash = QSplashScreen(splash_image)
splash.show()
time.sleep(5)
splash.finish(dialog)

dialog.show()

app.exec_()
