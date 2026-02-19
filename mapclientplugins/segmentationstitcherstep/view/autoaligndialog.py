from cmlibs.widgets.utils import parse_real
from mapclientplugins.segmentationstitcherstep.view.ui_autoaligndialog import Ui_auto_align_dialog
from PySide6 import QtWidgets


class AutoAlignDialog(QtWidgets.QDialog):
    """
    Modal dialog allowing a dict of options to be edited, then OK/Cancel to be returned.
    """

    def __init__(self, parent, connection, dependent_segment_index):
        """
        :param parent: Parent widget.
        :param connection: Stitcher Connection to drive alignment.
        :param dependent_segment_index: Index of connection's segment to align to the other.
        """
        super(AutoAlignDialog, self).__init__(parent)
        self._connection = connection
        self._dependent_segment_index = dependent_segment_index
        self._ui = Ui_auto_align_dialog()
        self._ui.setupUi(self)
        self._setup()

    def _setup(self):
        self.setWindowTitle('Auto-Align Segment...')
        segments = self._connection.get_segments()
        fixed_segment_index = 1 if (self._dependent_segment_index == 0) else 0
        fixed_segment_name = segments[fixed_segment_index].get_name()
        dependent_segment_name = segments[self._dependent_segment_index].get_name()
        summary_text = 'Auto-align ' + dependent_segment_name + ' relative to ' + fixed_segment_name + '?'
        self._ui.summary_label.setText(summary_text)
        self._ui.phase_1_align_ends_checkBox.setChecked(True)
        self._ui.align_gap_distance_lineEdit.setText('0')
        self._ui.phase_2_optimize_transformation_checkBox.setChecked(True)

    def get_options(self):
        """
        Get options from dialog.
        :return: bool phase1_align, float gap_distance, bool phase_2_optimize.
        """
        phase1_align = self._ui.phase_1_align_ends_checkBox.isChecked()
        gap_distance = parse_real(self._ui.align_gap_distance_lineEdit)
        phase_2_optimize = self._ui.phase_2_optimize_transformation_checkBox.isChecked()
        return phase1_align, gap_distance, phase_2_optimize
