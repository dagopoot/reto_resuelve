from decimal import Decimal

from .settings import RESUELVE_FC_LEVELS


class Salary:
    def __init__(self, players, levels=[]):
        self._players = players
        self._levels = levels

        self._goal_team = {}
        self._level_team = {}

    def calculate_salaries(self):
        try:
            self._proccess_info()

            return self._get_salaries()

        except Exception as ex:
            raise ex

    def _proccess_info(self):
        self._process_levels()
        self._process_players()

    def _process_levels(self):
        self._level_team = {level["equipo"]: level for level in self._levels}

    def _process_players(self):
        for player in self._players:
            team = player["equipo"]

            if team not in self._goal_team:
                self._goal_team[team] = {}
                self._goal_team[team]["goal"] = 0
                self._goal_team[team]["reached"] = 0

            self._goal_team[team]["reached"] += player["goles"]
            self._goal_team[team]["goal"] += self._get_goal_level(
                team,
                player["nivel"]
            )

    def _get_goal_level(self, team, level):
        if team in self._level_team:
            return self._level_team[team][level]

        return RESUELVE_FC_LEVELS[level]

    def _get_salaries(self):
        team = []

        for player in self._players:
            player["goles_minimos"] = self._get_goal_level(
                player["equipo"],
                player["nivel"]
            )

            player["sueldo_completo"] = self._calculate_salary(player)

            team.append(player)

        return team

    def _calculate_salary(self, player):
        team = player["equipo"]
        bonus = Decimal(player["bono"])
        base_salary = Decimal(player["sueldo"])

        team_goal = self._goal_team[team]["goal"]
        team_goal_achieved = self._goal_team[team]["reached"]

        individual_goal = self._get_goal_level(team, player["nivel"])

        player_percentage = self._get_percentage(
            individual_goal,
            player["goles"]
        )

        team_percentage = self._get_percentage(
            team_goal,
            team_goal_achieved
        )

        team_bonus = Decimal(0.5) * bonus * team_percentage
        individual_bonus = Decimal(0.5) * bonus * player_percentage

        return base_salary + team_bonus + individual_bonus

    def _get_percentage(self, goal, achieved):
        goal = Decimal(goal)
        achieved = Decimal(achieved)

        if goal > 0 and achieved < goal:
            return achieved/goal

        return 1
