# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc2_example.krb'):
           [1672601746.3157125, 'bc2_example_bc.py'],
         ('', '', 'Car.kfb'):
           [1672601746.321663, 'Car.fbc'],
         ('', '', 'fc_example.krb'):
           [1672601746.3276777, 'fc_example_fc.py'],
         ('', '', 'questions.kqb'):
           [1672601746.331637, 'questions.qbc'],
        },
        compiler_version)

