import doctest
import re
# from bs4 import BeautifulSoup

# with open('index.html', 'r') as f:
#     soup = BeautifulSoup(f, 'html.parser')


# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print(soup.file_all('a'))
# print(soup.find(id='link3'))
# print(soup.get_text())

# soup = BeautifulSoup('<html>A Web Page</html>', 'html.parser')
# print(BeautifulSoup("<html><head></head><body>Sacr&eacute; bleu!</body></html>", "html.parser"))

#########################################
#            Kinds of Object            #
#########################################

# Tag
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
# tag = soup.b
# print(type(tag))
# print(tag)

# Name
# print(tag.name)
# tag.name = 'blockquote'
# print(tag)

# Attributes
# tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
# print(tag['id'])

# print(tag.attrs)
# tag['id'] = 'verybold'
# tag['another-attribute'] = 1
# print(tag)

# del tag['id']
# del tag['another-attribute']
# print(tag)

# print(tag['id']) # Cause error cause the tag['id'] is already deleted
# print(tag.get('id'))

# Multi-valued attributes
# css_soup = BeautifulSoup('<p class="body"></p>', 'html.parser')
# print(css_soup.p['class'])

# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
# print(css_soup.p['class'])

# id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
# print(id_soup.p['id'])

# rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', 'html.parser')
# print(rel_soup.a['rel'])
# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)

# no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
# print(no_list_soup.p['class'])

# id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
# print(id_soup.p.get_attribute_list('id'))

# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
# print(xml_soup.p['class'])

# class_is_multi = {'*' : 'class'}
# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
# print(xml_soup.p['class'])

# Not Necessary to code this but okay...
# This is to avoid HTML specification
# from bs4.builder import builder_registry
# builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES

# NavigableString
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
# tag = soup.b
# print(tag.string)
# print(type(tag.string))

# unicode_string = str(tag.string)
# print(unicode_string)
# print(type(unicode_string))

# tag.string.replace_with("No Longer Bold")
# print(tag)

# BeautifulSoup
# doc = BeautifulSoup('<document><content/>INSERT FOOTER HERE</document', 'xml')
# footer = BeautifulSoup('<footer>Here\'s the footer</footer>', 'xml')
# print(doc.find(text="INSERT FOOTER HERE").replace_with(footer))
# print(doc)
# print(soup.name)

# Comments and other special strings
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'html.parser')
# comment = soup.b.string
# print(type(comment))
# print(comment)

# print(soup.b.prettify())
# from bs4 import CData
# cdata = CData('A CDATA block')
# comment.replace_with(cdata)
# print(soup.b.prettify())



###################
# NAVIGATING TREE #
###################

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# Going down

# Navigating using tag names
# print(soup.head)
# print(soup.title)
# print(soup.body.b)
# print(soup.a)
# print(soup.find_all('a'))

# .contents and .children
# head_tag = soup.head
# print(head_tag)
# print(head_tag.contents)

# title_tag = head_tag.contents[0]
# print(title_tag)
# print(title_tag.contents)

# Confusing Huh?
# print(len(soup.contents))
# print(soup.contents[0].name)

# text = title_tag.contents[0]
# print(text.contents) # output error, string can't contain anything

# for child in title_tag.children:
#     print(child)

# .decendants
# print(head_tag.contents)

# for child in head_tag.descendants:
#     print(child)

# print(len(list(soup.children)))
# print(len(list(soup.descendants)))

# .string
# print(title_tag.string)

# print(head_tag.contents)
# print(head_tag.string)

# print(soup.html.string)

# .strings and stipped_strings
# for string in soup.strings:
#     print(repr(string))
#     '\n'

# for string in soup.stripped_strings:
#     print(repr(string))

# Going up
# .parent

# title_tag = soup.title
# print(title_tag)
# print(title_tag.parent)

# print(title_tag.string.parent)

# html_tag = soup.html
# print(type(html_tag.parent))
# print(soup.parent)

# .parents not .parent
# link = soup.a
# print(link)
# for parent in link.parents:
#     print(parent.name)

# Going sideways
# sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>", 'html.parser')
# print(sibling_soup.prettify())

