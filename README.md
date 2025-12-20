# Pip Package with C++ Backend Template

## Components
### Essential
- `pipcpptemp_src`: Source file of the package, will be usable only after compilation. `_src` is added as a suffix to avoid Python mixing up the source folder before compile and the package folder after compile.
- `pyproject.toml`: Define the essential info and metadata on PyPI of a pip package.
- `setup.py`: Define the package structure, including sub-package and their folder, where the C++ package is one of the sub-packages.
- `MANIFEST.in`: Define what files will be packed into the package. Remember to include C++ source/header to ensure successful compilation.

### Optional
- `example`: The scripts serve as examples for other users, or test scripts for you to see if the package will be working.
- `README.md`: The poster of this package. Please make sure it's elegant since it will be illustrated on project mainpage of Github or PyPI.
- `requirements.txt`: A convenient list so that user can install the depencencies via `pip install -r requirements.txt`.
- `LICENSE`: License file, without this other researchers will be unable to reuse your code. MIT license is recommended for academic usage, which only asks others to retain your authorship.

## Useful Command
### Debug
To upload the package to TestPyPI
```bash
rm -rf dist; python -m build
python -m twine upload --repository testpypi dist/*.tar.gz
rm -rf dist build *.egg-info
```

To install the package from TestPyPI
```bash
rm -rf dist build *.egg-info
pip uninstall pipcpptemp -y
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pipcpptemp -y
```

### Release
To upload the package to PyPI
```bash
rm -rf dist; python -m build
python -m twine upload dist/*.tar.gz
rm -rf dist build *.egg-info
```

To install the package from PyPI
```bash
rm -rf dist build *.egg-info
pip uninstall pipcpptemp -y
pip install pipcpptemp -y
```