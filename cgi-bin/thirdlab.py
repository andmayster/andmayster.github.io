#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import *

forms = """
    <div><input type="text" id="input">
    
    <input type="text" id="edit">
    </div>
    <div>
    <button onclick="add()">></button> 
    <button><</button>
    </div>
    <div>
        <div id="list"></div>
    </div>
"""

script = """

<script>
    let arr = []
    
    const add = () => {
       arr.push(document.getElementById('input').value)
    }
    
    const list = () => {
        let list = document.getElementById('list')
        list.innerHTML = 
    
    }
    
    list()
    </script>
"""

print(forms)
print(script)