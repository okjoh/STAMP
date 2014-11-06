# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HeatmapPlot.ui'
#
# Created: Thu Nov 06 18:40:24 2014
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HeatmapPlotDialog(object):
    def setupUi(self, HeatmapPlotDialog):
        HeatmapPlotDialog.setObjectName(_fromUtf8("HeatmapPlotDialog"))
        HeatmapPlotDialog.resize(310, 628)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HeatmapPlotDialog.sizePolicy().hasHeightForWidth())
        HeatmapPlotDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../icons/programIcon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        HeatmapPlotDialog.setWindowIcon(icon)
        self.verticalLayout_4 = QtGui.QVBoxLayout(HeatmapPlotDialog)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(HeatmapPlotDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.cboFieldToPlot = QtGui.QComboBox(HeatmapPlotDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFieldToPlot.sizePolicy().hasHeightForWidth())
        self.cboFieldToPlot.setSizePolicy(sizePolicy)
        self.cboFieldToPlot.setObjectName(_fromUtf8("cboFieldToPlot"))
        self.cboFieldToPlot.addItem(_fromUtf8(""))
        self.cboFieldToPlot.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.cboFieldToPlot)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.chkPlotOnlyActiveFeatures = QtGui.QCheckBox(HeatmapPlotDialog)
        self.chkPlotOnlyActiveFeatures.setObjectName(_fromUtf8("chkPlotOnlyActiveFeatures"))
        self.verticalLayout_4.addWidget(self.chkPlotOnlyActiveFeatures)
        self.groupBox_3 = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblFigureWidth = QtGui.QLabel(self.groupBox_3)
        self.lblFigureWidth.setObjectName(_fromUtf8("lblFigureWidth"))
        self.horizontalLayout.addWidget(self.lblFigureWidth)
        self.spinFigWidth = QtGui.QDoubleSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFigWidth.sizePolicy().hasHeightForWidth())
        self.spinFigWidth.setSizePolicy(sizePolicy)
        self.spinFigWidth.setDecimals(2)
        self.spinFigWidth.setMinimum(0.5)
        self.spinFigWidth.setMaximum(100.0)
        self.spinFigWidth.setSingleStep(0.1)
        self.spinFigWidth.setProperty("value", 7.0)
        self.spinFigWidth.setObjectName(_fromUtf8("spinFigWidth"))
        self.horizontalLayout.addWidget(self.spinFigWidth)
        self.lblFigureHeight = QtGui.QLabel(self.groupBox_3)
        self.lblFigureHeight.setObjectName(_fromUtf8("lblFigureHeight"))
        self.horizontalLayout.addWidget(self.lblFigureHeight)
        self.spinFigHeight = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.spinFigHeight.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinFigHeight.sizePolicy().hasHeightForWidth())
        self.spinFigHeight.setSizePolicy(sizePolicy)
        self.spinFigHeight.setDecimals(2)
        self.spinFigHeight.setMinimum(0.5)
        self.spinFigHeight.setMaximum(100.0)
        self.spinFigHeight.setSingleStep(0.1)
        self.spinFigHeight.setProperty("value", 7.0)
        self.spinFigHeight.setObjectName(_fromUtf8("spinFigHeight"))
        self.horizontalLayout.addWidget(self.spinFigHeight)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(HeatmapPlotDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.cboColourMap = QtGui.QComboBox(HeatmapPlotDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboColourMap.sizePolicy().hasHeightForWidth())
        self.cboColourMap.setSizePolicy(sizePolicy)
        self.cboColourMap.setObjectName(_fromUtf8("cboColourMap"))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.cboColourMap.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.cboColourMap)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.groupBox = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lblDendrogramMethod = QtGui.QLabel(self.groupBox)
        self.lblDendrogramMethod.setObjectName(_fromUtf8("lblDendrogramMethod"))
        self.horizontalLayout_5.addWidget(self.lblDendrogramMethod)
        self.cboRowSortMethod = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboRowSortMethod.sizePolicy().hasHeightForWidth())
        self.cboRowSortMethod.setSizePolicy(sizePolicy)
        self.cboRowSortMethod.setObjectName(_fromUtf8("cboRowSortMethod"))
        self.cboRowSortMethod.addItem(_fromUtf8(""))
        self.cboRowSortMethod.addItem(_fromUtf8(""))
        self.cboRowSortMethod.addItem(_fromUtf8(""))
        self.cboRowSortMethod.addItem(_fromUtf8(""))
        self.cboRowSortMethod.addItem(_fromUtf8(""))
        self.cboRowSortMethod.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.cboRowSortMethod)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lblClusteringThreshold = QtGui.QLabel(self.groupBox)
        self.lblClusteringThreshold.setObjectName(_fromUtf8("lblClusteringThreshold"))
        self.horizontalLayout_2.addWidget(self.lblClusteringThreshold)
        self.spinRowClusteringThreshold = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinRowClusteringThreshold.sizePolicy().hasHeightForWidth())
        self.spinRowClusteringThreshold.setSizePolicy(sizePolicy)
        self.spinRowClusteringThreshold.setDecimals(2)
        self.spinRowClusteringThreshold.setMinimum(0.0)
        self.spinRowClusteringThreshold.setMaximum(1.0)
        self.spinRowClusteringThreshold.setSingleStep(0.05)
        self.spinRowClusteringThreshold.setProperty("value", 0.75)
        self.spinRowClusteringThreshold.setObjectName(_fromUtf8("spinRowClusteringThreshold"))
        self.horizontalLayout_2.addWidget(self.spinRowClusteringThreshold)
        spacerItem1 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.chkShowRowDendrogram = QtGui.QCheckBox(self.groupBox)
        self.chkShowRowDendrogram.setEnabled(True)
        self.chkShowRowDendrogram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkShowRowDendrogram.setChecked(True)
        self.chkShowRowDendrogram.setObjectName(_fromUtf8("chkShowRowDendrogram"))
        self.verticalLayout_2.addWidget(self.chkShowRowDendrogram)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.lblDendrogramWidth = QtGui.QLabel(self.groupBox)
        self.lblDendrogramWidth.setObjectName(_fromUtf8("lblDendrogramWidth"))
        self.horizontalLayout_9.addWidget(self.lblDendrogramWidth)
        self.spinDendrogramRowWidth = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDendrogramRowWidth.sizePolicy().hasHeightForWidth())
        self.spinDendrogramRowWidth.setSizePolicy(sizePolicy)
        self.spinDendrogramRowWidth.setDecimals(2)
        self.spinDendrogramRowWidth.setMinimum(0.0)
        self.spinDendrogramRowWidth.setMaximum(50.0)
        self.spinDendrogramRowWidth.setSingleStep(0.05)
        self.spinDendrogramRowWidth.setProperty("value", 1.5)
        self.spinDendrogramRowWidth.setObjectName(_fromUtf8("spinDendrogramRowWidth"))
        self.horizontalLayout_9.addWidget(self.spinDendrogramRowWidth)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.lblDendrogramMethod_2 = QtGui.QLabel(self.groupBox_2)
        self.lblDendrogramMethod_2.setObjectName(_fromUtf8("lblDendrogramMethod_2"))
        self.horizontalLayout_10.addWidget(self.lblDendrogramMethod_2)
        self.cboColSortMethod = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboColSortMethod.sizePolicy().hasHeightForWidth())
        self.cboColSortMethod.setSizePolicy(sizePolicy)
        self.cboColSortMethod.setObjectName(_fromUtf8("cboColSortMethod"))
        self.cboColSortMethod.addItem(_fromUtf8(""))
        self.cboColSortMethod.addItem(_fromUtf8(""))
        self.cboColSortMethod.addItem(_fromUtf8(""))
        self.cboColSortMethod.addItem(_fromUtf8(""))
        self.cboColSortMethod.addItem(_fromUtf8(""))
        self.cboColSortMethod.addItem(_fromUtf8(""))
        self.horizontalLayout_10.addWidget(self.cboColSortMethod)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.lblClusteringThreshold_2 = QtGui.QLabel(self.groupBox_2)
        self.lblClusteringThreshold_2.setObjectName(_fromUtf8("lblClusteringThreshold_2"))
        self.horizontalLayout_11.addWidget(self.lblClusteringThreshold_2)
        self.spinColClusteringThreshold = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinColClusteringThreshold.sizePolicy().hasHeightForWidth())
        self.spinColClusteringThreshold.setSizePolicy(sizePolicy)
        self.spinColClusteringThreshold.setDecimals(2)
        self.spinColClusteringThreshold.setMinimum(0.0)
        self.spinColClusteringThreshold.setMaximum(1.0)
        self.spinColClusteringThreshold.setSingleStep(0.05)
        self.spinColClusteringThreshold.setProperty("value", 0.75)
        self.spinColClusteringThreshold.setObjectName(_fromUtf8("spinColClusteringThreshold"))
        self.horizontalLayout_11.addWidget(self.spinColClusteringThreshold)
        spacerItem3 = QtGui.QSpacerItem(5, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.chkShowColDendrogram = QtGui.QCheckBox(self.groupBox_2)
        self.chkShowColDendrogram.setEnabled(True)
        self.chkShowColDendrogram.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chkShowColDendrogram.setChecked(True)
        self.chkShowColDendrogram.setObjectName(_fromUtf8("chkShowColDendrogram"))
        self.verticalLayout_3.addWidget(self.chkShowColDendrogram)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.lblTopDendrogramHeight_2 = QtGui.QLabel(self.groupBox_2)
        self.lblTopDendrogramHeight_2.setObjectName(_fromUtf8("lblTopDendrogramHeight_2"))
        self.horizontalLayout_13.addWidget(self.lblTopDendrogramHeight_2)
        self.spinDendrogramColHeight = QtGui.QDoubleSpinBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinDendrogramColHeight.sizePolicy().hasHeightForWidth())
        self.spinDendrogramColHeight.setSizePolicy(sizePolicy)
        self.spinDendrogramColHeight.setDecimals(2)
        self.spinDendrogramColHeight.setMinimum(0.0)
        self.spinDendrogramColHeight.setMaximum(50.0)
        self.spinDendrogramColHeight.setSingleStep(0.05)
        self.spinDendrogramColHeight.setProperty("value", 1.5)
        self.spinDendrogramColHeight.setObjectName(_fromUtf8("spinDendrogramColHeight"))
        self.horizontalLayout_13.addWidget(self.spinDendrogramColHeight)
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.groupBox_6 = QtGui.QGroupBox(HeatmapPlotDialog)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.radioLegendPosNone = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosNone.setObjectName(_fromUtf8("radioLegendPosNone"))
        self.gridLayout.addWidget(self.radioLegendPosNone, 0, 0, 1, 1)
        self.radioLegendPosLowerLeft = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerLeft.setObjectName(_fromUtf8("radioLegendPosLowerLeft"))
        self.gridLayout.addWidget(self.radioLegendPosLowerLeft, 0, 2, 1, 1)
        self.radioLegendPosLowerRight = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosLowerRight.setObjectName(_fromUtf8("radioLegendPosLowerRight"))
        self.gridLayout.addWidget(self.radioLegendPosLowerRight, 1, 2, 1, 1)
        self.radioLegendPosUpperRight = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosUpperRight.setObjectName(_fromUtf8("radioLegendPosUpperRight"))
        self.gridLayout.addWidget(self.radioLegendPosUpperRight, 0, 1, 1, 1)
        self.radioLegendPosUpperLeft = QtGui.QRadioButton(self.groupBox_6)
        self.radioLegendPosUpperLeft.setChecked(True)
        self.radioLegendPosUpperLeft.setObjectName(_fromUtf8("radioLegendPosUpperLeft"))
        self.gridLayout.addWidget(self.radioLegendPosUpperLeft, 1, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupBox_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.buttonBox = QtGui.QDialogButtonBox(HeatmapPlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(HeatmapPlotDialog)
        self.cboFieldToPlot.setCurrentIndex(1)
        self.cboColourMap.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), HeatmapPlotDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), HeatmapPlotDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(HeatmapPlotDialog)

    def retranslateUi(self, HeatmapPlotDialog):
        HeatmapPlotDialog.setWindowTitle(QtGui.QApplication.translate("HeatmapPlotDialog", "Heatmap plot", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Field to plot:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboFieldToPlot.setItemText(0, QtGui.QApplication.translate("HeatmapPlotDialog", "Number of sequences", None, QtGui.QApplication.UnicodeUTF8))
        self.cboFieldToPlot.setItemText(1, QtGui.QApplication.translate("HeatmapPlotDialog", "Proportion of sequences (%)", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPlotOnlyActiveFeatures.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Plot only active features", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("HeatmapPlotDialog", "Figure size", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureWidth.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblFigureHeight.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Colour map:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(0, QtGui.QApplication.translate("HeatmapPlotDialog", "Blues", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(1, QtGui.QApplication.translate("HeatmapPlotDialog", "Blue to red to green", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(2, QtGui.QApplication.translate("HeatmapPlotDialog", "Blue to white to red", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(3, QtGui.QApplication.translate("HeatmapPlotDialog", "Cool to warm", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(4, QtGui.QApplication.translate("HeatmapPlotDialog", "Grayscale", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(5, QtGui.QApplication.translate("HeatmapPlotDialog", "Jet", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(6, QtGui.QApplication.translate("HeatmapPlotDialog", "Orange to red", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(7, QtGui.QApplication.translate("HeatmapPlotDialog", "Paired", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(8, QtGui.QApplication.translate("HeatmapPlotDialog", "Purple to green", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(9, QtGui.QApplication.translate("HeatmapPlotDialog", "Reds", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(10, QtGui.QApplication.translate("HeatmapPlotDialog", "Red to blue", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(11, QtGui.QApplication.translate("HeatmapPlotDialog", "Spectral", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColourMap.setItemText(12, QtGui.QApplication.translate("HeatmapPlotDialog", "Yellow to orange to red", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("HeatmapPlotDialog", "Sort rows", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDendrogramMethod.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Methods:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboRowSortMethod.setItemText(0, QtGui.QApplication.translate("HeatmapPlotDialog", "Alphabetical order", None, QtGui.QApplication.UnicodeUTF8))
        self.cboRowSortMethod.setItemText(1, QtGui.QApplication.translate("HeatmapPlotDialog", "Average neighbour (UPGMA)", None, QtGui.QApplication.UnicodeUTF8))
        self.cboRowSortMethod.setItemText(2, QtGui.QApplication.translate("HeatmapPlotDialog", "Centroid", None, QtGui.QApplication.UnicodeUTF8))
        self.cboRowSortMethod.setItemText(3, QtGui.QApplication.translate("HeatmapPlotDialog", "Furthest neighbour", None, QtGui.QApplication.UnicodeUTF8))
        self.cboRowSortMethod.setItemText(4, QtGui.QApplication.translate("HeatmapPlotDialog", "Nearest neighbour", None, QtGui.QApplication.UnicodeUTF8))
        self.cboRowSortMethod.setItemText(5, QtGui.QApplication.translate("HeatmapPlotDialog", "Ward", None, QtGui.QApplication.UnicodeUTF8))
        self.lblClusteringThreshold.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Dendrogram clustering threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowRowDendrogram.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Show dendrogram", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDendrogramWidth.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Width (inches):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("HeatmapPlotDialog", "Sort rows", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDendrogramMethod_2.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Methods:", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColSortMethod.setItemText(0, QtGui.QApplication.translate("HeatmapPlotDialog", "Alphabetical order", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColSortMethod.setItemText(1, QtGui.QApplication.translate("HeatmapPlotDialog", "Average neighbour (UPGMA)", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColSortMethod.setItemText(2, QtGui.QApplication.translate("HeatmapPlotDialog", "Centroid", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColSortMethod.setItemText(3, QtGui.QApplication.translate("HeatmapPlotDialog", "Furthest neighbour", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColSortMethod.setItemText(4, QtGui.QApplication.translate("HeatmapPlotDialog", "Nearest neighbour", None, QtGui.QApplication.UnicodeUTF8))
        self.cboColSortMethod.setItemText(5, QtGui.QApplication.translate("HeatmapPlotDialog", "Ward", None, QtGui.QApplication.UnicodeUTF8))
        self.lblClusteringThreshold_2.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Dendrogram clustering threshold:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkShowColDendrogram.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Show dendrogram", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTopDendrogramHeight_2.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Height (inches):", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("HeatmapPlotDialog", "Legend position", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosNone.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerLeft.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Lower left", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosLowerRight.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Lower right", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosUpperRight.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Upper right", None, QtGui.QApplication.UnicodeUTF8))
        self.radioLegendPosUpperLeft.setText(QtGui.QApplication.translate("HeatmapPlotDialog", "Upper left", None, QtGui.QApplication.UnicodeUTF8))

