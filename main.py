from settings import *
import moderngl as mgl
import pygame as pg
import sys
from shader import Shaders
from scene import Scene
from player import Player


class VoxelEngine:
    def __init__(self):
        #initialize pygame and its attributes
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        #Set window resolution and create the OpenGL context
        pg.display.set_mode(SCRN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        #Enable fragment depth testing (handles unseen polys and garbage collection)
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        #Set game clock
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        #To stick cursor in middle of window
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_running = True
        #run on init processes
        self.on_init()

    def on_init(self):
        #init player
        self.player = Player(self)
        #init shaders
        self.shader_program = Shaders(self)
        #init scene
        self.scene = Scene(self)

    def update(self):
        #Update Player
        self.player.update()
        #Update shaders
        self.shader_program.update()
        #Update scene render
        self.scene.update()
        #Must update time + time delta
        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def render(self):
        #Clear frame and depth buffers and display new frame
        self.ctx.clear(color=BG_COLOR)
        #Render scene
        self.scene.render()
        pg.display.flip()
    
    def handle_events(self):
        #Look through events for pressing escape key or quitting to know when to pause game
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        #While running, check events, update and render. Otherwise, close
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = VoxelEngine()
    app.run()