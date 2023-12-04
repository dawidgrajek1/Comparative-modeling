from modeller import *
from modeller.automodel import *

env = Environ()
env.io.atom_files_directory = [".", "./atom_files"]
# a = AutoModel(env, alnfile='data/examp2.ali',
#               knowns=('5fd1', '1fdn', '1fxd'), sequence='1fdx')

a = AutoModel(
    env,
    alnfile="aligment.txt",
    knowns=("6F14", "3J4Q", "1CTP"),
    sequence="model",
)
# a.starting_model = 0
# a.ending_model = 5
a.make()
a.write("model.pdb")

# 4ae6_A
