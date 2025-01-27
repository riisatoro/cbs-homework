# Завдання 2
#
# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші. 
# Опишіть клас кнопки. 
# Створіть об'єкт кнопки та звичайного прямокутника. 
# Викличте метод натискання на кнопку.


class RenderObject:
    def __init__(self, vertexes: list[tuple[int]]):
        self.vertexes = vertexes

    def render(self):
        for index in range(0, len(self.vertexes) - 1):
            start_point, end_point = self.vertexes[index], self.vertexes[index + 1]
            print(f"Rendering object from {start_point} to {end_point}")


class Triangle(RenderObject):
    def calculate_square(self):
        print("Calculating square based on vertexes")


class OnClickRenderHandler:
    def handle_click(self, renderer: RenderObject):
        renderer.render()


class MouseOnClickRenderHandler(OnClickRenderHandler):
    def on_left_click(self, renderer: RenderObject):
        self.handle_click(renderer)
    
    def on_right_click(self, renderer: RenderObject):
        print("Filling shape based on selected color")


triangle = Triangle(
    [(0, 0), (0, 1), (1, 0)]
)
triangle.calculate_square()

mouse_renderer = MouseOnClickRenderHandler()
mouse_renderer.on_left_click(triangle)
mouse_renderer.on_right_click(triangle)
