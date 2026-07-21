from manim import *
from manim_combinable import *

class IntroIntro(ThreeDScene):
    def construct(self):
        self.wait(1)
        torusX = Torus(major_radius=1, minor_radius=.05, stroke_width=0).set_color(color.BLUE_C).rotate(90*DEGREES, np.array([1, 0, 0]))
        torusY = Torus(major_radius=1.12, minor_radius=.05, stroke_width=0).set_color(color.RED_C)
        torusZ = Torus(major_radius=1.24, minor_radius=.05, stroke_width=0).set_color(color.GREEN_C).rotate(90*DEGREES, np.array([0, 1, 0]))
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.camera.set_zoom(.9)
        self.play(AnimationGroup(
            FadeIn(torusX),
            FadeIn(torusY),
            FadeIn(torusZ)
        ), AnimationGroup(
            Rotate(torusX, 360*DEGREES, np.array([1,2,3])),
            Rotate(torusY, 360*DEGREES, np.array([1,2,3])),
            Rotate(torusZ, 360*DEGREES, np.array([1,2,3])),
            rate_func=rate_functions.ease_out_cubic
        ),
        run_time=2
        )
        self.wait(2)