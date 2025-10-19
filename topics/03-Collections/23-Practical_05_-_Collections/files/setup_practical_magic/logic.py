from IPython import utils
from IPython.display import display, HTML
import itertools
import re

class Gob(object):
    pass

def calculateRow(inputs, outputs, p, ints, *args):
    
    # store inputs in an object context
    g = Gob()
    for a, b in zip(inputs, args): setattr(g, a, b)

    # add object context to any base variables in outputs
    # then evaluate each
    eval_outputs = []
    for item in outputs:
        item = p.sub(r'g.\1', item)
        try:
            eval_outputs.append(eval(item))
        except SyntaxError:
            print('This is not a valid logical expression. Check brackets, case and spelling.')
            return None
        
    # add the inputs and evaluated phrases to create a single row
    row = [getattr(g, b) for b in inputs] + eval_outputs
    if ints:
        return [int(item) for item in row]
    else:
        return row

def logicalStrip(s):
	return s.replace('and','').replace('or','').replace('not','').replace(')','').replace('(','').replace(' ','')

def TruthTable(inputs=None, outputs=None, ints=False):
    
    if type(inputs)==type('') and outputs==None:
        # entered a single expression, get inputs from it 
        tmp = logicalStrip(inputs)
        outputs = [inputs]
        inputs = sorted(list(set(tmp)))
    elif type(inputs)==type(list()) and outputs==None:
        tmp = logicalStrip(" ".join(inputs))
        outputs = inputs[:]
        inputs = sorted(list(set(tmp)))
    elif type(inputs)==type(''):
        inputs = list(inputs)
    else:
        if not inputs:
            raise Exception('You need to specify an expression or a list of inputs.')

    outputs = outputs or []
    if type(outputs)==type(''): outputs = [outputs]
    
    # generate the sets of booleans for the inputs
    inputs_conditions = list(itertools.product([False, True], repeat=len(inputs)))

    # re to match whole words as given in inputs 
    p = re.compile(r'(?<!\w)(' + '|'.join(inputs) + ')(?!\w)')

    # test evaluation - using first row
    if calculateRow(inputs, outputs, p, ints, *inputs_conditions[0]) is None: return
    result = "<table id=\"truthtable\">\n"
    result += "<thead><tr>" + "".join("<th>%s</th>" % c for c in (inputs + outputs)) + "</tr></thead>\n"
    result += "<tbody>\n"
    for conditions_set in inputs_conditions:
        result += "<tr>" + "".join("<td>%s</td>" % c for c in (calculateRow(inputs, outputs, p, ints, *conditions_set))) + "</tr>\n"

            #result += "<th></th>"
        #t = (self.inputs + self.phrases)
        #for conditions_set in self.inputs_conditions:
        #    t += (self.calculate(*conditions_set))
        #    print (self.calculate(*conditions_set))
        #    break
    result += "</tbody>\n</table>"
    return HTML(result)