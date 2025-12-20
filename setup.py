from setuptools import setup, Extension
import numpy

_sources = \
[
    './pipcpptemp_src/ext/main.cpp',
]

modExt = Extension\
(
    "pipcpptemp.ext", 
    sources = _sources,
    # libraries = ['jemalloc'],
    include_dirs = ["./pipcpptemp_src/ext/", numpy.get_include()],
    language = 'c++',
    # extra_compile_args = ["-O3", "-fopenmp"],
    # extra_link_args = ["-fopenmp"],
)

_packages = \
[
    "pipcpptemp", 
    "pipcpptemp.ext",
]

_package_dir = \
{
    "pipcpptemp":"./pipcpptemp_src/", 
    "pipcpptemp.ext":"./pipcpptemp_src/ext/",
}

setup\
(
    name = 'pipcpptemp',
    ext_modules = [modExt],
    packages = _packages,
    package_dir = _package_dir,
    include_package_data = True
)
