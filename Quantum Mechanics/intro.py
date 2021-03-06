from typing_extensions import runtime
from manimlib import *
import numpy as np

class intro(Scene):
    def construct(self):
        self.defination()
    def defination(self):
        sq1 = Rectangle(width=3,height=4,stroke_color=BLUE)
        sq2 = Rectangle(width=4,height=4,stroke_color=RED)
        elps = Ellipse(width= 10, height=5.5,stroke_color=GREEN) 

        texts = VGroup(
            Text("Classical Mechanics",font = "Maiandra GD", font_size= 30, color = BLUE),
            Text("Laws of Motion",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Electrodynamics",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Magnetism",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Thermodynamics",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Limitations",font = "Maiandra GD", font_size= 30, color = RED),
            Text("Quantum Mechanics",font = "Maiandra GD", font_size= 30, color = RED),
            Text("Black Body Radiation",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Photo Electric Effect",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Hydrogen Atom",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Uncertainty Principal",font = "Roboto Thin", font_size= 20, color = WHITE),
            Text("All of Physics",font = "Maiandra GD", font_size= 30, color = GREEN),
        )

        texts[0].next_to(sq1,direction=UP)

        self.play(Write(texts[0]))
        self.play(DrawBorderThenFill(sq1))

        for each in range(4):
            texts[each+1].next_to(texts[each],direction=DOWN, buff=0.7)
            self.play(Write(texts[each+1]))
        
        cls = VGroup(sq1,texts[:5])
        self.play(cls.animate.move_to(LEFT*3) )

        texts[5:7].next_to(sq2,direction=UP)
        
        qnt = VGroup(sq2,texts[5:11])
        qnt.move_to(RIGHT*3)
        self.wait()
        self.play(Write(texts[5]))
        self.play(DrawBorderThenFill(sq2))

        for each in range(6,10):
            texts[each+1].next_to(texts[each],direction=DOWN, buff=0.7)
            self.play(Write(texts[each+1]))

        self.wait()
        self.play(ReplacementTransform(texts[5],texts[6]))

        self.wait(2)
        self.play((VGroup(cls,qnt)).animate.scale(0.6))
        
        texts[11].next_to(elps, direction=DOWN)
        self.play(DrawBorderThenFill(elps))
        self.play(Write(texts[11]))
        self.wait(2)
        self.play(
            FadeOut(VGroup(cls,elps,texts[11])),
        )
        self.play(qnt.animate.scale(1.5).move_to(LEFT*5), run_time = 2)
        self.play(texts[7].copy().animate.move_to(ORIGIN+UP*3.2).scale(1.5).set_color(BLUE))
        self.wait()
        self.play(FadeOut(qnt))

class animated(Scene):
    def construct(self):
        axes =Axes(
            x_range=(0,1,0.1),
            y_range=(0,26,2),

            decimal_number_config={"num_decimal_places":2 },
            # include_numbers=True,
        )
        axes.x_labels = 'Wavelength'
        axes.add_coordinate_labels(num_decimal_places=2)
        self.wait()
        self.add(axes)


        T = ValueTracker(.1)
        sin_graph = always_redraw( lambda:axes.get_graph(
            lambda x: ((38)/(x**(5)))*((1)/(math.e**(((14400)/(x*T.get_value())))-1)) if x> 0.1 else 0,
            x_range = [0,1],
            color=BLUE,
        ))
        sin_graph1 = sin_graph.copy().set_color(YELLOW)
        self.add(sin_graph)
        self.add(sin_graph1)
        self.play(T.animate.set_value(5000), run_time=2)
        sin_graph2 = sin_graph.copy().set_color(RED)
        
        self.add(sin_graph2)
        self.play(T.animate.set_value(6000), run_time=2)
        sin_graph3 = sin_graph.copy().set_color(GREEN)
        
        self.add(sin_graph3)
        self.play(T.animate.set_value(7000), run_time=2)

class axis(Scene):
    def construct(self):
        l2 = Axes(
            x_range=(-2.5,3.5,0.5),
            # decimal_number_config={"num_decimal_places": 2},
            include_numbers=True,
        )
        l2.add_coordinate_labels(num_decimal_places=1)
        self.add(l2)