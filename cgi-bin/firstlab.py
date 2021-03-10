#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import *
import cgi

func_hidden = """<script type="text/javascript">
function showHide(element_id) {
    //Если элемент с id-шником element_id существует
    if (document.getElementById(element_id)) {
        //Записываем ссылку на элемент в переменную obj
        var obj = document.getElementById(element_id);
        //Если css-свойство display не block, то:
        if (obj.style.display != "block") {
            obj.style.display = "block"; //Показываем элемент
        }
        else obj.style.display = "none"; //Скрываем элемент
    }
    //Если элемент с id-шником element_id не найден, то выводим сообщение
    else alert("Элемент с id: " + element_id + " не найден!");
}
</script>"""

content = """<div className="contentWrap">
        <div style="font-size:35px; border:1px solid black; padding:5px; width:350px; background-color:whitesmoke">Task: Dev dialog window</div>
        <button onclick="showHide('window')" class="dopinfo">Show/hide window dialog</button>
        <div className="content" id="window" style="display:none; margin-top:50px; font-size:25px; border:1px solid black; padding:5px; width:550px; background-color:whitesmoke">
                Sistema monítoringu servísív kvalífíkovanikh nadavateley elektronnykh elektronnykh dovírchikh poslug Ukraí̈ni
            </div>
        </div>
    """
print(content)
print(func_hidden)
# print(end_of_page)