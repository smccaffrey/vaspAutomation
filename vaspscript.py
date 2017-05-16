import os
os.system('mkdir testingenv')

import os
os.system('phonopy diamond.conf -d')

import os
import shutil
source = os.listdir('/Users/andrewadams/desktop/vasp')
destination = 'testingenv'
for files in source:
    if files.startswith('POSCAR'):
        shutil.move(source, destination)

import os
import shutil
source = os.listdir('/Users/andrewadams/desktop/vasp')
destination = 'testingenv'
for files in source:
    if files('disp.yaml'):
        shutil.move(source, destination)

import os
os.system('cd /Users/andrewadams/desktop/vasp')

import os
os.system('phonopy -f disp-001/vasprun.xml disp-002/vasprun.xml')

import os
os.system('phonopy -f disp-001/vasprun.xml disp-002/vasprun.xml')

