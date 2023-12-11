try:
    from prototype.model.load_data import LoadData
except ModuleNotFoundError:
    from ..model.load_data import LoadData


class EnemiesAI(object):

    def __init__(self):
        self.enemies_routes = None
        self.enemies_position = {}

    def setup_routes(self, enemies_route: dict):
        self.enemies_routes = enemies_route
        self.enemies = enemies_route.keys()
        self.num_enemies = len(self.enemies)
        self.enemies_position = {self.enemies[i]: self.enemies_routes[self.enemies[i]][0] for i in range(self.num_enemies)}

    def move_enemy(self):

        pass
        
        
