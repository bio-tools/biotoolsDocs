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
You only need Docker to run *bio.tools* locally.


Installing bio.tools on your system
===================================
The local (development) installation is done via `Docker <https://www.docker.com/>`_. Other than Git (and a text editor), nothing else is required to run and write code for bio.tools. 

1. Download and Install Docker
------------------------------
Docker main installation page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`https://docs.docker.com/install/ <https://docs.docker.com/install/>`_

.. note:: You will need to create a `Docker Hub <https://hub.docker.com>`_ account.

**Windows**

`https://docs.docker.com/docker-for-windows/install/ <https://docs.docker.com/docker-for-windows/install/>`_

.. note:: Read the "What to know before you install" information to see if Docker Destktop for Windows can be installed on your system.  If your system does not meet the requirements to run Docker Desktop for Windows, you can install the legacy `Docker Toolbox <https://docs.docker.com/toolbox/overview/>`_.

**MacOS**

`https://docs.docker.com/docker-for-mac/install/ <https://docs.docker.com/docker-for-mac/install/>`_

**CentOS**

`https://docs.docker.com/install/linux/docker-ce/centos/ <https://docs.docker.com/install/linux/docker-ce/centos/>`_

**Debian**

`https://docs.docker.com/install/linux/docker-ce/debian/ <https://docs.docker.com/install/linux/docker-ce/debian/>`_

**Fedora**

`https://docs.docker.com/install/linux/docker-ce/fedora/ <https://docs.docker.com/install/linux/docker-ce/fedora/)>`_

**Ubuntu**

`https://docs.docker.com/install/linux/docker-ce/ubuntu/ <https://docs.docker.com/install/linux/docker-ce/ubuntu/)>`_

2. Clone the repo
-----------------
Using HTTPS
^^^^^^^^^^^
.. code-block:: text

 git clone https://github.com/bio-tools/biotoolsRegistry.git

Using SSH
^^^^^^^^^^^
.. code-block:: text

 git clone git@github.com:bio-tools/biotoolsRegistry.git

Go into the folder in which you cloned the bio.tools repo. By default it will be called ``biotoolsRegistry``: (e.g. ``cd biotoolsRegistry`` or ``cd /home/user/coding/biotoolsRegistry`` )

3.0 Inside the bio.tools repo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. note:: The Docker setup will require up to 5 GB of disk space. The bio.tools data will also add to this.

3.0.1 Build the necessary Docker images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

    docker-compose build

The above command will download / build all the Docker images required for bio.tools to run on your local machine. 

The images built can be seen by running: ``docker image ls`` and are:

* ``biotools/frontend`` ``(~ 827MB)``
* ``biotools/backend`` ``(~ 1.12GB)``
* ``mysql`` ``(~ 205MB)`` (will show up after running **3.0.2**)
* ``elasticsearch`` ``(~ 486MB)`` (will show up after running **3.0.2**)
* ``python`` ``(~ 925MB)``
* ``node`` ``(~ 650MB)``

3.0.2 Create and run the Docker containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker-compose up

The above command will create and run the required containers:

* ``biotools-mysql``
* ``biotools-elasticsearch``
* ``biotools-backend`` (depends on ``biotools-mysql`` and ``biotools-elasticsearch``)
* ``biotools-frontend`` (depends on ``biotools-backend``) 

.. note:: 

    After running the ``docker-compose up`` command, the containers will start and will output log messages which you can see in your terminal window. In order for the containers to keep running this window needs to stay open. You will need to open new terminal windows/tabs for other operations.
    
    ``docker-compose up`` will also build the images if they do not exist, but in order to be sure your latest source code and image changes are running make sure you run ``docker-compose build`` beforehand

Too see the running containers run: ``docker container ls``

3.1 The short(er) setup
-----------------------
**Run the steps below in the root folder of the Git project (e.g.** ``biotoolsRegistry`` **)** 

3.1.1 Make migrations
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py makemigrations

Make Django migrations from the exiting models. Executed on the ``biotools-backend`` container. If you get the ``No changes detected`` message it means that you are up to date.

3.1.2 Migrate to the DB
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py migrate

Create necessary tables and other DB objects from the migrations. Executed on the ``biotools-backend`` container. If you get the ``No migrations to apply.`` message it means that you are up to date. 

