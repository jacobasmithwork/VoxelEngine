from numpy.core.multiarray import array as array
from settings import *
from meshes.base_mesh import BaseMesh


class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.quad

        #Define data format (3 floats for vertex coords, 3 floats for vertex color)
        self.vbo_format = '3f 3f'
        self.attrs = ('in_position', 'in_color')
        self.vao = self.get_vao()


    def get_vertex_data(self):
        #According to OpenGL specs: Two triangles with counter-clockwise vertex traversal
        verts = [
            (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0)
        ]
        #Gives verts colors
        colors = [
            (0,1,0),(1,0,0),(1,1,0),
            (0,1,0),(1,1,0),(0,0,1)
        ]
        #Join lists into one array with numpy
        vertex_data = np.hstack([verts, colors], dtype='float32')
        return vertex_data