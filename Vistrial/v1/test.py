#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from string import Template

def main():
    
    module_name = raw_input("module name:")

# write init.py file    
    os.mkdir(module_name)
    filePath = r'./%s/init.py' %module_name
    outfile = open(filePath,'w')
    
    lines = []
    template_file = open(r'init.template','r')
    
    tmpl = Template(template_file.read())
    
    lines.append(tmpl.substitute(
                    ModuleName = module_name))
                    
    outfile.writelines(lines)
    outfile.close()

# write __init__.py file    
    filePath = r'./%s/__init__.py' %module_name
    outfile = open(filePath,'w')
    lines = []
    template_file = open(r'__init__.template','r')
    
    tmpl = Template(template_file.read())
    
    lines.append(tmpl.substitute(
                    ModuleName = module_name))
                    
    outfile.writelines(lines)
    outfile.close()    
    
    print 'generate %s over !\n' %module_name

if __name__ == '__main__':
    main()