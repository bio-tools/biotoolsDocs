Curators Guide
==============

**UNDER CONSTRUCTION**: guidelines for `bio.tools <https://bio.tools>`_  curators, including EDAM annotation guidelines, will appear here. 

bio.tools includes all types of *bioinformatics tools* - application software with well-defined data processing functions (inputs, outputs and operations).  bio.tools includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions.  Tools may be available for immediate use as online services, or in a form which a user can download, install, configure and run themselves.  Each bio.tools entry describes a discrete, but possibly complex software entity.  The `types of tools <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst#tool-types>`_ defined in the `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ define the technical scope of the registry, *i.e.* the types of software that may be included.

The guidelines below are organised as follows:

- `guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#summary>`_ on specific attributes defined in the `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ and organised into sections as they appear in the `bio.tools <https://bio.tools>`_ registration user interface
- `guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#id19>`_ for EDAM annotations in general
- `guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#guidelines-per-tool-type>`_ specific to individual `types of tools <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst#tool-types>`_

.. note::
    For curation advice or to make suggestions about these guidelines please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.

    
Summary
-------

Name
^^^^
**Canonical software name assigned by the software developer or service provider**

*e.g.* **"SignalP"**

- use the name that is commonly used to refer to the software
- preserve the canonical capitalisation, if any *e.g.* ``ExPASy`` 
- use the short form (*e.g.* acronym) of the name, if available *e.g.* use ``ExPASy`` **not** ``ExPASy Bioinformatics Resource Portal``
- if shortening the name is necessary, do no truncate within a word and ensure the name remains intuitive
- for database portals, use common abbreviation if available, *e.g.*  ``PDB`` **not** ``The Protein Databank``
- for APIs, use the pattern ``name API`` *e.g.* ``Open PHACTS API``
- for Web services (SOAP+WSDL), use the pattern ``name WS`` *e.g.* ``EMMA WS``

.. note:: The name has a 100 character limit and may only contain uppercase and lowercase letters, decimal digits, period, comma, dash, colon, plus symbol, semicolon and parentheses

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
     
- the ID should be clean and intuitive: where possible, simply use the default
- **do not** truncate the name (in the middle of a word, or at all) if this renders the ID ugly or meaningless
- if (but only if) necessary, use '_' to delimit parts of names
   - for wrappers, interfaces *etc.* to other tool, use the pattern ``toolName-providerName`` as per guideline for `name <http://biotools.readthedocs.io/en/latest/curators_guide.html#name>`_ above, *e.g.* ``cufflinks-cloud IFB``.

.. note::
   - the ID is a URL-safe derivative of (often identical to) the tool name restricted to 12 characters maximum.  Unreserved characters (uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde) are allowed. All other characters including reserved characters and other characters deemed unsafe are not allowed. Spaces are preserved as underscore ("_").
   - once set, the ID can only be changed by bio.tools admin!
   - the ID is used in the Tool Card URLs, *e.g.* https://bio.tools/tool/signalp
   - the 12 char limit is not currently enforced by bio.tools and will be increased in the next release of `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_.


Version
^^^^^^^
**Version (typically a version number) of the software assigned by the software developer or service provider.**

*e.g.* **4.1**

- specify exactly the version label in use
- for database portals and web applications, only specify a version if this is used in the public name

.. note:: The version has a 100 character limit and may only contain uppercase and lowercase letters, decimal digits, period, comma, dash, colon, plus symbol, semicolon and parentheses.

.. attention::
   - **do not** include labels such as "v", "ver", "version", "rel", "release" *etc.*
   - **do not** assume version "1" in case the version number is not readily findable

  
  
Description
^^^^^^^^^^^
**Short and concise textual description of the software function**

*e.g.* **"Prediction of the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms."**

- use declarative sentences (ideally a single sentence!) in the present tense
- provide only a terse statement of the tool function: what is done not how: this can include the primary operation(s) and possibly the types of primary input and output data
- begin with a capital letter and end with a '.': 

.. note:: Description is minimum 10 and maximum 200 characters

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

*e.g.* **CBS**

- keep it short and intuitive

.. note::
   - the ID is a URL-safe name restricted to 12 characters maximum.  Unreserved characters (uppercase and lowercase letters, decimal digits, hyphen, period, underscore, and tilde) are allowed. All other characters including reserved characters and other characters deemed unsafe are not allowed.
   - the 12 char limit is not currently enforced by bio.tools and will be increased in the next release of `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_.
   - collections are used to group together entries which would otherwise be unrelated
   - collections may be created for some other registry, catalogue, WIKI *etc.* where this tool is described, or for any arbitrary purpose.
     


