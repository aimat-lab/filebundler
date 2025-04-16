from holytools.devtools import Unittest

from filebundler.resources.interval import Interval


class TestIntervalSubtraction(Unittest):

    def test_no_overlap(self):
        a = Interval(1, 5)
        b = Interval(6, 10)

        diff = a.subtract(b)
        print(diff)

        self.assertTrue(len(diff) == 1)
        i1 = a.subtract(b)[0]
        self.assertTrue(i1 == Interval(1, 5))

    def test_overlap_lower(self):
        a = Interval(1, 5)
        b = Interval(0, 3)

        diff = a.subtract(b)
        print(diff)
        self.assertTrue(len(diff) == 1)
        i1 = a.subtract(b)[0]
        self.assertTrue(i1 == Interval(3, 5))

    def test_overlap_upper(self):
        a = Interval(1, 5)
        b = Interval(3, 6)

        i1 = a.subtract(b)[0]
        self.assertTrue(len(a.subtract(b)) == 1)
        self.assertTrue(i1 == Interval(1, 3))

    def test_overlap_inside(self):
        a = Interval(1, 5)
        b = Interval(2, 4)

        intervals = a.subtract(b)
        print(f'{intervals}')

        self.assertTrue(len(intervals) == 2)
        i1, i2 = intervals[0], intervals[1]
        self.assertTrue(i1 == Interval(1, 2))
        self.assertTrue(i2 == Interval(4, 5))

    def test_entire_coverage(self):
        a = Interval(1, 5)
        b = Interval(0, 6)
        self.assertTrue(len(a.subtract(b)) == 0)


    def test_exact_overlap(self):
        a = Interval(1, 5)
        b = Interval(1, 5)

        diff = a.subtract(b)
        print(diff)
        self.assertTrue(len(diff) == 0)


if __name__ == '__main__':
    TestIntervalSubtraction.execute_all()
