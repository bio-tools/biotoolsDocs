API endpoints - development
===========================

.. important:: This is the API documentation for upcoming features, available on the dev server at https://dev.bio.tools.

.. note::
   The bio.tools Web API provides an easy way to access the bio.tools database.
   If you find a bug, have any questions or suggestions, please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.

List tools
----------
*List and search through all the available tools. Can sort, filter, and search the results.*

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/tool/
    https://dev.bio.tools/api/t/

Endpoint parameters
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
~~~~~~~~~~

These are the attributes supported by bio.tools:


============        =======================================================================                       =========================
Parameter           Search behaviour                                                                              Example
============        =======================================================================                       =========================
biotoolsID          Exact search for bio.tools tool ID                                                            ``biotoolsid=signalp``
name                Fuzzy search for tool name                                                                    ``name=signalp``
homepage            Fuzzy search for tool homepage URL                                                            ````
description         Fuzzy search over tool description                                                            ````
version             Exact search for tool version                                                                 ````
topic               Fuzzy search for EDAM Topic (term)                                                            ````
topicID             Exact search for EDAM Topic (URI)                                                             ````
function            Fuzzy search over function (input, operation, output, note and command)                       ````
operation           Fuzzy search for EDAM Operation (term)                                                        ````
operationID         Exact search for EDAM Operation (ID)                                                          ````
dataType            Fuzzy search over input and output for EDAM Data (term)                                       ````
dataTypeID          Exact search over input and output for EDAM Data (ID)                                         ````
dataFormat          Fuzzy search over input and output for EDAM Format (term)                                     ````
dataFormatID        Exact search over input and output for EDAM Format (ID)                                       ````
input               Fuzzy search over input for EDAM Data and Format (term)                                       ````
inputID             Exact search over input for EDAM Data and Format (ID)                                         ````
inputDataType       Fuzzy search over input for EDAM Data (term)                                                  ````
inputDataTypeID     Exact search over input for EDAM Data (ID)                                                    ````
inputDataFormat     Fuzzy search over input for EDAM Format (term)                                                ````
inputDataFormatID   Exact search over input for EDAM Format (ID)                                                  ````
output              Fuzzy search over output for EDAM Data and Format (term)                                      ````
outputID            Exact search over output for EDAM Data and Format (ID)                                        ````
outputDataType      Fuzzy search over output for EDAM Data (term)                                                 ````
outputDataTypeID    Exact search over output for EDAM Data (ID)                                                   ````
outputDataFormat    Fuzzy search over output for EDAM Format (term)                                               ````
outputDataFormatID  Exact search over output for EDAM Format (ID)                                                 ````
toolType            Exact search for tool type                                                                    ````
collectionID        Exact search for tool collection                                                              ````
maturity            Exact search for tool maturity                                                                ````
operatingSystem     Exact search for tool operation system                                                        ````
language            Exact search for programming language                                                         ````
cost                Exact search for cost                                                                         ````
license             Exact search for software or data usage license                                               ````
accessibility       Exact search for tool accessibility                                                           ````
credit              Fuzzy search over credit (name, email, URL, ORCID iD, type of entity, type of role and note)  ````
creditName          Exact search for name of credited entity                                                      ````
creditTypeRole      Exact search for role of credited entity                                                      ````
creditTypeEntity    Exact search for type of credited entity                                                      ````
creditOrcidID       Exact search for ORCID iD of credited entity                                                  ````
publication         Fuzzy search over publication (DOI, PMID, PMCID, publication type and tool version)           ````
publicationID       Exact search for publication ID (DOI, PMID or PMCID)                                          ````
publicationType     Exact search for publication type                                                             ````
publicationVersion  Exact search for tool version associated with a publication                                   ````
link                Fuzzy search over general link (URL, type and note)                                           ````
linkType            Exact search for type of information found at a link                                          ````
documentation       Fuzzy search over documentation link (URL, type and note)                                     ````
documentationType   Exact search for type of documentation                                                        ````
download            Fuzzy search over download link (URL, type, version and note)                                 ````
downloadType        Exact search for type of download                                                             ````
downloadVersion     Exact search for tool version associated with a download                                      ````
otherID             Fuzzy search over alternate tool IDs (ID value, type of ID and version)                       ````
otherIDType         Exact search for type of alternate tool ID                                                    ````
otherIDVersion      Exact search for tool version associated with an alternate ID                                 ````
============        =======================================================================                       =========================


Example
"""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/tool/?page=1&format=json&name=signalp&sort=name&ord=asc&q=protein-signal-peptide-detection"

.. note::
   An EDAM concept ID can be specified in any of the following formats:
   * Concept URI *e.g.* ``http://edamontology.org/operation_2403``
   * Concept CURIE *e.g.* ``EDAM:operation_2403``
   * Concept ID *e.g.* ``operation_2403``
   * Numerical ID *e.g.* ``2403``

.. caution::
   If querying by ``homepage`` you must quote the query value, *e.g.*
   ```https://bio.tools/api/tool?homepage="http://cosbi4.ee.ncku.edu.tw/pirScan/"```

Response data
"""""""""""""
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
*Obtain information about a single tool.*

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
"""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/tool/signalp/?format=json"


Register a tool
---------------

*Register a new tool.*


.. important:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/tool/
    https://dev.bio.tools/api/t/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
