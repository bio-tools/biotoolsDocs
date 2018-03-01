## From curators_guide.rst

Short description
.................
*Short and concise textual description of the software function, e.g. "Needleman-Wunsch global alignment of two sequences."*

- **1.** **MUST** provide a terse statement of the primary purpose / function of the tool: what is done not how
- **2.** **MUST** begin with a capital letter and end with a period ('.') 
- **3.** **MUST NOT** include tool name
- **4.** **MUST NOT** include any of the following, *unless* essential to distinguish the tool from other bio.tool entries:

  - general or technical terms ("software", "application", "server", "service", "SOAP", "REST", "RESTful" *etc.*) 
  - provenance information *e.g.* software provider, institute or person name

- **5.** **MUST NOT** describe how good the software is (mentions of applicability are OK)
- **6.** **MUST NOT** include URLs
- **7.** **SHOULD** use declarative sentences (ideally a single sentence!) in the present tense


.. note::
   - see the `syntax guidelines <http://biotools.readthedocs.io/en/latest/api_attribute_model_dev.html#shortDescription>`_.
  
Cmd
...
*A useful command pertinent to the download, e.g. for getting or installing a tool, e.g. "-s best".*

- **1.** **MUST** be a functional commmand of practical value

GRID ID
.......
*Unique identifier (GRID ID) of an organisation that is credited, e.g. "grid.5170.3"*

- **1.** **MUST** correctly identify a credited organisation 


.. note::
   Global Research Identifier Database (GRID) IDs provide a persistent reference to information on research organisations, see https://www.grid.ac/.  If ORCID institutional identifiers become available, these will also be supported.



Telephone number
................
*Telephone number of the entity that is credited, e.g. "+49-89-636-48018"*

- **1.** **MUST** specify a valid telephone number
- **2.** **MUST NOT** specify a telephone number that is not publicly advertised as a contact point for the software, *e.g.* on a webpage or in a publication
- **3.** **MUST NOT** specify a stale (obsolete) telephone number


.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``isPluginFor`` relationship will allow specification of the tool to which the plug-in is applicable.
   
.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``isInterfaceTo`` relationship will allow specification of the data resource (database portal) that a SPARQL endpoint provides an interface to.
     
.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``includes`` relationship will allow specification of the tools that are included in a suite.

.. note::     
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``isInterfaceTo`` and ``uses`` relationships will allow specification of the tools that a web application provides an interface to or uses.

.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``isInterfaceTo`` relationship will allow specification of the tool or data resource (database portal) that the web service provides an interface to.

.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``isInterfaceTo`` relationship will allow specification of the tool that the web service provides an interface to     

.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``includes`` relationship will allow specification of the tools that are included in a workbench.

.. note::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In future, the ``includes`` relationship will allow specification of the tools that are included in a workflow.       

.. tip::
   - `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ allows tool relationships to be defined, but these are not yet supported in bio.tools.  In the meantime, collections may be used to group together related entries.     


## From api_attribute_model_dev.rst
.. _short-description:

Short description
-----------------
*Short and concise textual description of the software function, e.g. "Needleman-Wunsch global alignment of two sequences."*

Attribute name
  shortDescription

Required
  No

Type
  String

Restrictions
  Min length: 10

  Max length: 100

**Example**

.. code-block:: js

  # XML
  <shortDescription>Needleman-Wunsch global alignment of two sequences.</shortDescription>

  # JSON
  "shortDescription": "Needleman-Wunsch global alignment of two sequences."

.. note::
   - minimum 10 and maximum 100 characters.
   - line feeds, carriage returns, tabs, leading and trailing spaces, and multiple spaces are not allowed / will be removed.
  - see the `curation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#shortdescription>`_.


    * cmd
        * Required: No
        * Type: String
        * Restrictions: min length: 1, max length: 100
   <cmd>n/a</cmd>
      "cmd": "n/a",


    * gridId
        * Required: No
        * Type: String
        * Restrictions: pattern: grid.[0-9]{4,}.[a-f0-9]{1,2}
   <gridId>grid.5170.3</gridId>
      "gridId": "grid.5170.3",
	  

          * tel
        * Required: No
        * Type: String
        * Restrictions: min length: 5, max length: 50

	     <tel>12345678</tel>
      "tel": "12345678"
          "tel": "123456798",


          "gridid": "test",

	  
**Example**

.. code-block:: js

  # XML
  <link>
   <isAvailable>Not available</isAvailable>
   <type>Repository</type>
  </download> 
   
  # JSON
  "link":
  [
    {
      "isAvailable": "Not available"
      "type": "Repository"
    }
  ]

.. note::
   - if a link of a certain type is known to *not* be available, this can be specified using the ``isAvailable`` attribute (see Example)	  


**Example**

.. code-block:: js

  # XML
  <download>
   <isAvailable>Not available</isAvailable>
   <type>Source code</type>
  </download> 
   
  # JSON
  "download":
  [
    {
      "isAvailable": "Not available"
      "type": "Source code"
    }
  ]
  
.. note::
   - if a download link of a certain type is known to *not* be available, this can be specified using the ``isAvailable`` attribute (see Example)



**Example**

.. code-block:: js

  # XML
  <documentation>
   <isAvailable>Not available</isAvailable>
   <type>General</type>
  </documentation> 
   
  # JSON
  "documentation":
  [
    {
      "isAvailable": "Not available"
      "type": "General"
    }
  ]
  
.. note::
   - if a documentation link of a certain type is known to *not* be available, this can be specified using the ``isAvailable`` attribute (see Example)
     

**Example**

.. code-block:: js

  # XML
  <publication>
   <isAvailable>Not available</isAvailable>
  </publication> 
   
  # JSON
  "publication":
  [
    {
      "isAvailable": "Not available"
    }
  ]
  
.. note::
   - if a publication is known to *not* be available, this can be specified using the ``isAvailable`` attribute (see Example)     
