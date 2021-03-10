#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import *

script = """
<script>const getOS = () => {
        if (navigator.appVersion.indexOf('Windows') >= 0) return 'Windows'
        if (navigator.appVersion.indexOf('Linux') >= 0) return 'Linux'
        if (navigator.appVersion.indexOf('Sun') == 0) return 'SunOS'
        if (navigator.appVersion.indexOf('5.0 (Macintosh)') == 0) return 'MacOS'
    }

    console.log(navigator.appVersion)

    const getBrowserId = () => {

        let
            aKeys = ["MSIE", "Firefox", "Safari", "Chrome", "Opera"],
            sUsrAg = navigator.userAgent, nIdx = aKeys.length - 1;

        for (nIdx; nIdx > -1 && sUsrAg.indexOf(aKeys[nIdx]) === -1; nIdx--);

        return (aKeys[nIdx])

    }
    
    document.getElementById('os').value = getOS()
    document.getElementById('browser').value = getBrowserId()
    
    </script> """


html = """<form> 
    <input type="text" id="os">
    <input type="text" id="browser">
</form>"""



print(html)
print(script)
