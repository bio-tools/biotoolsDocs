API endpoints
=============

.. warning:: This document is a work in progress

This is a lightweight web service, (REST interface), which provides an easy way to access the bio.tools database. 
An API (Application programming interface) is a protocol intended to be used as an interface by software components to communicate with each other. 

If you find any bug, or have any questions, or any suggestions please get in touch with us. TODO: add link

List resources
------------------
Used to list and search through out all the available resources. Can sort, filter, and search the results.

*HTTP GET*

.. code-block:: text

    https://bio.tools/api/tool/
    https://bio.tools/api/t/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ====================================================                        ===================                 ==========================================================
Parameter  Required  Type                                                                        Default                             Description        
=========  ========  ====================================================                        ===================                 ==========================================================
page       No        Integer                                                                     1                                   Result page number 
format     No        String(json, xml, api)                                                      json                                Response media type
q          No        String                                                                      0                                   Query term, used for searching, matches all attributes
sort       No        String(lastUpdate, additionDate, name, affiliation)                         lastUpdate                          Sorts the results by choosen value
ord        No        String(desc, asc)                                                           desc                                Orders the results by either Ascending or Descending order
=========  ========  ====================================================                        ===================                 ==========================================================

Filtering
"""""""""
To filter the results by attribute name, the attribute name has to be added as a parameter to the URL, with the value being the desired search term, e.g. ``?name=signalp``

.. _Attributes:

Attributes
~~~~~~~~~~~~~~~~

These are attributes supported by bio.tools

.. code-block:: js

  name, version, description, function, functionDescription, functionHandle, functionName, input, output, dataType, dataFormat, dataHandle, dataDescription, topic, homepage, contact, contactName, contactEmail, contactURL, contactTel, contactRole, resourceType, interface, interfaceType, interfaceDocs, interfaceSpecURL, interfaceSpecFormat, accesibility, publications, publicationsPrimaryID, publicationsOtherID, affiliation, collection, mirror, uses, usesName, usesHomepage, usesVersion, tag, uri, term, sourceRegistry, canonicalID, cost, elixirInfo, elixirStatus, elixirNode, docs, docsHome, docsTermsOfUse, docsDownload, docsCitationInstructions, docsDownloadSource, docsDownloadBinaries, docsGithub, maturity, platform, language, license, credits, creditsDeveloper, creditsContributor, creditsInstitution, creditsInfrastructure, creditsFunding, id


Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET "https://bio.tools/api/tool/?page=5&format=json&name=signalp&sort=name&ord=asc&q=protein-signal-peptide-detection"

Response data
"""""""""""""""""""
================== ========================================================================== =========================
Key Name           Description                                                                Example
================== ========================================================================== =========================
count              The total resource count results for your query                            2313
previous           Link to the previous page                                                  ?page=4
next               Link to the next page                                                      ?page=6
list               An array which will hold multiple resources and their relative information ARRAY
================== ========================================================================== =========================

Resource detail
------------------
Used to obtain information about a single resource by using it's ID.

*HTTP GET*

.. code-block:: text

    https://bio.tools/api/tool/:id/
    https://bio.tools/api/t/:id/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ====================================================                        ===================                 ==========================================================
Parameter  Required  Type                                                                        Default                             Description        
=========  ========  ====================================================                        ===================                 ==========================================================
id         Yes       String                                                                                                          Resource unique ID 
format     No        String(json, xml, api)                                                      json                                Response media type
=========  ========  ====================================================                        ===================                 ==========================================================


Example
"""""""""""""""""""

.. code-block:: bash

   curl -X GET "https://bio.tools/api/tool/signalp/?format=json"

Response data
"""""""""""""""""""
================== ========================================================================== ======================================================================================================
Response           Description                                                                Example
================== ========================================================================== ======================================================================================================
<resource>         The description of the requested resource                                  `See an example <resource> <https://bio.tools/api/tool/CBS/SignalP/4.1?format=json>`_. TODO: fix link
================== ========================================================================== ======================================================================================================


Register a resource
-------------------

.. note:: This method requires the user to be authenticated. `Learn how to obtain a token <http://sphinx.pocoo.org>`_. TODO: fix link

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/tool/
    https://bio.tools/api/t/

Headers
""""""""""
=============  ========  =========================================  ==============================================================================================
Parameter      Required  Allowed values                             Description        
=============  ========  =========================================  ==============================================================================================
Content-Type   Yes       String(application/json, application/xml)  Resource media type 
Authorization  Yes       String(Token <authorization token>)        Authorization header. `Learn how to obtain a token <http://sphinx.pocoo.org>`_. TODO: fix link
=============  ========  =========================================  ==============================================================================================

Example
"""""""""""""""""""

.. code-block:: bash

   curl -X POST -H "Content-Type: application/json" \
   -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7" \
   -d '<resource>' "https://bio.tools/api/tool/"

.. note:: `See an example <resource> <https://bio.tools/api/tool/CBS/SignalP/4.1?format=json>`_. TODO: fix link