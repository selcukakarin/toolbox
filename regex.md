## Python regex

import re

delimiters = "a", "...", "(c)"

example = "stackoverflow (c) is awesome... isn't it?"

regexPattern = '|'.join(map(re.escape, delimiters))

regexPattern('a|\\.\\.\\.|\\(c\\)'

re.split(regexPattern, example)

['st', 'ckoverflow ', ' is ', 'wesome', " isn't it?"]
