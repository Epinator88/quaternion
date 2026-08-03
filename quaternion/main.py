from manim import *
from manim_combinable import *

class IntroIntro(ThreeDScene):
    def construct(self):
        world_x = Arrow3D(start=ORIGIN, end=RIGHT).set_color(RED) # pyright: ignore[reportUndefinedVariable]
        world_y = Arrow3D(start=ORIGIN, end=UP).set_color(GREEN)
        world_z = Arrow3D(start=ORIGIN, end=np.array([0,0,1])).set_color(BLUE)
        anchor = VGroup(world_x,world_y,world_z).set_opacity(0.0)
        self.add(anchor)
        self.wait(1)
        light = self.camera.light_source
        light.shift(UP*20)
        torusX = Torus(major_radius=1, minor_radius=.05, stroke_width=0).set_color(color.RED_C).rotate(90*DEGREES, np.array([0, 1, 0]))
        xcon1 = Cylinder(radius=.04, height=.1, direction=UP).shift(IN*1.05).set_color(color.RED_C)
        xcon2 = Cylinder(radius=.04, height=.1, direction=UP).shift(OUT*1.05).set_color(color.RED_C)
        localX = Arrow3D(start=ORIGIN, end=RIGHT).set_color(RED_C)
        torusY = Torus(major_radius=1.12, minor_radius=.05, stroke_width=0).set_color(color.GREEN_C).rotate(90*DEGREES, np.array([1, 0, 0]))
        ycon1 = Cylinder(radius=.04, height=.1, direction=RIGHT).shift(RIGHT*1.17).set_color(color.GREEN_C)
        ycon2 = Cylinder(radius=.04, height=.1, direction=RIGHT).shift(LEFT*1.17).set_color(color.GREEN_C)
        localY = Arrow3D(start=ORIGIN, end=UP).set_color(GREEN_C)
        torusZ = Torus(major_radius=1.24, minor_radius=.05, stroke_width=0).set_color(color.BLUE_C)
        zcon1 = Cylinder(radius=.04, height=.1, direction=UP).shift(UP*1.29).set_color(color.BLUE_C)
        zcon2 = Cylinder(radius=.04, height=.1, direction=UP).shift(DOWN*1.29).set_color(color.BLUE_C)
        localZ = Arrow3D(start=ORIGIN, end=np.array([0,0,1])).set_color(BLUE_C)
        linkages = VGroup(xcon1, xcon2, ycon1, ycon2, zcon1, zcon2).set_opacity(0.0)
        gimbal = VGroup(torusX, torusY, torusZ, linkages)
        core = VGroup(localX, localY, localZ).set_opacity(0.0)
        self.add(core)
        rig = VGroup(gimbal, core).rotate(20*DEGREES, RIGHT).rotate(-10*DEGREES, localY.get_end())
        self.camera.set_zoom(.7)
        self.play(AnimationGroup(
            FadeIn(gimbal),
        ), AnimationGroup(
            Rotate(gimbal, 360*DEGREES, np.array([1,2,3])),
            rate_func=rate_functions.ease_out_cubic
        ),
        run_time=2
        )
        self.wait(2)
        self.play(AnimationGroup(
            #x, z, y
            Rotate(gimbal, 180*DEGREES, localZ.get_end()),
            Rotate(gimbal, 180*DEGREES, localY.get_end()),
            Rotate(gimbal, 180*DEGREES, localX.get_end()),  
            lag_ratio=1.4,
            run_time=3
        ))
        self.wait(5)    
        GLock = Text("Gimbal Lock").shift(UP*1.5).scale(.7)
        self.play(AnimationGroup(
            rig.animate.shift(DOWN*.5),
            Write(GLock),
            lag_ratio=.5,
            run_time=2
        ))
        self.wait(3)
        self.play(AnimationGroup(
            Unwrite(GLock),
            rig.animate.shift(UP*.5),
            lag_ratio=.5,
            run_time=2
        ))
        self.play(
            linkages.animate.set_opacity(1.0)
        )
        self.wait(3)


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