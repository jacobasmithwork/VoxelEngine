from numba import njit
import numpy as np
import glm
import math

#Screen Resolution
SCRN_RES = glm.vec2(1920, 1080)

#Colors
BG_COLOR = glm.vec3(0.1, 0.11, 0.28)

#Camera specs
ASPECT_RATIO = SCRN_RES.x / SCRN_RES.y
FOV_DEG = 60
V_FOV = glm.radians(FOV_DEG) #Vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO) # Horizontal FOV (i do not understand the math on this one, from tutorial)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89) #How far up and down player can look

#Player
PLAYER_WALKSPEED = 0.005
PLAYER_ROTATION_SPEED = 0.003
PLAYER_POS = glm.vec3(0,0,1)
MOUSE_SENS = 0.002
