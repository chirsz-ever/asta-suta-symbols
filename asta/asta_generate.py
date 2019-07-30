#/usr/bin/env python3

from math import sin,cos,sqrt,pi
import sys
import jinja2 

asta_svg_template = jinja2.Template(
'''
<?xml version="1.0" standalone="no"?>
<!-- generated with {{ __file__ }} {{ angle }} {{ ratio1 }} {{ ratio2 }} -->

<svg width="{{ w }}" height="{{ w }}" xmlns="http://www.w3.org/2000/svg">
  <path d="M {{ (w-l)/2 }} {{ (w+l)/2 }}
           a {{ r1 }} {{ r1 }} 0 0 1 {{ l - y1 }} {{ -y1 }}
           a {{ ra }} {{ ratio1 * ra }} 45 0 1 {{ sqrt(2)*ra }} {{ sqrt(2)*ra }}
           a {{ ra/2 }} {{ ra/2*ratio2 }} 45 0 1 {{ -sqrt(0.5)*ra }} {{ -sqrt(0.5)*ra }}
           l 128 -128 h -256 l 256 256 z"
        stroke-width="3" stroke="#000" fill="none"
        stroke-linejoin="round"/>
</svg> 
'''.lstrip())

argv = sys.argv
angle, ratio1, ratio2 = float(argv[1]), float(argv[2]), float(argv[3])
θ = angle*pi/180

w = 300
l = 256

r1 = sqrt(2) * l / (2 * sin(θ))
y1 = 0.5 * l + sqrt(2) * (1 - cos(θ)) * r1 / 2
ra = r1 * (1 - cos(θ))

print(asta_svg_template.render(locals()))
