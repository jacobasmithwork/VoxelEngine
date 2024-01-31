import pygame as pg
from camera import Camera
from settings import *

#Inherits from camera class
class Player(Camera):
    def __init__(self, app, position=PLAYER_POS, yaw=-90, pitch=0):
        self.app = app
        super().__init__(position, yaw, pitch)

    #Control KBM before calling cam udpate
    def update(self):
        self.kb_control()
        self.mouse_control()
        super().update()

    #Mouse control for pitch/yaw
    def mouse_control(self):
        mouse_dx, mouse_dy = pg.mouse.get_rel()
        if mouse_dy:
            self.rotate_yaw(delta_x=mouse_dx * MOUSE_SENS)
        if mouse_dy:
            self.rotate_pitch(delta_y=mouse_dy * MOUSE_SENS)

    #Get keyboard input, calc velocity based on time
    def kb_control(self):
        key_state = pg.key.get_pressed()
        vel = PLAYER_WALKSPEED * self.app.delta_time
        #WASD for movement, Q and E for ascend/descend (for now)
        if(key_state[pg.K_w]):
            self.move_forward(vel)
        if(key_state[pg.K_a]):
            self.move_left(vel)
        if(key_state[pg.K_s]):
            self.move_backward(vel)
        if(key_state[pg.K_d]):
            self.move_right(vel)
        if(key_state[pg.K_q]):
            self.move_down(vel)
        if(key_state[pg.K_e]):
            self.move_up(vel)