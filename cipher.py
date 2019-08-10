# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:29:17 2019

@author: jack
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from fpdf import FPDF
import random

seed = 26
shift = 25
input_file = "normal_text.txt"
output_file = "cipher_text.txt"

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ä', 'Ö',
         'Ü', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 
         'ö', 'ü', 'ß', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '°']
         #'€', '@', '[', ']', '(', ')'

def GetTextDimensions(ax, s, textSize):
    r = ax.figure.canvas.get_renderer()
    t = ax.text(0, 0, s, size=textSize, alpha=0)
    bb = t.get_window_extent(renderer=r)
    inv = ax.transData.inverted()
    dbox = inv.transform(bb)
    width = np.abs(dbox[0,0]-dbox[1,0])
    height = np.abs(dbox[0,1]-dbox[1,1])
    return width, height

def PlotChars(characters, d, textSize, ax, outer_radius=None):
#    d = 10
    d1 = d
    d2 = d
#    textSize = 1
    seperator_lines = 1
    count = len(chars)
    angle_fraction = 360 / count
    i = 0
    if outer_radius is None:
        outer_radius = d
    text_shrink = 1.4
    
    ax.axis('off')
    ax.axis("equal")
    ax.set_xlim(-outer_radius, outer_radius)
    ax.set_ylim(-outer_radius, outer_radius)
    
    circle = mpatches.Circle((0,0), d, ec="black", fc="none")
    ax.add_patch(circle)
    circle = mpatches.Circle((0,0), d*0.1, ec="black", fc="none")
    ax.add_patch(circle)
    circle = mpatches.Circle((0,0), d*0.025, ec="black", fc="none")
    ax.add_patch(circle)
    
    width, height = GetTextDimensions(ax, "W", textSize*30)   
    radians = angle_fraction*np.pi/180 * d
    text_scale = radians/(width*text_shrink)
    textSize *= text_scale
    width, height = GetTextDimensions(ax, "W", textSize*30)   
    d1 = d-height * 0.55
    d2 = d-height * 1.3
    
    circle = mpatches.Circle((0,0), d2, ec="black", fc="none")
    ax.add_patch(circle)
    
    #width = ax.transData.inverted(bb.width)
    #height = bb.height
    
    
    for c in characters:
        angle = angle_fraction * i
        x = np.cos(angle*np.pi/180)*d1
        y = np.sin(angle*np.pi/180)*d1
        ax.text(x, y, c, size=textSize*30, rotation=angle+90,
             ha="center", va="center")
        angle = angle_fraction * (i + 0.5)
        x = np.cos(angle*np.pi/180)*d
        y = np.sin(angle*np.pi/180)*d
        x2 = np.cos(angle*np.pi/180)*d2*seperator_lines
        y2 = np.sin(angle*np.pi/180)*d2*seperator_lines
        ax.plot((x,x2),(y,y2), "black")
        i += 1
    ax.set_xlim(-outer_radius, outer_radius)
    ax.set_ylim(-outer_radius, outer_radius)
    return outer_radius, d2

#d is the outer radius
def PlotNumbers(ax, count, d, textSize, relativePosition):
    d1 = d*relativePosition
    d2 = d*relativePosition
    text_d = d1
    angle_fraction = 360 / count
    text_shrink = 1.3
    
    #scale text
    width, height = GetTextDimensions(ax, str(count), textSize*30)   
    radians = angle_fraction*np.pi/180 * text_d
    text_scale = radians/(height*text_shrink)
    textSize *= text_scale
    #scale lines
    width, height = GetTextDimensions(ax, str(count), textSize*30)   
    d1 -= width * 0.6
    d2 += width * 0.6
    
    circle = mpatches.Circle((0,0), d1, ec="black", fc="none")
    ax.add_patch(circle)
    circle = mpatches.Circle((0,0), d2, ec="black", fc="none")
    ax.add_patch(circle)
    
    radians = angle_fraction*np.pi/180 * text_d
    text_scale = radians/(width*text_shrink)
    textSize *= text_scale
    for i in range(count):
        angle = angle_fraction * (i)
        x = np.cos(angle*np.pi/180)*text_d
        y = np.sin(angle*np.pi/180)*text_d
        ax.text(x, y, str(i+1), size=textSize*30, rotation=angle,
             ha="center", va="center")
        angle = angle_fraction * (i + 0.5)
        x = np.cos(angle*np.pi/180)*d1
        y = np.sin(angle*np.pi/180)*d1
        x2 = np.cos(angle*np.pi/180)*d2
        y2 = np.sin(angle*np.pi/180)*d2
        ax.plot((x,x2),(y,y2), "black")
    return d1, d2

