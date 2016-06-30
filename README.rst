=============================
django-minirest
=============================

.. image:: https://badge.fury.io/py/django-minirest.png
    :target: https://badge.fury.io/py/django-minirest

.. image:: https://travis-ci.org/vahaah/django-minirest.png?branch=master
    :target: https://travis-ci.org/vahaah/django-minirest

Micro rest framework

Documentation
-------------
Mini DRF for you project


The full documentation is at https://django-minirest.readthedocs.org.

Quickstart
----------

Install django-minirest::

    pip install django-minirest

Then use it in a project urls::

    urlpatterns = [
        url(r'^api/v1/', include('minirest.urls', namespace='minirest')),
    ]
Enjoy::

    GET localhost:8000/api/v1/<app_name>/<model_name>/

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-test.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
