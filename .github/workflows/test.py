from datetime import datetime
import os

print(os.getcwd())

with open('README.md', 'w') as f:
    f.write("bob")
    f.write(str(datetime.now()))

print("\n".join(os.listdir()))
