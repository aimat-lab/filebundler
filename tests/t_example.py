import time

from holytools.devtools import Unittest
from filebundler.app import DataCollectApp


class TestAppLaunch(Unittest):
    def test_launch(self):
        app = DataCollectApp()
        app.run()
        time.sleep(20)

if __name__ == "__main__":
    TestAppLaunch.execute_all()