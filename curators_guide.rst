Curators Guide
==============

**UNDER CONSTRUCTION**: guidelines for `bio.tools <https://bio.tools>`_  curators, including EDAM annotation guidelines, will appear here. 

.. note::
    For curation advice or to make suggestions about these guidelines please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.

bio.tools includes all types of bioinformatics tools - application software with well-defined data processing functions (inputs, outputs and operations).  bio.tools includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions.  Tools may be available for immediate use as online services, or in a form which a user can download, install, configure and run themselves.  Each bio.tools entry describes a discrete, but possibly complex software entity.  The `types of tools <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst#tool-types>`_ defined in the `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ define the technical scope of the registry, i.e. the types of software that may be included.

The guidelines below are organised as follows:
- guidelines on specific attributes defined in the `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ and organised into sections as they appear in the `bio.tools <https://bio.tools>`_ registration user interface
- general guidelines for EDAM annotations
- guidelines specific to individual `types of tools <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst#tool-types>`_

    
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
- for Web services (SOAP+WSDL), use the pattern ``name WS`` *e.g.* ``EMMA WS``


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
     
.. note::
   - the ID is a URL-safe derivative of (often identical to) the tool name restricted to 12 characters maximum.  Unreserved characters (uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde) are allowed. All other characters including reserved characters and other characters deemed unsafe are not allowed. Spaces are preserved as underscore ("_").
   - once set, the ID can only be changed by bio.tools admin!
   - the ID is used in the Tool Card URLs, *e.g.* https://bio.tools/tool/signalp
   - the 12 char limit is not currently enforced by bio.tools and will be increased in the next release of `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_.

- the ID should be clean and intuitive: where possible, simply use the default
- **do not** truncate the name (in the middle of a word, or at all) if this renders the ID ugly or meaningless
- if (but only if) necessary, use '_' to delimit parts of names
   - for wrappers, interfaces *etc.* to other tool, use the pattern ``toolName-providerName`` as per guideline for `name <>`_ above, *e.g.* ``cufflinks-cloud IFB``.


Version
^^^^^^^
**Version (typically a version number) of the software assigned by the software developer or service provider.**

*e.g.* **4.1**

.. note:: The version has a 100 character limit and may only contain uppercase and lowercase letters, decimal digits, period, comma, dash, colon, plus symbol, semicolon and parentheses.

- specify exactly the version label in use
- for database portals and web applications, only specify a version if this is used in the public name

.. attention::
   - **do not** include labels such as "v", "ver", "version", "rel", "release" *etc.*
   - **do not** assume version "1" in case the version number is not readily findable

  
  
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
**Unique ID of a collection that the software has been assigned to within bio.tools.**
*e.g.* **de.NBI**

.. note::
   - the ID is a URL-safe name restricted to 12 characters maximum.  Unreserved characters (uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde) are allowed. All other characters including reserved characters and other characters deemed unsafe are not allowed.
   - the 12 char limit is not currently enforced by bio.tools and will be increased in the next release of `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_.
   - collections are used to group together entries which would otherwise be unrelated
   - collections may be created for some other registry, catalogue, WIKI *etc.* where this tool is described, or for any arbitrary purpose.
     
- keep it short and intuitive



Function
--------

.. note::
   - bio.tools usee a model of software (see Figure below) defined within `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_.  A tool can have one or more basic functions (modes of operation), each function performing one or more specific operation(s) (e.g."Sequence alignment"), each of which may have one or more primary inputs and outputs, each of a defined type of data and listing supported format(s).
   - See the general `EDAM annotation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#edam-annotation-guidelines>`_.
  
.. image:: tool_function.PNG

Operation
^^^^^^^^^
**The basic operation(s) performed by the software, e.g. 'Multiple sequence alignment'**

.. note::
   - an EDAM Operation concept URL and / or term are specified, e.g. "Multiple sequence alignment", http://edamontology.org/operation_0492.

- specify the primary operations performed by this function of the tool
     
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
****
*e.g.* ****
     
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
****
*e.g.* ****

Language
^^^^^^^^
****
*e.g.* ****

Maturity
^^^^^^^^
****
*e.g.* ****

License
^^^^^^^
****
*e.g.* ****

Cost
^^^^
****
*e.g.* ****

Accessibility
^^^^^^^^^^^^^
****
*e.g.* ****

Contact
-------
**Primary contact, e.g. a person, helpdesk or mailing list**

Email
^^^^^
****
*e.g.* ****

URL
^^^
****
*e.g.* ****

Name
^^^^
****
*e.g.* ****

Telephone number
^^^^^^^^^^^^^^^^
****
*e.g.* ****

Links
-----

URL
^^^
****
*e.g.* ****

Comment
^^^^^^^
****
*e.g.* ****

Link type
^^^^^^^^^
****
*e.g.* ****

Download
--------

URL
^^^
****
*e.g.* ****

Comment
^^^^^^^
****
*e.g.* ****

Download type
^^^^^^^^^^^^^
****
*e.g.* ****

Documentation
-------------

URL
^^^
****
*e.g.* ****

Comment
^^^^^^^
****
*e.g.* ****

Documentation type
^^^^^^^^^^^^^^^^^^
****
*e.g.* ****


Publications
------------
**Publications about the software**

PubMed Central ID
^^^^^^^^^^^^^^^^^
****
*e.g.* ****

PubMed ID
^^^^^^^^^
****
*e.g.* ****

Digital Object ID
^^^^^^^^^^^^^^^^^
****
*e.g.* ****

Publication type
^^^^^^^^^^^^^^^^
****
*e.g.* ****

Credits
-------

GRID ID
^^^^^^^
****
*e.g.* ****

ORCID ID
^^^^^^^^
****
*e.g.* ****

Name
^^^^
****
*e.g.* ****

Email
^^^^^
****
*e.g.* ****

URL
^^^
****
*e.g.* ****

Entity type
^^^^^^^^^^^
****
*e.g.* ****

Role
^^^^
****
*e.g.* ****

Comment
^^^^^^^
****
*e.g.* ****



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



