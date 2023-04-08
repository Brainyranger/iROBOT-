import pygame as pg
import moderngl as mgl
import sys
import numpy as np
from camera import Camera
import time


class GraphicsEngine:
    def __init__(self, win_size=(540, 400)):
        # init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.temps = time.time()
        self.camera = Camera(self)
        #scene
        self.scene = Cube(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #render scene
        self.scene.render()
        # swap buffers
        pg.display.flip()

    def run(self):
        while True:
            self.temps = time.time() - self.temps
            self.check_events()
            self.render()
            self.clock.tick(60)

class Triangle:
    def __init__(self,app) -> None:
        self.app = app
        self.ctx = app.ctx
        self.position_triangle = [(-0.6, -0.8, 0.0),(0.6, -0.8, 0.0), (0.0, 0.8, 0.0)]
        self.position_triangle = np.array(self.position_triangle, dtype='f4')
        self.vbo = self.ctx.buffer(self.position_triangle)
        self.program = self.get_program('default')
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '3f', 'in_position')])

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()

    def get_program(self, shader_name):
        with open(f'{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'{shader_name}.frag') as file:
            fragment_shader = file.read()
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program
    
class Cube:
    def __init__(self,app) -> None:
        self.app = app
        self.ctx = app.ctx
        self.position_cube = self.get_position_cube()
        self.vbo = self.ctx.buffer(self.position_cube)
        self.program = self.get_program('default')
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '3f', 'in_position')])
        self.on_init()

    def on_init(self):
        self.program['m_proj'].write(self.app.camera.m_proj)
        #self.program['m_view'].write(self.app.camera.m_view)

    def render(self):
        self.vao.render()

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()

    def get_position_cube(self):
        vertices = [(-1,-1,1),(1, -1, 1),(1, 1, 1),(-1, 1, 1),(-1, 1, -1),(-1, -1, -1),(1, -1, -1),(1, 1, -1)]
        indices = [(0,2,3), (0,1,2), (1,7,2), (1,6,7), (6,5,4), (4,7,6), (3,4,5), (3,5,0), (3,7,4), (3,2,7), (0,6,1), (0,5,6)]
        data = [vertices[ind]for triangle in indices for ind in triangle]
        vertex_data = np.array(data, dtype='f4')
        return vertex_data

    def get_program(self, shader_name):
        with open(f'{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'{shader_name}.frag') as file:
            fragment_shader = file.read()
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()

