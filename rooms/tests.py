from rest_framework.test import APITestCase
from .models import Amenity


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Description"

    def setUp(self):
        Amenity.objects.create(name=self.NAME, description=self.DESC)

    def test_all_amenities(self):
        response = self.client.get("/api/v1/rooms/amenities/")
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code isn't 200.")
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)
