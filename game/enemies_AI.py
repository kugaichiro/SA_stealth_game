import time
import random

try:
    from prototype.model.load_data import LoadData
except ModuleNotFoundError:
    from model.load_data import LoadData


class EnemiesAI(object):
    
    """
    敵の動きを制御するクラス
    """

    def __init__(self):
        self.enemies_routes = None
        self.enemies = []
        self.num_enemies = 0
        self.enemies_position = {}
        self.enemies_direction = {}
        self.t1 = {}
        self.t2 = {}
        self.is_found_player = False
        self.last_direction = {}
        self.next_direction = {}
        self.is_go = {}

    def setup_routes(self, enemies_route: dict):
        self.enemies_routes = enemies_route
        self.enemies = list(enemies_route.keys())
        self.num_enemies = len(self.enemies)
        self.t1 = {self.enemies[i]: time.time() for i in range(self.num_enemies)}
        self.last_direction = {self.enemies[i]: 0 for i in range(self.num_enemies)}
        self.is_go = {self.enemies[i]: False for i in range(self.num_enemies)}
        self.next_direction = {self.enemies[i]: [] for i in range(self.num_enemies)}
        self.enemies_position = {self.enemies[i]: self.enemies_routes[self.enemies[i]][0].copy() for i in range(self.num_enemies)}
        self.enemies_direction = {self.enemies[i]: 0 for i in range(self.num_enemies)}

    def move_enemy(self, player_square_x, player_square_y, map_info):
        
        """"
        この関数では、敵の動きの制御を行う
        この関数は、繰り返し処理の中で呼び出されることを前提にしている
        敵の動き:
            まず、四方向を見て、自分のルートのポイントがあるかを確認し、次の方向の候補を作る
            確認出来たら、その中からランダムに方向を選び、その方向に進む
            次のポインタについたら、また同じ動作を繰り返す
            もしその制御の中で、プレイヤーを見つけたら、is_found_playerをTrueにする
        """
        wall_blocks = [1, 2, 3, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19]
        
        for enemy in range(self.num_enemies):
            if self.enemies_position[self.enemies[enemy]] in self.enemies_routes[self.enemies[enemy]] and\
                                                                    not self.is_go[self.enemies[enemy]]:
                self.is_go[self.enemies[enemy]] = False
                self.t2[self.enemies[enemy]] = time.time()
                if self.t2[self.enemies[enemy]] - self.t1[self.enemies[enemy]] >= 2:
                    self.enemies_direction[self.enemies[enemy]] = (self.enemies_direction[self.enemies[enemy]] + 1)%4
                    
                    if self.enemies_direction[self.enemies[enemy]] == self.last_direction[self.enemies[enemy]]:
                        self.enemies_direction[self.enemies[enemy]] = \
                            self.next_direction[self.enemies[enemy]][random.randint(0, len(self.next_direction[self.enemies[enemy]])-1)]
                        self.is_go[self.enemies[enemy]] = True
                        
                    routes_x = [route[0] for route in self.enemies_routes[self.enemies[enemy]] 
                                if route != self.enemies_position[self.enemies[enemy]]]
                    routes_y = [route[1] for route in self.enemies_routes[self.enemies[enemy]]
                                if route != self.enemies_position[self.enemies[enemy]]]
                    self.t1[self.enemies[enemy]] = time.time()
                    if self.enemies_direction[self.enemies[enemy]] == 0:
                        if self.enemies_position[self.enemies[enemy]][0] in routes_x and\
                                self.enemies_position[self.enemies[enemy]][1] > \
                                routes_y[routes_x.index(self.enemies_position[self.enemies[enemy]][0])]:
                            self.next_direction[self.enemies[enemy]].append(0)
                    elif self.enemies_direction[self.enemies[enemy]] == 1:
                        if self.enemies_position[self.enemies[enemy]][1] in routes_y and\
                                self.enemies_position[self.enemies[enemy]][0] < \
                                    routes_x[routes_y.index(self.enemies_position[self.enemies[enemy]][1])]:
                            self.next_direction[self.enemies[enemy]].append(1)
                    elif self.enemies_direction[self.enemies[enemy]] == 2:
                        if self.enemies_position[self.enemies[enemy]][0] in routes_x and\
                                self.enemies_position[self.enemies[enemy]][1] < \
                                    routes_y[routes_x.index(self.enemies_position[self.enemies[enemy]][0])]:
                            self.next_direction[self.enemies[enemy]].append(2)
                    elif self.enemies_direction[self.enemies[enemy]] == 3:
                        if self.enemies_position[self.enemies[enemy]][1] in routes_y and\
                                self.enemies_position[self.enemies[enemy]][0] > \
                                    routes_x[routes_y.index(self.enemies_position[self.enemies[enemy]][1])]:
                            self.next_direction[self.enemies[enemy]].append(3)
            
            else:
                self.last_direction[self.enemies[enemy]] = self.enemies_direction[self.enemies[enemy]]
                self.t2[self.enemies[enemy]] = time.time()
                if self.t2[self.enemies[enemy]] - self.t1[self.enemies[enemy]] >= 0.75:
                    if self.enemies_direction[self.enemies[enemy]] == 0:
                        self.enemies_position[self.enemies[enemy]][1] -= 1
                    elif self.enemies_direction[self.enemies[enemy]] == 1:
                        self.enemies_position[self.enemies[enemy]][0] += 1
                    elif self.enemies_direction[self.enemies[enemy]] == 2:
                        self.enemies_position[self.enemies[enemy]][1] += 1
                    elif self.enemies_direction[self.enemies[enemy]] == 3:
                        self.enemies_position[self.enemies[enemy]][0] -= 1
                    self.t1[self.enemies[enemy]] = time.time()
                    self.next_direction[self.enemies[enemy]] = []
                    self.is_go[self.enemies[enemy]] = False
                    
            if self.enemies_direction[self.enemies[enemy]] == 0:
                map_info_x = [map_info[self.enemies_position[self.enemies[enemy]][1]-1][2*i:2*(i+1)] 
                              for i in range(self.enemies_position[self.enemies[enemy]][0]+1)]
                
                if self.enemies_position[self.enemies[enemy]][0] == player_square_x and\
                        self.enemies_position[self.enemies[enemy]][1] >= player_square_y: #and\
                    """not(map_info_x in wall_blocks):"""
                    print("found")
                    self.is_found_player = True
            elif self.enemies_direction[self.enemies[enemy]] == 1:
                if self.enemies_position[self.enemies[enemy]][1] == player_square_y and\
                        self.enemies_position[self.enemies[enemy]][0] <= player_square_x:
                    print("found")
                    self.is_found_player = True
            elif self.enemies_direction[self.enemies[enemy]] == 2:
                if self.enemies_position[self.enemies[enemy]][0] == player_square_x and\
                        self.enemies_position[self.enemies[enemy]][1] <= player_square_y:
                    print("found")
                    self.is_found_player = True
            elif self.enemies_direction[self.enemies[enemy]] == 3:
                if self.enemies_position[self.enemies[enemy]][1] == player_square_y and\
                        self.enemies_position[self.enemies[enemy]][0] >= player_square_x:
                    print("found")
                    self.is_found_player = True
                
                    """not(map_info[self.enemies_position[self.enemies[enemy]][1]]
                            [:2*self.enemies_position[self.enemies[enemy]]] in wall_blocks):"""
                    
        