l = ['one', 'two', 'three']

my_html_list = ''
for word in l:
    #my_list += '<li>' + word + '</li>'
    #my_list += '<li>{}</li>'.format(word)
    my_html_list += f'<li>{word}</li>'

my_html = f'''
<h1>Heading 1</h1>
<p>paragraph</p>
<ol>
    <li>one</li>
    <li>two</li>
</ol>

<ul>
    {my_html_list}
</ul>
'''
f = open('render.html', 'w')
f.write(my_html)
f.close()