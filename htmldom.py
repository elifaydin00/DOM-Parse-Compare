from htmldom import htmldom

dom = htmldom.HtmlDom("https://www.google.com/").createDom()

#Print all links
a = dom.find( "a" )
for link in a:
    print( link.attr( "href" ) )


#Using the dom instance from the above code snippet
div = dom.find( "div" )
# Gets all the children
chldrn = div.children()
print(chldrn)

print(dom.domNodes.keys())

div = dom.find( "div" )
# Gets all the children
chldrn = div.children()
print(chldrn)