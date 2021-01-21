from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QPushButton, QProgressBar, QLabel


def set_ui(window):
    layout = QVBoxLayout()
    window.resize(500, 100)
    window.setWindowTitle('AutoMontażysta')
    window.setWindowIcon(QIcon('styk_logo.png'))
    # buttons
    window.choose_clip_button = QPushButton('Wybierz plik do którego dodać intro')
    window.render_button = QPushButton('Renderuj')

    # progress bar
    # window.progress = QProgressBar(window)
    # window.progress.setGeometry(0, 0, 400, 30)
    # window.progress.setMaximum(100)

    # label
    window.text = QLabel()
    window.text.setText('Progress bar')

    # setting layout
    layout.addWidget(window.choose_clip_button)
    layout.addWidget(window.render_button)
    # layout.addWidget(window.progress)
    layout.addWidget(window.text)

    window.setLayout(layout)
    window.choose_clip_button.clicked.connect(window.get_file)
    window.render_button.clicked.connect(window.render_video)
