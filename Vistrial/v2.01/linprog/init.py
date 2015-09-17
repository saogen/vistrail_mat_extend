
import vistrails.core.modules.module_registry
from vistrails.core.modules.vistrails_module import Module, ModuleError
from vistrails.core.modules.module_registry import get_module_registry
import pymatlab as py

################################################################################

# linprog

class linprog(Module):
    def __init__(self):
        Module.__init__(self)

    def compute(self):
        in1 = self.getInputFromPort("in1")
        in2 = self.getInputFromPort("in2")
        in3 = self.getInputFromPort("in3")
        in4 = self.getInputFromPort("in4")
        in5 = self.getInputFromPort("in5")
        in6 = self.getInputFromPort("in6")
        
  
        eng=py.session_factory()
        
        eng.putvalue('in1',in1)
        eng.putvalue('in2',in2)
        eng.putvalue('in3',in3)
        eng.putvalue('in4',in4)
        eng.putvalue('in5',in5)
        eng.putvalue('in6',in6)
        
        
        
        
        eng.run('[o1,o2,o3]=linprog(in1,in2,in3,in4,in5,in6)')
    
        
        o1=eng.getvalue('o1').tolist()
        o2=eng.getvalue('o2').tolist()
        o3=eng.getvalue('o3').tolist()
        
        
        self.setResult("o1", o1)
        self.setResult("o2", o2)
        self.setResult("o3", o3)
        

       
################################################################################
def initialize(*args, **keywords):
    reg = get_module_registry()

    reg.add_module(linprog)

    reg.add_input_port(linprog, "in1",
                       (vistrails.core.modules.basic_modules.List, '1 input'))
    reg.add_input_port(linprog, "in2",
                       (vistrails.core.modules.basic_modules.List, '2 input'))
    reg.add_input_port(linprog, "in3",
                       (vistrails.core.modules.basic_modules.List, '3 input'))
    reg.add_input_port(linprog, "in4",
                       (vistrails.core.modules.basic_modules.List, '4 input'))
    reg.add_input_port(linprog, "in5",
                       (vistrails.core.modules.basic_modules.List, '5 input'))
    reg.add_input_port(linprog, "in6",
                       (vistrails.core.modules.basic_modules.List, '6 input'))
    

    reg.add_output_port(linprog, "o1",
                        (vistrails.core.modules.basic_modules.List, '1 output'))
    reg.add_output_port(linprog, "o2",
                        (vistrails.core.modules.basic_modules.Float, '2 output'))
    reg.add_output_port(linprog, "o3",
                        (vistrails.core.modules.basic_modules.Float, '3 output'))
    

