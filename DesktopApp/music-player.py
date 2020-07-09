from PyQt5 import QtCore, QtGui, QtWidgets
import random
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.commonPath = "/Users/anmolrajarora/Documents/msit-advance-python/DesktopApp/icons/"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.musicControlFrame = QtWidgets.QFrame(self.centralwidget)
        self.musicControlFrame.setGeometry(QtCore.QRect(0, 469, 801, 120))
        self.musicControlFrame.setStyleSheet(
            "background-color: rgb(223, 233, 247);")
        self.musicControlFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.musicControlFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.musicControlFrame.setObjectName("musicControlFrame")
        self.horizontalSlider = QtWidgets.QSlider(self.musicControlFrame)
        self.horizontalSlider.setGeometry(QtCore.QRect(9, 0, 781, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.playPauseBtn = QtWidgets.QPushButton(self.musicControlFrame)
        self.playPauseBtn.setGeometry(QtCore.QRect(340, 20, 101, 71))
        self.playPauseBtn.setStyleSheet("background-color: rgb(57, 163, 238);")
        self.playPauseBtn.setText("")
        self.playPauseBtn.setObjectName("playPauseBtn")
        self.nextBtn = QtWidgets.QPushButton(self.musicControlFrame)
        self.nextBtn.setGeometry(QtCore.QRect(450, 20, 71, 71))
        self.nextBtn.setStyleSheet(
            f"background-image: url({self.commonPath + 'next_btn.png'});background-color: rgb(57, 163, 238);")
        self.nextBtn.setText("")
        self.nextBtn.setObjectName("nextBtn")
        self.previousBtn = QtWidgets.QPushButton(self.musicControlFrame)
        self.previousBtn.setGeometry(QtCore.QRect(230, 20, 71, 71))
        self.previousBtn.setStyleSheet(
            f"background-image: url({self.commonPath + 'prev_btn.png'});background-color: rgb(57, 163, 238);")
        self.previousBtn.setText("")
        self.previousBtn.setObjectName("previousBtn")
        self.shuffleBtn = QtWidgets.QPushButton(self.musicControlFrame)
        self.shuffleBtn.setGeometry(QtCore.QRect(120, 20, 71, 71))
        self.shuffleBtn.setStyleSheet(
            f"background-image: url({self.commonPath + 'shuffle_btn.png'});background-color: rgb(57, 163, 238);")
        self.shuffleBtn.setText("")
        self.shuffleBtn.setObjectName("shuffleBtn")
        self.repeatBtn = QtWidgets.QPushButton(self.musicControlFrame)
        self.repeatBtn.setGeometry(QtCore.QRect(560, 20, 101, 71))
        self.repeatBtn.setStyleSheet("background-color: rgb(57, 163, 238);\n"
                                     "")
        self.repeatBtn.setText("")
        self.repeatBtn.setObjectName("repeatBtn")
        self.songCurrentDuration = QtWidgets.QLabel(self.musicControlFrame)
        self.songCurrentDuration.setGeometry(QtCore.QRect(10, 20, 60, 16))
        self.songCurrentDuration.setObjectName("songCurrentDuration")
        self.songTotalDuration = QtWidgets.QLabel(self.musicControlFrame)
        self.songTotalDuration.setGeometry(QtCore.QRect(750, 20, 60, 16))
        self.songTotalDuration.setObjectName("songTotalDuration")
        self.playlistFrame = QtWidgets.QFrame(self.centralwidget)
        self.playlistFrame.setGeometry(QtCore.QRect(559, 0, 241, 471))
        self.playlistFrame.setStyleSheet(
            "background-color: rgb(242, 246, 252);")
        self.playlistFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playlistFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playlistFrame.setObjectName("playlistFrame")
        self.playlistTable = QtWidgets.QTableWidget(self.playlistFrame)
        self.playlistTable.setGeometry(QtCore.QRect(10, 31, 221, 431))
        self.playlistTable.setObjectName("playlistTable")
        self.playlistTable.setColumnCount(2)
        self.playlistTable.setColumnWidth(0, 150)
        self.playlistTable.setColumnWidth(1, 52)
        self.playlistTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(213, 229, 241))
        self.playlistTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(213, 229, 241))
        self.playlistTable.setHorizontalHeaderItem(1, item)
        self.playlistHeading = QtWidgets.QLabel(self.playlistFrame)
        self.playlistHeading.setGeometry(QtCore.QRect(80, 10, 81, 21))
        self.playlistHeading.setStyleSheet(
            "font: 20pt \"American Typewriter\";")
        self.playlistHeading.setObjectName("playlistHeading")
        self.currentlyPlayingFrame = QtWidgets.QFrame(self.centralwidget)
        self.currentlyPlayingFrame.setGeometry(QtCore.QRect(0, 0, 221, 471))
        self.currentlyPlayingFrame.setStyleSheet(
            "background-color: rgb(242, 246, 252);")
        self.currentlyPlayingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.currentlyPlayingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentlyPlayingFrame.setObjectName("currentlyPlayingFrame")
        self.currentlyPlayingHeading = QtWidgets.QLabel(
            self.currentlyPlayingFrame)
        self.currentlyPlayingHeading.setGeometry(QtCore.QRect(60, 10, 101, 51))
        self.currentlyPlayingHeading.setStyleSheet(
            "font: 20pt \"American Typewriter\";")
        self.currentlyPlayingHeading.setObjectName("currentlyPlayingHeading")
        self.currentlyPlayingSong = QtWidgets.QLabel(
            self.currentlyPlayingFrame)
        self.currentlyPlayingSong.setGeometry(QtCore.QRect(60, 60, 101, 51))
        self.currentlyPlayingSong.setStyleSheet(
            "font: 20pt \"American Typewriter\";")
        self.currentlyPlayingSong.setObjectName("currentlyPlayingSong")
        self.songsListFrame = QtWidgets.QFrame(self.centralwidget)
        self.songsListFrame.setGeometry(QtCore.QRect(180, 0, 380, 471))
        self.songsListFrame.setStyleSheet(
            "background-color: rgb(213, 229, 241);")
        self.songsListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.songsListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.songsListFrame.setObjectName("songsListFrame")
        self.songsTable = QtWidgets.QListWidget(self.songsListFrame)
        self.songsTable.setGeometry(QtCore.QRect(5, 30, 320, 441))
        self.songsTable.setObjectName("songsTable")
        self.songsTable.setStyleSheet("font: 15pt \"American Typewriter\";")
        self.songActionTable = QtWidgets.QListWidget(self.songsListFrame)
        self.songActionTable.setGeometry(QtCore.QRect(330, 30, 50, 441))
        self.songActionTable.setObjectName("songActionTable")
        self.songsTable.setStyleSheet("font: 15pt \"American Typewriter\";")
        self.featuredSongsHeading = QtWidgets.QLabel(self.songsListFrame)
        self.featuredSongsHeading.setGeometry(QtCore.QRect(60, 5, 161, 21))
        self.featuredSongsHeading.setStyleSheet(
            "font: 20pt \"American Typewriter\";")
        self.featuredSongsHeading.setObjectName("featuredSongsHeading")
        # self.splashScreenFrame = QtWidgets.QFrame(self.centralwidget)
        # self.splashScreenFrame.setGeometry(QtCore.QRect(-1, -1, 801, 600))
        # self.splashScreenFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.splashScreenFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.splashScreenFrame.setObjectName("splashScreenFrame")
        # self.imageLabel = QtWidgets.QLabel(self.splashScreenFrame)
        # self.imageLabel.setGeometry(QtCore.QRect(-1, -5, 801, 600))
        # self.imageLabel.setText("")
        # self.imageLabel.setObjectName("imageLabel")

        # self.wallpaper = QtGui.QPixmap(
        #     "/Users/anmolrajarora/Documents/msit-advance-python/DesktopApp/wallpaper.jpg")
        # self.imageLabel.setPixmap(self.wallpaper)

        # self.welcomeLabel = QtWidgets.QLabel(self.splashScreenFrame)
        # self.welcomeLabel.setGeometry(QtCore.QRect(180, 50, 451, 81))
        # self.welcomeLabel.setStyleSheet(
        #     "font: italic 25pt \"Zapfino\";color: white")
        # self.welcomeLabel.setObjectName("welcomeLabel")
        # self.listenNowBtn = QtWidgets.QPushButton(self.splashScreenFrame)
        # self.listenNowBtn.setGeometry(QtCore.QRect(330, 450, 141, 51))
        # self.listenNowBtn.setStyleSheet(
        #     "font: 20pt \"Montserrat Alternates\";")
        # self.listenNowBtn.setObjectName("listenNowBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Playlist = QtWidgets.QAction(MainWindow)
        self.actionSave_Playlist.setObjectName("actionSave_Playlist")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Playlist)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.songCurrentDuration.setText(_translate("MainWindow", "00:00"))
        self.songTotalDuration.setText(_translate("MainWindow", "00:00"))
        item = self.playlistTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Song Name"))
        item = self.playlistTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Action"))
        self.playlistHeading.setText(_translate("MainWindow", "Playlist"))
        self.currentlyPlayingHeading.setText(_translate("MainWindow", "Currently\n"
                                                        "  Playing"))
        self.currentlyPlayingSong.setText(_translate("MainWindow", "-"))
        self.featuredSongsHeading.setText(
            _translate("MainWindow", "Featured Songs"))
        # self.welcomeLabel.setText(_translate(
        # "MainWindow", "Welcome to XOMP Player"))
        # self.listenNowBtn.setText(_translate("MainWindow", "Listen Now"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_Playlist.setText(
            _translate("MainWindow", "Save Playlist"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        # self.listenNowBtn.clicked.connect(self.hideSplashScreen)
        self.shuffleBtn.clicked.connect(self.toggleShuffle)
        self.isShuffle = False
        self.previousBtn.clicked.connect(self.previousSong)
        self.nextBtn.clicked.connect(self.nextSong)
        self.featuredSongs = os.listdir(
            "/Users/anmolrajarora/Documents/adv-python-reg-dec/MusicPlayer/songs")
        self.playlistSongs = []
        self.songs = self.featuredSongs
        self.selectedPlaylist = "featured songs"

        for i in range(len(self.featuredSongs)):
            listItem = QtWidgets.QListWidgetItem()
            listItem.setText(self.featuredSongs[i])
            self.songsTable.addItem(listItem)
            listItem = QtWidgets.QListWidgetItem()
            listItem.setIcon(QtGui.QIcon(f"{self.commonPath}add_btn.png"))
            self.songActionTable.addItem(listItem)

        tableItem = QtWidgets.QTableWidgetItem()
        tableItem.setText("Aankh_Marey.mp3")
        tableItem2 = QtWidgets.QTableWidgetItem()
        tableItem2.setIcon(QtGui.QIcon(f"{self.commonPath}delete_btn.png"))
        self.playlistTable.insertRow(0)
        self.playlistTable.setItem(0, 0, tableItem)
        self.playlistTable.setItem(0, 1, tableItem2)

    def hideSplashScreen(self):
        self.splashScreenFrame.hide()

    def toggleShuffle(self):
        self.isShuffle = not self.isShuffle
        if self.isShuffle:
            self.shuffleBtn.setStyleSheet(
                f"background-image: url({self.commonPath}shuffle_btn.png); background-color: #eea639;")
        else:
            self.shuffleBtn.setStyleSheet(
                f"background-image: url({self.commonPath + 'shuffle_btn.png'}); background-color: rgb(57, 163, 238);")

    def previousSong(self):
        if self.selectedPlaylist == "user playlist":
            self.songs = self.playlistSongs
        else:
            self.songs = self.featuredSongs

        if self.isShuffle:
            self.songIndex = random.randint(0, len(self.songs) - 1)
        else:
            self.songIndex = self.songs.index(self.currentSong)
            self.songIndex -= 1
            if (self.songIndex == len(self.songs)):
                self.songIndex = 0
            self.currentSong = self.songs[self.songIndex]
            print(self.selectedSong)
            self.playSong()

    def nextSong(self):
        if self.selectedPlaylist == "user playlist":
            self.songs = self.playlistSongs
        else:
            self.songs = self.featuredSongs

        if self.isShuffle:
            self.songIndex = random.randint(0, len(self.songs) - 1)
        else:
            self.songIndex = self.songs.index(self.currentSong)
            self.songIndex += 1
            if (self.songIndex == len(self.songs)):
                self.songIndex = 0
            self.currentSong = self.songs[self.songIndex]
            print(self.selectedSong)
            self.playSong()

    def playSong(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