# .next_sibling and .previous_sibling
# print(sibling_soup.b.next_sibling)
# print(sibling_soup.c.previous_sibling)
# print(sibling_soup.b.previous_sibling)
# print(sibling_soup.c.next_sibling)

# print(sibling_soup.b.string)
# print(sibling_soup.b.string.next_sibling)

# link = soup.a
# print(link)
# print(link.next_sibling)
# print(link.next_sibling.next_sibling)

# .next_siblings and .previous_siblings
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))

# for sibling in soup.find(id="link3").previous_siblings:
#     print(repr(sibling))

# Going back and forth
# .next_element and .previous_element

# last_a_tag = soup.find('a', id='link3')
# print(last_a_tag)
# print(last_a_tag.next_sibling)
# print(last_a_tag.next_element)

# print(last_a_tag.previous_element)
# print(last_a_tag.previous_element.next_element)

# .next_elements and .previous_elements
# for element in last_a_tag.next_elements:
#     print(repr(element))

#################################
#       Searching the tree      #
#################################

# Kinds of filters

# A string
# print(soup.find_all('b'))

# A regular expression
# for tag in soup.find_all(re.compile("^b")):
#     print(tag.name)

# for tag in soup.find_all(re.compile("t")):
#     print(tag.name)

# A list
# print(soup.find_all(['a', 'b']))

# True
# for tag in soup.find_all(True):
#     print(tag.name)

# A function
# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# print(soup.find_all(has_class_but_no_id))

# def not_lacie(href):
#     return href and not re.compile('lacie').search(href)

# print(soup.find_all(href=not_lacie))

# from bs4 import NavigableString
# def surrounded_by_strings(tag):
#     return (isinstance(tag.next_element, NavigableString) and isinstance(tag.previous_element, NavigableString))

# for tag in soup.find_all(surrounded_by_strings):
#     print(tag.name)

# find_all()
# print(soup.find_all('title'))
# print(soup.find_all('p', 'title'))
# print(soup.find_all('a'))
# print(soup.find_all(id='link2'))
# print(soup.find(string=re.compile('sisters')))

# The name argument
# print(soup.find_all('title'))
# print(soup.find_all(id='link2'))
# print(soup.find_all(href=re.compile('elsie')))
# print(soup.find_all(id=True))
# print(soup.find_all(href=re.compile('elsie'), id='link1'))

# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'html.parser')
# print(data_soup.find_all(data-foo='value')) # Causes error
# print(data_soup.find_all(attrs={'data-foo' : 'value'}))

# name_soup = BeautifulSoup('<input name="email"/>', 'html.parser')
# print(name_soup.find_all(name='email'))
# print(name_soup.find_all(attrs={'name' : 'email'}))

# Searching by CSS class
# print(soup.find_all('a', class_='sister'))
# print(soup.find_all(class_=re.compile('itl')))

# def has_six_characters(css_class):
#     return css_class is not None and len(css_class) == 6

# print(soup.find_all(class_=has_six_characters))

# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
# print(css_soup.find_all('p', class_='stikeout'))
# print(css_soup.find_all('p', class_='body'))
# print(css_soup.find_all('p', class_='body strikeout'))
# print(css_soup.find_all('p', class_='strikeout body'))
# print(soup.find_all('a', attrs={'class' : 'sister'}))

# The string argument
# print(soup.find_all(string='Elsie'))
# print(soup.find_all(string=['Tillie', 'Elsie', 'Lacie']))
# print(soup.find_all(string=re.compile('Dormouse')))

# def is_the_only_string_within_a_tag(s):
#     """"Return True if this string is the only child of its parent tag. """
#     return (s == s.parent.string)

# print(soup.find_all(string=is_the_only_string_within_a_tag))
# print(soup.find_all('a', string='Elsie'))
# print(soup.find_all('a', text='Elsie'))

# The limit argument
# print(soup.find_all('a', limit=2))

# The recursive argument
# print(soup.html.find_all('title'))
# print(soup.html.find_all('title', recursive=False))

# Calling a tag is like calling find_all()
# print(soup.find_all('a'))
# print(soup('a'))

# print(soup.title.find_all(string=True))
# print(soup.title(string=True))

