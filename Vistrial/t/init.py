import vistrails.core.modules.module_registry
from vistrails.core.modules.vistrails_module import Module, ModuleError
import pymatlab

###############################################################################
# t

class t(Module):
    """t is a module that output to matlab function."""

    def __init__(self):
        Module.__init__(self)

    def compute(self):
        
        c0 = "in0"+self.getInputFromPort("in0")
        c1 = "in1"+self.getInputFromPort("in1")
        c2 = "in2"+self.getInputFromPort("in2")
        

        ####### start matlab platform
        m = pymatlab.session_factory()
        #######
        
        ####### input several variables in matlab
        
        m.putvalue('in0',c0)
        m.putvalue('in1',c1)
        m.putvalue('in2',c2)
        
        
        #######
        
        m.run("ret = t(c0,c1,c2)")
        result = m.getvalue('ret')
        
        
        ####### set result to store the result to "answer"
        self.setResult("answer", result)
        #########################################

###############################################################################
# the function initialize is called for each package, after all
# packages have been loaded. It is used to register the module with
# the VisTrails runtime.

def initialize(*args, **keywords):

    reg = vistrails.core.modules.module_registry.get_module_registry()

    reg.add_module(t)

################################ add output port ##############################
    reg.add_output_port(t, "answer",
                        (vistrails.core.modules.basic_modules.String, 'the result'))
    
                        
################################ add input port ###############################
    reg.add_input_port(t, "in0",
                        (vistrails.core.modules.basic_modules.String, 'in0 ='))
    reg.add_input_port(t, "in1",
                        (vistrails.core.modules.basic_modules.String, 'in1 ='))
    reg.add_input_port(t, "in2",
                        (vistrails.core.modules.basic_modules.String, 'in2 ='))
    
