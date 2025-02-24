from holytools.devtools import Unittest

from filebundler.resources.interval import Interval


class TestIntervalSubtraction(Unittest):

    def test_no_overlap(self):
        a = Interval(1, 5)
        b = Interval(6, 10)
        self.assertEqual(a.subtract(b), [a])

    def test_overlap_lower(self):
        a = Interval(1, 5)
        b = Interval(0, 3)
        self.assertEqual(a.subtract(b), [Interval(3, 5)])

    def test_overlap_upper(self):
        a = Interval(1, 5)
        b = Interval(3, 6)
        self.assertEqual(a.subtract(b), [Interval(1, 3)])

    def test_overlap_inside(self):
        a = Interval(1, 5)
        b = Interval(2, 4)
        self.assertEqual(a.subtract(b), [Interval(1, 2), Interval(4, 5)])

    def test_entire_coverage(self):
        a = Interval(1, 5)
        b = Interval(0, 6)
        self.assertEqual(a.subtract(b), [])

    def test_exact_overlap(self):
        a = Interval(1, 5)
        b = Interval(1, 5)
        self.assertEqual(a.subtract(b), [])


if __name__ == '__main__':
    TestIntervalSubtraction.execute_all()
