from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import (
    OtherTeamsSerializer,
    TeamSalariesSerializer,
    TeamSerializer
)

from .salary import Salary


@api_view(['POST'])
def calculate_salaries(request):
    serializer = TeamSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    try:
        salary = Salary(serializer.data)

        players = salary.calculate_salaries()

        salaries = TeamSalariesSerializer(players, many=True)

        return Response(salaries.data, status=status.HTTP_200_OK)

    except Exception as ex:
        response = {
            "message": f"Error al calcular los salarios, error: {ex}"}

        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def calculate_salaries_bonus(request):
    serializer = OtherTeamsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        salary = Salary(
            serializer.data["jugadores"], serializer.data["niveles"])

        players = salary.calculate_salaries()

        salaries = TeamSalariesSerializer(players, many=True)

        return Response(salaries.data, status=status.HTTP_200_OK)

    except Exception as ex:
        response = {
            "message": f"Error al calcular los salarios, error: {ex}"}

        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
