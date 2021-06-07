'''
Local module, contains global staments implementation
'''

def forinrange(step, **kwargs):
  '''
  Wrap next step(steps) into for in range.

  Keyword arguments:
  - idx: the step index in a workflow 
  - include: copy of 'include' step argument
  - end: flag

  Step arguments:
  --n;s;[];"0"-- start: the first value in the range
  --n;s;[];"0"-- stop:  the upper bound of the range
  --n;s;[];"0"-- step:  the value controls the increment between the values in the range
  --s;s;[];""-- i: next step parameter name that will get i value
  --n;s;[];"0"-- include: number of flow steps are in the loop

  Returns:
  - kwargs[parameter name] = i
  - kwargs['end'] - flag end of loop
  '''

  # performs 'i' mapping in runtime
  def update_stm_state(meta):
    meta[param_name] = kwargs[param_name]
    return

  number_of_steps = step.get('include', 0)
  start = step.get('start', 0)
  stop = step.get('stop', 0)
  stp = step.get('step', 0)
  param_name = step.get('i', '')

  i = kwargs.get(param_name, 0) 
  end = kwargs.get('end', False)

  if i == 0:
    i = start

  i += stp
  kwargs[param_name] = i
  if i > stop:
    kwargs[param_name] = 0

  kwargs['end'] = False
  if i >= stop:
    kwargs['end'] = True

  kwargs['stm_state'] = update_stm_state

  return kwargs

