*************
API Reference
*************


.. attention::

   - reference docs for the `bio.tools <https://bio.tools>`_ API 
   - to make suggestions about these guidelines please add comments via `GitHub <https://github.com/bio-tools/biotoolsDocs/issues/>`_
   - if you find a bug, have any questions or suggestions, please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.
   - see also the `API Usage Guide <https://biotools.readthedocs.io/en/latest/api_usage_guide.html>`_

     
The bio.tools Web API provides an easy way to access the bio.tools database.


List tools
----------
*List and search through all the available tools. Can sort, filter, and search the results.*

*HTTP GET*

.. code-block:: text

    https://bio.tools/api/tool/
    https://bio.tools/api/t/

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


==================  ============================================================================================
Parameter           Search behaviour                                                                            
==================  ============================================================================================
biotoolsID          Search for bio.tools tool ID (usually quoted - to get exact match)

                    `biotoolsID="signalp" <https://bio.tools/api/t/?biotoolsID="signalp">`_

name                Search for tool name (quoted as needed)

                    `name=signalp <https://bio.tools/api/t/?name=signalp>`_ 
homepage            Exact search for tool homepage URL (**must** be quoted)

                    `homepage="http://cbs.dtu.dk/services/SignalP/" <https://bio.tools/api/t/?homepage="http://cbs.dtu.dk/services/SignalP/">`_ 
description         Search over tool description (quoted as needed)

                    `description="peptide cleavage" <https://bio.tools/api/t/?description="peptide%20cleavage">`_ 
version             Exact search for tool version (**must** be quoted)

                    `version="4.1" <https://bio.tools/api/t/?version="4.1">`_ 
topic               Search for EDAM Topic (term) (usually quoted - to get exact match)

                    `topic="Proteomics" <https://bio.tools/api/t/?topic="Proteomics">`_ 

topicID             Exact search for EDAM Topic (URI): **must** be quoted                                               

                    `topicID="topic_3510" <https://bio.tools/api/t/?topicID="topic_3510">`_ 
function            Fuzzy search over function (input, operation, output, note and command)                         

                    `function="Sequence analysis" <https://bio.tools/api/t/?function="Sequence%20analysis">`_ 
operation           Fuzzy search for EDAM Operation (term)                                                          

                    `operation="Sequence analysis" <https://bio.tools/api/t/?operation="Sequence%20analysis">`_ 
operationID         Exact search for EDAM Operation (ID): must be quoted                                            

                    `operationID="operation_2403" <https://bio.tools/api/t/?operationID="operation_2403">`_ 
dataType            Fuzzy search over input and output for EDAM Data (term)                                         

                    `dataType="Protein sequence" <https://bio.tools/api/t/?dataType="Protein%20sequence">`_ 
dataTypeID          Exact search over input and output for EDAM Data (ID): must be quoted                           

                    `dataTypeID="data_2976" <https://bio.tools/api/t/?dataTypeID="data_2976">`_ 
dataFormat          Fuzzy search over input and output for EDAM Format (term)                                       

                    `dataFormat="FASTA" <https://bio.tools/api/t/?dataFormat="FASTA">`_ 
dataFormatID        Exact search over input and output for EDAM Format (ID): must be quoted                         

                    `dataFormatID="format_1929" <https://bio.tools/api/t/?dataFormatID="format_1929">`_ 
input               Fuzzy search over input for EDAM Data and Format (term)                                         

                    `input="Protein sequence" <https://bio.tools/api/t/?input="Protein%20sequence">`_ 
inputID             Exact search over input for EDAM Data and Format (ID)                                           

                    `inputID="data_2976" <https://bio.tools/api/t/?inputID="data_2976">`_ 
inputDataType       Fuzzy search over input for EDAM Data (term)                                                    

                    `inputDataType="Protein sequence" <https://bio.tools/api/t/?inputDataType="Protein%20sequence">`_ 
inputDataTypeID     Exact search over input for EDAM Data (ID): must be quoted                                      

                    `inputDataTypeID="data_2976" <https://bio.tools/api/t/?inputDataTypeID="data_2976">`_ 
