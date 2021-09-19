'''
Local module, contains global staments descriptions
'''

def forinrangestm(params, **data):
  '''
  Presents the statement parameters.

  parameters:
    - params: 
      --n;s;[];0-- include: number of flow steps are in the loop
      --n;s;[];0-- start: the first value in the range
      --n;s;[];0-- stop:  the upper bound of the range
      --n;s;[];0-- step:  the value controls the increment between the values in the range
      --s;s;[];""-- map: parameter name that will get current value
    - data: 
  returns:
    - data: as is
  '''
  return data


def whilestm(params, **data):
  '''
  Presents the statement parameters.

  parameters:
    - params: 
      --n;s;[];0-- include: number of flow steps are in the loop
      --s;s;[];"true"-- cond: condition 
      --s;s;[];""-- map: map condition to a predicate inside while stm
    - data: 
  returns:
    - data: as is
  '''
  return data
