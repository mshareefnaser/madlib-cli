import re  # regular expression
def read_template (path):
    with open(path) as file:
        content = file.read()
        return content
def parse_template(content): 
    lst=[]
    res = re.findall(r'\{.*?\}', content) 
    for i in res:
        lst.append(i.strip("{ }")) 
    return lst
