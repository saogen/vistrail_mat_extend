#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from string import Template

def main():
    
    module_name = raw_input("module name:")
    in_port_num = int(raw_input("in_port_num:"))
    
#    out_port_num = int(raw_input("out_port_num:"))

# write init.py file    
    os.mkdir(module_name)
    filePath = r'./%s/init.py' %module_name
    outfile = open(filePath,'w')
    
################## in port number and string ########################
    name = []
    c = []
    for i in range(in_port_num):
        name.append('in'+str(i))
        c.append('c'+str(i))
    
    # InputPort
    in_port = ''
    for i in range(in_port_num):
        in_port += '''reg.add_input_port(%s, "%s",
                        (vistrails.core.modules.basic_modules.String, '%s ='))
    ''' %(module_name,name[i],name[i])

    # GetInputData
    in_data = ''
    for i in range(in_port_num):
        in_data +='''%s = "%s"+self.getInputFromPort("%s")
        ''' %(c[i],name[i],name[i])

################## matlab execute data ###############################
    mat_exec = ''
    for i in range(in_port_num):
        mat_exec += '''h.execute(%s)
        '''%c[i]
        

    
################## out port number and string ########################

    # OutputPort
    out_port_1 = '''reg.add_output_port(%s, "answer",
                        (vistrails.core.modules.basic_modules.String, 'the result'))
    ''' %module_name
                   
    out_port = out_port_1 * 1 # out_port_num
    
################## using template to substitute ########################        
    
    lines = []
    template_file = open(r'init.template','r')
    
    tmpl = Template(template_file.read())
    
    lines.append(tmpl.substitute(
                    InputPort = in_port,
                    GetInputData = in_data,
                    OutputPort = out_port,
                    ModuleName = module_name,
                    MatExecInput = mat_exec))          
    
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