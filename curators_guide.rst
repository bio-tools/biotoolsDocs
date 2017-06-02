Curators Guide
==============

Guidelines for `bio.tools <https://bio.tools>`_  curators, including EDAM annotation guidelines, will appear here. 

General advice 
==============

Attributes 
==========

Name
^^^^
*Canonical software name assigned by the software developer or service provider*
Exmaple: "SignalP"

.. note:: The name has a 100 character limit and may only contain uppercase and lowercase letters, decimal digits, period, comma, dash, colon, plus symbol, semicolon and parentheses.

- use the name that is commonly used to refer to the software
- preserve the canonical capitalisation, if any *e.g.* ``ExPASy`` 
- use the short form of the name, if available *e.g.* use ``ExPASy`` not ``ExPASy Bioinformatics Resource Portal``
- for database portals, use common abbreviation if available, *e.g.*  ``PDB`` **not** ``The Protein Databank``
- for APIs, use the pattern ``name API`` *e.g.* ``Open PHACTS API``.  
- for Web services (SOAP+WSDL), use the pattern ``name web service`` *e.g.* ``EMMA web service``.  


.. tip::
   - for software that essentially just wraps or provides an interface to some other tool, use the pattern ``toolName providerName`` where ``providerName`` is the name of some institute, workbench, collection *etc.*, *e.g.* ``cufflinks cloud IFB``.  **Do not** misappropriate the original name!
   - in case of mulitple related entries which may all include a common tool in part of their name, be consistent, *e.g.* ``HOMER-A`` and ``HOMER-M``
  
.. attention:: in general, **do not** include general or technical terms such as "software", "application", "server", "service", "SOAP", "REST", "RESTful" *etc.* unless these are part of the common name
  
  
Description
^^^^^^^^^^^
*Short and concise textual description of the software function*
Example: "Detect and visualise single-nucleotide polymorphisms (SNPs)"

- use a single declarative sentence in the present tense
- provide only a terse statement of the tool function: what is done not how: this can include the primary operation(s) and possibly the types of primary input and output data
- **do not** include tool name
- **do not** include technical terms describing the type of software
- **do not** include details about the software provider *e.g.* institute or person name




Do not include tool name. Minimum 10 and maximum 200 characters. See http://biotools.readthedocs.io/.



Homepage
^^^^^^^^
*Homepage of the software, or some URL that best serves this purpose*

Software type
^^^^^^^^^^^^^
*The type of application software: a discrete software entity can have more than one type*

Unique ID
^^^^^^^^^
*Unique ID of the tool that is assigned upon registration of the software in bio.tools*

Topic
^^^^^
*General scientific domain the software serves or other general category, e.g. 'Proteomics'*

Scientific operations
^^^^^^^^^^^^^^^^^^^^^
*The basic operation(s) performed by the software, e.g. 'Multiple sequence alignment'*

Type of input and output data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Type of primary input / output data (if any), e.g. 'Protein sequences'*

Supported data formats
^^^^^^^^^^^^^^^^^^^^^^
*Allowed format(s) of primary inputs/outputs, e.g. 'FASTA'*

Publications
^^^^^^^^^^^^
*Publications about the software*

Contact information
^^^^^^^^^^^^^^^^^^^
*Primary contact, e.g. a person, helpdesk or mailing list*

Issue tracker
^^^^^^^^^^^^^
*Link to tracker for software issues, bug reports, feature requests etc.*

Mailing list
^^^^^^^^^^^^
*Link to mailing list for software announcements, discussions, support etc.*

Repository
^^^^^^^^^^
*Link to repository where source code, data and other files may be downloaded*

Documentation
^^^^^^^^^^^^^
*Link to documentation about the software e.g. manual, API specification or training material*

License
^^^^^^^
*Software or data usage license*


Tool types
==========


