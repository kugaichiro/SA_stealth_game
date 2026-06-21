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
        self.last_direction = {self.enemies[i]: random.randint(0,3) for i in range(self.num_enemies)}
        self.is_go = {self.enemies[i]: False for i in range(self.num_enemies)}
        self.next_direction = {self.enemies[i]: [] for i in range(self.num_enemies)}
        self.enemies_position = {self.enemies[i]: self.enemies_routes[self.enemies[i]][0].copy() for i in range(self.num_enemies)}
        self.enemies_direction = {self.enemies[i]: self.last_direction[self.enemies[i]] for i in range(self.num_enemies)}

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
        wall_blocks = ["01", "02", "03", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
                       "19", "20", "21", "22", "23", "24", "25", "26"]
        
        for enemy in self.enemies:
            
            #敵のルートのポイントについたら、次の方向を決める
            if self.enemies_position[enemy] in self.enemies_routes[enemy] and\
                                                                    not self.is_go[enemy]:
                self.is_go[enemy] = False
                
                self.t2[enemy] = time.time()
                if self.t2[enemy] - self.t1[enemy] >= 2:
                    routes_x = [route[0] for route in self.enemies_routes[enemy] 
                                if route != self.enemies_position[enemy]]
                    routes_y = [route[1] for route in self.enemies_routes[enemy]
                                if route != self.enemies_position[enemy]]
                    self.t1[enemy] = time.time()
                    if self.enemies_direction[enemy] == 0:
                        if self.enemies_position[enemy][0] in routes_x and\
                                self.enemies_position[enemy][1] > \
                                routes_y[routes_x.index(self.enemies_position[enemy][0])]:
                            self.next_direction[enemy].append(0)
                    elif self.enemies_direction[enemy] == 1:
                        if self.enemies_position[enemy][1] in routes_y and\
                                self.enemies_position[enemy][0] < \
                                    routes_x[routes_y.index(self.enemies_position[enemy][1])]:
                            self.next_direction[enemy].append(1)
                    elif self.enemies_direction[enemy] == 2:
                        if self.enemies_position[enemy][0] in routes_x and\
                                self.enemies_position[enemy][1] < \
                                    routes_y[routes_x.index(self.enemies_position[enemy][0])]:
                            self.next_direction[enemy].append(2)
                    elif self.enemies_direction[enemy] == 3:
                        if self.enemies_position[enemy][1] in routes_y and\
                                self.enemies_position[enemy][0] > \
                                    routes_x[routes_y.index(self.enemies_position[enemy][1])]:
                            self.next_direction[enemy].append(3)
                            
                    self.enemies_direction[enemy] = (self.enemies_direction[enemy] + 1)%4
                    if self.enemies_direction[enemy] == self.last_direction[enemy]:
                        self.enemies_direction[enemy] = \
                            self.next_direction[enemy][random.randint(0, len(self.next_direction[enemy])-1)]
                        self.is_go[enemy] = True
                            
            #敵の移動
            else:
                self.last_direction[enemy] = self.enemies_direction[enemy]
                self.t2[enemy] = time.time()
                if self.t2[enemy] - self.t1[enemy] >= 0.75:
                    if self.enemies_direction[enemy] == 0:
                        self.enemies_position[enemy][1] -= 1
                    elif self.enemies_direction[enemy] == 1:
                        self.enemies_position[enemy][0] += 1
                    elif self.enemies_direction[enemy] == 2:
                        self.enemies_position[enemy][1] += 1
                    elif self.enemies_direction[enemy] == 3:
                        self.enemies_position[enemy][0] -= 1
                    self.t1[enemy] = time.time()
                    self.next_direction[enemy] = []
                    self.is_go[enemy] = False
                    
            #プレイヤーを見つけたかどうかの判定
            wall_info_x = [i for i in range(16) if map_info[self.enemies_position[enemy][1]][2*i:2*(i+1)] in wall_blocks]
            wall_info_y = [i for i in range(12) 
                          if map_info[i][2*self.enemies_position[enemy][0]:2*(self.enemies_position[enemy][0]+1)] in wall_blocks]
            if self.enemies_direction[enemy] == 0:
                near_wall = 0
                for wall_y in wall_info_y:
                    if self.enemies_position[enemy][1] >= wall_y >= near_wall:
                        near_wall = wall_y
                if self.enemies_position[enemy][0] == player_square_x and\
                        self.enemies_position[enemy][1] >= player_square_y >= near_wall:
                    print("found")
                    self.is_found_player = True
            elif self.enemies_direction[enemy] == 1:
                near_wall = 15
                for wall_x in wall_info_x:
                    if self.enemies_position[enemy][0] <= wall_x <= near_wall:
                        near_wall = wall_x
                if self.enemies_position[enemy][1] == player_square_y and\
                        self.enemies_position[enemy][0] <= player_square_x <= near_wall:
                    print("found")
                    self.is_found_player = True
            elif self.enemies_direction[enemy] == 2:
                near_wall = 11
                for wall_y in wall_info_y:
                    if self.enemies_position[enemy][1] <= wall_y <= near_wall:
                        near_wall = wall_y
                if self.enemies_position[enemy][0] == player_square_x and\
                        self.enemies_position[enemy][1] <= player_square_y <= near_wall:
                    print("found")
                    self.is_found_player = True
            elif self.enemies_direction[enemy] == 3:
                near_wall = 0
                for wall_x in wall_info_x:
                    if self.enemies_position[enemy][0] >= wall_x >= near_wall:
                        near_wall = wall_x
                if self.enemies_position[enemy][1] == player_square_y and\
                        self.enemies_position[enemy][0] >= player_square_x >= near_wall:
                    print("found")
                    self.is_found_player = True
                    
        