3.1.3 Copy initial (seed) DB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker cp initial_db.sql biotools-mysql:/root

Copies the ``initial_db.sql`` SQL file into the ``biotools-mysql`` container (where the MySQL database server runs) into the ``/root`` folder.


3.1.4 Copy initial DB load script file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker cp load_initial_db.sh biotools-mysql:/root

Copies the ``load_initial_db.sh`` into the ``biotools-mysql`` container. This file will run the MySQL commands used to load the database described in ``initial_db.sql``

3.1.5 Execute initial DB load script file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-mysql bash /root/load_initial_db.sh

Executes the ``load_initial_db.sh`` file in the ``biotools-mysql`` container which loads the initial (seed) DB data.

.. note:: The initial DB contains 11 tool annotations, a superuser (username: ``biotools``, password: ``biotools``), an initial ``test`` subdomain and the necessary EDAM files. See 3.1.8 for more.


3.1.6 Purge Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py es_purge

Purges (clears) any data in the Elasticsearch index. Executed in the ``biotools-backend`` container which communicates with the ``biotools-elasticsearch`` container.

3.1.7 Regenerate Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py es_regenerate

Takes all the tools, subdomains annotations etc. in the DB  and creates the equivalent entries in the Elasticsearch index. Executed in the ``biotools-backend`` container.

3.1.8 Done
^^^^^^^^^^
At this point you can go to `http://localhost:8000 <http://localhost:8000>`_ to see the local bio.tools homepage.

The ``test`` subdomain can be viewed at `http://test.localhost:8000 <http://test.localhost:8000>`_


You can login with the existing superuser (user: ``biotools``, password: ``biotools``).

All running Docker containers can be stopped by running: ``docker-compose down`` from the root Git folder. This will preserve the data in the MySQL database and Elasticsearch. To reinstantiate everything again run: ``docker-compose up``. 

Only need to run ``docker-compose build`` once at the beginning or if changes are made to the bio.tools Docker settings files.

If you wish to remove the data along with the containers run: ``docker-compose down -v`` which will also remove the Docker volumes which preserve the MySQL and Elasticsearch data.



3.2 The longer setup
--------------------
This is an alternative to **3.1** in which some of the steps were contained in the initial DB files. This will start with no data.

**Run the steps below in the root folder of the Git project (e.g.** ``biotoolsRegistry`` **)** 

3.2.1 Make migrations
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py makemigrations

Make Django migrations from the exiting models. Executed on the ``biotools-backend`` container.

3.2.2 Migrate to the DB
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py migrate

Create necessary tables and other DB objects from the migrations. Executed on the ``biotools-backend`` container.

3.2.3 Create a superuser
^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec -it biotools-backend python manage.py createsuperuser

Prompts the creation of a superuser, need to input superuser name, email (optional) and password. Executed on the ``biotools-backend`` container.


3.2.4 Setup EDAM ontology
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend bash /elixir/application/backend/data/edam/update_edam.sh

Download EDAM ontology and push it to the DB. Can also be used to update to new EDAM version. The file which indicates the EDAM version is ``<git_project_root>/backend/data/edam/current_version.txt``, e.g. ``biotoolsRegistry/backend/data/edam/current_version.txt``


3.2.5 Copy helper tables SQL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker cp update_site_settings.sql biotools-mysql:/root

Copies the ``update_site_settings.sql`` SQL file into the ``biotools-mysql`` container (where the MySQL database server runs) into the ``/root`` folder. This file contains SQL instructions used to create helper tables and settings for the project.

3.2.6 Copy script file to run helper tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker cp update_site_settings.sh biotools-mysql:/root

Copies the ``update_site_settings.sh`` into the ``biotools-mysql`` container. This file will run the MySQL commands described in ``update_site_settings.sql``

3.2.7 Execute script file
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-mysql bash /root/update_site_settings.sh

Executes the ``update_site_settings.sh`` file in the ``biotools-mysql`` container which loads the helper tables and settings in the DB.

3.2.8 Purge Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py es_purge

Purges (clears) any data in the Elasticsearch index. Executed in the ``biotools-backend`` container which communicates with the ``biotools-elasticsearch`` container.

3.2.9 Regenerate Elasticsearch
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker exec biotools-backend python manage.py es_regenerate

