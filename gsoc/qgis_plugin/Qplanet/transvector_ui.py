# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Shared/Development/gsoc/OssimPlanetSasha/gui/transvector_ui.ui'
#
# Created: Wed Aug  5 19:58:14 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(365, 269)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabwidjet = QtGui.QTabWidget(Form)
        self.tabwidjet.setObjectName("tabwidjet")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.input_tr = QtGui.QToolButton(self.tab)
        self.input_tr.setObjectName("input_tr")
        self.horizontalLayout_7.addWidget(self.input_tr)
        self.input_trlabel = QtGui.QLineEdit(self.tab)
        self.input_trlabel.setObjectName("input_trlabel")
        self.horizontalLayout_7.addWidget(self.input_trlabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.output_tr = QtGui.QToolButton(self.tab)
        self.output_tr.setObjectName("output_tr")
        self.horizontalLayout_8.addWidget(self.output_tr)
        self.output_trlabel = QtGui.QLineEdit(self.tab)
        self.output_trlabel.setObjectName("output_trlabel")
        self.horizontalLayout_8.addWidget(self.output_trlabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.tx = QtGui.QLineEdit(self.tab)
        self.tx.setObjectName("tx")
        self.horizontalLayout_6.addWidget(self.tx)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.ty = QtGui.QLineEdit(self.tab)
        self.ty.setObjectName("ty")
        self.horizontalLayout_6.addWidget(self.ty)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.traslate = QtGui.QPushButton(self.tab)
        self.traslate.setObjectName("traslate")
        self.horizontalLayout_9.addWidget(self.traslate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.tabwidjet.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem4)
        self.input_rot = QtGui.QToolButton(self.tab_2)
        self.input_rot.setObjectName("input_rot")
        self.horizontalLayout_11.addWidget(self.input_rot)
        self.input_rotlabel = QtGui.QLineEdit(self.tab_2)
        self.input_rotlabel.setObjectName("input_rotlabel")
        self.horizontalLayout_11.addWidget(self.input_rotlabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.output_rot = QtGui.QToolButton(self.tab_2)
        self.output_rot.setObjectName("output_rot")
        self.horizontalLayout_12.addWidget(self.output_rot)
        self.output_rotlabel = QtGui.QLineEdit(self.tab_2)
        self.output_rotlabel.setObjectName("output_rotlabel")
        self.horizontalLayout_12.addWidget(self.output_rotlabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.angle = QtGui.QLineEdit(self.tab_2)
        self.angle.setObjectName("angle")
        self.horizontalLayout_10.addWidget(self.angle)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.rotate = QtGui.QPushButton(self.tab_2)
        self.rotate.setObjectName("rotate")
        self.horizontalLayout_13.addWidget(self.rotate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.tabwidjet.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem9)
        self.input_scal = QtGui.QToolButton(self.tab_3)
        self.input_scal.setObjectName("input_scal")
        self.horizontalLayout_14.addWidget(self.input_scal)
        self.input_scallabel = QtGui.QLineEdit(self.tab_3)
        self.input_scallabel.setObjectName("input_scallabel")
        self.horizontalLayout_14.addWidget(self.input_scallabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem10)
        self.output_scal = QtGui.QToolButton(self.tab_3)
        self.output_scal.setObjectName("output_scal")
        self.horizontalLayout_15.addWidget(self.output_scal)
        self.output_scallabel = QtGui.QLineEdit(self.tab_3)
        self.output_scallabel.setObjectName("output_scallabel")
        self.horizontalLayout_15.addWidget(self.output_scallabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_8 = QtGui.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_17.addWidget(self.label_8)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem11)
        self.scefactor = QtGui.QLineEdit(self.tab_3)
        self.scefactor.setObjectName("scefactor")
        self.horizontalLayout_17.addWidget(self.scefactor)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem12)
        self.scale = QtGui.QPushButton(self.tab_3)
        self.scale.setObjectName("scale")
        self.horizontalLayout_16.addWidget(self.scale)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem13)
        self.tabwidjet.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_11 = QtGui.QLabel(self.tab_4)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout.addWidget(self.label_11)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.gcp1 = QtGui.QToolButton(self.tab_4)
        self.gcp1.setObjectName("gcp1")
        self.horizontalLayout.addWidget(self.gcp1)
        self.gcp1label = QtGui.QLineEdit(self.tab_4)
        self.gcp1label.setObjectName("gcp1label")
        self.horizontalLayout.addWidget(self.gcp1label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtGui.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.gcp2 = QtGui.QToolButton(self.tab_4)
        self.gcp2.setObjectName("gcp2")
        self.horizontalLayout_2.addWidget(self.gcp2)
        self.gcp2label = QtGui.QLineEdit(self.tab_4)
        self.gcp2label.setObjectName("gcp2label")
        self.horizontalLayout_2.addWidget(self.gcp2label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem16)
        self.input_rep = QtGui.QToolButton(self.tab_4)
        self.input_rep.setObjectName("input_rep")
        self.horizontalLayout_3.addWidget(self.input_rep)
        self.input_replabel = QtGui.QLineEdit(self.tab_4)
        self.input_replabel.setObjectName("input_replabel")
        self.horizontalLayout_3.addWidget(self.input_replabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_14 = QtGui.QLabel(self.tab_4)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem17)
        self.output_rep = QtGui.QToolButton(self.tab_4)
        self.output_rep.setObjectName("output_rep")
        self.horizontalLayout_4.addWidget(self.output_rep)
        self.output_replabel = QtGui.QLineEdit(self.tab_4)
        self.output_replabel.setObjectName("output_replabel")
        self.horizontalLayout_4.addWidget(self.output_replabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.affine = QtGui.QRadioButton(self.tab_4)
        self.affine.setObjectName("affine")
        self.horizontalLayout_5.addWidget(self.affine)
        self.conforme = QtGui.QRadioButton(self.tab_4)
        self.conforme.setObjectName("conforme")
        self.horizontalLayout_5.addWidget(self.conforme)
        self.reproject = QtGui.QPushButton(self.tab_4)
        self.reproject.setObjectName("reproject")
        self.horizontalLayout_5.addWidget(self.reproject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.tabwidjet.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabwidjet)

        self.retranslateUi(Form)
        self.tabwidjet.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "TX", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "TY", None, QtGui.QApplication.UnicodeUTF8))
        self.traslate.setText(QtGui.QApplication.translate("Form", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.tabwidjet.setTabText(self.tabwidjet.indexOf(self.tab), QtGui.QApplication.translate("Form", "Traslate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Angle", None, QtGui.QApplication.UnicodeUTF8))
        self.rotate.setText(QtGui.QApplication.translate("Form", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.tabwidjet.setTabText(self.tabwidjet.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Rotate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.scale.setText(QtGui.QApplication.translate("Form", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.tabwidjet.setTabText(self.tabwidjet.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "Scale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "GCP1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Form", "GCP2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Form", "Input", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Form", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.affine.setText(QtGui.QApplication.translate("Form", "Affine", None, QtGui.QApplication.UnicodeUTF8))
        self.conforme.setText(QtGui.QApplication.translate("Form", "Conforme", None, QtGui.QApplication.UnicodeUTF8))
        self.reproject.setText(QtGui.QApplication.translate("Form", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.tabwidjet.setTabText(self.tabwidjet.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Reproject", None, QtGui.QApplication.UnicodeUTF8))
