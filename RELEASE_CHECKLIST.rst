RELEASE HOWTO
=============

- [ ] Bump Version in

    - field/__init.py
    - docs/field.1
    - setup.py

- [ ] Build source and wheel distributions

    python setup.py sdist bdist_wheel

- [ ] Pip install local versions in seperate virtualenvs

    mkvirtualenv field-$VERSION-sdist
    pip install dist/field-$VERSION.tar.gz

    mkvirtualenv field-$VERSION-wheel
    pip install dist/field-$VERSION-*.whl

- [ ] GPG Sign new releases

    rm -r dist/
    gpg --detach-sign -a field-$VERSION.tar.gz
    gpg --detach-sign -a field-$VERSION-*.whl

- [ ] Upload to TestPypi

    twine upload -r testpypi dist/*

- [ ] Create a new virtualenv and install from testpypi

    mkvirtualenv field-$VERSION
    pip install -i https://testpypi.python.org/pypi field

- [ ] Verify everything is in order.

    - mandb && man -f field
    - man field
    - manpage EXAMPLES work as expected

- [ ] Git Tag release and push

    git tag -u 722C0606 "v${VERSION}"

- [ ] Upload to Pypi

    twine upload dist/*
