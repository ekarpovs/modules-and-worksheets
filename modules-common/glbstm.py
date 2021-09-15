'''
Local module, contains global staments descriptions
'''

def forinrangestm(step, **kwargs):
  '''
  Presents the statement parameters.

  Keyword arguments:

  Step arguments:
  --n;s;[];0-- include: number of flow steps are in the loop
  --n;s;[];0-- start: the first value in the range
  --n;s;[];0-- stop:  the upper bound of the range
  --n;s;[];0-- step:  the value controls the increment between the values in the range
  --s;s;[];""-- map: parameter name that will get current value

  Returns:
  - kwargs as is
  '''
  return kwargs


def whilestm(step, **kwargs):
  '''
  Presents the statement parameters.

  Keyword arguments:

  Step arguments:
  --n;s;[];0-- include: number of flow steps are in the loop
  --s;s;[];"true"-- cond: condition 
  --s;s;[];""-- map: map condition to a predicate inside while stm

  Returns:
  - kwargs as is
  '''
  return kwargs
