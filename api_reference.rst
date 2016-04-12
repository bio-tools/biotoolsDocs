API endpoints
=============

.. warning:: This document is a work in progress

All resources
------------------

.. code-block:: text

    /tool/
    /t/

GET
^^^^

Return a list of all currently registered resources

.. code-block:: bash

   curl -X GET "https://bio.tools/api/tool/?page=5&format=json"

**Output**:

.. code-block:: js

   {
     "count": 2312,
     "previous": "?page=4",
     "next": "?page=6",
     "list": [ < list of resources for this page > ]
   }

URL Params
""""""""""
=========  ========  ============== ===================
Parameter  Required  Allowed values Description        
=========  ========  ============== ===================
page       No        <integer>      Result page number 
format     No        json, xml, api Response media type
=========  ========  ============== ===================

POST
^^^^

Register a new tool

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '< resource json/xml >' "https://bio.tools/api/tool/"

**POST data**:

.. code-block:: js

   < resource json/xml >

**Output**:

.. code-block:: js

   < resource json/xml >

Headers
""""""""""
=============  ========  =================================  ====================
Parameter      Required  Allowed values                     Description        
=============  ========  =================================  ====================
Content-Type   Yes       application/json, application/xml  Resource media type 
Authorization  Yes       Token < authorization token >      Authorization header
=============  ========  =================================  ====================

.. note:: This method requires the user to be authenticated. `Learn how to obtain a token <http://sphinx.pocoo.org>`_. TODO: fix link

.. note:: `See an example < resource json/xml > <https://bio.tools/api/tool/CBS/SignalP/4.1?format=json>`_. TODO: fix link