# coding=utf-8
import unittest
import pymapia


class PyMapiaTests(unittest.TestCase):
    wikimapia = None

    def setUp(self):
        self.wikimapia = pymapia.PyMapia(open('WIKIMAPIA_API_KEY').read().strip())

    def test_get_place_by_id_simple(self):
        id_ = 55
        result = self.wikimapia.get_place_by_id(id_)

        self.assertIn('object_type', result)
        self.assertIn('location', result)
        self.assertIn('availableLanguages', result)
        self.assertIn('id', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['object_type'], int)
        self.assertIsInstance(result['location'], dict)
        self.assertIsInstance(result['availableLanguages'], dict)

        self.assertIs(result['id'], id_)

    def test_get_place_by_area_simple(self):
        result = self.wikimapia.get_place_by_area(bbox={'lon_min': 2.292493, 'lat_min': 48.8590143,
                                                        'lon_max': 2.293493, 'lat_max': 48.8599143})

        self.assertIn('count', result)
        self.assertIn('found', result)
        self.assertIn('places', result)
        self.assertIn('language', result)
        self.assertIn('page', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['count'], unicode)
        self.assertIsInstance(result['found'], unicode)
        self.assertIsInstance(result['places'], list)
        self.assertIsInstance(result['language'], unicode)
        self.assertIsInstance(result['page'], unicode)

    def test_get_nearest_place_simple(self):
        result = self.wikimapia.get_nearest_place(48.858252, 2.29451)

        self.assertIn('language', result)
        self.assertIn('places', result)
        self.assertIn('count', result)
        self.assertIn('found', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['language'], unicode)
        self.assertIsInstance(result['places'], list)
        self.assertIsInstance(result['count'], int)
        self.assertIsInstance(result['found'], int)

    def test_search_place_simple(self):
        result = self.wikimapia.search_place('eiffel', 48.858252, 2.29451)

        self.assertIn('count', result)
        self.assertIn('found', result)
        self.assertIn('places', result)
        self.assertIn('language', result)
        self.assertIn('page', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['count'], int)
        self.assertIsInstance(result['found'], unicode)
        self.assertIsInstance(result['places'], list)
        self.assertIsInstance(result['language'], unicode)
        self.assertIsInstance(result['page'], int)

    def test_get_street_by_id_simple(self):
        id_ = 10
        result = self.wikimapia.get_street_by_id(id_)

        self.assertIn('object_type', result)
        self.assertIn('location', result)
        self.assertIn('availableLanguages', result)
        self.assertIn('id', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['object_type'], int)
        self.assertIsInstance(result['location'], dict)
        self.assertIsInstance(result['availableLanguages'], dict)

        self.assertIs(result['id'], id_)

    def test_get_category_by_id(self):
        id_ = 203
        result = self.wikimapia.get_category_by_id(id_, 'en')

        self.assertIn('category', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['category'], dict)

        self.assertIn('description', result['category'])
        self.assertIn('synonyms', result['category'])
        self.assertIn('amount', result['category'])
        self.assertIn('icon', result['category'])
        self.assertIn('id', result['category'])
        self.assertIn('name', result['category'])

        self.assertIsInstance(result['category']['description'], unicode)
        self.assertIsInstance(result['category']['synonyms'], list)
        self.assertIsInstance(result['category']['amount'], int)
        self.assertIsInstance(result['category']['icon'], unicode)
        self.assertIsInstance(result['category']['id'], int)
        self.assertIsInstance(result['category']['name'], unicode)

        self.assertIs(result['category']['id'], id_)

    def test_get_all_categories_simple(self):
        result = self.wikimapia.get_all_categories()

        self.assertIn('count', result)
        self.assertIn('found', result)
        self.assertIn('page', result)
        self.assertIn('categories', result)

        self.assertNotIn('debug', result)

        self.assertIsInstance(result['count'], int)
        self.assertIsInstance(result['found'], int)
        self.assertIsInstance(result['page'], int)
        self.assertIsInstance(result['categories'], list)

if __name__ == '__main__':
    unittest.main()



