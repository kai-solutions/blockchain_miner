import os, shutil

def create_path(path_to_create, delete_first=True):
    ''' Creates necessary folder paths in where to export files
    '''
    if delete_first:
        if os.path.exists(path_to_create):
            shutil.rmtree(path_to_create)
    if not os.path.exists(path_to_create):
        os.makedirs(path_to_create)

    if os.path.exists(os.path.abspath(path_to_create)):
        print(f'{path_to_create} succesfully created')