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
    def __init__(self,app,pos,scale,rot) -> None:
        self.app = app
        self.ctx = app.ctx
        self.position_cube = self.get_position_cube()
        self.pos = pos
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1,0,0)
        self.forward = glm.vec3(0,0,-1)
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.vbo = self.ctx.buffer(self.position_cube)
        self.program = self.get_program('default')
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '2f 3f', 'in_texcoord_0','in_position')])
        self.m_model = self.get_model_matrix()
        self.speed = 0.5
        self.texture = self.get_texture(path='obstacle_3D.png')
        self.on_init()

    def move(self):
        velocity = self.speed * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.pos += self.forward * velocity
        if keys[pg.K_s]:
            self.pos -= self.forward * velocity
        if keys[pg.K_a]:
            self.pos -= self.right * velocity
        if keys[pg.K_d]:
            self.pos += self.right * velocity
        if keys[pg.K_q]:
            self.pos += self.up * velocity
        if keys[pg.K_e]:
            self.pos -= self.up * velocity

    def get_texture(self,path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    def update(self):
        m_model = glm.rotate(self.m_model, self.app.time*0.5, glm.vec3(0, 1, 0))
        self.program['m_model'].write(m_model)
        self.program['m_view'].write(self.app.camera.m_view)
        self.move()

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def on_init(self):
        self.program['u_texture_0'] = 0
        self.texture.use()
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
        vertex_data = self.get_data(vertices, indices)
        tex_coord = [(0,0), (1,0) ,(1,1) ,(0,1)]
        tex_coord_indices = [(0,2,3), (0,1,2), (0,2,3), (0,1,2), (0,1,2), (2,3,0), (2,3,0), (2,0,1), (0,2,3), (0,1,2), (3,1,2), (3,0,1)]
        tex_coord_data = self.get_data(tex_coord, tex_coord_indices)
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

    def get_data(self, vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data,dtype='f4')

    def get_program(self, shader_name):
        with open(f'{shader_name}.vert') as file:
            vertex_shader = file.read()
        with open(f'{shader_name}.frag') as file:
            fragment_shader = file.read()
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

