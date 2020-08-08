import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from reto.fixtures.calculate_salaries_request import (
    REQUEST_VALID_DATA,
    REQUEST_INVALID_DATA,
    REQUEST_INVALID_LEVEL
)


class LocalTeamTestCase(APITestCase):

    def test_calculate_salaries(self):
        """calculating salaries of the resuelve fc team"""

        response = self.client.post(
            '/api/reto/calculate_salaries',
            REQUEST_VALID_DATA,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["goles_minimos"], 15)
        self.assertEqual(response.data[1]["goles_minimos"], 20)
        self.assertEqual(response.data[2]["goles_minimos"], 5)
        self.assertEqual(response.data[3]["goles_minimos"], 10)
        self.assertEqual(response.data[0]["sueldo_completo"], "67833.33")
        self.assertEqual(response.data[1]["sueldo_completo"], "130000.00")
        self.assertEqual(response.data[2]["sueldo_completo"], "30000.00")
        self.assertEqual(response.data[3]["sueldo_completo"], "42450.00")

    def test_empty_request(self):
        response = self.client.post(
            '/api/reto/calculate_salaries',
            None,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_required_fields(self):
        response = self.client.post(
            '/api/reto/calculate_salaries',
            [{}],
            format='json'
        )

        data = response.data[0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["nombre"][0], "This field is required.")
        self.assertEqual(data["nivel"][0], "This field is required.")
        self.assertEqual(data["goles"][0], "This field is required.")
        self.assertEqual(data["sueldo"][0], "This field is required.")
        self.assertEqual(data["bono"][0], "This field is required.")
        self.assertEqual(data["sueldo_completo"][0], "This field is required.")
        self.assertEqual(data["equipo"][0], "This field is required.")

    def test_invalid_data(self):
        response = self.client.post(
            '/api/reto/calculate_salaries',
            REQUEST_INVALID_DATA,
            format='json'
        )

        data = response.data[0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(data["goles"][0], "A valid integer is required.")
        self.assertEqual(data["sueldo"][0], "A valid number is required.")
        self.assertEqual(data["bono"][0], "A valid number is required.")
        self.assertEqual(data["sueldo_completo"][0],"A valid number is required.")

    def test_invalid_level(self):
        response = self.client.post(
            '/api/reto/calculate_salaries',
            REQUEST_INVALID_LEVEL,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data[0]["nivel"][0], "\"H\" is not a valid choice.")
