from PySide2.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
    QPushButton,
)
from PySide2.QtGui import QCloseEvent
from threading import Timer


class ThreadControlWidget(QWidget):
    """ """

    def __init__(self) -> None:
        """ """
        super().__init__()

        self._button_report: QPushButton = QPushButton(text="REPORT")
        self._button_run_timer: QPushButton = QPushButton(text="RUN TIMER")
        self._button_stop_timer: QPushButton = QPushButton(text="STOP TIMER")
        self._timer: Timer = None

        self._button_run_timer.setEnabled(True)
        self._button_stop_timer.setEnabled(False)
        layout: QVBoxLayout = QVBoxLayout(self)
        layout.addWidget(self._button_report)
        layout.addWidget(self._button_run_timer)
        layout.addWidget(self._button_stop_timer)

        self._button_report.clicked.connect(self._button_report_clicked)
        self._button_run_timer.clicked.connect(self._button_run_timer_clicked)
        self._button_stop_timer.clicked.connect(self._button_stop_timer_clicked)

    def _timer_callback(self) -> None:
        """ """
        print("Timer callback!!!")
        self._button_stop_timer.setEnabled(False)
        self._button_run_timer.setEnabled(True)
        self._timer = None

    def _button_report_clicked(self) -> None:
        """ """
        print(f"Reporting!")

    def _button_run_timer_clicked(self) -> None:
        """ """

        if self._timer is None or not self._timer.is_alive():
            self._button_run_timer.setEnabled(False)
            self._button_stop_timer.setEnabled(True)
            # create new timer and start
            self._timer = Timer(5, self._timer_callback)
            self._timer.start()
        else:
            # do not allow restart of timer
            raise SyntaxError("This should not be possible!")

    def _button_stop_timer_clicked(self) -> None:
        """ """
        if self._timer is not None and self._timer.is_alive():
            self._button_stop_timer.setEnabled(False)
            self._button_run_timer.setEnabled(True)
            self._timer.cancel()
            self._timer = None
        else:
            raise SyntaxError("This should not be possible!")

    def closeEvent(self, event: QCloseEvent) -> None:
        print("Closing event...")
        if self._timer is not None and self._timer.is_alive():
            self._timer.cancel()
        return super().closeEvent(event)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    thread_control_widget: ThreadControlWidget = ThreadControlWidget()
    thread_control_widget.show()
    sys.exit(app.exec_())