inputDataFormat     Fuzzy search over input for EDAM Format (term)                                                  

                    `inputDataFormat="FASTA" <https://bio.tools/api/t/?inputDataFormat="FASTA">`_ 
inputDataFormatID   Exact search over input for EDAM Format (ID): must be quoted                                    

                    `inputDataFormatID="format_1929" <https://bio.tools/api/t/?inputDataFormatID="format_1929">`_ 
output              Fuzzy search over output for EDAM Data and Format (term)                                        

                    `output="Sequence alignment" <https://bio.tools/api/t/?output="Sequence%20alignment">`_ 
outputID            Exact search over output for EDAM Data and Format (ID): must be quoted                          

                    `outputID="data_0863" <https://bio.tools/api/t/?outputID="data_0863">`_ 
outputDataType      Fuzzy search over output for EDAM Data (term)                                                   

                    `outputDataType="Sequence alignment" <https://bio.tools/api/t/?outputDataType="Sequence%20alignment">`_ 
outputDataTypeID    Exact search over output for EDAM Data (ID): must be quoted                                     

                    `outputDataTypeID="data_0863" <https://bio.tools/api/t/?outputDataTypeID="data_0863">`_ 
outputDataFormat    Fuzzy search over output for EDAM Format (term)                                                 

                    `outputDataFormat="ClustalW format" <https://bio.tools/api/t/?outputDataFormat="ClustalW%20format">`_ 
outputDataFormatID  Exact search over output for EDAM Format (ID): must be quoted                                   

                    `outputDataFormatID="format_1982" <https://bio.tools/api/t/?outputDataFormatID="format_1982">`_ 
toolType            Exact search for tool type (quote as needed)

                    `toolType="Command-line tool" <https://bio.tools/api/t/?toolType="Command-line%20tool">`_ 
collectionID        Exact search for tool collection (normally quoted)

                    `collectionID="Rare Diseases" <https://bio.tools/api/t/?collectionID="Rare%20Diseases">`_ 
maturity            Exact search for tool maturity

                    `maturity=Mature <https://bio.tools/api/t/?maturity=Mature>`_ 
operatingSystem     Exact search for tool operation system                                                          

                    `operatingSystem=Linux <https://bio.tools/api/t/?operatingSystem=Linux>`_ 
language            Exact search for programming language

                    `language=C <https://bio.tools/api/t/?language=C>`_ 
cost                Exact search for cost (quoted as needed)                  

                    `cost="Free of charge" <https://bio.tools/api/t/?cost="Free%20of%20charge">`_ 
license             Exact search for software or data usage license

                    `license=GPL-3.0 <https://bio.tools/api/t/?>`_ 
accessibility       Exact search for tool accessibility (quoted as needed)                                       

                    `accessibility="Open access" <https://bio.tools/api/t/?accessibility="Open%20access">`_ 
credit              Fuzzy search over credit (name, email, URL, ORCID iD, type of entity, type of role and note)    

                    `credit="Henrik Nielsen" <https://bio.tools/api/t/?credit="Henrik%20Nielsen">`_ 
creditName          Exact search for name of credited entity                                                        

                    `creditName="Henrik Nielsen" <https://bio.tools/api/t/?creditName="Henrik%20Nielsen">`_ 
creditTypeRole      Exact search for role of credited entity (quoted as needed)              

                    `creditTypeRole=Developer <https://bio.tools/api/t/?creditTypeRole=Developer>`_ 
creditTypeEntity    Exact search for type of credited entity (quoted as needed)

                    `creditTypeEntity="Funding agency" <https://bio.tools/api/t/?creditTypeEntity="Funding%20agency">`_ 
creditOrcidID       Exact search for ORCID iD of credited entity: must be quoted                                    

                    `creditOrcidID=0000-0001-5121-2036 <https://bio.tools/api/t/?creditOrcidID=0000-0001-5121-2036>`_ 
publication         Fuzzy search over publication (DOI, PMID, PMCID, publication type and tool version) (quoted as needed)            

                    `publication=10.12688/f1000research.12974.1 <https://bio.tools/api/t/?publication=10.12688/f1000research.12974.1>`_ 
