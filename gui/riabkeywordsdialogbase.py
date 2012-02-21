# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'riabkeywordsdialogbase.ui'
#
# Created: Tue Feb 21 12:50:23 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RiabKeywordsDialogBase(object):
    def setupUi(self, RiabKeywordsDialogBase):
        RiabKeywordsDialogBase.setObjectName(_fromUtf8("RiabKeywordsDialogBase"))
        RiabKeywordsDialogBase.resize(520, 475)
        RiabKeywordsDialogBase.setWindowTitle(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Risk in a Box - Keyword Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout_2 = QtGui.QGridLayout(RiabKeywordsDialogBase)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lblCategory = QtGui.QLabel(RiabKeywordsDialogBase)
        self.lblCategory.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.lblCategory.setObjectName(_fromUtf8("lblCategory"))
        self.gridLayout_2.addWidget(self.lblCategory, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radHazard = QtGui.QRadioButton(RiabKeywordsDialogBase)
        self.radHazard.setToolTip(QtGui.QApplication.translate("RiabKeywordsDialogBase", "A hazard is a situation that poses a level of threat to life, health, property, or environment. (Wikipedia)", None, QtGui.QApplication.UnicodeUTF8))
        self.radHazard.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Hazard", None, QtGui.QApplication.UnicodeUTF8))
        self.radHazard.setObjectName(_fromUtf8("radHazard"))
        self.horizontalLayout_3.addWidget(self.radHazard)
        self.radExposure = QtGui.QRadioButton(RiabKeywordsDialogBase)
        self.radExposure.setToolTip(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Where people and property are situated.", None, QtGui.QApplication.UnicodeUTF8))
        self.radExposure.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.radExposure.setObjectName(_fromUtf8("radExposure"))
        self.horizontalLayout_3.addWidget(self.radExposure)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 2)
        self.label_2 = QtGui.QLabel(RiabKeywordsDialogBase)
        self.label_2.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Subcategory", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.cboSubcategory = QtGui.QComboBox(RiabKeywordsDialogBase)
        self.cboSubcategory.setToolTip(QtGui.QApplication.translate("RiabKeywordsDialogBase", "A subcategory represents the type of hazard.", None, QtGui.QApplication.UnicodeUTF8))
        self.cboSubcategory.setObjectName(_fromUtf8("cboSubcategory"))
        self.gridLayout_2.addWidget(self.cboSubcategory, 2, 1, 1, 2)
        self.pbnAdvanced = QtGui.QPushButton(RiabKeywordsDialogBase)
        self.pbnAdvanced.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Show advanced", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAdvanced.setCheckable(True)
        self.pbnAdvanced.setObjectName(_fromUtf8("pbnAdvanced"))
        self.gridLayout_2.addWidget(self.pbnAdvanced, 3, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(RiabKeywordsDialogBase)
        self.groupBox.setTitle(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Advanced editor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Keyword", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.cboKeyword = QtGui.QComboBox(self.frame)
        self.cboKeyword.setObjectName(_fromUtf8("cboKeyword"))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(0, QtGui.QApplication.translate("RiabKeywordsDialogBase", "Subcategory", None, QtGui.QApplication.UnicodeUTF8))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(1, QtGui.QApplication.translate("RiabKeywordsDialogBase", "Units", None, QtGui.QApplication.UnicodeUTF8))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(2, QtGui.QApplication.translate("RiabKeywordsDialogBase", "Density", None, QtGui.QApplication.UnicodeUTF8))
        self.cboKeyword.addItem(_fromUtf8(""))
        self.cboKeyword.setItemText(3, QtGui.QApplication.translate("RiabKeywordsDialogBase", "Datatype", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalLayout.addWidget(self.cboKeyword)
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.cboValue = QtGui.QComboBox(self.frame)
        self.cboValue.setEditable(True)
        self.cboValue.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.cboValue.setObjectName(_fromUtf8("cboValue"))
        self.horizontalLayout.addWidget(self.cboValue)
        self.pbnAddToList1 = QtGui.QPushButton(self.frame)
        self.pbnAddToList1.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Add to list", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAddToList1.setObjectName(_fromUtf8("pbnAddToList1"))
        self.horizontalLayout.addWidget(self.pbnAddToList1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Current keywords", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.lstKeywords = QtGui.QListWidget(self.groupBox)
        self.lstKeywords.setAlternatingRowColors(True)
        self.lstKeywords.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.lstKeywords.setObjectName(_fromUtf8("lstKeywords"))
        self.gridLayout.addWidget(self.lstKeywords, 5, 0, 1, 1)
        self.pbnRemove = QtGui.QPushButton(self.groupBox)
        self.pbnRemove.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Remove selected", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnRemove.setObjectName(_fromUtf8("pbnRemove"))
        self.gridLayout.addWidget(self.pbnRemove, 6, 0, 1, 1)
        self.radPredefined = QtGui.QRadioButton(self.groupBox)
        self.radPredefined.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Predefined", None, QtGui.QApplication.UnicodeUTF8))
        self.radPredefined.setObjectName(_fromUtf8("radPredefined"))
        self.gridLayout.addWidget(self.radPredefined, 0, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.leKey = QtGui.QLineEdit(self.frame_2)
        self.leKey.setObjectName(_fromUtf8("leKey"))
        self.horizontalLayout_2.addWidget(self.leKey)
        self.label_7 = QtGui.QLabel(self.frame_2)
        self.label_7.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.leValue = QtGui.QLineEdit(self.frame_2)
        self.leValue.setObjectName(_fromUtf8("leValue"))
        self.horizontalLayout_2.addWidget(self.leValue)
        self.pbnAddToList2 = QtGui.QPushButton(self.frame_2)
        self.pbnAddToList2.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "Add to list", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnAddToList2.setObjectName(_fromUtf8("pbnAddToList2"))
        self.horizontalLayout_2.addWidget(self.pbnAddToList2)
        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)
        self.radUserDefined = QtGui.QRadioButton(self.groupBox)
        self.radUserDefined.setText(QtGui.QApplication.translate("RiabKeywordsDialogBase", "User Defined", None, QtGui.QApplication.UnicodeUTF8))
        self.radUserDefined.setObjectName(_fromUtf8("radUserDefined"))
        self.gridLayout.addWidget(self.radUserDefined, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 4, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(RiabKeywordsDialogBase)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout_2.addWidget(self.buttonBox, 5, 0, 1, 3)
        self.lblLayerName = QtGui.QLabel(RiabKeywordsDialogBase)
        self.lblLayerName.setText(_fromUtf8(""))
        self.lblLayerName.setObjectName(_fromUtf8("lblLayerName"))
        self.gridLayout_2.addWidget(self.lblLayerName, 0, 0, 1, 3)
        self.label_2.setBuddy(self.cboSubcategory)
        self.label_4.setBuddy(self.cboKeyword)
        self.label_5.setBuddy(self.cboValue)
        self.label_8.setBuddy(self.lstKeywords)
        self.label_6.setBuddy(self.leKey)
        self.label_7.setBuddy(self.leValue)

        self.retranslateUi(RiabKeywordsDialogBase)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RiabKeywordsDialogBase.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RiabKeywordsDialogBase.reject)
        QtCore.QObject.connect(self.pbnAdvanced, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.groupBox.setVisible)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame.setEnabled)
        QtCore.QObject.connect(self.radPredefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_2.setDisabled)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame_2.setEnabled)
        QtCore.QObject.connect(self.radUserDefined, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frame.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(RiabKeywordsDialogBase)
        RiabKeywordsDialogBase.setTabOrder(self.radHazard, self.radExposure)
        RiabKeywordsDialogBase.setTabOrder(self.radExposure, self.cboSubcategory)
        RiabKeywordsDialogBase.setTabOrder(self.cboSubcategory, self.pbnAdvanced)
        RiabKeywordsDialogBase.setTabOrder(self.pbnAdvanced, self.radPredefined)
        RiabKeywordsDialogBase.setTabOrder(self.radPredefined, self.cboKeyword)
        RiabKeywordsDialogBase.setTabOrder(self.cboKeyword, self.cboValue)
        RiabKeywordsDialogBase.setTabOrder(self.cboValue, self.pbnAddToList1)
        RiabKeywordsDialogBase.setTabOrder(self.pbnAddToList1, self.radUserDefined)
        RiabKeywordsDialogBase.setTabOrder(self.radUserDefined, self.leKey)
        RiabKeywordsDialogBase.setTabOrder(self.leKey, self.leValue)
        RiabKeywordsDialogBase.setTabOrder(self.leValue, self.pbnAddToList2)
        RiabKeywordsDialogBase.setTabOrder(self.pbnAddToList2, self.lstKeywords)
        RiabKeywordsDialogBase.setTabOrder(self.lstKeywords, self.pbnRemove)
        RiabKeywordsDialogBase.setTabOrder(self.pbnRemove, self.buttonBox)

    def retranslateUi(self, RiabKeywordsDialogBase):
        pass
