### 7. 그래픽스 프로그래밍

#### 7.1 OpenGL
**이론**:
- **OpenGL의 개념**: OpenGL은 크로스 플랫폼 그래픽스 API로, 2D 및 3D 그래픽스를 렌더링하는 데 사용됩니다. 주로 C와 C++에서 사용되며, 다양한 그래픽 카드에서 하드웨어 가속을 지원합니다.
- **기본 구조**: 버텍스 쉐이더, 프래그먼트 쉐이더, 렌더링 파이프라인

**실습**:
Python과 PyOpenGL을 사용하여 간단한 2D 삼각형을 그려보겠습니다.

1. PyOpenGL 설치:
```sh
pip install PyOpenGL PyOpenGL_accelerate
```

2. 코드 작성:
```python
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 0.5)
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluOrtho2D(-1, 1, -1, 1)
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
```

이 코드는 간단한 2D 삼각형을 OpenGL을 사용하여 그리는 예제입니다.

#### 7.2 DirectX
**이론**:
- **DirectX의 개념**: DirectX는 마이크로소프트가 개발한 그래픽스 API로, 주로 Windows 환경에서 사용됩니다. Direct3D는 DirectX의 3D 그래픽스 부분을 담당합니다.
- **기본 구조**: 디바이스 초기화, 버퍼 생성, 렌더링 루프

**실습**:
C++과 DirectX를 사용하여 간단한 2D 삼각형을 그려보겠습니다.

1. DirectX SDK 설치.
2. Visual Studio에서 새 프로젝트를 만들고, DirectX 헤더와 라이브러리를 추가합니다.
3. 코드 작성:
```cpp
#include <windows.h>
#include <d3d11.h>

#pragma comment (lib, "d3d11.lib")

IDXGISwapChain *swapchain;
ID3D11Device *dev;
ID3D11DeviceContext *devcon;
ID3D11RenderTargetView *backbuffer;

void InitD3D(HWND hWnd);
void RenderFrame(void);
void CleanD3D(void);

LRESULT CALLBACK WindowProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam) {
    switch(message) {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
    }
    return DefWindowProc(hWnd, message, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    HWND hWnd;
    WNDCLASSEX wc;

    wc.cbSize = sizeof(WNDCLASSEX);
    wc.style = CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WindowProc;
    wc.cbClsExtra = 0;
    wc.cbWndExtra = 0;
    wc.hInstance = hInstance;
    wc.hIcon = LoadIcon(NULL, IDI_APPLICATION);
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)COLOR_WINDOW;
    wc.lpszMenuName = NULL;
    wc.lpszClassName = L"WindowClass";
    wc.hIconSm = LoadIcon(NULL, IDI_APPLICATION);

    RegisterClassEx(&wc);

    hWnd = CreateWindowEx(NULL, L"WindowClass", L"Our First Direct3D Program", WS_OVERLAPPEDWINDOW, 0, 0, 800, 600, NULL, NULL, hInstance, NULL);
    ShowWindow(hWnd, nCmdShow);

    InitD3D(hWnd);

    MSG msg = {0};
    while(TRUE) {
        while(PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        if(msg.message == WM_QUIT)
            break;

        RenderFrame();
    }

    CleanD3D();

    return msg.wParam;
}

void InitD3D(HWND hWnd) {
    DXGI_SWAP_CHAIN_DESC scd;

    ZeroMemory(&scd, sizeof(DXGI_SWAP_CHAIN_DESC));

    scd.BufferCount = 1;
    scd.BufferDesc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
    scd.BufferDesc.Width = 800;
    scd.BufferDesc.Height = 600;
    scd.BufferUsage = DXGI_USAGE_RENDER_TARGET_OUTPUT;
    scd.OutputWindow = hWnd;
    scd.SampleDesc.Count = 4;
    scd.Windowed = TRUE;

    D3D11CreateDeviceAndSwapChain(NULL, D3D_DRIVER_TYPE_HARDWARE, NULL, NULL, NULL, NULL, D3D11_SDK_VERSION, &scd, &swapchain, &dev, NULL, &devcon);

    ID3D11Texture2D *pBackBuffer;
    swapchain->GetBuffer(0, __uuidof(ID3D11Texture2D), (LPVOID*)&pBackBuffer);
    dev->CreateRenderTargetView(pBackBuffer, NULL, &backbuffer);
    pBackBuffer->Release();

    devcon->OMSetRenderTargets(1, &backbuffer, NULL);

    D3D11_VIEWPORT viewport;
    ZeroMemory(&viewport, sizeof(D3D11_VIEWPORT));

    viewport.TopLeftX = 0;
    viewport.TopLeftY = 0;
    viewport.Width = 800;
    viewport.Height = 600;

    devcon->RSSetViewports(1, &viewport);
}

void RenderFrame(void) {
    devcon->ClearRenderTargetView(backbuffer, D3DXCOLOR(0.0f, 0.2f, 0.4f, 1.0f));

    swapchain->Present(0, 0);
}

void CleanD3D(void) {
    swapchain->Release();
    backbuffer->Release();
    dev->Release();
    devcon->Release();
}
```

이 코드는 간단한 DirectX 프로그램을 작성하여 파란색 배경의 창을 렌더링합니다.

#### 7.3 Shader Programming
**이론**:
- **셰이더 프로그래밍의 개념**: 셰이더는 GPU에서 실행되는 작은 프로그램으로, 주로 그래픽스 렌더링 과정에서 사용됩니다. 셰이더는 주로 버텍스 셰이더와 프래그먼트 셰이더로 구성됩니다.
- **버텍스 셰이더**: 각 정점(vertex)의 위치를 계산합니다.
- **프래그먼트 셰이더**: 각 픽셀의 색상을 계산합니다.

**실습**:
Python과 PyOpenGL을 사용하여 간단한 셰이더 프로그램을 작성해보겠습니다.

1. PyOpenGL 설치:
```sh
pip install PyOpenGL PyOpenGL_accelerate
```

2. 코드 작성:
```python
import pygame
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

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
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    gluOrtho2D(-1, 1, -1, 1)
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
```

이 코드는 간단한 셰이더 프로그램을 사용하여 빨간색 삼각형을 OpenGL로 그리는 예제입니다.