publicationID       Exact search for publication ID (DOI, PMID or PMCID): must be quoted                            

                    `publicationID=10.12688/f1000research.12974.1 <https://bio.tools/api/t/?publicationID=10.12688/f1000research.12974.1>`_ 
publicationType     Exact search for publication type

                    `publicationType=Primary <https://bio.tools/api/t/?publicationType=Primary>`_ 
publicationVersion  Exact search for tool version associated with a publication: must be quoted                     

                    `publicationVersion=1.0 <https://bio.tools/api/t/?publicationVersion=1.0>`_ 
link                Fuzzy search over general link (URL, type and note) (quote as needed)

                    `link="Issue tracker" <https://bio.tools/api/t/?link="Issue%20tracker">`_ 
linkType            Exact search for type of information found at a link (quote as needed)

                    `linkType="Issue tracker" <https://bio.tools/api/t/?>`_
documentation       Fuzzy search over documentation link (URL, type and note) (quote as needed)                          

                    `documentation=Manual <https://bio.tools/api/t/?documentation=Manual>`_ 
documentationType   Exact search for type of documentation (quote as needed)                     

                    `documentationType=Manual <https://bio.tools/api/t/?documentationType=Manual>`_ 
download            Fuzzy search over download link (URL, type, version and note) (quote as needed)

                    `download=Binaries <https://bio.tools/api/t/?download=Binaries>`_ 
downloadType        Exact search for type of download (quote as needed)                 

                    `downloadType=Binaries <https://bio.tools/api/t/?downloadType=Binaries>`_ 
downloadVersion     Exact search for tool version associated with a download: must be quoted                        

                    `downloadVersion="1.0" <https://bio.tools/api/t/?downloadVersion="1.0">`_ 
otherID             Fuzzy search over alternate tool IDs (ID value, type of ID and version)                         

                    `otherID=SCR_015644 <https://bio.tools/api/t/?otherID=SCR_015644>`_ 
otherIDType         Exact search for type of alternate tool ID                                                      

                    `otherIDType=RRID <https://bio.tools/api/t/?otherIDType=RRID>`_ 
otherIDVersion      Exact search for tool version associated with an alternate ID: must be quoted                   

                    `otherIDVersion="1.0" <https://bio.tools/api/t/?otherIDVersion="1.0">`_ 
==================  ============================================================================================


.. important::
   Values of the following parameters **must** be given in quotes to get sensible (or any) results:
     * ``homepage``
     * ``version``
     * ``topicID``
     * ...

   *e.g.* 
     * ``https://bio.tools/api/tool?topicID="topic_3510"``
       
   Values of other parameters can be quoted or unquoted:
     *  Unquoted values invoke a fuzzy word search: it will search for fuzzy matches of words in the search phrase, to the target field
     *  Quoted values invoke an exact phrase search; it will search for an exact match of the full-length of the search phrase, to the target field

   *e.g.*
     * ``https://bio.tools/api/tool?biotoolsID="signalp"`` returns the tool with the ID of "signalp"
     * ``https://bio.tools/api/tool?biotoolsID=signalp`` returns tools with an ID that fuzzy-matches "signalp"       

	
.. caution::
   The parameters are (currently) case-sensitive, *e.g.* you **must** use ``&biotoolsID=`` and not ``&biotoolsid``==================  ============================================================================================


.. important=  The API parameters will be made case-insensitive in future.


Example
"""""""

.. code-block:: bash

   curl -X GET "https://bio.tools/api/tool/?page=1&format=json&name=signalp&sort=name&ord=asc&q=protein-signal-peptide-detection"

.. note::
   An EDAM concept ID can be specified as a concept URI or ID:
     * Concept URI *e.g.* ``http://edamontology.org/operation_2403``
     * Concept ID *e.g.* ``operation_2403``

   In future we may add support for:  
     * Concept CURIE *e.g.* ``EDAM:operation_2403``
     * Numerical ID *e.g.* ``2403``

   Note: URIs and IDs **must** be quoted, *e.g.* ``&topicID="operation_2403"``
   
     
