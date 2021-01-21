from PySide2.QtCore import QThread
from PySide2.QtWidgets import QWidget, QFileDialog

from src.movie_maker.archive_composer import Compositor
from . import set_ui
from .bar_logger import ProgressObserver


class Renderer(QThread):
    def __init__(self, clip, alg, size, archive_name, proglogger):
        super().__init__()
        self.archive_name = archive_name
        self.proglogger = proglogger
        self.clip = clip
        self.alg = alg
        self.size = size

    def run(self) -> None:
        compositor = Compositor(clip=self.clip,
                                alg=self.alg,
                                size=self.size)
        compositor.write(f'#Archiwum - {self.archive_name}', logger=self.proglogger)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        set_ui(self)
        self.archive_path = ''

    def render_video(self):
        archive_name = self.get_clear_video_name(self.archive_path[0])
        proglogger = ProgressObserver(self.text)
        worker = Renderer(clip=self.archive_path[0],
                          alg='bicubic',
                          size=None,
                          archive_name=f'#Archiwum - {archive_name}',
                          proglogger=proglogger)
        worker.start()

    def get_clear_video_name(self, path: str) -> str:
        last_slash_index = path.rfind('/')
        return path[last_slash_index + 1:]

    def get_file(self):
        self.archive_path = QFileDialog.getOpenFileName(self, 'Wybierz Archiwum', '',
                                                        "Video files (*.mp4)")
