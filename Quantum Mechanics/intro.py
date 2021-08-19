from manimlib import *
import numpy as np

class intro(Scene):
    def construct(self):
        self.defination()
    def defination(self):
        sq1 = Rectangle(width=3,height=4,stroke_color=BLUE)
        sq2 = Rectangle(width=3,height=4,stroke_color=BLUE)
        
        texts = VGroup(
            Text("Classical Mechanics",font_name = "Roboto Thin", font_size= 30, color = BLUE),
            Text("Laws of Motion",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Electrodynamics",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Magnetism",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Thermodynamics",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Limitations",font_name = "Roboto Thin", font_size= 30, color = RED),
            Text("Quantum Mechanics",font_name = "Roboto Thin", font_size= 30, color = RED),
            Text("Black Body Radiation",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Photo Electric Effect",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Hydrogen Atom",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("Uncertainty Principal",font_name = "Roboto Thin", font_size= 20, color = WHITE),
            Text("All of Physics",font_name = "Roboto Thin", font_size= 30, color = GREEN),
        )

        texts[0].next_to(sq1,direction=UP)
        texts[5:7].next_to(sq1,direction=UP)

        self.play(Write(texts[0]))
        self.play(DrawBorderThenFill(sq1))

        for each in range(4):
            texts[each+1].next_to(texts[each],direction=DOWN, buff=0.7)
            self.play(Write(texts[each+1]))