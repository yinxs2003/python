import os
import sys

__all__ = ['get_project_path']

_project_dir = os.path.dirname(os.path.abspath(__file__))

src_folder = []

exclude_folder = ['.idea', '.git', 'logs', 'shell']
for namepath in os.listdir(os.getcwd()):
    if os.path.isdir(namepath) and namepath not in exclude_folder:
        src_folder.append(_project_dir + os.sep + namepath)

sys.path.extend(src_folder)
# print(sys.path)


def get_project_path():
    return _project_dir
