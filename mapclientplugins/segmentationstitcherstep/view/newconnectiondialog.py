from PySide6 import QtCore, QtWidgets


class NewConnectionDialog(QtWidgets.QDialog):
    """
    Modal dialog allowing a dict of options to be edited, then OK/Cancel to be returned.
    """

    def __init__(self, parent, stitcher):
        """
        :param parent: Parent widget.
        :param stitcher: Stitcher object to choose segments for.
        """
        super(NewConnectionDialog, self).__init__(parent)
        self._stitcher = stitcher
        self._segment_choosers = []
        self._setup()

    def _setup(self):
        self.setWindowTitle("Create new connection...")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self._dialogLayout = QtWidgets.QVBoxLayout(self)
        self._dialogLayout.setObjectName("dialogLayout")
        self.setModal(True)

        segment_tips = [
            "First segment to output in connection",
            "Second segment to output in connection"
        ]
        all_segments = self._stitcher.get_segments()
        for chooser_index in range(2):
            name = "Segment " + str(chooser_index + 1) + ":"
            label = QtWidgets.QLabel(self)
            label.setObjectName(name)
            label.setText(name)
            self._dialogLayout.addWidget(label)
            segment_chooser = QtWidgets.QComboBox(self)
            for segment in all_segments:
                segment_chooser.addItem(segment.get_name())
            segment_chooser.setToolTip(segment_tips[chooser_index])
            self._dialogLayout.addWidget(segment_chooser)
            self._segment_choosers.append(segment_chooser)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self._dialogLayout.addItem(spacerItem)

        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)  # hide window context help (?)
        self.resize(300, 150)
        self._buttonBox = QtWidgets.QDialogButtonBox(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._buttonBox.sizePolicy().hasHeightForWidth())
        self._buttonBox.setSizePolicy(sizePolicy)
        self._buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self._buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self._buttonBox.setObjectName("buttonBox")
        self._dialogLayout.addWidget(self._buttonBox)
        self._buttonBox.accepted.connect(self.accept)
        self._buttonBox.rejected.connect(self.reject)

    def get_segments(self):
        """
        :return: List of 2 segments to connect.
        """
        all_segments = self._stitcher.get_segments()
        segments = []
        for segment_chooser in self._segment_choosers:
            segment_name = segment_chooser.currentText()
            for segment in all_segments:
                if segment.get_name() == segment_name:
                    segments.append(segment)
                    break
        return segments
