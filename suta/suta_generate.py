#/usr/bin/env python3

from math import sqrt
import sys
import jinja2 

suta_svg_template = jinja2.Template(
'''
<?xml version="1.0" standalone="no"?>
<!-- generated with {{ __file__ }} {{ dx1 }} {{ dx2 }} -->

<svg width="{{ w }}" height="{{ w }}" xmlns="http://www.w3.org/2000/svg">
  <path d="M {{ (w-l)/2 }} {{ h1+(w-l)/2 }}
           h {{ l }}
           c {{ -dx1 }} {{ dy1 }} {{ dx2-l/4 }} {{ dh }} {{ -l/4 }} {{ dh }}
           s {{ dx1-l/4 }} {{ dy1-dh }} {{ -l/4 }} {{ -dh }}
           l {{ -d }} {{ -h1 }}
           v {{ l }}
           l {{ d+l/4 }} {{ -l }}
           v {{ l }} z"
        stroke-width="3" stroke="#000" fill="none"
        stroke-linejoin="round"/>
</svg> 
'''.lstrip())

dx1, dx2 = float(sys.argv[1]), float(sys.argv[2])
w = 300
l = 256
φ = (sqrt(5)+1)/2
h1 = l/(2*φ-1)
d  = l*(φ-1)/2
dy1 = dx1*h1/d
dh = (l-h1)*(2/(2*φ+1)*(2-φ)+2*(2-φ)/3*(φ-1))

print(suta_svg_template.render(locals()))