Function
--------

bio.tools usee a model of software (see Figure below) defined within `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_.  A tool can have one or more basic functions (modes of operation), each function performing one or more specific operation(s) (e.g."Sequence alignment"), each of which may have one or more primary inputs and outputs, each of a defined type of data and listing supported format(s).

See the general `EDAM annotation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#edam-annotation-guidelines>`_.
  
.. image:: tool_function.PNG

Operation
^^^^^^^^^
**The basic operation(s) performed by the software**

*e.g.* 'Protein signal peptide detection' (http://edamontology.org/operation_0418)**

- specify the primary operations performed by this function of the tool

.. note::
   - an EDAM Operation concept URL and / or term are specified, *e.g.* "Multiple sequence alignment", http://edamontology.org/operation_0492.

     
Data type (input and output data)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Type of primary input / output data (if any)**

*e.g.* 'Sequence' (http://edamontology.org/data_2044)**

.. note::
   - an EDAM Data concept URL and / or term are specified, *e.g.* "Protein sequences", http://edamontology.org/data_2976. 

Data format (input and output data)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Allowed format(s) of primary inputs/outputs**

*e.g.* 'FASTA' (http://edamontology.org/format_1929)**

.. note::
   - an EDAM Format concept URL and / or term are specified, *e.g.* "FASTA", http://edamontology.org/format_1929.

Comment
^^^^^^^
****
*e.g.* ****
     
Labels
------

Tool type
^^^^^^^^^
**The type of application software: a discrete software entity can have more than one type**

*e.g.* **Command-line tool**, **Web application**, 

- assign all types (see below) that are applicable

.. csv-table::
   :header: "Type", "Description"
   :widths: 25, 100
      
   "Command-line tool", "A tool with a text-based (command-line) interface."
   "Database portal", "A Web application, suite or workbench providing a portal to a biological database."
   "Desktop application", "A tool with a graphical user interface that runs on your desktop environment, *e.g.* on a PC or mobile device."
   "Library", "A collection of components that are used to construct other tools.  bio.tools scope includes component libraries performing high-level bioinformatics functions but excludes lower-level programming libraries."
   "Ontology", "A collection of information about concepts, including terms, synonyms, descriptions etc."
   "Plug-in", "A software component encapsulating a set of related functions, which are not standalone, *i.e.* depend upon other software for its use, *e.g.* a Javascript widget, or a plug-in, extension add-on etc. that extends the function of some existing tool."
   "Script", "A tool written for some run-time environment (*e.g.* other applications or an OS shell) that automates the execution of tasks. Often a small program written in a general-purpose languages (*e.g.* Perl, Python) or some domain-specific languages (*e.g.* sed)."
   "SPARQL endpoint", "A service that provides queries over an RDF knowledge base via the SPARQL query language and protocol, and returns results via HTTP."
   "Suite", "A collection of tools which are bundled together into a convenient toolkit.  Such tools typically share related functionality, a common user interface and can exchange data conveniently.  This includes collections of stand-alone command-line tools, or Web applications within a common portal."
   "Web application", "A tool with a graphical user interface that runs in your Web browser."
   "Web API", "An application programming interface (API) consisting of endpoints to a request-response message system accessible via HTTP.  Includes everything from simple data-access URLs to RESTful APIs."
   "Web service", "An API described in a machine readable form (typically WSDL) providing programmatic access via SOAP over HTTP."
   "Workbench", "An application or suite with a graphical user interface, providing an integrated environment for data analysis which includes or may be extended with any number of functions or tools.  Includes workflow systems, platforms, frameworks etc."
   "Workflow", "A set of tools which have been composed together into a pipeline of some sort.  Such tools are (typically) standalone, but are composed for convenience, for instance for batch execution via some workflow engine or script."

  
.. note:: bio.tools includes all types of bioinformatics tools: application software with well-defined data processing functions (inputs, outputs and operations). When registering a tool, one or more tool types may be assigned, reflecting the different facets of the software being described.

.. tip::  In cases where a given software is described by more than one entry (*e.g.* a web application and its API are described separately) then assign only the types that are applicable

Topic
^^^^^
**General scientific domain the software serves or other general category**

*e.g.* 'Protein sites, features and motifs' (http://edamontology.org/topic_3510)

.. note::
   - an EDAM Topic concept URL and / or term are specified, *e.g.* "Proteomics", http://edamontology.org/topic_0121.
   - see the general `EDAM annotation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#edam-annotation-guidelines>`_.

Operating system
^^^^^^^^^^^^^^^^
**The operating system supported by a downloadable software package.**

*e.g.* **Linux**

- valid types are defined in `biotoolsSchema <https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-2.0.0>`_ : assign all that apply

Language
^^^^^^^^
**Name of programming language the software source code was written in.**

*e.g.* ****

- valid types are defined in `biotoolsSchema <https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-2.0.0>`_ : assign all that apply
  
Maturity
^^^^^^^^
**How mature the software product is.**

*e.g.* **Mature**

- assign the tag (see below) that is most applicable; if you are not sure, then do not complete this field

.. csv-table::
   :header: "Maturity", "Description"
   :widths: 25, 100

   "Emerging", "Nascent or early release software that may not yet be fully featured or stable."
   "Mature", "Software that is generally considered to fulfill several of the following: secure, reliable, actively maintained, fully featured, proven in production environments, has an active community, and is described or cited in the scientific literature."
   "Legacy", "Software which is no longer in common use, deprecated by the provider, superseded by other software, replaced by a newer version, is obsolete etc."
   
  
License
^^^^^^^
**Software or data usage license.**

*e.g.* **CBS License**

- valid types are defined in `biotoolsSchema <https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-2.0.0>`_ : assign the one that applies
- use 'Proprietary' in case where some license (not defined in biotoolsSchema) exists and must be obtained from the provider before the software can be downloaded, used, owned *etc.*
- use 'Other' in all other cases where a license exists but is not defined in biotoolsSchema (and consider requesting it's addition via `GitHub <https://github.com/bio-tools/biotoolsSchema/issues/>`_)
  
.. note::
   Most permisible values are identifiers from the SPDX license list (https://spdx.org/licenses/). In future, based on the specified license a label (e.g. "Open-source") may be attached to the bio.tools entry (see table below)

.. csv-table::  Labelling based on license (future work)
   :header: "License", "Description"
   :widths: 25, 100

   "Open-source", "Software is made available under a license approved by the Open Source Initiative (OSI). The software is distributed in a way that satisfies the 10 criteria of the Open Source Definition maintained by OSI (see https://opensource.org/docs/osd). The source code is available to others."
   "Free software", "Free as in 'freedom' not necessarily free of charge.  Software is made available under a license approved by the Free Software Foundation (FSF). The software satisfies the criteria of the Free Software Definition maintained by FSF (see http://www.gnu.org/philosophy/free-sw.html). The source code is available to others."
   "Free and open source", "Software is made available under a license approved by both the Open Source Initiative (OSI) and the Free Software Foundation (FSF), and satisfies the criteria of the OSI Open Source Definition maintained (https://opensource.org/docs/osd) and the FSF Free Software Definition (http://www.gnu.org/philosophy/free-sw.html).  Such software ensures users have the freedom to run, copy, distribute, study, change and improve the software.  The source code is available to others."
   "Copyleft", "Software is made available under a license designated as 'copyleft' by the Free Software Foundation (FSF).  The license ensures such software is free and that all modified and extended versions of the program are free as well. Free as in 'freedom' not necessarily free of charge, as per the Free Software Definition maintained by FSF (see http://www.gnu.org/philosophy/free-sw.html)."

   
Cost
^^^^
**Monetary cost of acquiring the software.**

*e.g.* **Free of charge (with retritions)**

- apply the tag (see below) that is applicable

.. csv-table::
   :header: "Cost", "Description"
   :widths: 25, 100

   "Free of charge", "Software which available for use by all, with full functionality, at no monetary cost to the user."
   "Free of charge (with restrictions)", "Software which is available for use at no monetary cost to the user, but possibly with limited functionality, usage restrictions, or other limitations."
   "Commercial", "Software which you have to pay to access."
  
Accessibility
^^^^^^^^^^^^^
**Whether the software is freely available for use.**

*e.g.* **Open access**

- apply the tag (see below) that is applicable

.. csv-table::
   :header: "Accessibility", "Description"
   :widths: 25, 100

   "Open access", "An online service which is available for use to all, but possibly requiring user accounts / authentication."
   "Restricted access", "An online service which is available for use to a restricted audience, e.g. members of a specific institute."
   "Proprietary", "Software for which the software's publisher or another person retains intellectual property rights Å\ usually copyright of the source code, but sometimes patent rights."
   "Freeware", "Proprietary software that is available for use at no monetary cost. In other words, freeware may be used without payment but may usually not be modified, re-distributed or reverse-engineered without the author's permission."

Contact
-------
**Details of primary point(s) of contact, e.g. person, helpdesk or mailing list.**

- this is the first port-of-call when seeking help with the software
- 'Name' must be specified along with one or both of 'Email' and 'URL' (see below)
- in general, a URL is preferable to an email

Name
^^^^
**Name of the primary contact.**

*e.g.* **Henrik Nielsen**

- this is the name of the thing for which an email and/or URL is specified
- specify a name of a person, or something like "Mailing list", "Helpdesk" *etc.* as appropriate

Email
^^^^^
**Email address of the primary contact.**

*e.g.* **hnielsen@cbs.dtu.dk**

- only give an email if it already publicly advertised as a contact point for the software, *e.g.* on a webpage or in a publication

.. note:: A syntactically email address (*e.g.* hnielsen@cbs.dtu.dk) must be specified however this will be rendered in bio.tools UI in a spam-resilient form (*e.g. hnielsen at cbs.dtu.dk)
  
  
URL
^^^
**URL of the primary contact.**

*e.g.* ****

- the URL must resolve to a page of contact information

Telephone number
^^^^^^^^^^^^^^^^
**Telephone number of primary contact.**

*e.g.* **+49-89-636-48018**

- only give a telephone number if this is already publicly available

Links
-----

**Miscellaneous links for the software e.g. repository, issue tracker or mailing list.**


URL
^^^
**A link of some relevance to the software (URL).**

*e.g.* ****

Comment
^^^^^^^
**Comment about the link.**

*e.g.* ****

Link type
^^^^^^^^^
**The type of data, information or system that is obtained when the link is resolved.**

*e.g.* **Repository**

.. csv-table::
   :header: "Link type", "Description"
   :widths: 25, 100

   "Browser", "A website for browsing data."
   "Helpdesk", "Helpdesk providing support in using the software."
   "Issue tracker", "Tracker for software issues, bug reports, feature requests etc."
   "Mailing list", "Mailing list for the software announcements, discussions, support etc."
   "Mirror", "Mirror of an (identical) online service."
   "Registry", "Some registry, catalogue etc. other than bio.tools."
   "Repository", "Repository where source code, data and other files may be downloaded."
   "Social media", "A website used by the software community including social networking sites, discussion and support fora, WIKIs etc."
													


Download
--------
**A link to a download for the software, e.g. source code, virtual machine image or container.**

URL
^^^
**Link to download (or repo providing a download) for the software.**

*e.g.* ****

Comment
^^^^^^^
**Comment about the download**

*e.g.* ****

Download type
^^^^^^^^^^^^^
**Type of download that is linked to.**

*e.g.* ****

.. csv-table::
   :header: "Download type", "Description"
   :widths: 25, 100

   "API specification", "File providing an API specification for the software, e.g. Swagger/OpenAPI, WSDL or RAML file."
   "Biological data", "Biological data, or a web page on a database portal where such data may be downloaded. "
   "Binaries", "Binaries for the software."
   "Binary package", "Binary package for the software."
   "Command-line specification", "File providing a command line specification for the software."
   "Container file", "Container file including the software."
   "CWL file", "Common Workflow Language (CWL) file for the software."
   "Icon", "Icon of the software."
   "Ontology", "A file containing an ontology, controlled vocabulary, terminology etc."
   "Screenshot", "Screenshot of the software."
   "Source code", "Software source code."
   "Source package", "Source package (of various types) for the software."
   "Test data", "Data for testing the software is working correctly."
   "Test script", "Script used for testing testing whether the software is working correctly."
   "Tool wrapper (galaxy)", "Galaxy tool configuration file (wrapper) for the software."
   "Tool wrapper (taverna)", "Taverna configuration file for the software."
   "Tool wrapper (other)", "Workbench configuration file (other than taverna, galaxy or CWL wrapper) for the software."
   "VM image", "Virtual machine (VM) image for the software."

											
Documentation
-------------
**A link to documentation about the software e.g. manual, API specification or training material.**

URL
^^^
**Link to documentation on the web for the tool.**

*e.g.* ****

Comment
^^^^^^^
**Comment about the documentation.**

*e.g.* ****

Documentation type
^^^^^^^^^^^^^^^^^^
**Type of documentation that is linked to.**

*e.g.* ****

.. csv-table::
   :header: "Documentation type", "Description"
   :widths: 25, 100
		
   "API documentation", "Human-readable API documentation."
   "Citation instructions", "Information on how to correctly cite use of the software."
   "General", "General documentation."
   "Manual ", "Information on how to use the software."
   "Terms of use", "Rules that one must agree to abide by in order to use a service."
   "Training material", "Online training material such as text on a Web page, a presentation, video, tutorial etc."
   "Other", "Some other type of documentation not listed in biotoolsSchema."

		
Publications
------------
**Publications about the software**

PubMed Central ID
^^^^^^^^^^^^^^^^^
**PubMed Central Identifier (PMCID) of a publication about the software.**

*e.g.* ****

PubMed ID
^^^^^^^^^
**PubMed Identifier (PMID) of a publication about the software.**

*e.g.* ****

Digital Object ID
^^^^^^^^^^^^^^^^^
**Digital Object Identifier (DOI) of a publication about the software.**

*e.g.* ****

Publication type
^^^^^^^^^^^^^^^^
**Type of publication.**

*e.g.* ****

.. csv-table::
   :header: "Download type", "Description"
   :widths: 25, 100
	    
   "Primary", "The principal publication about the software itself; the article to cite when acknowledging use of the software."
   "Benchmark", "A publication which assessed the performance of the software."
   "Review", "A publication where the software was reviewed."
   "Other", "A publication about the software but not the primary publication or a benchmark study."

		
Credits
-------
**An individual or organisation that should be credited for the software.**

GRID ID
^^^^^^^
**Unique identifier (GRID ID) of an organisation that is credited.**

*e.g.* **grid.5170.3**

.. note:: Global Research Identifier Database (GRID) IDs provide a persistent reference to information on research organisations, see https://www.grid.ac/.

ORCID ID
^^^^^^^^
**Unique identifier (ORCID iD) of a person that is credited.**

*e.g.* **http://orcid.org/0000-0002-1825-0097**

.. note:: Open Researcher and Contributor IDs (ORCID IDs) provide a persistent reference to information on a researcher, see http://orcid.org/. 

Name
^^^^
**Name of the entity that is credited.**

*e.g.* ****

Email
^^^^^
**Email address of the entity that is credited.**

*e.g.* ****

URL
^^^
**URL for the entity that is credited, e.g. homepage of an institute.**

*e.g.* ****

Entity type
^^^^^^^^^^^
**Type of entity that is credited.**

*e.g.* ****

.. csv-table::
   :header: "Entity type", "Description"
   :widths: 25, 100

   "Person", "Credit of an individual."
   "Project", "Credit of a community software project not formally associated with any single institute."
   "Division", "Credit of or a formal part of an institutional organisation, e.g. a department, research group, team, etc"
   "Institute", "Credit of an organisation such as a university, hospital, research institute, service center, unit etc."
   "Consortium", "Credit of an association of two or more institutes or other legal entities which have joined forces for some common purpose.  Includes Research Infrastructures (RIs) such as ELIXIR, parts of an RI such as an ELIXIR node etc. "
   "Funding agency", "Credit of a legal entity providing funding for development of the software or provision of an online service."

	    
Role
^^^^
**Role performed by entity that is credited.**

*e.g.* **Developer**

.. csv-table::
   :header: "Role", "Description"
   :widths: 25, 100
	    
   "Developer", "Author of the original software source code."
   "Maintainer", "Maintainer of a mature software providing packaging, patching, distribution etc."
   "Provider", "Institutional provider of an online service."
   "Documentor", "Author of software documentation including making edits to a bio.tools entry."
   "Contributor", "Some other role in software production or service delivery including design, deployment, system administration, evaluation, testing, documentation, training, user support etc."
   "Support", "Provider of support in using the software."

- specify all the roles that are applicable

.. note:: The current version of biotoolsSchema and bio.tools only supports one "role" assignation per credit; this will be changed to support multiple asignations (see https://github.com/bio-tools/biotoolsSchema/issues/80)
Comment
^^^^^^^
**A comment about the credit.**

*e.g.* **Wrote the user manual.**

- use this to elaborate on the contribution of the credited entity.

.. attention:: **do not** merely duplicate information that is, or can, be provided via the ``role`` attribute, *i.e.* do not specify only "Developer", "Support" *etc.*

  
EDAM annotation guidelines
--------------------------

- if in any doubt as to meaning, refer to the concept definitions using:

  - `EBI OLS browser <http://www.ebi.ac.uk/ols/ontologies/edam>`_
  - `NCBO BioPortal browser <https://bioportal.bioontology.org/ontologies/EDAM>`_
  
- use the most specific concept(s) that apply
- in case more than sibling concept is applicable (*i.e.* concepts under a common parent) than consider using parent concept instead

.. attention:: in cases of multiple annotations per field, **do not** specify both a term and it's parent or other ancestor

Guidelines per tool type
------------------------

Command-line tool
^^^^^^^^^^^^^^^^^
**A tool with a text-based (command-line) interface.**

Database portal
^^^^^^^^^^^^^^^
**A Web application, suite or workbench providing a portal to a biological database.**

Desktop application
^^^^^^^^^^^^^^^^^^^
**A tool with a graphical user interface that runs on your desktop environment, e.g. on a PC or mobile device.**

Library
^^^^^^^
**A collection of components that are used to construct other tools. bio.tools scope includes component libraries performing high-level bioinformatics functions but excludes lower-level programming libraries.**

Ontology
^^^^^^^^
**A collection of information about concepts, including terms, synonyms, descriptions etc.**

Plug-in
^^^^^^^
**A software component encapsulating a set of related functions, which are not standalone, i.e. depend upon other software for its use, e.g. a Javascript widget, or a plug-in, extension add-on etc. that extends the function of some existing tool.**

Script
^^^^^^
**A tool written for some run-time environment (e.g. other applications or an OS shell) that automates the execution of tasks. Often a small program written in a general-purpose languages (e.g. Perl, Python) or some domain-specific languages (e.g. sed).**

SPARQL endpoint
^^^^^^^^^^^^^^^
**A service that provides queries over an RDF knowledge base via the SPARQL query language and protocol, and returns results via HTTP.**

Suite
^^^^^
**A collection of tools which are bundled together into a convenient toolkit. Such tools typically share related functionality, a common user interface and can exchange data conveniently. This includes collections of stand-alone command-line tools, or Web applications within a common portal.**

Web application
^^^^^^^^^^^^^^^
**A tool with a graphical user interface that runs in your Web browser.**

Web API
^^^^^^^
**An application programming interface (API) consisting of endpoints to a request-response message system accessible via HTTP. Includes everything from simple data-access URLs to RESTful APIs.**

Web service
^^^^^^^^^^^
**An API described in a machine readable form (typically WSDL) providing programmatic access via SOAP over HTTP.**

Workbench
^^^^^^^^^
**An application or suite with a graphical user interface, providing an integrated environment for data analysis which includes or may be extended with any number of functions or tools. Includes workflow systems, platforms, frameworks etc.**

Workflow
^^^^^^^^
**A set of tools which have been composed together into a pipeline of some sort. Such tools are (typically) standalone, but are composed for convenience, for instance for batch execution via some workflow engine or script.**

