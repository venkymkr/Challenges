def get(value, keys, default_value = None):
'''
    Useful for reaching into nested JSON like data
    Inspired by JavaScript lodash get and Clojure get-in etc.
'''
  if value is None or keys is None:
      return None
  path = keys.split('.') if isinstance(keys, str) else keys
  result = value
  def valid_index(key):
      return re.match('^([1-9][0-9]*|[0-9])$', key) and int(key) >= 0
  def is_dict_like(v):
      return hasattr(v, '__getitem__') and hasattr(v, '__contains__')
  for key in path:
      if isinstance(result, list) and valid_index(key) and int(key) < len(result):
          result = result[int(key)] if int(key) < len(result) else None
      elif is_dict_like(result) and key in result:
          result = result[key]
      else:
          result = default_value
          break
  return result