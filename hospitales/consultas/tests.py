from django.test import TestCase


class TestConsulta(TestCase):

    def test_humo(self):
        self.assertEquals(2, 1+1)

    def test_consulta(self):
        self.assertFalse(False)
