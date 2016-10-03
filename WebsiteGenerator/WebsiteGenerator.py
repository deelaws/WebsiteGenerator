from jinja2 import Environment, PackageLoader
import sys

def generate_index_page(env):
    template = env.get_template('index_template.html')
    a = template.render(title='Waleed\'s website')
    #a = a.encode(sys.stdout.encoding, errors='replace')
    #print(type(a))
    index_file = open('index.html', mode='w', encoding='utf8')
    index_file.writelines(a)
    index_file.flush()
    index_file.close()


if __name__ == "__main__":
    
    print(sys.stdout.encoding)
    pack_load = PackageLoader('WebsiteGenerator', 'html')
    templates = pack_load.list_templates()
        
    # List all the available templates
    for t in templates:
        print(t)

    env = Environment(loader=pack_load)

    generate_index_page(env)