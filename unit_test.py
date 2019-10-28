import unittest

from app import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_with_name_only(self):
        response = self.app.get('/search_gene/brc')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_with_both_name_and_species(self):
        resp = self.app.get(path='/search_gene/brc/homo_sapiens/')
        self.assertEqual(resp.status_code, 200)


    def test_with_both_name_and_species_2(self):
        response = self.app.get('/search_gene/samuel/drosophila_melanogaster')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)


if __name__ == "__main__":
    unittest.main()