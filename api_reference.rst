API endpoints
=============

.. warning:: This document is a work in progress

List all resources
------------------

- **URL**

  ``/tool/``

  ``/t/``

- **Method**

  `GET`

-  **URL Params**

   **Optional**
 
   `page = [ integer ]`

   `format = [ json, xml, api ]`

- **Success Response**

  - **Code:** HTTP_200_OK

    **Content:** 
    ::
      
      {
        "count": < number of resources found >,
        "previous": < link to previous page>,
        "next": < link to next page >,
        "list": [ < list of resources for this page > ]
      }

- **Error Response**

  - **Code:** HTTP_404_NOT_FOUND

    **Content:** ::
      
    {"detail": "Invalid page \"X\": That page contains no results."}

- **Example Call**

    `curl -X GET "https://bio.tools/api/tool/?page=5&format=xml"`


Create a resource
-----------------

- **URL**

  ``/tool/``

  ``/t/``

- **Method**

  `POST`

-  **Header Params**

   **Required:**
 
   `Content-Type: [application/json, application/xml]`

   `Authorization: Token 028595d682541e7q1a5dcf2306eccb720dadafd7`

- **Data Params**

  < JSON / XML object with resource data >


- **Success Response**

  - **Code:** HTTP_200_OK

    **Content:** 
    ::
      
      < JSON / XML object with resource data >

- **Error Response**

  - **Code:** HTTP_400_BAD_REQUEST

    **Content:** ::
    
    < list of validation errors >

- **Example Call**

    `curl -X POST -H "Content-Type: application/json" -H "Authorization: Token 028595d682541e7e1a5dcf2306eccb720dadafd7"  -d '{"id":"SignalP","name":"SignalP","topic":[{"uri":"http://edamontology.org/topic_3070","term":"Biology"}],"function":[{"functionDescription":"predicts the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms","functionHandle":"--someOption","functionName":[{"uri":"http://edamontology.org/operation_0418","term":"Protein signal peptide detection"},{"uri":"http://edamontology.org/operation_0422","term":"Protein cleavage site prediction"}],"input":[{"dataType":{"uri":"http://edamontology.org/data_2044","term":"Sequence"},"dataFormat":[{"uri":"http://edamontology.org/format_1929","term":"FASTA"}]}],"output":[{"dataType":{"uri":"http://edamontology.org/data_1277","term":"Protein features"},"dataFormat":[{"uri":"http://edamontology.org/format_2305","term":"GFF"}]},{"dataType":{"uri":"http://edamontology.org/data_2955","term":"Sequence report"}}]}],"version":"4.1","affiliation":"CBS","homepage":"http://cbs.dtu.dk/services/SignalP/","description":"Prediction of the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms.","accessibility":"Public","cost":"Free with restrictions","maturity":"Stable","credits":{"creditsDeveloper":[{"name":"TN Petersen"}],"creditsInstitution":[{"name":"CBS"}]},"license":"GNU General Public License v3","platform":[{"name":"Linux"},{"name":"Mac"}],"resourceType":[{"name":"Tool"}],"docs":{"docsHome":"http://www.cbs.dtu.dk/services/SignalP","docsDownload":"http://www.cbs.dtu.dk/cgi-bin/sw_request?signalp"},"interface":[{"interfaceType":"Web UI","interfaceDocs":"http://cbs.dtu.dk/services/SignalP/instructions.php"},{"interfaceType":"Command line","interfaceDocs":"http://cbs.dtu.dk/cgi-bin/nph-runsafe?man=signalp","interfaceSpecFormat":"WSDL"}],"publications":{"publicationsOtherID":[{"publicationsOtherID":"doi:10.1038/nmeth.1701"}],"publicationsPrimaryID":"21959131"},"collection":[{"name":"CBS"}],"contact":[{"contactEmail":"hnielsen@cbs.dtu.dk","contactName":"Henrik Nielsen","contactRole":[{"name":"Scientific"},{"name":"General"},{"name":"Developer"}]}]}' "https://bio.tools/api/tool/"`

.. note:: This API endpoint requires the user to be authenticated and use a token. 
          Obtaining the token is (will be) described in the Authentication section.