.. caution::
   If querying by ``homepage`` you must quote the query value, *e.g.*


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

    https://bio.tools/api/tool/:id/
    https://bio.tools/api/t/:id/
    https://bio.tools/api/:id/


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

   curl -X GET "https://bio.tools/api/tool/signalp/?format=json"


Register a tool
---------------

*Register a new tool.*


.. important:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/tool/
    https://bio.tools/api/t/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
data       Yes       Tool     Tool you wish to register.
                              See an `example tool <https://bio.tools/api/tool/SignalP?format=json>`_.
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
   -d '<resource>' "https://bio.tools/api/tool/"


Validate registering a tool
---------------------------

*Test registering a tool without it actually being saved into the database.*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/tool/validate/
    https://bio.tools/api/t/validate/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
data       Yes       Tool     Tool you wish to validate.
                              See an `example tool <https://bio.tools/api/tool/SignalP?format=json>`_.
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
   -d '<resource>' "https://bio.tools/api/tool/validate/"


Update a tool
-------------
*Update a tool description.*

.. important:: This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP PUT*

.. code-block:: text

    https://bio.tools/api/tool/:id/
    https://bio.tools/api/t/:id/
    https://bio.tools/api/:id/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
id         Yes       String   biotoolsID 
data       Yes       Tool     Description with which you wish to update the tool
                              See an `example tool <https://bio.tools/api/tool/SignalP?format=json>`_.
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
   -d '<resource>' "https://bio.tools/api/tool/SignalP"



Validate updating a tool
------------------------
*Test updating a tool without it actually being saved into the database.*

.. important::
   This method requires the user to be authenticated. Learn how to :ref:`Token`.

*HTTP PUT*

.. code-block:: text

    https://bio.tools/api/tool/:id/validate/
    https://bio.tools/api/t/:id/validate/
    https://bio.tools/api/:id/validate/

Endpoint Parameters
"""""""""""""""""""
=========  ========  ======== ====================================================================================================================================
Parameter  Required  Type     Description        
=========  ========  ======== ====================================================================================================================================
id         Yes       String   biotoolsID 
data       Yes                Tool Description with which you wish to update the tool for validation
                              See an `example tool <https://bio.tools/api/tool/SignalP?format=json>`_.
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
   -d '<resource>' "https://bio.tools/api/tool/SignalP/validate/"


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

    https://bio.tools/api/tool/:id/
    https://bio.tools/api/t/:id/
    https://bio.tools/api/:id/

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
   "https://bio.tools/api/tool/SignalP"


List used terms
---------------
*Obtain a list of terms registered with tools for some attributes, e.g. a list of names of all tools.*

*HTTP GET*

.. code-block:: text

    https://bio.tools/api/used-terms/:attribute

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

   curl -X GET "https://bio.tools/api/used-terms/name/?format=json"

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

    https://bio.tools/api/rest-auth/registration/

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
   "https://bio.tools/api/rest-auth/registration/"



Verify a user account
---------------------

*Verifies a user account based on the emailed verification key.*

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/rest-auth/registration/verify-email/

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
   "https://bio.tools/api/rest-auth/registration/verify-email/"


.. _Token:

Log in / obtain token
---------------------

*Logs the user in and returns an authentication token.*

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/rest-auth/login/

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
   "https://bio.tools/api/rest-auth/login/"

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

    https://bio.tools/api/rest-auth/user/

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
   "https://bio.tools/api/rest-auth/user/?format=json"

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

    https://bio.tools/api/rest-auth/logout/

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
  "https://bio.tools/api/rest-auth/logout/"


Reset user password
-------------------

*Send a password reset email.*

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/rest-auth/password/reset/

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
   "https://bio.tools/api/rest-auth/password/reset/"

Confirm password reset
----------------------

*Confirm a password reset using uid and token from a password reset email.*

*HTTP POST*

.. code-block:: text

    https://bio.tools/api/rest-auth/password/reset/confirm/

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
   "https://bio.tools/api/rest-auth/password/reset/confirm/"

Stats
-----
*Compile stats about a the registry.*

*HTTP GET*

.. code-block:: text

    https://bio.tools/api/stats

Example
"""""""

.. code-block:: bash

   curl -X GET "https://bio.tools/api/stats"
