from filebundler.configs import set_configs
set_configs()

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

from kivy.modules import inspector
from filebundler.app import DataCollectApp
# -------------------------------------------


def main():
    win_test_dir = 'C:\\Users\\daniel\\OneDrive\\Desktop\\test_folder'
    win_target_test = 'C:\\Users\\daniel\\OneDrive\\Desktop'

    linux_input_test = '/home/daniel/testdir/sourcefiles'
    linux_target_test = '/home/daniel/testdir'


    _, __ = win_test_dir, win_target_test
    _, __ = linux_input_test, linux_target_test

    app = DataCollectApp(override_input_folder=linux_target_test,
                         override_target_folder=linux_target_test)
    inspector.create_inspector(Window, app)

    app.run()

main()