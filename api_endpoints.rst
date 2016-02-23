API endpoints
=============

Resource
--------

``/tool/`` (GET)
    Get a list of all resources in bio.tools.
    
    Available to everyone.


``/tool/`` (POST)
    - resource (json, xml, yaml)

    Insert a resource into bio.tools.
    
    Available to registered users.


``/tool/<id>/`` (GET)
    Get the description of a single resource, identified by ``<id>``.


``/tool/<id>/`` (PUT)
    - resource (json, xml, yaml)

    Update resource description.


``/tool/<id>/`` (DELETE)
    Remove resource from bio.tools.


User
-----

``/rest-auth/registration/`` (POST)
    - username (string)
    - password1 (string)
    - password2 (string)
    - email (string)

    Register a new user. A verification email will be sent to the specified email address.

``/rest-auth/login/`` (POST)
    - username (string)
    - password (string)

    Login user and obtain a token.


.. note:: Many more coming...