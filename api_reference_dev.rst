API endpoints - development
===========================

.. note:: This is the API documentation for upcoming features, available on the dev server at https://dev.bio.tools.

This is a lightweight web service with a REST interface, which provides an easy way to access the bio.tools database. 
An API (Application programming interface) is a protocol intended to be used as an interface by software components to communicate with each other. 

If you find a bug, have any questions or suggestions, please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.

List tools
----------
List and search through all the available tools. Can sort, filter, and search the results.

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/tool/
    https://dev.bio.tools/api/t/

Endpoint Parameters
"""""""""""""""""""
===========    ========  =======================================  ==========  ============================================
Parameter      Required  Type                                     Default     Description        
===========    ========  =======================================  ==========  ============================================
page           No        Integer                                  1           Result page number 
format         No        String(json, xml, api)                   json        Response media type
q              No        String                                               Query term, used for searching, 
                                                                              matches all attributes
sort           No        String(lastUpdate,                       lastUpdate  Sorts the results by choosen value
                         additionDate, name, affiliation, score)              (score only available when there is a query)
ord            No        String(desc, asc)                        desc        Orders the results by either 
                                                                              Ascending or Descending order
<attribute>    No        String                                               Filter by <attribute>. 
                                                                              List of supported attributes below.
===========    ========  =======================================  ==========  ============================================



Filtering
"""""""""
To filter the results by attribute name, the attribute name has to be added as a parameter to the URL, with the value being the desired search term, e.g. ``?name=signalp``

.. _Attributes:

Attributes
~~~~~~~~~~~~~~~~

These are attributes supported by bio.tools

.. code-block:: js

  name
  description
  homepage
  biotoolsID
  version
  function
  operation
  input
  inputDataType
  inputDataFormat
  output
  outputDataType
  outputDataFormat, 
   
, topic, accessibility, toolType, collection, maturity, operatingSystem, language, cost, license, documentation, link, download, publication, credit, owner

These attributes will be supported by bio.tools in due course:

.. code-block:: js

   otherID
  

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/tool/?page=1&format=json&name=signalp&sort=name&ord=asc&q=protein-signal-peptide-detection"


.. caution::
   If querying by ``homepage`` you must quote the query value, *e.g.*
   ```https://bio.tools/api/tool?homepage="http://cosbi4.ee.ncku.edu.tw/pirScan/"```

Response data
"""""""""""""""""""
================== ========================================================================== =========================
Key Name           Description                                                                Example
================== ========================================================================== =========================
count              The total tool count results for your query                                2313
previous           Link to the previous page                                                  ?page=4
next               Link to the next page                                                      ?page=6
list               An array with multiple tools                                               ARRAY
                   and their relative information 
================== ========================================================================== =========================


Tool detail
-----------
Obtain information about a single tool.

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/tool/:id/
    https://dev.bio.tools/api/t/:id/
    https://dev.bio.tools/api/:id/


Endpoint Parameters
"""""""""""""""""""
=========  ========  ======================  =======  ===================
Parameter  Required  Type                    Default  Description        
=========  ========  ======================  =======  ===================
id         Yes       String                           biotoolsID 
format     No        String(json, xml, api)  json     Response media type
=========  ========  ======================  =======  ===================


Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/tool/signalp/?format=json"


Register a tool
---------------

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/tool/
    https://dev.bio.tools/api/t/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
data       Yes       Tool Tool you wish to register.
                              See an `example tool <https://dev.bio.tools/api/tool/SignalP?format=json>`_.
=========  ========  ======== ====================================================================================================================================

.. note:: It is possible to specify editing permissions for tools. Learn how to manage :ref:`Editing_permissions`.

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Resource media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/"


Validate registering a tool
-------------------------------

Test registering a tool without it actually being saved into the database.

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/tool/validate/
    https://dev.bio.tools/api/t/validate/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
data       Yes       Tool     Tool you wish to validate.
                              See an `example tool <https://dev.bio.tools/api/tool/SignalP?format=json>`_.
=========  ========  ======== ====================================================================================================================================


Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Resource media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/validate/"


Update a tool
------------------
Update a tool description.

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP PUT*

.. code-block:: text

    https://dev.bio.tools/api/tool/:id/
    https://dev.bio.tools/api/t/:id/
    https://dev.bio.tools/api/:id/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
id         Yes       String   biotoolsID 
data       Yes       Tool     Description with which you wish to update the tool
                              See an `example tool <https://dev.bio.tools/api/tool/SignalP?format=json>`_.
=========  ========  ======== ====================================================================================================================================

.. note:: It is possible to specify editing permissions for tools. Learn how to manage :ref:`Editing_permissions`.

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Resource media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X PUT -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/SignalP"



Validate updating a tool
-----------------------------
Test updating a tool without it actually being saved into the database.

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP PUT*

.. code-block:: text

    https://dev.bio.tools/api/tool/:id/validate/
    https://dev.bio.tools/api/t/:id/validate/
    https://dev.bio.tools/api/:id/validate/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
id         Yes       String   biotoolsID 
data       Yes       Tool Description with which you wish to update the tool for validation
                              See an `example tool <https://dev.bio.tools/api/tool/SignalP?format=json>`_.
=========  ========  ======== ====================================================================================================================================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Resource media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X PUT -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/SignalP/validate/"


.. _Editing_permissions:

Editing permissions
-------------------
It is possible to manage editing permissions for the registered tools. There are currently three types of editing permissions supported by the system:

.. _Private:

Private
"""""""
A private tool can only be edited by the creator of the tool. This is the default option. In order to set this kind of permission, add the following info into the tool data:

.. code-block:: text

    "editPermission": {
        "type": "private"
    }

.. _Public:

Public
""""""
Public tool can be modified by any user registered in the system. In order to set this kind of permission, add the following info into the tool data:

.. code-block:: text

    "editPermission": {
        "type": "public"
    }

.. _Group:

Group
"""""
Specify a list of users in the system that can edit the tool. In order to set this kind of permission, add the following info into the tool data:

