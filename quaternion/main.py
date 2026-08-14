from manim import *
from manim_combinable import *
import math

class IntroIntro(ThreeDScene):
    def construct(self): #please excuse the mess; i did not know the existence of self.camera.add_fixed_position_mobject
        self.camera.set_zoom(.8)
        world_x = Arrow3D(start=ORIGIN, end=RIGHT).set_color(RED) # pyright: ignore[reportUndefinedVariable]
        world_y = Arrow3D(start=ORIGIN, end=UP).set_color(GREEN)
        world_z = Arrow3D(start=ORIGIN, end=np.array([0,0,1])).set_color(BLUE)
        anchor = VGroup(world_x,world_y,world_z).set_opacity(0.0)
        self.add(anchor)
        self.wait(1)
        light = self.camera.light_source
        light.shift(UP*40)
        torusX = Torus(major_radius=3, minor_radius=.15, stroke_width=0).set_color(color.RED).rotate(90*DEGREES, np.array([0, 1, 0]))
        xcon1 = Cylinder(radius=.12, height=.3, direction=UP).shift(IN*3.15).set_color(color.RED)
        xcon2 = Cylinder(radius=.12, height=.3, direction=UP).shift(OUT*3.15).set_color(color.RED)
        localX = Arrow3D(start=ORIGIN, end=RIGHT).set_color(RED)
        rigX = VGroup(torusX, xcon1, xcon2)
        torusY = Torus(major_radius=3.36, minor_radius=.15, stroke_width=0).set_color(color.GREEN).rotate(90*DEGREES, np.array([1, 0, 0]))
        ycon1 = Cylinder(radius=.12, height=.3, direction=RIGHT).shift(RIGHT*3.51).set_color(color.GREEN)
        ycon2 = Cylinder(radius=.12, height=.3, direction=RIGHT).shift(LEFT*3.51).set_color(color.GREEN)
        localY = Arrow3D(start=ORIGIN, end=UP).set_color(GREEN)
        rigY = VGroup(torusY, ycon1, ycon2)
        torusZ = Torus(major_radius=3.72, minor_radius=.15, stroke_width=0).set_color(color.BLUE)
        zcon1 = Cylinder(radius=.12, height=.3, direction=UP).shift(UP*3.87).set_color(color.BLUE)
        zcon2 = Cylinder(radius=.12, height=.3, direction=UP).shift(DOWN*3.87).set_color(color.BLUE)
        rigZ = VGroup(torusZ, zcon1, zcon2)
        localZ = Arrow3D(start=ORIGIN, end=np.array([0,0,1])).set_color(BLUE)
        gimbal = VGroup(rigX, rigY, rigZ)
        core = VGroup(localX, localY, localZ).set_opacity(0.0)
        self.add(core)
        rig = VGroup(gimbal, core).rotate(20*DEGREES, RIGHT).rotate(-10*DEGREES, localY.get_end())
        xcon1.set_opacity(0.0),
        xcon2.set_opacity(0.0),
        ycon1.set_opacity(0.0),
        ycon2.set_opacity(0.0),
        zcon1.set_opacity(0.0),
        zcon2.set_opacity(0.0)
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
        self.wait(2)    
        GLock = Text("Gimbal Lock").shift(UP*4).scale(1.5)
        self.play(AnimationGroup(
            gimbal.animate.shift(DOWN*.75),
            Write(GLock),
            lag_ratio=.5,
            run_time=2
        ))
        self.wait(3)
        self.play(AnimationGroup(
            Unwrite(GLock),
            gimbal.animate.shift(UP*.75), #the numbers were off on the previous rig shift so all rotations were messed up slightly (i think)
            lag_ratio=.5,
            run_time=2
        ))
        self.play(
            xcon1.animate.set_opacity(1.0),
            xcon2.animate.set_opacity(1.0),
            ycon1.animate.set_opacity(1.0),
            ycon2.animate.set_opacity(1.0),
            zcon1.animate.set_opacity(1.0),
            zcon2.animate.set_opacity(1.0)
        )
        self.wait(3)
        self.play(
            Rotate(rigX, 90*DEGREES, localX.get_end()),
            Rotate(torusY, 90*DEGREES, localX.get_end()),
        )
        self.play(
            Rotate(torusX, 90*DEGREES, localY.get_end())
        )
        self.wait(3)
        self.play(gimbal.animate.shift(DOWN*.75))
        text = Text("Rotating about z-axis", t2c={"z": BLUE_C}).shift(UP*4).scale(1.5)
        self.play(Write(text))
        self.play(
            Rotate(rigY, 180*DEGREES, localY.get_end()),
            Rotate(rigX, 180*DEGREES, localY.get_end()),
            Rotate(rigZ, 180*DEGREES, localY.get_end())
        )
        self.wait(1)
        tex2 = Text("Rotating about x-axis", t2c={" x": RED_C}).shift(UP*4).scale(1.5)
        self.play(
            TransformMatchingShapes(text, tex2)
        )
        self.wait(1)
        self.play(
            Rotate(rigX, 180*DEGREES, localY.get_end())
        )
        self.wait(2)
        self.play(
            Unwrite(tex2)
        )
        self.play(
            gimbal.animate.shift(UP*.75)
        )
        self.play(
            Rotate(rigX, 30*DEGREES, localX.get_end()),
            Rotate(torusY, 30*DEGREES, localX.get_end()),
        )
        self.wait(1)
        self.play(
            Rotate(rigX, -30*DEGREES, localX.get_end()),
            Rotate(torusY, -30*DEGREES, localX.get_end()),
        )
        self.wait(1)
        localZ.set_color(RED).scale(3)
        self.play(
            localZ.animate.set_opacity(1)
        )
        self.wait(2)
        self.play(
            Uncreate(localZ)
        )
        self.wait(2)
        self.play(
            Uncreate(gimbal)
        )

