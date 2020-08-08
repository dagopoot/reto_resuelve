from rest_framework import serializers

from .settings import LEVEL_TYPES


class TeamSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)
    nivel = serializers.ChoiceField(LEVEL_TYPES, required=True)
    goles = serializers.IntegerField(required=True)
    sueldo = serializers.DecimalField(
        max_digits=11,
        decimal_places=2,
        required=True
    )
    bono = serializers.DecimalField(
        max_digits=11,
        decimal_places=2,
        required=True
    )
    sueldo_completo = serializers.DecimalField(
        max_digits=11,
        decimal_places=2,
        allow_null=True
    )
    equipo = serializers.CharField(required=True)


class TeamSalariesSerializer(serializers.Serializer):
    nombre = serializers.CharField(required=True)
    goles_minimos = serializers.IntegerField(required=True)
    goles = serializers.IntegerField(required=True)
    sueldo = serializers.DecimalField(
        max_digits=11,
        decimal_places=2,
        required=True
    )
    bono = serializers.DecimalField(
        max_digits=11,
        decimal_places=2,
        required=True
    )
    sueldo_completo = serializers.DecimalField(
        max_digits=11,
        decimal_places=2,
        required=True
    )
    equipo = serializers.CharField(required=True)


class GoalSerializer(serializers.Serializer):
    equipo = serializers.CharField(required=True)
    A = serializers.IntegerField(required=True)
    B = serializers.IntegerField(required=True)
    C = serializers.IntegerField(required=True)
    Cuauh = serializers.IntegerField(required=True)


class OtherTeamsSerializer(serializers.Serializer):
    jugadores = TeamSerializer(many=True, required=True)
    niveles = GoalSerializer(many=True, required=True)

    def validate(self, data):
        players = data.get('jugadores', [])
        levels = data.get('niveles', [])

        if len(players) == 0:
            raise serializers.ValidationError(
                {'jugadores': 'At least one player is required.'})

        if len(levels) == 0:
            raise serializers.ValidationError(
                {'niveles': 'At least one level is required.'})

        if len(levels) > 0 and len(players) > 0:
            levels = [level["equipo"] for level in levels]

            for player in players:
                team = player["equipo"]

                if team not in levels:
                    error = f"Provide levels for \"{team}\" team."
                    message = {'niveles': error}

                    raise serializers.ValidationError(message)

        return data
