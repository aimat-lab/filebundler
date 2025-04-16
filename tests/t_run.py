import time

from holytools.devtools import Unittest
from kivy.clock import Clock

from filebundler.app import DataCollectApp


class TestAppLaunch(Unittest):
    def test_launch(self):
        def stop_app(*args):
            app.stop()

        Clock.schedule_once(stop_app, 5)

        app = DataCollectApp()
        app.run()

if __name__ == "__main__":
    TestAppLaunch.execute_all()