# find()
# print(soup.find_all('title', limit=1))
# print(soup.find('title'))
# print(soup.find('nosuchtag'))
# print(soup.head.title)
# print(soup.find('head').find('title'))

# find_parents() and find_parent()
# a_string = soup.find(string="Lacie")
# print(a_string)
# print(a_string.find_parents('a'))
# print(a_string.find_parent('p'))
# print(a_string.find_parents('p', class_='title'))

# find_next_siblings() and find_next_sibling()
# first_link = soup.a
# print(first_link)
# print(first_link.find_next_siblings('a'))
# first_story_paragraph = soup.find('p', 'story')
# print(first_story_paragraph.find_next_sibling('p'))

# find_previous_siblings() and find_previous_sibling()
# last_link = soup.find('a', id='link3')
# print(last_link)
# print(last_link.find_previous_siblings('a'))

# first_story_paragraph = soup.find('p', 'story')
# print(first_story_paragraph.find_previous_sibling('p'))

# find_all_next() and find_next()
# first_link = soup.a
# print(first_link)
# print(first_link.find_all_next(string=True))
# print(first_link.find_next('p'))

# find_all_previous() and find_previous()
# first_link = soup.a
# print(first_link)
# print(first_link.find_all_previous('p'))
# print(first_link.find_previous('title'))

# CSS selectors
# find tags:
# print(soup.select('title'))
# print(soup.select('p:nth-of-type(3)'))

# find tags beneath other tags:
# print(soup.select('body a'))
# print(soup.select('html head title'))

# Find tags directly beneath other tags:
# print(soup.select('head > title'))
# print(soup.select('p > a'))
# print(soup.select('p > a:nth-of-type(2)'))
# print(soup.select('p > #link1'))
# print(soup.select('body > a'))

# Find the siblings of tags:
# print(soup.select('#link1 ~ .sister'))
# print(soup.select('#link1 + .sister'))

# Find tags by CSS class:
# print(soup.select('.sister'))
# print(soup.select('[class~=sister]'))

# Find tags by ID:
# print(soup.select('#link1'))
# print(soup.select('a#link2'))

# Find tags that match any selector from a list of selectors:
# print(soup.select('#link1, #link2'))

# Test for the existence of an attribute:
# print(soup.select('a[href]'))

# Find tags by attribute value:
# print(soup.select('a[href="http://example.com/elsie"]'))
# print(soup.select('a[href^="http://example.com/"]'))
# print(soup.select('a[href$="tillie"]'))
# print(soup.select('a[href*=".com/el"]'))

# There's also a method called select_one(), which finds only the first tag that matches a selector:
# print(soup.select_one('.sister'))

# If you've parsed SML that defines namespaces, you can use them in CSS selectors:
# xml = """<tag xmlns:ns1="http://namespace1/" xmlns:ns2="http://namespace2/>"
# <ns1:child>I'm in namespace 1</ns1:child>
# <ns2:child>I'm in namespace 2</ns2:child>
# </tag> """
# soup = BeautifulSoup(xml, 'xml')
# print(soup.select('child'))
# print(soup.select('ns1|child'))

# namespaces = dict(first='http://namespace1/', second='http://namespace2/')
# print(soup.select('second|child', namespaces=namespaces))


############################################
#            Modifying the tree            #
############################################

# Changing tag names and attributes
# soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
# tag = soup.b

# tag.name = "blockquote"
# tag['class'] = 'very bold'
# tag['id'] = 1
# print(tag)

# del tag['class']
# del tag['id']
# print(tag)

# Modfying .string
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# tag = soup.a
# tag.string = "New link text."
# print(tag)

# append()
# soup = BeautifulSoup('<a>Foo</a>', 'html.parser')
# soup.a.append('Bar')
# print(soup)
# print(soup.a.contents)

# extend()
# soup = BeautifulSoup('<a>Soup</a>', 'html.parser')
# soup.a.extend(["'s", " ", "on"])
# print(soup)
# print(soup.a.contents)

# NavigableString() and .new_tag()
# soup = BeautifulSoup("<b></b>", 'html.parser')
# tag = soup.b
# tag.append('Hello')
# new_string = NavigableString(' there')
# tag.append(new_string)
# print(tag)
# print(tag.contents)