class Imaginary(Scene):
    def construct(self):
        imag = MathTex("i=\\sqrt{-1}")
        self.play(
            Write(imag)
        )
        self.wait(1)
        eq = MathTex("x^{2}+1=0")
        self.play(
            AnimationGroup(imag.animate.shift(UP*1.5)),
            Write(eq),
            lag_ratio=.4
        )
        self.wait(1)
        sol = MathTex("x=i,-i")
        self.play(
            AnimationGroup(eq.animate.shift(DOWN*1.5)),
            Write(sol),
            lag_ratio=.4
        )
        self.wait(2)
        self.play(
            Unwrite(imag),
            Unwrite(eq),
            Unwrite(sol)
        )
        std_plane = NumberPlane(
            background_line_style={
                "stroke_color": GREY,
                "stroke_width": 4,
                "stroke_opacity": 0.6
            }
        )
        self.wait(1)
        self.play(
            Create(std_plane)
        )
        func1 = FunctionGraph(
            lambda x: x**2 + 1
        )
        self.wait(1)
        self.play(
            Write(func1)
        )
        self.wait(2)
        self.play(
            FadeOut(func1),
            FadeOut(std_plane)
        )
        self.wait(1)
        tex1 = Text("Useless").shift(UP)
        tex2 = Text("False")
        tex3 = Text("Imaginary").set_color(YELLOW).shift(DOWN)
        self.play(AnimationGroup(
            Write(tex1),
            Write(tex2),
            Write(tex3),
            lag_ratio=1,
            run_time=4.5
        ))
        self.wait(3)
        self.play(
            FadeOut(tex1),
            FadeOut(tex2),
            FadeOut(tex3)
        )
        eq2 = MathTex("x^{3}-15x-4").shift(UP*2)
        key2 = MathTex("x^3+px+q").shift(UP*1.25)
        eq3 = MathTex("u_1=-\\frac{q}{2}+\\sqrt{\\frac{q^2}{4}+\\frac{p^3}{27}}").shift(LEFT*3)
        eq4 = MathTex("u_2=-\\frac{q}{2}-\\sqrt{\\frac{q^2}{4}+\\frac{p^3}{27}}").shift(RIGHT*3)
        eq5 = MathTex("x=\\sqrt[3]{u_1}+\\sqrt[3]{u_2}").shift(DOWN*1.25)
        self.wait(2)
        self.play(AnimationGroup(
            Write(eq2),
            Write(key2),
            Write(eq3),
            Write(eq4),
            Write(eq5),
            lag_ratio=.3
        ))
        self.wait(5)
        self.play(
            eq2.animate.set_color(RED)
        )
        self.wait(1)
        self.play(
            eq3.animate.set_color(RED),
            eq4.animate.set_color(RED)
        )
        self.wait(2)
        self.play(
            FadeOut(eq2),
            FadeOut(key2),
            FadeOut(eq3),
            FadeOut(eq4),
            FadeOut(eq5)
        )
        self.remove(eq2)
        self.wait(2)
        eq2.shift(DOWN*1.5)
        eq6 = MathTex("{{(4)^3}}-{{15(4)}}-{{(4)}}").shift(UP*.5)
        eq65 = MathTex("{{64}}-{{60}}-{{4}}").shift(UP*.5)
        eq675 = MathTex("{{64}}-{{64}}=0").shift(UP*.5)
        eq7 = MathTex("x^3+2x-4").shift(DOWN*.5).shift(LEFT*1.5)
        self.play(
            Write(eq2)
        )
        self.wait(.5)
        self.play(
            TransformMatchingTex(eq2, eq6)
        )
        self.wait(.5)
        self.play(
            TransformMatchingTex(eq6, eq65)
        )
        self.wait(.5)
        self.play(
            TransformMatchingTex(eq65, eq675)
        )
        self.wait(2)
        self.play(
            Write(eq7)
        )
        eq8 = MathTex("x=2").shift(DOWN*.5).shift(RIGHT*1.5)
        self.wait(2)
        self.play(
            Write(eq8)
        )
        self.wait(2)
        self.play(
            Unwrite(eq675),
            Unwrite(eq7),
            Unwrite(eq8)
        )
        self.wait(2)
        line = NumberLine(
            x_range=[-5,5,1],
            length=20, #should be going off-screen
            color=WHITE,
            include_numbers=True
        ).center()
        line.shift(-line.n2p(0))
        self.play(
            Create(line),
        )
        ind = Arrow(start=UP, end=DOWN).shift(UP*1.25+RIGHT)
        self.wait(1)
        self.play(
            Create(ind)
        )
        self.play(
            ind.animate.shift(LEFT*4)
        )
        self.play(
            ind.animate.shift(RIGHT*16)
        )
        self.remove(ind)
        eq9 = MathTex("i=\\sqrt{-1}").shift(UP*2)
        self.play(
            Write(eq9)
        )
        self.wait(1)
        self.play(Unwrite(eq9))
        self.wait(1)
        self.play(
            line.animate.flip(),
        )
        self.wait(2)
        self.play(
            line.animate.flip(),
        )
        self.wait(2)
        self.play(
            Rotate(line),
        )
        self.wait(2)
        self.play(
            Rotate(line),
        )
        self.wait(3)
        imagLine = NumberLine(
            x_range=[-5,5,1],
            length=20, #should be going off-screen
            color=GOLD_A,
            include_numbers=True,
            decimal_number_config={"unit":"i", "num_decimal_places":0},
            numbers_to_exclude=[0]
        ).center()
        imagLine.shift(-imagLine.n2p(0))
        for n in imagLine.numbers:
            n.rotate(-90*DEGREES) #check if it doesn't just send all of the numbers flying off and rotates locally
            #it fcuking worked i'm amazing
        self.play(
            FadeIn(imagLine),
            imagLine.animate.rotate_about_zero(90*DEGREES),
            FadeOut(line.get_number_mobject(0)),
            run_time=4,
            rate_func=rate_functions.rush_into
        )
        line.set_z_index(2)
        imagLine.set_z_index(1)
        for i in range(1,5,1):
            #pos neg both axis
            self.play(
                Create(Line(line.n2p(i)+5*UP,line.n2p(i)+5*DOWN).set_color(DARK_GREY)),
                Create(Line(line.n2p(-i)+5*UP,line.n2p(-i)+5*DOWN).set_color(DARK_GREY)),
                Create(Line(imagLine.n2p(i)+8*RIGHT,imagLine.n2p(i)+8*LEFT).set_color(DARK_GREY)),
                Create(Line(imagLine.n2p(-i)+8*RIGHT,imagLine.n2p(-i)+8*LEFT).set_color(DARK_GREY)),
            )
        self.wait(2)
        onei = CurvedArrow(line.n2p(1)+UP*.2, imagLine.n2p(1)+RIGHT*.2)
        ineg = CurvedArrow(imagLine.n2p(1)+LEFT*.2, line.n2p(-1)+UP*.2)
        negi = CurvedArrow(line.n2p(-1)+DOWN*.2, imagLine.n2p(-1)+LEFT*.2)
        ione = CurvedArrow(imagLine.n2p(-1)+RIGHT*.2, line.n2p(1)+DOWN*.2)
        self.play(
            Write(onei),
            Write(ineg),
            Write(negi),
            Write(ione),
            run_time=6,
            lag_ratio=1.5
        )
        self.wait(2)
        self.play(
            Indicate(onei),
            Indicate(ineg)
        )
        self.wait(1)
        self.play(
            Indicate(onei)
        )
        self.wait(1)
        self.play(AnimationGroup(
            Indicate(onei),
            Indicate(ineg),
            lag_ratio=.5,
            run_time=2
        ))
        self.wait(2)
        self.play(
            Unwrite(onei),
            Unwrite(ineg),
            Unwrite(negi),
            Unwrite(ione)
        )
        circ = Circle(radius=2.0)
        self.play(
            Write(circ)
        )
        self.wait(2)
        lline = Line(line.n2p(0), line.n2p(5)).set_color(RED).shift(OUT*.01)
        self.add(lline)
        self.play(
            lline.animate.rotate_about_origin(45*DEGREES)
        )
        self.wait(1)
        coord = 1/math.sqrt(2)
        dot = Dot().set_color(BLUE).shift(coord*UP*2+coord*RIGHT*2)
        coords = MathTex("(\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}})").move_to(dot).shift(RIGHT*1.5).set_color(BLUE)
        self.play(
            Write(coords),
            Create(dot)
        )
        degrees = MathTex("45^{\\circ}").set_color(RED).move_to(dot).shift(DOWN*1+RIGHT*1.3)
        self.play(
            Write(degrees)
        )
        square = Rectangle(GOLD_A).set_fill(BLACK, 1.0).set_z_index(3)
        eq10 = MathTex("\\cos(\\theta)+i\\sin(\\theta)").set_z_index(4)
        self.play(AnimationGroup(
            FadeIn(square),
            Write(eq10),
            run_time=2,
            lag_ratio=.5
        ))
        self.wait(5)

