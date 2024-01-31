from settings import *

#Class for handling shaders
class Shaders:
    #init app with context
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.player = app.player
        #====Shaders====#
        self.quad = self.get_program(shader_name='quad')
        #===============#
        self.set_uniforms_on_init()

    #Open shader frag and vert files associated with the shader name
    def get_program(self, shader_name):
        with open(f'shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()
        
        with open(f'shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()
        #assign program with the vert and frag shaders
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader = fragment_shader)
        return program
    
    #Pass player matrix and identity model matrix
    def set_uniforms_on_init(self):
        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

    #pass view matrix for update
    def update(self):
        self.quad['m_view'].write(self.player.m_view)