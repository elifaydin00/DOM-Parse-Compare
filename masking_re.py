#Assumption: https://example.com/?product=shirt&color=blue&newuser&size=m
#Id starts after = end with &

import re

#original_string = "https://sube.assets.garantibbva.com.tr/assets/css/addtohomescreen.css?__ctst__=1675217208654&&__mtmt__=121313"
original_string='''</script>
    <link rel="stylesheet"
        href="https://sube.assets.garantibbva.com.tr/assets/css/bootstrap-login.css?__ctst__=1675217164787">
    <link rel="stylesheet"
        href="https://sube.assets.garantibbva.com.tr/assets/css/bootstrap-login-utility.css?__ctst__=1675217164787">
    <link rel="stylesheet"
        href="https://sube.assets.garantibbva.com.tr/assets/css/gt-facelift-login-style.css?__ctst__=1675217164787">
    <script type="text/javascript"
        src="https://sube.a'''
# Replacing the integers with A and B
modified_string = re.sub(r'(?<=__ctst__=)\d+', 'A', original_string)
modified_string = re.sub(r'(?<=__mtmt__=)\d+', 'B', modified_string)

print(modified_string)