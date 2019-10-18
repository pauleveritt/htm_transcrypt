# __pragma__ ('skip')
from htm import htm

# __pragma__ ('noskip')

# __pragma__ ('ecom')
'''?
__pragma__('js', 'const htmjs = require("htm");')
def htm(h):
    def _htm(string):
        raise Exception("not supported")
    def wrapped_h(type, props, *children):
        return h(type, props, children)
    def func(strings, values):
        return htmjs.call(wrapped_h, strings, *values)
    _htm.func = func
    return _htm
?'''
# __pragma__ ('noecom')