# from bs4 import Comment
# new_comment = Comment('Nice to see you.')
# tag.append(new_comment)
# print(tag)
# print(tag.contents)

# soup = BeautifulSoup('<b></b>', 'html.parser')
# original_tag = soup.b
# new_tag = soup.new_tag('a', href="http://www.example.com")
# original_tag.append(new_tag)
# print(original_tag)
# new_tag.string = "Link text."
# print(original_tag)

# insert()
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# tag = soup.a
# tag.insert(1, "but did not endorse ")
# print(tag)
# print(tag.contents)

# insert_before() and insert_after()
# soup = BeautifulSoup('<b>leave</b>', 'html.parser')
# tag = soup.new_tag('i')
# tag.string = "Don't"
# soup.b.string.insert_before(tag)
# print(soup.b)

# div = soup.new_tag('div')
# div.string = 'ever'
# soup.b.i.insert_after(' you ', div)
# print(soup.b)
# print(soup.b.contents)

# clear()
# markup = '<a href="http://example.com/">I linked to <i>example</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# tag = soup.a
# tag.clear()
# print(tag)

# extract()
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# a_tag = soup.a
# i_tag = soup.i.extract()
# print(a_tag)
# print(i_tag)
# print(i_tag.parent)

# my_string = i_tag.string.extract()
# print(my_string)
# print(my_string.parent)
# print(i_tag)

# decompose()
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# a_tag = soup.a
# i_tag = soup.i
# i_tag.decompose()
# print(a_tag)
# print(i_tag.decomposed)
# print(a_tag.decomposed)

# replace_with()
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# a_tag = soup.a
# new_tag = soup.new_tag('b')
# new_tag.string = 'example.com'
# a_tag.i.replace_with(new_tag)
# print(a_tag)
# bold_tag = soup.new_tag('b')
# bold_tag.string = 'example'
# i_tag = soup.new_tag('i')
# i_tag.string = 'net'
# a_tag.b.replace_with(bold_tag, '.', i_tag)
# print(a_tag)

# wrap()
# soup = BeautifulSoup('<p>I wish I was bold.</p>', 'html.parser')
# print(soup.p.string.wrap(soup.new_tag('b')))
# print(soup.p.wrap(soup.new_tag('div')))

# unwrap()
# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# a_tag = soup.a
# a_tag.i.unwrap()
# print(a_tag)

# smooth()
# soup = BeautifulSoup('<p>A one</p>', 'html.parser')
# soup.p.append(', a two')
# print(soup.p.contents)
# print(soup.p.encode())
# print(soup.p.prettify())
# soup.smooth()
# print(soup.p.contents)
# print(soup.p.prettify())

###############################
#            Output           #
###############################

# Pretty-printing
# markup = '<html><head><body><a href="http://example.com/">I linked to <i>example.com</i></a>'
# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.prettify())
# print(soup.a.prettify())

# Non-pretty printing
# print(str(soup))
# print(str(soup.a))

# soup = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.", 'html.parser')
# print(str(soup))
# print(soup.encode('utf8'))

# soup = BeautifulSoup('<p>The law firm of Dewey, Cheatem, & Howe</p>', 'html.parser')
# print(soup.p)

# soup = BeautifulSoup('<a href="http://example.com/?foo=val1&bar=val2">A link</a>', 'html.parser')
# print(soup.a)

# french = '<p>Il a dit &lt;&lt;Sacr&eacute; bleu!&gt;&gt;</p>'
# soup = BeautifulSoup(french, 'html.parser')
# print(soup.prettify(formatter='minimal'))
# print(soup.prettify(formatter='html'))

# br = BeautifulSoup('<br>', 'html.parser').br
# print(br.encode(formatter='html'))
# print(br.encode(formatter='html5'))

# option = BeautifulSoup('<option selected=""></option>').option
# print(option.encode(formatter='html'))
# print(option.encode(formatter='html5'))

# print(soup.prettify(formatter=None))

# link_soup = BeautifulSoup('<a href="http://example.com/?foo=val1&bar=val2">A link</a>', 'html.parser')
# print(link_soup.a.encode(formatter=None))

# from bs4.formatter import HTMLFormatter

