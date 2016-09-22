from jinja2 import Environment, PackageLoader



env = Environment(loader=PackageLoader('WebsiteGenerator', 'html'))

template = env.get_template('index_template.html')

print(template.render(title="Main Page"))

print("==========================================")