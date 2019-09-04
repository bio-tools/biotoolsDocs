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
You only need Docker to run *bio.tools* locally. View the installation steps at:

https://github.com/bio-tools/biotoolsRegistry/blob/master/INSTALL.md


API Guidelines
--------------
You can also check out our API instructions at the links below:

- `API reference <https://biotools.readthedocs.io/en/latest/api_reference.html>`_
- `API Usage Guide <https://biotools.readthedocs.io/en/latest/api_usage_guide.html>`_