# def uppercase(str):
#     return str.upper()

# formatter = HTMLFormatter(uppercase)
# print(soup.prettify(formatter=formatter))
# print(link_soup.a.prettify(formatter=formatter))

# formatter = HTMLFormatter(indent=8)
# print(link_soup.a.prettify(formatter=formatter))

# attr_soup = BeautifulSoup(b'<p z="1" m="2" a="3"></p>', 'html.parser')
# print(attr_soup.p.encode())

# class UnsortedAttributes(HTMLFormatter):
#     def attributes(self, tag):
#         for k, v in tag.attrs.items():
#             if k == 'm':
#                 continue
#             yield k, v

# print(attr_soup.p.encode(formatter=UnsortedAttributes()))

# from bs4.element import CData
# soup = BeautifulSoup('<a></a>', 'html.parser')
# soup.a.string = CData('one < three')
# print(soup.a.prettify(formatter='html'))

# get_text()
# markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.get_text())
# print(soup.i.get_text())
# print(soup.get_text("|"))
# print(soup.get_text("|", strip="True"))
# print(text for text in soup.stripped_strings)

######################################################
#            Specifying the parser to use            #
######################################################

# Differences between parsers
# print(BeautifulSoup('<a></b></a>', 'html.parser'))
# print(BeautifulSoup('<a></b></a>', 'xml'))
# print(BeautifulSoup('<a></p>', 'lxml'))
# print(BeautifulSoup('<a></p>', 'html5lib'))
# print(BeautifulSoup('<a></p>', 'html.parser'))

###################################
#            Encodings            #
###################################

# markup = "<h1>Sacr\xc3\xa9 bleu!</h1>"
# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.h1)
# print(soup.h1.string)
# print(soup.original_encoding)

# markup = b'<h1>\xed\xe5\xec\xf9</h1>'
# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.h1)
# print(soup.original_encoding)

# soup = BeautifulSoup(markup, 'html.parser', from_encoding='iso-8859-8')
# print(soup.h1)
# print(soup.original_encoding)

# soup = BeautifulSoup(markup, 'html.parser', exclude_encodings=['iso-8859-7'])
# print(soup.h1)
# print(soup.original_encoding)

# Output encoding
# markup = b'''
# <html>
#     <head>
#         <meta content="text/html; charset=ISO-Latin-1" http-equiv="Content-type" />
#     </head>
#     <body>
#         <p>Sacr\xe9 bleu!</p>
#     </body>
# </html>
# '''

# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.prettify())
# print(soup.prettify("latin-1"))
# print(soup.p.encode('latin-1'))
# print(soup.p.encode('utf-8'))

# markup = u'<b>\N{SNOWMAN}</b>'
# snowman_soup = BeautifulSoup(markup, 'html.parser')
# tag = snowman_soup.b
# print(tag.encode('utf-8'))
# print(tag.encode('latin-1'))
# print(tag.encode('ascii'))

# Unicode, Dammit
# from bs4 import UnicodeDammit
# dammit = UnicodeDammit('Sacr\xc3\xa9 bleu!')
# print(dammit.unicode_markup)
# print(dammit.original_encoding)

# dammit = UnicodeDammit('Sacr\xe9 bleu!', ['latin-1', 'iso-8859-1'])
# print(dammit.unicode_markup)
# print(dammit.original_encoding)

# Smart quotes
# markup = b'<p>I just \x93love\x94 Microsoft Word\x92s smart quotes</p>'
# print(UnicodeDammit(markup, ['windows-1252'], smart_quotes_to='html').unicode_markup)
# print(UnicodeDammit(markup, ['windows-1252'], smart_quotes_to='xml').unicode_markup)
# print(UnicodeDammit(markup, ['windows-1252'], smart_quotes_to='ascii').unicode_markup)
# print(UnicodeDammit(markup, ['windows-1252']).unicode_markup)

# Inconsistent encodings
# snowmen = (u"\N{SNOWMAN}" * 3)
# quote = (u"\N{LEFT DOUBLE QUOTATION MARK}I like snowmen!\N{RIGHT DOUBLE QUOTATION MARK}")
# doc = snowmen.encode('utf8') + quote.encode('windows_1252')
# print(doc)
# print(doc.decode('windows-1252'))