Takes all the tools, subdomains annotations etc. in the DB  and creates the equivalent entries in the Elasticsearch index. Executed in the ``biotools-backend`` container.

3.1.10 Done
^^^^^^^^^^^
At this point you can go to `http://localhost:8000 <http://localhost:8000>`_ to see the local bio.tools homepage.

Login with the user created in **3.2.3**

No tools or subdomains are available, add tools at `http://localhost:8000/register <http://localhost:8000/register>`_ and subdomains at `http://localhost:8000/subdomain <http://localhost:8000/subdomain>`_

All running Docker containers can be stopped by running: ``docker-compose down`` from the root Git folder. This will preserve the data in the MySQL database and Elasticsearch. To reinstantiate everything again run: ``docker-compose up``.

Only need to run ``docker-compose build`` once at the beginning or if changes are made to the bio.tools Docker settings files.

If you wish to remove the data along with the containers run: ``docker-compose down -v`` which will also remove the Docker volumes which preserve the MySQL and Elasticsearch data.


4. Useful information
---------------------
4.0 Basic usage
---------------
After completing steps 1-3 above, the only required commands for basic use are

.. code-block:: text

 docker-compose up

and

.. code-block:: text

 docker-compose down

and perhaps

.. code-block:: text

 docker-compose down -v

4.1 Local dev
-------------
After running ``docker-compose up`` you will see a number of log messages. These messages come from the running containers:

* `biotools-mysql` (MySQL logs)
* `biotools-elasticsearch` (Elasticsearch logs)
* `biotools-backend` (Mostly Apache logs, sometimes Python logs)
* `biotools-frontend` (Gulp logs)

4.1.1 Backend dev
^^^^^^^^^^^^^^^^^
The ``biotools-backend`` container is based on an image which uses an Apache server. The logs from ``biotools-backend`` come from Apache or sometimes from Python. 

.. note:: 
    Changes in Python/Django/backend files will be reflected in the ``biotools-backend`` container, **BUT** because of how Apache works, the changes won't be reflected in your browser ``http://localhost:8000`` until Apache is reloaded. In order to see the changes in the reflected in the browser you need to run: 
    
    ``docker exec biotools-backend /etc/init.d/apache2 reload``

    **Remember** to run the above command whenever you want to see your code changes reflected in your local bio.tools.

    Bringing the containers down and up agail will also work, but this takes significantly longer. The above command is almost instant.

Most issues with the backend code will be reflected in the browser at ``http://localhost:8000/api/{some_path}``, e.g. `http://localhost:8000/api/tool <http://localhost:8000/api/tool>`_ or `http://localhost:8000/api/jaspar <http://localhost:8000/api/jaspar>`_ etc. 

See `https://biotools.readthedocs.io/en/latest/api_reference.html <https://biotools.readthedocs.io/en/latest/api_reference.html>`_ or Django route files (``urls.py``) for more API endpoints.

4.1.2 Frontend dev
^^^^^^^^^^^^^^^^^^
The ``biotools-frontend`` container outputs logs from ``gulp`` ( `https://gulpjs.com/ <https://gulpjs.com/>`_ )  which bundles all frontend JavaScript and CSS code. 

Every time you change and save a ``.js`` or ``.css`` file in the frontend, gulp will re-bundle everything automatically. This implies that all changes in the frontend are reflected automatically in thr browser, unlike for the backend.

.. note:: If you have a syntax error in your JavaScript or CSS files, gulp will fail and you won't see any changes reflected in the browser. So, if your changes are not reflected, look at the ``biotools-frontend`` logs of gulp which will indicate if you made a syntax error in your code.

4.2 Update EDAM
---------------

Similarly to section **3.2.4**, in order to update to the latest EDAM version (or just use a different EDAM version) the ``update_edam.sh`` needs to be executed on the ``biotools-backend`` container.

The version number used for updating EDAM is specified in the file:

.. code-block:: text

 <git_project_root>/backend/data/edam/current_version.txt

In order to update to the latest EDAM version (e.g. ``1.23``) edit the ``current_version.txt`` file to store the value ``1.23``, save the file and run:

.. code-block:: text

 docker exec biotools-backend bash /elixir/application/backend/data/edam/update_edam.sh

