# import os
# os.remove("test.txt")

import os
file_name = "test.txt"
if os.path.exists(file_name):
  os.remove(file_name)
else:
  # raise Exception("file doesn't exist!")
  print(f"file {file_name} doesn't exist!")