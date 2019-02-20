from django.test import TestCase
from views import vista


class TestCatalogo(TestCase):

    def test_smoke(self):
        self.assertEquals(2, 1+1)

    def test_catalgo(self):
        self.assertFalse(False)

    def test_cuando_es_true(self):
        self.assertEquals('Es True', vista(True))

    def test_cuando_es_false(self):
        self.assertEquals('Es False', vista(False))
