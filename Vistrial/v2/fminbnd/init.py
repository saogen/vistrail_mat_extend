
import vistrails.core.modules.module_registry
from vistrails.core.modules.vistrails_module import Module, ModuleError
from vistrails.core.modules.module_registry import get_module_registry
import pymatlab as py

################################################################################

# fminbnd

class fminbnd(Module):
    def __init__(self):
        Module.__init__(self)

    def compute(self):
        in1 = self.getInputFromPort("in1")
        in2 = self.getInputFromPort("in2")
        in3 = self.getInputFromPort("in3")
        
  
        eng=py.session_factory()
        
        eng.putvalue('in1',in1)
        eng.putvalue('in2',in2)
        eng.putvalue('in3',in3)
        
        
        eng.run('in1 = eval(in1)')
        
        
        eng.run('[o1,o2,o3]=fminbnd(in1,in2,in3)')
    
        
        o1=eng.getvalue('o1').tolist()
        o2=eng.getvalue('o2').tolist()
        o3=eng.getvalue('o3').tolist()
        
        
        self.setResult("o1", o1)
        self.setResult("o2", o2)
        self.setResult("o3", o3)
        

       
################################################################################
def initialize(*args, **keywords):
    reg = get_module_registry()

    reg.add_module(fminbnd)

    reg.add_input_port(fminbnd, "in1",
                       (vistrails.core.modules.basic_modules.String, '1 input'))
    reg.add_input_port(fminbnd, "in2",
                       (vistrails.core.modules.basic_modules.List, '2 input'))
    reg.add_input_port(fminbnd, "in3",
                       (vistrails.core.modules.basic_modules.List, '3 input'))
    

    reg.add_output_port(fminbnd, "o1",
                        (vistrails.core.modules.basic_modules.Float, '1 output'))
    reg.add_output_port(fminbnd, "o2",
                        (vistrails.core.modules.basic_modules.Float, '2 output'))
    reg.add_output_port(fminbnd, "o3",
                        (vistrails.core.modules.basic_modules.Float, '3 output'))
    

