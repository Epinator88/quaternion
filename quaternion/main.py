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

class Transition(Scene):
    def construct(self):
        self.wait(1)
        rects_pre = VGroup([Rectangle(height=9/9, width=16/9) for _ in range(20)])
        self.add(rects_pre)
        rects_pre.center()
        self.play(
            FadeIn(rects_pre),
            rects_pre.animate.scale(3),
            lag_ratio=.15,
            run_time=10
        )