# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'U:/extensions/studioTools/python/arxLoader/ui4.ui'
#
# Created: Sun Apr 05 23:00:24 2015
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_loaderWindow(object):
    def setupUi(self, loaderWindow):
        loaderWindow.setObjectName("loaderWindow")
        loaderWindow.resize(800, 670)
        loaderWindow.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget = QtGui.QWidget(loaderWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_5 = QtGui.QFrame(self.frame)
        self.frame_5.setMinimumSize(QtCore.QSize(311, 611))
        self.frame_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtGui.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtGui.QFrame.Box)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shotgun_radioButton = QtGui.QRadioButton(self.frame_3)
        self.shotgun_radioButton.setChecked(True)
        self.shotgun_radioButton.setObjectName("shotgun_radioButton")
        self.horizontalLayout.addWidget(self.shotgun_radioButton)
        self.manualBrowser_radioButton = QtGui.QRadioButton(self.frame_3)
        self.manualBrowser_radioButton.setObjectName("manualBrowser_radioButton")
        self.horizontalLayout.addWidget(self.manualBrowser_radioButton)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_6 = QtGui.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setContentsMargins(9, 2, 9, 2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.type_checkBox = QtGui.QCheckBox(self.frame_6)
        self.type_checkBox.setObjectName("type_checkBox")
        self.horizontalLayout_6.addWidget(self.type_checkBox)
        self.type_comboBox = QtGui.QComboBox(self.frame_6)
        self.type_comboBox.setEnabled(False)
        self.type_comboBox.setObjectName("type_comboBox")
        self.horizontalLayout_6.addWidget(self.type_comboBox)
        self.showMayaAsset_checkBox = QtGui.QCheckBox(self.frame_6)
        self.showMayaAsset_checkBox.setObjectName("showMayaAsset_checkBox")
        self.horizontalLayout_6.addWidget(self.showMayaAsset_checkBox)
        self.label_4 = QtGui.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.viewMode_comboBox = QtGui.QComboBox(self.frame_6)
        self.viewMode_comboBox.setMaximumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.viewMode_comboBox.setFont(font)
        self.viewMode_comboBox.setObjectName("viewMode_comboBox")
        self.horizontalLayout_6.addWidget(self.viewMode_comboBox)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(3, 1)
        self.horizontalLayout_6.setStretch(4, 1)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_2 = QtGui.QFrame(self.frame_5)
        self.frame_2.setMinimumSize(QtCore.QSize(291, 520))
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.main_label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")
        self.horizontalLayout_5.addWidget(self.main_label)
        self.extra_label = QtGui.QLabel(self.frame_2)
        self.extra_label.setText("")
        self.extra_label.setAlignment(QtCore.Qt.AlignCenter)
        self.extra_label.setObjectName("extra_label")
        self.horizontalLayout_5.addWidget(self.extra_label)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.asset_tabWidget = QtGui.QTabWidget(self.frame_2)
        self.asset_tabWidget.setMaximumSize(QtCore.QSize(16777215, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 40))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 20, 20))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.asset_tabWidget.setPalette(palette)
        self.asset_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.asset_tabWidget.setObjectName("asset_tabWidget")
        self.all = QtGui.QWidget()
        self.all.setObjectName("all")
        self.asset_tabWidget.addTab(self.all, "")
        self.charmain_2 = QtGui.QWidget()
        self.charmain_2.setObjectName("charmain_2")
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.charmain_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.asset_tabWidget.addTab(self.charmain_2, "")
        self.charsec_2 = QtGui.QWidget()
        self.charsec_2.setObjectName("charsec_2")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.charsec_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.asset_tabWidget.addTab(self.charsec_2, "")
        self.prop_2 = QtGui.QWidget()
        self.prop_2.setObjectName("prop_2")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.prop_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.asset_tabWidget.addTab(self.prop_2, "")
        self.envint_2 = QtGui.QWidget()
        self.envint_2.setObjectName("envint_2")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.envint_2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.asset_tabWidget.addTab(self.envint_2, "")
        self.envext_2 = QtGui.QWidget()
        self.envext_2.setObjectName("envext_2")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.envext_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.asset_tabWidget.addTab(self.envext_2, "")
        self.twoD_2 = QtGui.QWidget()
        self.twoD_2.setObjectName("twoD_2")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.twoD_2)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.asset_tabWidget.addTab(self.twoD_2, "")
        self.fx_2 = QtGui.QWidget()
        self.fx_2.setObjectName("fx_2")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.fx_2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.asset_tabWidget.addTab(self.fx_2, "")
        self.verticalLayout_7.addWidget(self.asset_tabWidget)
        self.main_listWidget = QtGui.QListWidget(self.frame_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.main_listWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.main_listWidget.setFont(font)
        self.main_listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.main_listWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.main_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.main_listWidget.setMovement(QtGui.QListView.Static)
        self.main_listWidget.setProperty("isWrapping", False)
        self.main_listWidget.setResizeMode(QtGui.QListView.Adjust)
        self.main_listWidget.setLayoutMode(QtGui.QListView.SinglePass)
        self.main_listWidget.setViewMode(QtGui.QListView.ListMode)
        self.main_listWidget.setWordWrap(True)
        self.main_listWidget.setObjectName("main_listWidget")
        self.verticalLayout_7.addWidget(self.main_listWidget)
        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 12)
        self.verticalLayout.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selectedReference_checkBox = QtGui.QCheckBox(self.frame_2)
        self.selectedReference_checkBox.setChecked(False)
        self.selectedReference_checkBox.setObjectName("selectedReference_checkBox")
        self.horizontalLayout_4.addWidget(self.selectedReference_checkBox)
        self.thumbnail_checkBox = QtGui.QCheckBox(self.frame_2)
        self.thumbnail_checkBox.setChecked(True)
        self.thumbnail_checkBox.setObjectName("thumbnail_checkBox")
        self.horizontalLayout_4.addWidget(self.thumbnail_checkBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.uploadAsset_pushButton = QtGui.QPushButton(self.frame_2)
        self.uploadAsset_pushButton.setMinimumSize(QtCore.QSize(0, 26))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(162, 79, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 79, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 79, 46))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.uploadAsset_pushButton.setPalette(palette)
        self.uploadAsset_pushButton.setObjectName("uploadAsset_pushButton")
        self.verticalLayout.addWidget(self.uploadAsset_pushButton)
        self.createReference_pushButton = QtGui.QPushButton(self.frame_2)
        self.createReference_pushButton.setMinimumSize(QtCore.QSize(271, 31))
        self.createReference_pushButton.setObjectName("createReference_pushButton")
        self.verticalLayout.addWidget(self.createReference_pushButton)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_15.addWidget(self.frame_5)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(251, 611))
        self.frame_4.setMaximumSize(QtCore.QSize(251, 900))
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.filter_frame = QtGui.QFrame(self.frame_4)
        self.filter_frame.setGeometry(QtCore.QRect(9, 491, 231, 111))
        self.filter_frame.setFrameShape(QtGui.QFrame.Box)
        self.filter_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.filter_frame.setObjectName("filter_frame")
        self.gridLayout_2 = QtGui.QGridLayout(self.filter_frame)
        self.gridLayout_2.setHorizontalSpacing(11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.parent_comboBox = QtGui.QComboBox(self.filter_frame)
        self.parent_comboBox.setEnabled(False)
        self.parent_comboBox.setObjectName("parent_comboBox")
        self.gridLayout_2.addWidget(self.parent_comboBox, 2, 0, 1, 1)
        self.variation_checkBox = QtGui.QCheckBox(self.filter_frame)
        self.variation_checkBox.setObjectName("variation_checkBox")
        self.gridLayout_2.addWidget(self.variation_checkBox, 3, 1, 1, 1)
        self.variation_comboBox = QtGui.QComboBox(self.filter_frame)
        self.variation_comboBox.setEnabled(False)
        self.variation_comboBox.setObjectName("variation_comboBox")
        self.gridLayout_2.addWidget(self.variation_comboBox, 3, 0, 1, 1)
        self.parent_checkBox = QtGui.QCheckBox(self.filter_frame)
        self.parent_checkBox.setObjectName("parent_checkBox")
        self.gridLayout_2.addWidget(self.parent_checkBox, 2, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.filter_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 4)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.projectInfo_frame = QtGui.QFrame(self.frame_4)
        self.projectInfo_frame.setGeometry(QtCore.QRect(9, 76, 231, 90))
        self.projectInfo_frame.setMaximumSize(QtCore.QSize(233, 93))
        self.projectInfo_frame.setFrameShape(QtGui.QFrame.Box)
        self.projectInfo_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.projectInfo_frame.setObjectName("projectInfo_frame")
        self.gridLayout = QtGui.QGridLayout(self.projectInfo_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.shot_label = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.shot_label.setFont(font)
        self.shot_label.setObjectName("shot_label")
        self.gridLayout.addWidget(self.shot_label, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.episode_label = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.episode_label.setFont(font)
        self.episode_label.setObjectName("episode_label")
        self.gridLayout.addWidget(self.episode_label, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.sequence_label = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.sequence_label.setFont(font)
        self.sequence_label.setObjectName("sequence_label")
        self.gridLayout.addWidget(self.sequence_label, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.step_label = QtGui.QLabel(self.projectInfo_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.step_label.setFont(font)
        self.step_label.setObjectName("step_label")
        self.gridLayout.addWidget(self.step_label, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.inforamtion_frame = QtGui.QFrame(self.frame_4)
        self.inforamtion_frame.setGeometry(QtCore.QRect(9, 175, 233, 148))
        self.inforamtion_frame.setMinimumSize(QtCore.QSize(233, 148))
        self.inforamtion_frame.setMaximumSize(QtCore.QSize(233, 138))
        self.inforamtion_frame.setFrameShape(QtGui.QFrame.Box)
        self.inforamtion_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.inforamtion_frame.setObjectName("inforamtion_frame")
        self.label_15 = QtGui.QLabel(self.inforamtion_frame)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.information_label = QtGui.QLabel(self.inforamtion_frame)
        self.information_label.setGeometry(QtCore.QRect(10, 30, 211, 111))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.information_label.setFont(font)
        self.information_label.setObjectName("information_label")
        self.showSceneAsset_checkBox = QtGui.QCheckBox(self.frame_4)
        self.showSceneAsset_checkBox.setGeometry(QtCore.QRect(9, 422, 114, 17))
        self.showSceneAsset_checkBox.setChecked(False)
        self.showSceneAsset_checkBox.setObjectName("showSceneAsset_checkBox")
        self.search_frame = QtGui.QFrame(self.frame_4)
        self.search_frame.setGeometry(QtCore.QRect(9, 445, 231, 40))
        self.search_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.search_frame.setMaximumSize(QtCore.QSize(233, 40))
        self.search_frame.setFrameShape(QtGui.QFrame.Box)
        self.search_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.search_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtGui.QLabel(self.search_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.search_lineEdit = QtGui.QLineEdit(self.search_frame)
        self.search_lineEdit.setText("")
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.horizontalLayout_2.addWidget(self.search_lineEdit)
        self.logo_label = QtGui.QLabel(self.frame_4)
        self.logo_label.setGeometry(QtCore.QRect(9, 9, 221, 61))
        self.logo_label.setMinimumSize(QtCore.QSize(221, 61))
        self.logo_label.setMaximumSize(QtCore.QSize(221, 61))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.logo_label.setFont(font)
        self.logo_label.setText("")
        self.logo_label.setObjectName("logo_label")
        self.information2_frame = QtGui.QFrame(self.frame_4)
        self.information2_frame.setGeometry(QtCore.QRect(9, 330, 233, 91))
        self.information2_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.information2_frame.setFrameShape(QtGui.QFrame.Box)
        self.information2_frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.information2_frame.setObjectName("information2_frame")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.information2_frame)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.info2_label = QtGui.QLabel(self.information2_frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.info2_label.setFont(font)
        self.info2_label.setObjectName("info2_label")
        self.verticalLayout_5.addWidget(self.info2_label)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.showWrongAsset_checkBox = QtGui.QCheckBox(self.information2_frame)
        self.showWrongAsset_checkBox.setObjectName("showWrongAsset_checkBox")
        self.horizontalLayout_7.addWidget(self.showWrongAsset_checkBox)
        self.showInfo_pushButton = QtGui.QPushButton(self.information2_frame)
        self.showInfo_pushButton.setObjectName("showInfo_pushButton")
        self.horizontalLayout_7.addWidget(self.showInfo_pushButton)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.email_pushButton = QtGui.QPushButton(self.information2_frame)
        self.email_pushButton.setObjectName("email_pushButton")
        self.verticalLayout_5.addWidget(self.email_pushButton)
        self.horizontalLayout_15.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame)
        loaderWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(loaderWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        loaderWindow.setMenuBar(self.menubar)

        self.retranslateUi(loaderWindow)
        self.asset_tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.type_checkBox, QtCore.SIGNAL("toggled(bool)"), self.type_comboBox.setEnabled)
        QtCore.QObject.connect(self.parent_checkBox, QtCore.SIGNAL("toggled(bool)"), self.parent_comboBox.setEnabled)
        QtCore.QObject.connect(self.variation_checkBox, QtCore.SIGNAL("toggled(bool)"), self.variation_comboBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(loaderWindow)

    def retranslateUi(self, loaderWindow):
        loaderWindow.setWindowTitle(QtGui.QApplication.translate("loaderWindow", "Arx Anim Loader v.1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_radioButton.setText(QtGui.QApplication.translate("loaderWindow", "Shotgun shot assets", None, QtGui.QApplication.UnicodeUTF8))
        self.manualBrowser_radioButton.setText(QtGui.QApplication.translate("loaderWindow", "Manual Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.type_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.showMayaAsset_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Shot asset not in Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("loaderWindow", "View Mode", None, QtGui.QApplication.UnicodeUTF8))
        self.main_label.setText(QtGui.QApplication.translate("loaderWindow", "Shotgun Asset List", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.all), QtGui.QApplication.translate("loaderWindow", "all", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.charmain_2), QtGui.QApplication.translate("loaderWindow", "charmain", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.charsec_2), QtGui.QApplication.translate("loaderWindow", "charsec", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.prop_2), QtGui.QApplication.translate("loaderWindow", "prop", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.envint_2), QtGui.QApplication.translate("loaderWindow", "envint", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.envext_2), QtGui.QApplication.translate("loaderWindow", "envext", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.twoD_2), QtGui.QApplication.translate("loaderWindow", "2d", None, QtGui.QApplication.UnicodeUTF8))
        self.asset_tabWidget.setTabText(self.asset_tabWidget.indexOf(self.fx_2), QtGui.QApplication.translate("loaderWindow", "fx", None, QtGui.QApplication.UnicodeUTF8))
        self.main_listWidget.setSortingEnabled(False)
        self.selectedReference_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Create selected only", None, QtGui.QApplication.UnicodeUTF8))
        self.thumbnail_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Show Thumbnail", None, QtGui.QApplication.UnicodeUTF8))
        self.uploadAsset_pushButton.setText(QtGui.QApplication.translate("loaderWindow", "Upload list to Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.createReference_pushButton.setText(QtGui.QApplication.translate("loaderWindow", "Create All Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.variation_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Variation", None, QtGui.QApplication.UnicodeUTF8))
        self.parent_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Parent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("loaderWindow", "Asset filters : ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("loaderWindow", "Sequence : ", None, QtGui.QApplication.UnicodeUTF8))
        self.shot_label.setText(QtGui.QApplication.translate("loaderWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("loaderWindow", "Shot : ", None, QtGui.QApplication.UnicodeUTF8))
        self.episode_label.setText(QtGui.QApplication.translate("loaderWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("loaderWindow", "Episode : ", None, QtGui.QApplication.UnicodeUTF8))
        self.sequence_label.setText(QtGui.QApplication.translate("loaderWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("loaderWindow", "Step : ", None, QtGui.QApplication.UnicodeUTF8))
        self.step_label.setText(QtGui.QApplication.translate("loaderWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("loaderWindow", "Information : ", None, QtGui.QApplication.UnicodeUTF8))
        self.information_label.setText(QtGui.QApplication.translate("loaderWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.showSceneAsset_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Show only in scene", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("loaderWindow", "Search : ", None, QtGui.QApplication.UnicodeUTF8))
        self.info2_label.setText(QtGui.QApplication.translate("loaderWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.showWrongAsset_checkBox.setText(QtGui.QApplication.translate("loaderWindow", "Show", None, QtGui.QApplication.UnicodeUTF8))
        self.showInfo_pushButton.setText(QtGui.QApplication.translate("loaderWindow", "Show Info", None, QtGui.QApplication.UnicodeUTF8))
        self.email_pushButton.setText(QtGui.QApplication.translate("loaderWindow", "Email Coordinator", None, QtGui.QApplication.UnicodeUTF8))
