import os
import shutil

os.makedirs('/Users/lolitiy/test', exist_ok = True)


shutil.rmtree('/Users/lolitiy/test')


from glob import glob