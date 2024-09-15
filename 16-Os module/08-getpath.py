# using getenv() we can directly access the system variable resources such as ex-PATH
import os
path=os.getenv('PATH')
print(path)