.. code-block:: text

    "editPermission": {
        "type": "private",
        "authors": [
            "registered_user_1", "registered_user_2"
        ]
    }


Delete a tool
------------------

Removes a tool from the registry.

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP DELETE*

.. code-block:: text

    https://dev.bio.tools/api/tool/:id/
    https://dev.bio.tools/api/t/:id/
    https://dev.bio.tools/api/:id/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
id         Yes       String   biotoolsID
=========  ========  ======== ====================================================================================================================================


Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X DELETE \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   "https://dev.bio.tools/api/tool/SignalP"


List used terms
------------------
Obtain a list of terms registered with tools for some attributes, e.g. a list of names of all tools.

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/used-terms/:attribute

Endpoint Parameters
"""""""""""""""""""
=========  ========  ==============================================================  =======  ==========================================================
Parameter  Required  Type                                                            Default  Description        
=========  ========  ==============================================================  =======  ==========================================================
attribute  Yes       String(name, topic, functionName, input, output, credits, all)           Attribute for which a list of used terms will be returned
format     No        String(json, xml, api)                                          json     Response media type
=========  ========  ==============================================================  =======  ==========================================================


Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/used-terms/name/?format=json"

Response data
"""""""""""""""""""
================== ====================
Key Name           Description         
================== ====================
data               A list of used terms
================== ====================


Create a user account
---------------------

Creates a user account and emails a verification email.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/registration/

POST data
"""""""""""""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
username            Yes       String  Account username                                                           username
password1           Yes       String  Password                                                                   password
password2           Yes       String  Repeated password                                                          password
email               Yes       String  Account email. The verification email will be sent to this address         example@example.org
==================  ========  ======  ========================================================================== =========================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"username":"username", "password1":"password", \
   "password2":"password", "email":"example@example.org"}' \
   "https://dev.bio.tools/api/rest-auth/registration/"



Verify a user account
---------------------

Verifies a user account based on the emailed verification key.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/registration/verify-email/

POST data
"""""""""""""""""""
==================  ========  ======  ========================================================================== ================================================================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== ================================================================
key                 Yes       String  Verification key from account creation email                               ndwowtbpmlk5zxdxfrwgu2822xynjidhizhwosycve7hro1of156hjwdsf1f6gbn
==================  ========  ======  ========================================================================== ================================================================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"key":"ndwowtbpmlk5zxdxfrwgu2822xynjidhizhwosycve7hro1of156hjwdsf1f6gbn"}' \
   "https://dev.bio.tools/api/rest-auth/registration/verify-email/"


.. _Token:

Log in / obtain token
--------------------------------

Logs the user in and returns an authentication token.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/login/

POST data
"""""""""""""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
username            Yes       String  Account username                                                           username
password            Yes       String  Password                                                                   password
==================  ========  ======  ========================================================================== =========================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"username":"username","password":"password"}' \
   "https://dev.bio.tools/api/rest-auth/login/"

Response data
"""""""""""""""""""
================== ====================
Key Name           Description         
================== ====================
key                Authentication token
================== ====================

Get user information
--------------------------------

Returns information about the logged in user account, including a list of registered tool (name, id, version, additionDate, lastUpdate)

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/user/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ==============================================================  =======  ==========================================================
Parameter  Required  Type                                                            Default  Description        
=========  ========  ==============================================================  =======  ==========================================================
format     No        String(json, xml, api)                                          json     Response media type
=========  ========  ==============================================================  =======  ==========================================================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   "https://dev.bio.tools/api/rest-auth/user/?format=json"

Response data
"""""""""""""""""""
================== ========================================================
Key Name           Description         
================== ========================================================
username           Account username
email              Account email
resources          List of registered tools 
                   (limited to name, id, version, additionDate, lastUpdate)
================== ========================================================


Log out
------------------

.. note:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/logout/

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

  curl -X POST 
  -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
  "https://dev.bio.tools/api/rest-auth/logout/"


Reset user password
--------------------------------

Sends a password reset email.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/password/reset/

POST data
"""""""""""""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
email               Yes       String  Account email                                                              example@example.org
==================  ========  ======  ========================================================================== =========================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"email":"example@example.org"}' \
   "https://dev.bio.tools/api/rest-auth/password/reset/"

Confirm password reset
--------------------------------

Confirms a password reset using uid and token from a password reset email.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/password/reset/confirm/

POST data
"""""""""""""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
uid                 Yes       String  UID from password reset email                                              MQ
token               Yes       String  Token from password reset email                                            4ct-67e90a1ab4f22fbb9b9f
password1           Yes       String  New password                                                               new_password
password2           Yes       String  New password repeated                                                      new_password
==================  ========  ======  ========================================================================== =========================

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"uid":"MQ", "token":"4ct-67e90a1ab4f22fbb9b9f", \
   "password1":"new_password", "password2":"new_password"}' \
   "https://dev.bio.tools/api/rest-auth/password/reset/confirm/"

Stats
-----
Compile stats about a the registry.

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/stats

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/stats"