The script file will download the specific EDAM version .owl file from `https://github.com/edamontology/edamontology <https://github.com/edamontology/edamontology>`_ and execute the:

.. code-block:: text

 python /elixi/application/manage.py parse_edam

command in the ``biotools-backend`` container.

.. note:: The ``current_version.txt`` file is tracked by Git and any changes involving EDAM versions other than latest should not be pushed to the main branches of the repo.

4.3 Local email setup
---------------------
Important to note that the email system used to send emails regarding account creation and password reset will not work as intended out of the box . 

In order for the emails to work you need to provide credetials (email, password, smtp settings) in the ``backend/elixirapp/settings.py`` file. bio.tools production uses Zoho mail (http://zoho.com) which currently works well with our setup. 

The easy way would be to make a Zoho email account and use that email information to make the email functionality run. Gmail and Yahoo were tried and the connections are blocked by Gmail and Yahoo because of security reasons. This is because Gmail and Yahoo don't accept a simple username-password login and require more strict settings. Feel free to implement this in your bio.tools instance.


4.4 Docker notes
----------------

Build bio.tools Docker images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker-compose build

Run bio.tools containers
^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker-compose up

Stop bio.tools containers
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker-compose down

Stop bio.tools containers and remove data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker-compose down -v


View running containers
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker container ls

View all containers
^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker container ls -a

Remove stopped containers
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker container rm <CONTAINER_ID>

or

.. code-block:: text

 docker container rm <CONTAINER_ID1> <CONTAINER_ID2> <CONTAINER_ID3>


Force remove containers
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker container rm -f <CONTAINER_ID>

or 

.. code-block:: text

 docker container rm -f <CONTAINER_ID1> <CONTAINER_ID2> <CONTAINER_ID3>

Prune containers (Remove all stopped containers)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: text

 docker container prune

View images 
^^^^^^^^^^^
.. code-block:: text

 docker image ls

Remove image
^^^^^^^^^^^^
.. code-block:: text

 docker image rm <IMAGE_ID>

or

.. code-block:: text

 docker image rm <IMAGE_ID1> <IMAGE_ID2> <IMAGE_ID2>


(will not work if containers are running this image)

Enter a container and run commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Any of the bio.tools runnning containers can provide a bash terminal to run commands inside the containers (similar to ``docker exec``). Examples of the commands are:

.. code-block:: text

  - docker exec -it biotools-mysql bash
  - docker exec -it biotools-elasticsearch bash
  - docker exec -it biotools-backend bash
  - docker exec -it biotools-frontend bash

As an example, to view the info in a MySQL database table run:

1. ``docker exec -it biotools-mysql bash``
2. In container: ``mysql -u elixir -p`` (password is by default ``123``)
3. In MySQL: 

.. code-block:: text

 use elixir;

 SELECT * FROM elixir_resource WHERE visibility = 1;


bio.tools Docker settings files:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Backend build config file

.. code-block:: text

 <git_project_root>/backend/Dockerfile

Backend dockerignore file

.. code-block:: text

 <git_project_root>/backend/.dockerignore

Frontend build config file

.. code-block:: text

 <git_project_root>/frontend/Dockerfile

docker-compose YAML config file

.. code-block:: text

 <git_project_root>/docker-compose.yml



Docker documentation:
^^^^^^^^^^^^^^^^^^^^^
* `https://docs.docker.com/ <https://docs.docker.com/>`_
* `https://docs.docker.com/reference/ <https://docs.docker.com/reference/>`_
* `https://docs.docker.com/engine/reference/commandline/container/ <https://docs.docker.com/engine/reference/commandline/container/>`_
* `https://docs.docker.com/engine/reference/commandline/image/ <https://docs.docker.com/engine/reference/commandline/image/>`_
* `https://docs.docker.com/config/pruning/ <https://docs.docker.com/config/pruning/>`_
* `https://docs.docker.com/compose/ <https://docs.docker.com/compose/>`_
* `https://hub.docker.com/ <https://hub.docker.com/>`_



API Guidelines
--------------
You can also check out our API instructions at the links below:

- `API reference <https://biotools.readthedocs.io/en/latest/api_reference.html>`_
- `API Usage Guide <https://biotools.readthedocs.io/en/latest/api_usage_guide.html>`_
