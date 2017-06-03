Curators Guide
==============

**UNDER CONSTRUCTION**: guidelines for `bio.tools <https://bio.tools>`_  curators, including EDAM annotation guidelines, will appear here. 

.. note::
    For curation advice or to make suggestions about these guidelines please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.

    bio.tools includes all types of bioinformatics tools - application software with well-defined data processing functions (inputs, outputs and operations).  bio.tools includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions.  Tools may be available for immediate use as online services, or in a form which a user can download, install, configure and run themselves.  Each bio.tools entry describes a discrete, but possibly complex software entity.  The `types of tools <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst#tool-types>`_ defined in the `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ define the technical scope of the registry, i.e. the types of software that may be included.

    
Summary
-------

Name
^^^^
**Canonical software name assigned by the software developer or service provider**

*e.g.* **"SignalP"**

.. note:: The name has a 100 character limit and may only contain uppercase and lowercase letters, decimal digits, period, comma, dash, colon, plus symbol, semicolon and parentheses

- use the name that is commonly used to refer to the software
- preserve the canonical capitalisation, if any *e.g.* ``ExPASy`` 
- use the short form (*e.g.* acronym) of the name, if available *e.g.* use ``ExPASy`` **not** ``ExPASy Bioinformatics Resource Portal``
- if shortening the name is necessary, do no truncate within a word and ensure the name remains intuitive
- for database portals, use common abbreviation if available, *e.g.*  ``PDB`` **not** ``The Protein Databank``
- for APIs, use the pattern ``name API`` *e.g.* ``Open PHACTS API``
- for Web services (SOAP+WSDL), use the pattern ``name web service`` *e.g.* ``EMMA web service``


.. tip::
   - for software that essentially just wraps or provides an interface to some other tool, use the pattern ``toolName providerName`` where ``providerName`` is the name of some institute, workbench, collection *etc.*, *e.g.* ``cufflinks cloud IFB``.  **Do not** misappropriate the original name!
   - in case of mulitple related entries which may all include a common tool in part of their name, be consistent, *e.g.* ``HOMER-A`` and ``HOMER-M``, or ``Open PHACTS`` and ``Open PHACTS API``
  
.. attention::
   - **do not** include version information **unless** this is used in the common name (*e.g.* as in the tool homepage and publication)
   - **do not** include general or technical terms such as "software", "application", "server", "service", "SOAP", "REST", "RESTful" *etc.* unless these are part of the common name


ID
^^
**Unique ID of the tool that is assigned upon registration of the software in bio.tools**

*e.g.* **signalp**

.. important:: The tool ID can only be set by bio.tools admin!
	      
.. note::
   - The ID is a URL-safe derivative of (often identical to) the tool name restricted to 12 characters maximum.  Unreserved characters (uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde) are allowed. All other characters including reserved characters and other characters deemed unsafe are not allowed. Spaces can be preserved as underscore ("_").
   - The ID is used in the Tool Card URLs, *e.g.* https://bio.tools/tool/signalp

- where possible, simply use the tool name
- if (but only if) necessary, use '_' to delimit parts of names
- **do not** truncate the name (in the middle of a word, or at all) if this renders the ID ugly or meaningless


Version
^^^^^^^

  
Description
^^^^^^^^^^^
**Short and concise textual description of the software function**

*e.g.* **"Detect and visualise single-nucleotide polymorphisms (SNPs)"**

.. note:: Description is minimum 10 and maximum 200 characters

- use declarative sentences (ideally a single sentence!) in the present tense
- provide only a terse statement of the tool function: what is done not how: this can include the primary operation(s) and possibly the types of primary input and output data
- begin with a capital letter and end with a '.': 

.. attention::
   **do not** include any of the following:

   - tool name
   - technical terms describing the type of software
   - details about the software provider *e.g.* institute or person name
   - URLs
   - statements about how good the software is (although mentions of applicability are OK)

   **do not** truncate longer descriptions within words!
  

Homepage
^^^^^^^^
**Homepage of the software, or some URL that best serves this purpose**

*e.g.* **http://cbs.dtu.dk/services/SignalP/**

- the URL should resolve to a web page of information specific to the software
- in case a tool lacks it's own website, URL of it's code repository is OK

.. attention:: **do not** specify a general URL such as an institutional homepage

Collection
^^^^^^^^^^


Function
--------

.. note::
- A tool can perform one or more basic functions (a mode of operation), each function performing one or more specific operation(s) (e.g."Sequence alignment"), each of which may have one or more primary inputs and outputs, each of a defined type of data and listing supported format(s) (see Figure below).
- See the general `EDAM annotation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#edam-annotation-guidelines>`_.
  