data       Yes       Tool     Tool you wish to register.
                              See an `example tool <https://dev.bio.tools/api/tool/SignalP?format=json>`_.
=========  ========  ======== ====================================================================================================================================

.. note:: It is possible to specify editing permissions for tools. Learn how to manage :ref:`Editing_permissions`.

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/"


Validate registering a tool
---------------------------

*Test registering a tool without it actually being saved into the database.*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

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
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/validate/"


Update a tool
-------------
*Update a tool description.*

.. important:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

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
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X PUT -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/SignalP"



Validate updating a tool
------------------------
*Test updating a tool without it actually being saved into the database.*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

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
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   Media type
                         application/xml)   
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X PUT -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://dev.bio.tools/api/tool/SignalP/validate/"


.. _Editing_permissions:

Editing permissions
-------------------
*Manage editing permissions for the registered tools.*

There are currently three types of editing permissions supported by the system:

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
-------------

*Removes a tool from the registry.*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

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
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X DELETE \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   "https://dev.bio.tools/api/tool/SignalP"


List used terms
---------------
*Obtain a list of terms registered with tools for some attributes, e.g. a list of names of all tools.*

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
"""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/used-terms/name/?format=json"

Response data
"""""""""""""
================== ====================
Key Name           Description         
================== ====================
data               A list of used terms
================== ====================


Create a user account
---------------------

*Creates a user account and emails a verification email.*

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/registration/

POST data
"""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
username            Yes       String  Account username                                                           username
password1           Yes       String  Password                                                                   password
password2           Yes       String  Repeated password                                                          password
email               Yes       String  Account email. The verification email will be sent to this address         example@example.org
==================  ========  ======  ========================================================================== =========================

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"username":"username", "password1":"password", \
   "password2":"password", "email":"example@example.org"}' \
   "https://dev.bio.tools/api/rest-auth/registration/"



Verify a user account
---------------------

*Verifies a user account based on the emailed verification key.*

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/registration/verify-email/

POST data
"""""""""
==================  ========  ======  ========================================================================== ================================================================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== ================================================================
key                 Yes       String  Verification key from account creation email                               ndwowtbpmlk5zxdxfrwgu2822xynjidhizhwosycve7hro1of156hjwdsf1f6gbn
==================  ========  ======  ========================================================================== ================================================================

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"key":"ndwowtbpmlk5zxdxfrwgu2822xynjidhizhwosycve7hro1of156hjwdsf1f6gbn"}' \
   "https://dev.bio.tools/api/rest-auth/registration/verify-email/"


.. _Token:

Log in / obtain token
---------------------

*Logs the user in and returns an authentication token.*

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/login/

POST data
"""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
username            Yes       String  Account username                                                           username
password            Yes       String  Password                                                                   password
==================  ========  ======  ========================================================================== =========================

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"username":"username","password":"password"}' \
   "https://dev.bio.tools/api/rest-auth/login/"

Response data
"""""""""""""
================== ====================
Key Name           Description         
================== ====================
key                Authentication token
================== ====================

Get user information
--------------------
*Return information about the logged in user account, including a list of registered tool (name, id, version, additionDate, lastUpdate)*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

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
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X GET \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   "https://dev.bio.tools/api/rest-auth/user/?format=json"

Response data
"""""""""""""
================== ========================================================
Key Name           Description         
================== ========================================================
username           Account username
email              Account email
resources          List of registered tools 
                   (limited to name, id, version, additionDate, lastUpdate)
================== ========================================================


Log out
-------
*Log out of the system.*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/logout/

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Authorization  Yes       String('Token <authorization token>')      Authorization header.
                                                                    Learn how to :ref:`Token`.
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

  curl -X POST 
  -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
  "https://dev.bio.tools/api/rest-auth/logout/"


Reset user password
-------------------

*Send a password reset email.*

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/password/reset/

POST data
"""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
email               Yes       String  Account email                                                              example@example.org
==================  ========  ======  ========================================================================== =========================

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"email":"example@example.org"}' \
   "https://dev.bio.tools/api/rest-auth/password/reset/"

Confirm password reset
----------------------

*Confirm a password reset using uid and token from a password reset email.*

*HTTP POST*

.. code-block:: text

    https://dev.bio.tools/api/rest-auth/password/reset/confirm/

POST data
"""""""""
==================  ========  ======  ========================================================================== =========================
Key Name            Required  Type    Description                                                                Example
==================  ========  ======  ========================================================================== =========================
uid                 Yes       String  UID from password reset email                                              MQ
token               Yes       String  Token from password reset email                                            4ct-67e90a1ab4f22fbb9b9f
password1           Yes       String  New password                                                               new_password
password2           Yes       String  New password repeated                                                      new_password
==================  ========  ======  ========================================================================== =========================

Headers
"""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json,                   POST data media type
                         application/xml)   
=============  ========  =========================================  ==============================================================================================

Example
"""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -d '{"uid":"MQ", "token":"4ct-67e90a1ab4f22fbb9b9f", \
   "password1":"new_password", "password2":"new_password"}' \
   "https://dev.bio.tools/api/rest-auth/password/reset/confirm/"

Stats
-----
*Compile stats about a the registry.*

*HTTP GET*

.. code-block:: text

    https://dev.bio.tools/api/stats

Example
"""""""

.. code-block:: bash

   curl -X GET "https://dev.bio.tools/api/stats"
