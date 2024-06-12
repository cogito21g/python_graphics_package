import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

vertex_shader = """
#version 330
in vec4 position;
uniform mat4 projection;
void main()
{
    gl_Position = projection * position;
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

def draw_triangle(program, vao):
    glBindVertexArray(vao)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glBindVertexArray(0)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    program = compileProgram(
        compileShader(vertex_shader, GL_VERTEX_SHADER),
        compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    )
    
    glUseProgram(program)
    
    # 투영 행렬 설정
    projection = np.array([
        [2/display[0], 0, 0, 0],
        [0, 2/display[1], 0, 0],
        [0, 0, -1, 0],
        [-1, -1, 0, 1]
    ], dtype=np.float32)
    
    projection_location = glGetUniformLocation(program, "projection")
    glUniformMatrix4fv(projection_location, 1, GL_FALSE, projection)
    
    # VAO 생성 및 바인딩
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)
    
    # VBO 생성 및 설정
    vertices = [-0.5, -0.5, 0.0, 1.0, 0.5, -0.5, 0.0, 1.0, 0.0, 0.5, 0.0, 1.0]
    vertices = np.array(vertices, dtype=np.float32)
    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
    
    position = glGetAttribLocation(program, 'position')
    glEnableVertexAttribArray(position)
    glVertexAttribPointer(position, 4, GL_FLOAT, GL_FALSE, 0, None)
    
    # VAO 언바인딩
    glBindVertexArray(0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle(program, vao)
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