#camera coord system is like latitude longitude
#phi is 0 at north pole, higher = more down. inverted latitude
#theta is longitude
#gamma is roll of camera itself

#we want to be like 70* phi and then rotate passively around theta

#"why aren't you using radians" i've grown up with degrees & they're a more human measurement, like fahrenheit.
#why am i writing these like someone is going to read this lmfao

class Fourth(ThreeDScene):
    def construct(self):
        self.camera.set_zoom(.8)
        self.set_camera_orientation(phi=70*DEGREES, theta=30*DEGREES)
        self.begin_ambient_camera_rotation()
        axes = ThreeDAxes()
        axes.get_x_axis().set_color(RED)
        axes.get_y_axis().set_color(GREEN)
        axes.get_z_axis().set_color(BLUE)
        dot = Dot3D(radius=.12).set_color(GOLD).set_opacity(1.)
        xSlide = NumberLine(
            x_range=[-1,1,1], #use camera tricks to make it look bigger
            length=3,
            color=RED,
        ).set_shade_in_3d(False)
        xLabel = MathTex("x").set_shade_in_3d(False).set_color(RED)
        xDot = Dot().set_shade_in_3d(False).set_color(RED)
        ySlide = NumberLine(
            x_range=[-1,1,1], #use camera tricks to make it look bigger
            length=3,
            color=GREEN
        ).set_shade_in_3d(False)
        yLabel = MathTex("y").set_shade_in_3d(False).set_color(GREEN)
        yDot = Dot().set_shade_in_3d(False).set_color(GREEN)
        zSlide = NumberLine(
            x_range=[-1,1,1], #use camera tricks to make it look bigger
            length=3,
            color=BLUE
        ).set_shade_in_3d(False)
        zLabel = MathTex("z").set_shade_in_3d(False).set_color(BLUE)
        zDot = Dot().set_shade_in_3d(False).set_color(BLUE)
        sliders = VGroup(xSlide, ySlide, zSlide).arrange(RIGHT, buff=1)
        labels = VGroup(xLabel, yLabel, zLabel).arrange(RIGHT, buff=3.8)
        dots = VGroup(xDot, yDot, zDot).arrange(RIGHT, buff=3.84)
        self.play(FadeIn(axes))
        self.wait(5) #maybe not extract the axis to the screen but add the sliders on the bottom of the screen?
        self.add_fixed_in_frame_mobjects(sliders, labels, dots)
        sliders.shift(DOWN*2.5)
        labels.shift(DOWN*3)
        dots.shift(DOWN*2.5)
        self.play(
            axes.animate.shift(OUT),
            FadeIn(dot),
            dot.animate.shift(OUT),
            Create(sliders),
            Create(labels)
            #put each slider on and the dot at [0,0,0]
        )
        self.wait(2)
        self.play(
            dot.animate.shift(np.array([1,2,3])),
            xDot.animate.shift(RIGHT*.3),
            yDot.animate.shift(RIGHT*.6),
            zDot.animate.shift(RIGHT*.9),
            run_time=2
        )
        self.wait(2)
        self.play(
            dot.animate.shift(np.array([-3,1,-2])),
            xDot.animate.shift(LEFT*.9),
            yDot.animate.shift(RIGHT*.3),
            zDot.animate.shift(LEFT*.6),
            run_time=2
        )
        self.wait(2)
        self.play(
            dot.animate.shift(np.array([-2,-5,-2])),
            xDot.animate.shift(LEFT*.6),
            yDot.animate.shift(LEFT*1.5),
            zDot.animate.shift(LEFT*.6),
            run_time=2
        )
        self.wait(3)
        self.play(
            FadeOut(dot),
            FadeOut(axes),
            FadeOut(dots),
            sliders.animate.arrange(DOWN, buff=1).shift(UP*.75),
            labels.animate.arrange(DOWN, buff=1).shift(UP*.75+LEFT*2)
        )
        self.wait(2)
        wSlide = NumberLine(
            x_range=[-1,1,1], #use camera tricks to make it look bigger
            length=3,
            color=GOLD,
        ).set_shade_in_3d(False)
        wLabel = MathTex("w").set_shade_in_3d(False).set_color(GOLD)
        self.camera.add_fixed_in_frame_mobjects(wSlide, wLabel)
        wSlide.next_to(sliders, DOWN, buff=1)
        wLabel.next_to(wSlide, LEFT, buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER*1.5)
        self.play(
            Create(wSlide),
            FadeIn(wLabel)
        )
        self.wait(5)
        self.play(
            Indicate(wSlide),
            Indicate(wLabel),
            Indicate(xSlide),
            Indicate(xLabel)
        )
        self.wait(3)
        self.play(
            zSlide.animate.set_opacity(.2),
            zLabel.animate.set_opacity(.2),
            wSlide.animate.set_opacity(.2),
            wLabel.animate.set_opacity(.2)
        )
        self.wait(3)
        self.play(
            zSlide.animate.set_opacity(1.),
            zLabel.animate.set_opacity(1.),
        )
        self.wait(3)
        self.play(
            wSlide.animate.set_opacity(1.),
            wLabel.animate.set_opacity(1.),
        )
        self.stop_ambient_camera_rotation() 

