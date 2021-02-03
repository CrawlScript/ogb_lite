m2r README.md
rm -rf ogb_lite.egg-info
rm -rf dist
python setup.py sdist
twine upload dist/*
