import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_shader = """
#version 330
in vec4 position;
void main()
{
    gl_Position = position;
}
"""

fragment_shader = """
#version 330
out vec4 fragColor;
void main()
{
    fragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

def draw_triangle():
    program = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    glUseProgram(program)
    vertices = [-0.5, -0.5, 0.0, 1.0, 0.5, -0.5, 0.0, 1.0, 0.0, 0.5, 0.0, 1.0]
    vertices = np.array(vertices, dtype=np.float32)
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    position = glGetAttribLocation(program, 'position')
    glEnableVertexAttribArray(position)
    glVertexAttribPointer(position, 4, GL_FLOAT, GL_FALSE, 0, None)
    glDrawArrays(GL_TRIANGLES, 0, 3)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-1, 1, -1, 1, -1, 1)  # gluOrtho2D 대신 glOrtho 사용
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
