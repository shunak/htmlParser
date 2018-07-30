import lxml.html
import cssselect

# input what you want to pase at x. x=hoge.html
tree = lxml.html.parse('./x')

html = tree.getroot()

for a in html.cssselect('a'):
    print(a.get('href'), a.text)






