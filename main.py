from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import qdarkstyle

from gui import Ui_MainWindow
from search import *


class Teenoh(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.series_links = get_series_links()

        self.ser_box.textEdited.connect(self.reset)
        self.valid_btn.clicked.connect(self.validate_series)
        self.sea_box.valueChanged.connect(self.update_episodes)
        self.download_btn.clicked.connect(self.download)

    def validate_series(self):
        self.series_entered = (self.ser_box.text()).lower()
        
        #checks if value entered in the series box is part of
        # a series name and corrects to the right name if true
        for i in self.series_links.keys():
            if self.series_entered in i:
                self.series_entered = i
                break
        
        #checks if series in series box exists on 02tvseries
        if self.series_entered in self.series_links:
            #sets text on series box to full series name
            self.ser_box.setText(self.series_entered)

            #Gets the link of series entered
            self.ser_link = self.series_links[self.series_entered]
            
            self.sea_len, self.season_links = get_season_links(self.ser_link)
            
            #loads the image url of the series entered
            self.webView.load(QUrl(get_series_image(self.ser_link)))
            
            self.info_label.setText("Series Available")
            
            #Enables season combo box for use
            self.sea_box.setEnabled(True)
            
            #sets season combo box to max length of season od the series
            self.sea_box.setMaximum(self.sea_len)
            
            self.download_btn.setEnabled(True)
            self.valid_btn.setEnabled(False)
        
        else:  
            self.info_label.setText("Series Not Available")

    def reset(self):
        self.valid_btn.setEnabled(True)
        self.download_btn.setEnabled(False)
        self.sea_box.setEnabled(False)
        self.epis_box.setEnabled(False)

    def update_episodes(self):
        self.epis_box.setEnabled(True)
        
        if self.sea_box.value() < 10 : self.season_entered = "season 0"+ str(self.sea_box.value())
        else: self.season_entered = "season " + str(self.sea_box.value())
        
        self.episode_len, self.episode_links = get_episodes_links(self.season_links[self.season_entered])
        
        #sets episode combo box to max length of episodes based on season selected
        self.epis_box.setMaximum(self.episode_len)



    def download(self):
          
        if self.epis_box.value() < 10 : 
            episode = "episode 0"+ str(self.epis_box.value())
        else: 
            episode = "episode " + str(self.epis_box.value())
        for i in self.episode_links.keys():
            if episode in i:
                self.episode_entered = i
                break


        download_link = get_download_link(self.episode_links[self.episode_entered])
        
        #download the series
        download(download_link, self.series_entered, self.season_entered)
            


app = QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())
dialog = Teenoh()
dialog.show()
app.exec_()
