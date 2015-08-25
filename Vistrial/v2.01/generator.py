#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from string import Template

def main():

#################################  Get Basic Input #########################    
    module_name = raw_input("module name:")
    print
    in_port_num = int(raw_input("in_port_num:"))
    print
    in_type = []
    
    print "Date type for input ports: " 
    for i in range(in_port_num):
        port_type = raw_input("input port %d type:" %(i+1))
        in_type.append(port_type)
    capitalize_list(in_type)
    print 
    #print in_type
    
    out_port_num = int(raw_input("out_port_num:"))
    print
    out_type = []
    
    print "Data type for output ports: " 
    for i in range(out_port_num):
        port_type = raw_input("output port %d type:" %(i+1))
        out_type.append(port_type)
    capitalize_list(out_type)    
    print 
    #print out_type

################################## Write init.py file ##########################
    
    os.mkdir(module_name)
    filePath = r'./%s/init.py' %module_name
    outfile = open(filePath,'w')
    
    lines = []
    template_file = open(r'init.template','r')
    
    tmpl = Template(template_file.read())
    
    lines.append(tmpl.substitute(
                    ModuleName = module_name,
                    GetInputData = generate_GetInputData(in_port_num),
                    PutValue = generate_PutValue(in_port_num),
                    RunEval = generate_RunEval(in_type),
                    Run = generate_Run(module_name,in_port_num,out_port_num),
                    GetValue = generate_GetValue(out_port_num),
                    SetOutputData = generate_SetOutputData(out_port_num),
                    RegInputPort = generate_RegInputPort(module_name,in_port_num,in_type),
                    RegOutputPort = generate_RegOutputPort(module_name,out_port_num,out_type)))          
    
    outfile.writelines(lines)
    outfile.close()
    
############################ Write __init__.py file ###########################   

    filePath = r'./%s/__init__.py' %module_name
    outfile = open(filePath,'w')
    
    lines = []
    template_file = open(r'__init__.template','r')
    
    tmpl = Template(template_file.read())
    
    lines.append(tmpl.substitute(
                    ModuleName = module_name))
                    
    outfile.writelines(lines)
    outfile.close()    
    
    print 'Generate %s Success !\n' %module_name

############################################################################ 
    
def capitalize_list(list_in):
    for i in range(len(list_in)):
        list_in[i] = list_in[i].capitalize()
    return list_in
  
       
def generate_GetInputData(num):
    """generate GetInputData for template
    input: number of input port
    output: string 
    """
    name = []
    for i in range(num):
        name.append('in'+str(i+1))
        
    res = ''
    for i in range(num):
        res +='''%s = self.getInputFromPort("%s")
        ''' %(name[i],name[i])
    return res
    
def generate_PutValue(num):
    """generate PutValue for template
    input: number of input port
    output: string 
    """
    name = []
    for i in range(num):
        name.append('in'+str(i+1))
        
    res = ''
    for i in range(num):
        res +='''eng.putvalue('%s',%s)
        ''' %(name[i],name[i])
    return res
    
def generate_GetValue(num):
    """generate PutValue for template
    input: number of output port
    output: string 
    """
    name = []
    for i in range(num):
        name.append('o'+str(i+1))
        
    res = ''
    for i in range(num):
        res +='''%s=eng.getvalue('%s').tolist()
        ''' %(name[i],name[i])
    return res
    
def generate_SetOutputData(num):
    """generate SetOutputData for template
    input: number of output port
    output: string 
    """
    name = []
    for i in range(num):
        name.append('o'+str(i+1))
        
    res = ''
    for i in range(num):
        res +='''self.setResult("%s", %s)
        ''' %(name[i],name[i])
    return res
    
def generate_RegInputPort(module_name,num,in_type):
    """docstring for generate_RegInputPort
    register for input port
    input: number of input port
    output: string
    """
    name = []
    for i in range(num):
        name.append('in'+str(i+1))
        
    res = ''
    for i in range(num):
        res +='''reg.add_input_port(%s, "%s",
                       (vistrails.core.modules.basic_modules.%s, '%s input'))
    ''' %(module_name,name[i],in_type[i],i+1)
    return res
    
def generate_RegOutputPort(module_name,num,out_type):
    """docstring for generate_RegOutputPort
    register for output port
    input: number of input port
    output: string
    """
    name = []
    for i in range(num):
        name.append('o'+str(i+1))
        
    res = ''
    for i in range(num):
        res +='''reg.add_output_port(%s, "%s",
                        (vistrails.core.modules.basic_modules.%s, '%s output'))
    ''' %(module_name,name[i],out_type[i],i+1)
    return res
    
def generate_RunEval(in_type):
    """docstring for generate_RunEval
    check how many input 'String' exist. find the index of each string
    generate runeval for each string type
    input: in_type
    output: string
    """
    index = []
    for i in range(len(in_type)):
        if in_type[i] == 'String':
            index.append(i)
            
    res = ''
    for i in range(len(index)):
        res += '''eng.run('in%s = eval(in%s)')
        ''' %(index[i]+1,index[i]+1)
    return res
    
def generate_Run(module_name, in_num, out_num):
    """docstring for generate_Run
    generate Run
    input: module_name, input port number, output port number
    putput: string
    """
    all_out = ''
    for i in range(out_num):
        all_out += 'o%s,' %(i+1)
    all_out = all_out[0:-1]
    
    all_in = ''
    for i in range(in_num):
        all_in += 'in%s,' %(i+1)
    all_in = all_in[0:-1]
    
    res = '''eng.run('[%s]=%s(%s)')
    ''' %(all_out,module_name,all_in)
    return res
    

 
    
def test():
    print generate_GetInputData(3)
    
    print generate_PutValue(3)
    
    print generate_GetValue(3)
    
    print generate_SetOutputData(3)
    
    a = ['string', 'list', 'float']
    print capitalize_list(a)
    
    a = ['string', 'list', 'float']
    print capitalize_list(a)
    print generate_RegInputPort('linprog',3,a)
    
    a = ['string', 'list', 'float']
    print capitalize_list(a)
    print generate_RegOutputPort('linprog',3,a)
    
    a = ['string', 'list', 'float','string']
    print capitalize_list(a)
    print generate_RunEval(a)
    
    print generate_Run('linprog',5,3)
    pass
    
if __name__ == '__main__':
    #test()
    main()
      
