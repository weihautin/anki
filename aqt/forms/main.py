# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/main.ui'
#
# Created: Fri Aug 22 00:57:31 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(412, 301)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/anki.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuCol = QtGui.QMenu(self.menubar)
        self.menuCol.setObjectName(_fromUtf8("menuCol"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuPlugins = QtGui.QMenu(self.menuTools)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/preferences-plugin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuPlugins.setIcon(icon1)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setMenuRole(QtGui.QAction.PreferencesRole)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setMenuRole(QtGui.QAction.AboutRole)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionCheckMediaDatabase = QtGui.QAction(MainWindow)
        self.actionCheckMediaDatabase.setObjectName(_fromUtf8("actionCheckMediaDatabase"))
        self.actionOpenPluginFolder = QtGui.QAction(MainWindow)
        self.actionOpenPluginFolder.setObjectName(_fromUtf8("actionOpenPluginFolder"))
        self.actionDonate = QtGui.QAction(MainWindow)
        self.actionDonate.setObjectName(_fromUtf8("actionDonate"))
        self.actionDownloadSharedPlugin = QtGui.QAction(MainWindow)
        self.actionDownloadSharedPlugin.setStatusTip(_fromUtf8(""))
        self.actionDownloadSharedPlugin.setObjectName(_fromUtf8("actionDownloadSharedPlugin"))
        self.actionFullDatabaseCheck = QtGui.QAction(MainWindow)
        self.actionFullDatabaseCheck.setObjectName(_fromUtf8("actionFullDatabaseCheck"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionSwitchProfile = QtGui.QAction(MainWindow)
        self.actionSwitchProfile.setObjectName(_fromUtf8("actionSwitchProfile"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionStudyDeck = QtGui.QAction(MainWindow)
        self.actionStudyDeck.setObjectName(_fromUtf8("actionStudyDeck"))
        self.actionEmptyCards = QtGui.QAction(MainWindow)
        self.actionEmptyCards.setObjectName(_fromUtf8("actionEmptyCards"))
        self.actionCreateFiltered = QtGui.QAction(MainWindow)
        self.actionCreateFiltered.setObjectName(_fromUtf8("actionCreateFiltered"))
        self.actionNoteTypes = QtGui.QAction(MainWindow)
        self.actionNoteTypes.setObjectName(_fromUtf8("actionNoteTypes"))
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionDonate)
        self.menuHelp.addAction(self.actionAbout)
        self.menuEdit.addAction(self.actionUndo)
        self.menuCol.addAction(self.actionSwitchProfile)
        self.menuCol.addSeparator()
        self.menuCol.addAction(self.actionImport)
        self.menuCol.addAction(self.actionExport)
        self.menuCol.addSeparator()
        self.menuCol.addAction(self.actionExit)
        self.menuPlugins.addAction(self.actionDownloadSharedPlugin)
        self.menuPlugins.addAction(self.actionOpenPluginFolder)
        self.menuPlugins.addSeparator()
        self.menuTools.addAction(self.actionStudyDeck)
        self.menuTools.addAction(self.actionCreateFiltered)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionFullDatabaseCheck)
        self.menuTools.addAction(self.actionCheckMediaDatabase)
        self.menuTools.addAction(self.actionEmptyCards)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.menuPlugins.menuAction())
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionNoteTypes)
        self.menuTools.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuCol.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_("Anki"))
        self.menuHelp.setTitle(_("&Help"))
        self.menuEdit.setTitle(_("&Edit"))
        self.menuCol.setTitle(_("&File"))
        self.menuTools.setTitle(_("&Tools"))
        self.menuPlugins.setTitle(_("&Add-ons"))
        self.actionExit.setText(_("E&xit"))
        self.actionExit.setShortcut(_("Ctrl+Q"))
        self.actionPreferences.setText(_("&Preferences..."))
        self.actionPreferences.setStatusTip(_("Configure interface language and options"))
        self.actionPreferences.setShortcut(_("Ctrl+P"))
        self.actionAbout.setText(_("&About..."))
        self.actionUndo.setText(_("&Undo"))
        self.actionUndo.setShortcut(_("Ctrl+Z"))
        self.actionCheckMediaDatabase.setText(_("Check &Media..."))
        self.actionCheckMediaDatabase.setStatusTip(_("Check the files in the media directory"))
        self.actionOpenPluginFolder.setText(_("&Open Add-ons Folder..."))
        self.actionDonate.setText(_("&Support Anki..."))
        self.actionDownloadSharedPlugin.setText(_("Browse && Install..."))
        self.actionFullDatabaseCheck.setText(_("&Check Database..."))
        self.actionDocumentation.setText(_("&Guide..."))
        self.actionDocumentation.setShortcut(_("F1"))
        self.actionSwitchProfile.setText(_("&Switch Profile..."))
        self.actionSwitchProfile.setShortcut(_("Ctrl+Shift+P"))
        self.actionExport.setText(_("&Export..."))
        self.actionExport.setShortcut(_("Ctrl+E"))
        self.actionImport.setText(_("&Import..."))
        self.actionImport.setShortcut(_("Ctrl+I"))
        self.actionStudyDeck.setText(_("Study Deck..."))
        self.actionStudyDeck.setShortcut(_("/"))
        self.actionEmptyCards.setText(_("Empty Cards..."))
        self.actionCreateFiltered.setText(_("Create Filtered Deck..."))
        self.actionCreateFiltered.setShortcut(_("F"))
        self.actionNoteTypes.setText(_("Manage Note Types..."))

import icons_rc