def PlotWindow(ax, d1, d2, count):
    angle_fraction = 360 / count
#    angle = angle_fraction * 0.5
#    x = np.cos(angle*np.pi/180)*d1
#    y = np.sin(angle*np.pi/180)*d1
#    x2 = np.cos(angle*np.pi/180)*d2
#    y2 = np.sin(angle*np.pi/180)*d2
#    ax.plot((x,x2),(y,y2), "black")
#    angle = angle_fraction * -0.5
#    x = np.cos(angle*np.pi/180)*d1
#    y = np.sin(angle*np.pi/180)*d1
#    x2 = np.cos(angle*np.pi/180)*d2
#    y2 = np.sin(angle*np.pi/180)*d2
#    ax.plot((x,x2),(y,y2), "black")
    
    wedge1 = mpatches.Wedge((0,0), d2, angle_fraction * -0.5, angle_fraction * 0.5, width = d2-d1, ec="black", fc="none")
    ax.add_patch(wedge1)
#    wedge1 = mpatches.Wedge((0,0), d2, angle_fraction * -0.5, angle_fraction * 0.5, width = 0.1, ec="black", fc="none")
#    ax.add_patch(wedge1)
        
def ScrambleChars(characters, s):
    rand = random.Random(s)
    return rand.sample(characters, len(characters)) 
#    return characters

textSize = 1
plotSize = 10
numberPosition = 0.75
  
fig, ax = plt.subplots(2)
fig.set_size_inches((10, 25))
chars_cipher = ScrambleChars(chars, seed)
dmax, dmin = PlotChars(chars_cipher, plotSize, textSize, ax[1])
PlotChars(chars, dmin, textSize, ax[0], dmax)
d1, d2 = PlotNumbers(ax[1], len(chars), plotSize, textSize, numberPosition)
PlotWindow(ax[0], d1, d2, len(chars))
ax[0].axis("equal")
ax[0].set_aspect('equal')
ax[1].axis("equal")
ax[1].set_aspect('equal')
plt.savefig("cipher_card.pdf", bbox_inches='tight')
plt.show()

with open(input_file) as file:
    text = file.read()
    text = list(text)
    text_cipher = text
    for i in range(0, len(text)):
        try:
            ind = chars.index(text[i])
            ind = (ind + shift) % len(chars_cipher)
            text_cipher[i] = chars_cipher[ind]
        except ValueError:
            text_cipher[i] = text[i]
    with open(output_file, "w") as out_file:
        text_cipher = ''.join(text_cipher)
        out_file.write(text_cipher)
    
A4_width = 210
A4_height = 297
margin = 20     
line_height = 10
offset = 1
pdf = FPDF('P', 'mm', (A4_width,A4_height))
pdf.add_page()
pdf.set_margins(margin, margin)
pdf.set_xy(margin, margin)
pdf.set_font('Courier', 'B', 20)
charWidth = pdf.get_string_width("W")
lines = text_cipher.split("\n")
for line in lines:
    words = line.split(" ")
    total_width = 0
    pdf.set_x(margin)
    for word in words:
        width = pdf.get_string_width(word+" ")
        total_width += width
        #print(word + ": " + str(width) + ", " + str(total_width))
        if(total_width >= (A4_width - 2*margin)):
            #print('ln')
            pdf.ln()
            pdf.ln()
            total_width = width;
        pdf.cell(width, line_height, word+" ", 0)
        if word == '':
            continue
        x1 = margin + total_width - width + offset
        x2 = margin + total_width - pdf.get_string_width(" ") + offset
        y1 = pdf.get_y() + 1.8 * line_height
        y2 = y1
        pdf.line(x1, y1, x2, y2)
        y2 -= line_height * 0.5
        for i in range(len(word)+1):
            pdf.line(x1 + charWidth * i, y1, x1 + charWidth * i, y2)
        
    pdf.ln()
    pdf.ln()
pdf.output('cipher_text.pdf', 'F')