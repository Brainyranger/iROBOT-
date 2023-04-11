import pygame as pg
import moderngl as mgl
import glm
import sys
import numpy as np


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
        self.m_model = self.get_model_matrix()
        self.on_init()

    def update(self):
        m_model = glm.rotate(self.m_model, self.app.time, glm.vec3(0, 1, 0))
        self.program['m_model'].write(m_model)

    def get_model_matrix(self):
        m_model = glm.mat4()
        return m_model

    def on_init(self):
        self.program['m_proj'].write(self.app.camera.m_proj)
        self.program['m_view'].write(self.app.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def render(self):
        self.update()
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

