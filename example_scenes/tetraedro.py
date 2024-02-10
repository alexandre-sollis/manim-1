from manim import *

class ThreeDModel(ThreeDScene):
    def construct(self):
        # Create a 3D model
        box = Box()

        # Set the camera position
        self.set_camera_orientation(phi=PI/4, theta=-PI/4)

        # Add the model to the scene
        self.add(box)

        # Rotate the box
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()

class Box(ThreeDScene):
    def construct(self):
        # Define the vertices of a unit cube
        vertices = [
            [-0.5, -0.5, -0.5],
            [0.5, -0.5, -0.5],
            [0.5, 0.5, -0.5],
            [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5],
            [0.5, -0.5, 0.5],
            [0.5, 0.5, 0.5],
            [-0.5, 0.5, 0.5],
        ]

        # Create faces using the vertices
        faces = [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [0, 3, 7, 4],
            [1, 2, 6, 5],
            [0, 1, 5, 4],
            [2, 3, 7, 6],
        ]

        # Create a 3DVMobject
        box = ThreeDVMobject()
        box.set_points_as_corners(vertices)
        self.play(Create(box))
        self.add_faces(*faces)

if __name__ == "__main__":
    scene = ThreeDModel()
    scene.render()
