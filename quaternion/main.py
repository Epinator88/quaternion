from manim import *
class IntroIntro(ThreeDScene):
    def construct(self):
        self.wait(1)
        torusX = Torus(major_radius=1, minor_radius=.05, stroke_width=0).set_color(color.BLUE_C).rotate(90*DEGREES, np.array([1, 0, 0]))
        torusY = Torus(major_radius=1.1, minor_radius=.05, stroke_width=0).set_color(color.RED_C)
        torusZ = Torus(major_radius=1.2, minor_radius=.05, stroke_width=0).set_color(color.GREEN_C).rotate(90*DEGREES, np.array([0, 1, 0]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)