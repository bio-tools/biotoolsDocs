Code
====

.. note:: We are in the process of packaging the system in a docker container to achieve a more reproducible, environment-independent local deployment solution. In the meantime please see our guidelines below which summarie necessary components and steps to run *bio.tools*.

Source code
-----------
The source code of the registry is under standard GPL 3.0 `license <https://github.com/bio-tools/biotoolsRegistry/blob/master/LICENSE>`_ and is available from https://github.com/bio-tools/biotoolsRegistry/.


Architecture
------------
The architecture of the registry is designed around the principle of decoupling frontend from the backend in order to eliminate performance bottlenecks at scale. The backend serves the data through the RESTful APIs which are in turn consumed by the the frontend SPA (Single-Page Application). The main advantage of this paradigm is that the frontend uses the exact same API calls that any user can invoke in order to create their own customized interface. The overall goal of scalability can be achieved by hosting the components independently (master database, replicated cache layer and static frontend code in a CDN - Content Delivery Network - such as Cloudflare or Akamai).

Components
----------
You will need all of the following to run *bio.tools*.

Back-end
^^^^^^^^
- Python 2.7
- the following `Python dependencies <https://github.com/bio-tools/biotoolsRegistry/blob/master/requirements.txt>`_
- Java 8 Runtime Environment or compatible (e..g OpenJDK)
- Elasticsearch 5.x
- Database System compatible with Django (e.g. MySQL, PostgreSQL, SQLite etc.)
- Copy of the EDAM Ontology `EDAM.owl <http://edamontology.org/page>`_ file

Front-end
^^^^^^^^^
- npm
- Bower
- Gulp
- AngularJS 1.4.7
- Bootstrap 3.x
- Font Awesome 4.x
- Frontend dependencies:
  
  - https://github.com/bio-tools/biotoolsRegistry/blob/master/frontend/bower.json
  - https://github.com/bio-tools/biotoolsRegistry/blob/master/frontend/package.json


.. note:: Any developers who wish to run a local deployment of *bio.tools* should be familiar with technologies including Django REST Framework, AngularJS, npm and HTTP Server environments (e.g. Apache).  If you need help getting a local deployment working, contact `registry-support <mailto:registry-support@elixir-dk.org>`_.

Running steps
-------------

1. Clone the repository (suppose the repository is cloned in the folder ``elixir``)
2. Install Python and python dependencies
3. Install Java
4. Install Elasticsearch
5. Install a database management system

.. note:: Given the decoupled architecture of the registry, the two main components: backend and frontend both need to be served. Example of options to achieve this include having each component working on its own server; or both components being server by, for example, an Apache HTTP server with rules and configurations to serve both the backend and frontend given a URL. 

6. Configure the database

   The configuration settings can be found at:

   - ``elixir/backend/elixirapp/settings.py``

7. Run migrations

   - ``python elixir/application/backend/manage.py migrate``

8. Import EDAM 

   - Download the latest version of EDAM in owl format from http://edamontology.org

   - Put the owl file in ``elixir/application/backend/data/edam/owl``
   - Change the value in ``elixir/application/backend/data/edam/current_version.txt`` to the current version (e.g. 1.16)
   - Run: ``python elixir/application/backend/manage.py parse_edam``. This will populate the table ``elixir_ontology`` in the DB.

9. Create admin user

   - ``python elixir/application/backend/manage.py createsuperuser``

10. Populate Elastic

    - ``python elixir/application/backend/manage.py es_purge``
    - ``python elixir/application/backend/manage.py es_regenerate``

11. Frontend 

    In the ``elixir/frontend`` folder run:

    - ``npm install``
    - ``bower install``
    - ``gulp``


API Guidelines
--------------
You can also check out our API instructions at the links below:

- `API reference <https://biotools.readthedocs.io/en/latest/api_reference.html>`_
- `API Usage Guide <https://biotools.readthedocs.io/en/latest/api_usage_guide.html>`_
