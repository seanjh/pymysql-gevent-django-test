from django.test import TestCase


class SimpleTest(TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertTrue(False)
