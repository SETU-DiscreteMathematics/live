from IPython import utils
from IPython.display import display, HTML, Markdown

import os

# load libraries
import numpy as np
import scipy as sci
import sympy as sym
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

from pylab import *

__version__ = 23.2
   
notebook_ih = None

def apply_extra_css_styling(show_message=False):  
    """Update default styles using custom.css (from ipython profile) and then extra.css."""
    
    custom_css = ""
    
    extra_css = open(os.path.join('setup_practical_magic', 'extra.css'), 'r').read()
 
    styles = "<style>\n%s\n\n%s</style>" % (custom_css, extra_css)
    if show_message:
        styles += 'Python practical setup tools version %s. See <a target="_blank" href="https://setu-discretemathematics.github.io/live/00-Module_Introduction/33-Python_Practicals">https://setu-discretemathematics.github.io/live/00-Module_Introduction/33-Python_Practicals</a>' % __version__
    return HTML(styles)

def setup_practical(notebook_state, ih, require_id=True):
    
    global notebook_ih
    notebook_ih = ih

    field_name = 'student_id' if 'student_id' in notebook_state else 'your_student_number' 
    student_id = notebook_state[field_name] if field_name in notebook_state else ''

    if require_id and not student_id:
        js = "<script>alert('Make sure to specify your student ID and your name in the Setup section of this notebook.');</script>"
        display(HTML(js))

    #HTML("Ver " + str(__version__) + ' <a href="http://example.com">link</a>')
    #print ("Ver", __version__)

    # finally setup styles
    return apply_extra_css_styling(True)

from .logic import *

# pytutor

import urllib.parse
from IPython.display import IFrame

def pytutor(code_to_run=None):
    """Run python code via pytutor. """
    if code_to_run is None:
        code_to_run = notebook_ih[-2]
    code_text = urllib.parse.quote(code_to_run.strip()) 
    return IFrame(f"https://pythontutor.com/iframe-embed.html#code={code_text}&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false", width=1300, height=550)
