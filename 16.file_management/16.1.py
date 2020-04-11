import os
import shutil
import glob

def file_migration(PATH_dir, PATH_file):
    '''
    Function for
    folder creation with PATH_dir
    and mooving the file with PATH_file

    return None

    '''
    import os
    import shutil

    os.makedirs(PATH_dir, exist_ok=True)
    shutil.move(PATH_file, PATH_dir)


file_migration('/Users/lolitiy/test', '/Users/lolitiy/data.csv')


def copyfileobj(PATH_file, PATH_copyfile, buffer_size=1024 * 1024):
    """
    Copy a file from PATH_file to PATH_copyfile
    PATH_file and PATH_copyfile
    must be file-like objects, i.e. any object with a read or
    write method, like for example StringIO.

    """
    while True:
        copy_buffer = source.read(buffer_size)
        if not copy_buffer:
            break
        dest.write(copy_buffer)

def copyfile(PATH_file, PATH_copyfile):
    with open(PATH_file, 'rb') as file, open(PATH_copyfile, 'wb') as copyfile:
        copyfileobj(file, copyfile)


copyfile('/Users/lolitiy/test/data.csv', '/Users/lolitiy/test/data1.csv')

def rename_file(PATH_file, PATH_rename_file):
    import os

    os.rename(PATH_file, PATH_rename_file)


rename_file('/Users/lolitiy/test/data.csv', '/Users/lolitiy/test/d.csv')

def moveAllFilesinDir(srcDir, dstDir):
    """
    Move all files from source Dir to destination Dir
    """
    import os
    import shutil
    import glob
    # Check if both the are directories
    if os.path.isdir(srcDir) and os.path.isdir(dstDir) :
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            # Move each file to destination Directory
            shutil.move(filePath, dstDir);
    else:
        print("srcDir & dstDir should be Directories")


moveAllFilesinDir('/Users/lolitiy/test1', '/Users/lolitiy/test')

#remove dir
shutil.rmtree('/Users/lolitiy/test')

from pathlib import Path
#create path
p = Path(some_path)
name_without_extension = p.stem
ext = p.suffix
#rename file by pathlib
p.rename(Path(p.parent, f"{p.stem}_1_{p.suffix}"))

