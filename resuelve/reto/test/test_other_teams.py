import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from reto.fixtures.calculate_salaries_bonus_request import (
    REQUEST_VALID_DATA,
    REQUEST_EMPTY_LEVELS,
    REQUEST_EMPTY_PLAYERS,
    REQUEST_PLAYER_INFO_NOT_PROVIDED,
    REQUEST_TEAM_NOT_PROVIDED
)


class OtherTeamsTestCase(APITestCase):

    def test_calculate_salaries(self):
        """Test api calculate salaries for other teams"""

        response = self.client.post(
            '/api/reto/calculate_salaries_bonus', REQUEST_VALID_DATA, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["goles_minimos"], 15)
        self.assertEqual(response.data[1]["goles_minimos"], 60)
        self.assertEqual(response.data[2]["goles_minimos"], 6)
        self.assertEqual(response.data[3]["goles_minimos"], 12)
        self.assertEqual(response.data[0]["sueldo_completo"], "58333.33")
        self.assertEqual(response.data[1]["sueldo_completo"], "115000.00")
        self.assertEqual(response.data[2]["sueldo_completo"], "25000.00")
        self.assertEqual(response.data[3]["sueldo_completo"], "35000.00")

    def test_empty_request(self):
        response = self.client.post(
            '/api/reto/calculate_salaries_bonus',
            None,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_data(self):
        response = self.client.post(
            '/api/reto/calculate_salaries_bonus',
            [{}],
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_players(self):
        response = self.client.post(
            '/api/reto/calculate_salaries_bonus',
            REQUEST_EMPTY_PLAYERS,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data["jugadores"][0], "At least one player is required.")

    def test_empty_levels(self):
        response = self.client.post(
            '/api/reto/calculate_salaries_bonus',
            REQUEST_EMPTY_LEVELS,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["niveles"][0], "At least one level is required.")

    def test_required_fields(self):
        response = self.client.post(
            '/api/reto/calculate_salaries_bonus',
            REQUEST_PLAYER_INFO_NOT_PROVIDED,
            format='json'
        )

        player = response.data["jugadores"][0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(player["nombre"][0], "This field is required.")
        self.assertEqual(player["nivel"][0], "This field is required.")
        self.assertEqual(player["goles"][0], "This field is required.")
        self.assertEqual(player["sueldo"][0], "This field is required.")
        self.assertEqual(player["bono"][0], "This field is required.")
        self.assertEqual(player["sueldo_completo"][0], "This field is required.")
        self.assertEqual(player["equipo"][0], "This field is required.")

    def test_team_not_provided(self):
        response = self.client.post(
            '/api/reto/calculate_salaries_bonus',
            REQUEST_TEAM_NOT_PROVIDED,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["niveles"][0], "Provide levels for \"verde\" team.")
