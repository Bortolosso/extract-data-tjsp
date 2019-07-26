#!/usr/bin/python -tt
# coding: utf-8

from color_terminal import printer

p = printer()
 
p.print(msg="SUCCESS Test...", color="GREEN")
p.print(msg="WARN Test...", color="YELLOW")
p.print(msg="ERROR Test...", color="RED")

