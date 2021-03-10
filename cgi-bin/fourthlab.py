#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import *

script = """ <script> 
var canvas = document.getElementById("imgCanvas");
var context = canvas.getContext("2d");

function draw(e) {
    var pos = getMousePos(canvas, e);
    posx = pos.x;
    posy = pos.y;
    context.fillStyle = "#000000";
    context.beginPath();
    context.arc(posx, posy, 10, 0, 2*Math.PI);
    context.fill();
}

function drawR(e) {
    var pos = getMousePos(canvas, e);
    posx = pos.x;
    posy = pos.y;
    context.fillStyle = "red";
    context.beginPath();
    context.rect(posx, posy, 20, 20);
    context.fill();
}

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
      x: evt.clientX - rect.left,
      y: evt.clientY - rect.top
    };
}
</script>
"""

canvas = """
<div id="images"></div>
<canvas width="500" height="500" style="margin:0; border:1px solid; padding:0;position:relative;left:50px;top:50px;" id="imgCanvas" width="250" height="250" onclick="draw(event)" oncontextmenu="drawR(event)"></canvas>
"""

print(canvas)
print(script)