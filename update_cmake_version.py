import os

TARGET_LINE = 'cmake_minimum_required(VERSION 3.5)\n'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file == 'CMakeLists.txt':
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                lines = f.readlines()
            if lines:
                lines[0] = TARGET_LINE
                with open(path, 'w') as f:
                    f.writelines(lines)
            print(f'Updated: {path}')
