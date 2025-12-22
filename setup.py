from setuptools import setup, Extension
import numpy

PACKAGE_NAME = "pipcpptemp"

_sources = \
[
    f'./{PACKAGE_NAME}_src/ext/main.cpp',
]

modExt = Extension\
(
    f"{PACKAGE_NAME}.ext", 
    sources = _sources,
    # libraries = ['jemalloc'],
    include_dirs = [f"./{PACKAGE_NAME}_src/ext/", numpy.get_include()],
    language = 'c++',
    # extra_compile_args = ["-O3", "-fopenmp"],
    # extra_link_args = ["-fopenmp"],
)

_packages = \
[
    "{PACKAGE_NAME}", 
    "{PACKAGE_NAME}.ext",
]

_package_dir = \
{
    f"{PACKAGE_NAME}":f"./{PACKAGE_NAME}_src/", 
    f"{PACKAGE_NAME}.ext":f"./{PACKAGE_NAME}_src/ext/",
}

setup\
(
    name = f'{PACKAGE_NAME}',
    ext_modules = [modExt],
    packages = _packages,
    package_dir = _package_dir,
    include_package_data = True
)