# new_doc = UnicodeDammit.detwingle(doc)
# print(new_doc.decode('utf8'))

######################################
#            Line numbers            #
######################################

# markup = "<p\n>Paragraph 1</p>\n    <p>Paragraph 2</p>"
# soup = BeautifulSoup(markup, 'html.parser')
# for tag in soup.find_all('p'):
#     print(repr((tag.sourceline, tag.sourcepos, tag.string)))

# soup = BeautifulSoup(markup, 'html5lib')
# for tag in soup.find_all('p'):
#     print(repr((tag.sourceline, tag.sourcepos, tag.string)))

# markup = '<p\n>Paragraph 1</p>\n    <p>Paragraph 2</p>'
# soup = BeautifulSoup(markup, 'html.parser', store_line_numbers=False)
# print(soup.p.sourceline)

########################################################
#            Comparing objects for equality            #
########################################################

# markup = "<p>I want <b>pizza</b> and more <b>pizza</b>!</p>"
# soup = BeautifulSoup(markup, 'html.parser')
# first_b, second_b = soup.find_all('b')
# print(first_b == second_b)
# print(first_b.previous_element == second_b.previous_element)
# print(first_b is second_b)

########################################################
#            Copying Beautiful Soup objects            #
########################################################

# import copy
# p_copy = copy.copy(soup.p)
# print(p_copy)
# print(soup.p == p_copy)
# print(soup.p is p_copy)
# print(p_copy.parent)

#######################################################
#            Advanced parser customization            #
#######################################################
# Parsing only part of a document

# SoupStrainer
# from bs4 import SoupStrainer

# only_a_tags = SoupStrainer('a')
# only_tags_with_id_link2 = SoupStrainer(id='link2')

# def is_short_string(string):
#     return string is not None and len(string) < 10

# only_short_strings = SoupStrainer(string=is_short_string)

# print(BeautifulSoup(html_doc, 'html.parser', parse_only=only_a_tags).prettify())
# print(BeautifulSoup(html_doc, 'html.parser', parse_only=only_tags_with_id_link2).prettify())
# print(BeautifulSoup(html_doc, 'html.parser', parse_only=only_short_strings).prettify())

# soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.find_all(only_short_strings))

# Customizing multi-valued attributes
# markup = '<a class="cls1 cls2" id="id1 id2">'
# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.a['class'])
# print(soup.a['id'])

# soup = BeautifulSoup(markup, 'html.parser', multi_valued_attributes=None)
# print(soup.a['class'])
# print(soup.a['id'])

# Handling duplicate attributes
# markup = '<a href="http://url1/" href="http://url2/">'
# soup = BeautifulSoup(markup, 'html.parser')
# print(soup.a['href'])

# soup = BeautifulSoup(markup, 'html.parser', on_duplicate_attribute='replace')
# print(soup.a['href'])

# soup = BeautifulSoup(markup, 'html.parser', on_duplicate_attribute='ignore')
# print(soup.a['href'])

# def accumulate(attributes_so_far, key, value):
#     if not isinstance(attributes_so_far[key], list):
#         attributes_so_far[key] = [attributes_so_far[key]]
#     attributes_so_far[key].append(value)

# soup = BeautifulSoup(markup, 'html.parser', on_duplicate_attribute=accumulate)
# print(soup.a['href'])

# Instantiating custom subclasses

# from bs4 import Tag, NavigableString

# class MyTag(Tag):
#     pass

# class MyString(NavigableString):
#     pass

# markup = '<div>some text</div>'
# soup = BeautifulSoup(markup, 'html.parser')
# print(isinstance(soup.div, MyTag))
# print(isinstance(soup.div.string, MyString))

# my_classes = { Tag: MyTag, NavigableString: MyString}
# soup = BeautifulSoup(markup, 'html.parser', element_classes=my_classes)
# print(isinstance(soup.div, MyTag))
# print(isinstance(soup.div.string, MyString))

#########################################
#            Troubleshooting            #
#########################################

# diagnose()
from bs4.diagnose import diagnose
with open('index.html') as fp:
    data = fp.read()
print(diagnose(data))