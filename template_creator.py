import os
os.add_dll_directory(r"C:\Program Files\GTK3-Runtime Win64\bin")
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

loader = FileSystemLoader('templates')

env = Environment(loader=loader)

template = env.get_template('index.html')

html_out = template.render(
	title='2021 Tax Report',
	year='2021',
	)

if not os.path.isdir('output'):
	os.mkdir('output')

with open('output/index.html', 'w') as file:
	file.write(html_out)

HTML(string=html_out, base_url='templates/').write_pdf('output/index.pdf', stylesheets=["templates/styles.css"])