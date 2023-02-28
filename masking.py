#Assumption: https://example.com/?product=shirt&color=blue&newuser&size=m
#Id starts after = end with &

doc='"https://sube.assets.garantibbva.com.tr/assets/css/addtohomescreen.css?__ctst__=1675217208654&&__mtmt__=121313">'

after_doc= ""

process= False
for element in doc:
    if element == "=":
        process= True
        after_doc+="*"
    elif element == "&":
        process= False
        after_doc+=element
    elif not process:
        after_doc+=element

print(after_doc)