class Quaternions(ThreeDScene):
    def construct(self):
        tex1 = Text("Complex Numbers")
        tex2 = Text("Fourth Dimension")
        tex1.shift(LEFT*2+UP)
        self.play(
            Write(tex1)
        )
        self.wait(2)
        tex2.shift(RIGHT*2+DOWN)
        self.play(
            Write(tex2)
        )
        self.wait(3)
        self.play(AnimationGroup(
            tex1.animate.shift(RIGHT*2+DOWN),
            tex2.animate.shift(LEFT*2+UP),
            Rotate(tex1, 720*DEGREES),
            Rotate(tex2, 720*DEGREES),
            rate_func=rate_functions.rush_into
        ))
        self.remove(tex1, tex2)
        tex3 = Text("Quaternions").set_color(GOLD).scale(2)
        self.add(tex3)
        self.play(
            tex3.animate.scale(.75),
            rate_func=rate_functions.rush_from
        )
        self.wait(3)
        self.play(
            Unwrite(tex3)
        )
        units = MathTex("1","i","j","k",tex_to_color_map={'i':RED,'j':GREEN,'k':BLUE}).scale(1.5)
        self.wait(1)
        self.play(
            Write(units[:2])
        )
        self.wait(1)
        self.play(
            Write(units[2:])
        )
        self.wait(1)
        rules = MathTex("ij=k,","jk=i,","ki=j",tex_to_color_map={'i':RED,'j':GREEN,'k':BLUE}).scale(1.5)
        self.wait(2)
        self.play(AnimationGroup(
            units.animate.shift(UP).set_opacity(.4),
            Write(rules),
            lag_ratio=.4
        ))
        inf = MathTex("ijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijkijk",tex_to_color_map={'i':RED,'j':GREEN,'k':BLUE}).scale(1.5)
        self.wait(2)
        inf.set_opacity(.6).shift(RIGHT*10).set_opacity(0.0)
        def scroll(mobject, dt):
            mobject.shift(LEFT*dt*.2) #now we're thinking with updaters
        inf.add_updater(scroll)
        self.add(inf)
        self.play(
            rules.animate.shift(UP).set_opacity(.4),
            units.animate.shift(UP),
            inf.animate.set_opacity(1.0)
        )
        self.wait(2)


        self.wait(3)

class QuaternionRotation(Scene):
    def construct(self):
        return super().construct()
    
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