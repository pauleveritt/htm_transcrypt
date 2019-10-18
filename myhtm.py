# __pragma__ ('skip')
from htm import htm

# __pragma__ ('noskip')

# __pragma__ ('ecom')
'''?
def htm(h):
    def _htm(string):
        raise Exception("not supported")
    def wrapped_h(type, props, *children):
        return h(type, props, children)
    def func(strings, values):
        return htm.call(wrapped_h, strings, *values)
    _htm.func = func
    return _htm
?'''
# __pragma__ ('noecom')

