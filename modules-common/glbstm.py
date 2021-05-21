'''
Local module, contains global staments implementation
'''

def forinrange(step, **kwargs):
  '''
  Wrap next step(steps) into for in range.

  Keyword arguments:
  - current  

  Step arguments:
  --n;s;[];"0"-- start: the first value in the range
  --n;s;[];"0"-- stop:  the upper bound of the range
  --n;s;[];"0"-- step:  the value controls the increment between the values in the range
  --s;s;[];""-- i: next step parameter name that will get i value
  --n;s;[];"0"-- include: number of flow steps are in the loop

  Returns:
  - kwargs[parameter name] = i
  - kwargs['end'] - flag end of loop
  - kwargs['current'] - current increment value
  '''

  start = step.get('start', 0)
  stop = step.get('stop', 0)
  stp = step.get('stp', 0)
  param_name = step.get('i', '')
  number_of_steps = step.get('include', 0)

  current = kwargs.get('current', 0) 

  if current == 0:
    current = start

  kwargs[param_name] = current
  current += stp
  kwargs['current'] = current
  kwargs['end'] = False

  if current >= stop:
    kwargs['current'] = 0
    kwargs['end'] = True

  return kwargs

