from django.test import TestCase


class TestCatalogo(TestCase):

    def test_smoke(self):
        self.assertEquals(2, 1+1)

    def test_catalgo(self):
        self.assertFalse(False)