.. image:: tool_function.PNG

Operation
^^^^^^^^^
**The basic operation(s) performed by the software, e.g. 'Multiple sequence alignment'**

.. note::
   - an EDAM Operation concept URL and / or term are specified, e.g. "Multiple sequence alignment", http://edamontology.org/operation_0492.

Data type (input and output data)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Type of primary input / output data (if any), e.g. 'Protein sequences'**

.. note::
   - an EDAM Data concept URL and / or term are specified, e.g. "Protein sequences", http://edamontology.org/data_2976. 

Data format (input and output data)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Allowed format(s) of primary inputs/outputs, e.g. 'FASTA'**

.. note::
   - an EDAM Format concept URL and / or term are specified, e.g. "FASTA", http://edamontology.org/format_1929.

Comment
^^^^^^^
     
Labels
------

Tool type
^^^^^^^^^
**The type of application software: a discrete software entity can have more than one type**

*e.g.* **Web application**, **Command-line tool**

.. note:: bio.tools includes all types of bioinformatics tools: application software with well-defined data processing functions (inputs, outputs and operations). When registering a tool, one or more tool types may be assigned, reflecting the different facets of the software being described.

- read the `description of tool types <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst#tool-types>`_
- assign all types that are applicable

.. tip::  In cases where a given software is described by more than one entry (*e.g.* a web application and its API are described separately) then assign only the types that are applicable

Topic
^^^^^
**General scientific domain the software serves or other general category, e.g. 'Proteomics'**

.. note::
   - an EDAM Topic concept URL and / or term are specified, e.g. "Proteomics", http://edamontology.org/topic_0121.
   - see the general `EDAM annotation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#edam-annotation-guidelines>`_.

Operating system
^^^^^^^^^^^^^^^^

Language
^^^^^^^^

Maturity
^^^^^^^^

License
^^^^^^^

Cost
^^^^

Accessibility
^^^^^^^^^^^^^

Contact
-------
**Primary contact, e.g. a person, helpdesk or mailing list**

Email
^^^^^

URL
^^^

Name
^^^^

Telephone number
^^^^^^^^^^^^^^^^

Links
-----

URL
^^^

Comment
^^^^^^^

Link type
^^^^^^^^^

Download
--------

URL
^^^

Comment
^^^^^^^

Download type
^^^^^^^^^^^^^

Documentation
-------------

URL
^^^

Comment
^^^^^^^

Documentation type
^^^^^^^^^^^^^^^^^^


Publications
------------
**Publications about the software**

PubMed Central ID
^^^^^^^^^^^^^^^^^

PubMed ID
^^^^^^^^^

Digital Object ID
^^^^^^^^^^^^^^^^^

Publication type
^^^^^^^^^^^^^^^^

Credits
-------

GRID ID
^^^^^^^

ORCID ID
^^^^^^^^

Name
^^^^

Email
^^^^^

URL
^^^

Entity type
^^^^^^^^^^^

Role
^^^^

Comment
^^^^^^^



EDAM annotation guidelines
--------------------------

- if in any doubt as to meaning, refer to the concept definitions using:
  - ``EBI OLS browser <http://www.ebi.ac.uk/ols/ontologies/edam>`_
  - ``NCBO BioPortal browser <https://bioportal.bioontology.org/ontologies/EDAM>`_
  
- use the most specific concept(s) that apply
- in case more than sibling concept is applicable (*i.e.* concepts under a common parent) than consider using parent concept instead
- by default

.. important:: in cases of multiple annotations per field, **do not** specify both a term and it's parent or other ancestor

Guidelines per tool type
------------------------



