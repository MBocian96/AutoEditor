from proglog import ProgressBarLogger


class ProgressObserver(ProgressBarLogger):
    def __init__(self, front_progress_bar):
        super().__init__()
        self.progress = front_progress_bar

    def callback(self, **changes):
        # Every time the logger is updated, this function is called with
        # the `changes` dictionnary of the form `parameter: new value`.

        for parameter, value in changes.items():
            pass