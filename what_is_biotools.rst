What is bio.tools?
==================

`bio.tools <https://bio.tools>`_ is a portal to bioinformatics resources worldwide, aimed to help bioinformaticians and scientists:

* find, understand, compare and select resources == **discovery**
* use and connect them in workflows == **(inter)operability**

Our main objectives are:

* build and maintain a comprehensive registry of high-quality software metadata / descriptions 
* provide a web portal enabling registration, editing, search and discovery of the registry content
* support a community for the sustainable maintenance of the registry content and development of the portal features
* expose results of tool performance benchmarking, online service monitoring and other metrics of software and service quality
* integrate the registry with popular workbench environments in a way that improves resource interoperability
* support registry stakeholders including tool providers and end-users

bio.tools scope is *application software* with well-defined data processing functions (inputs, outputs and operations).  bio.tools includes a broad range of `software types <http://biotools.readthedocs.io/en/latest/curators_guide.html#tool-type-guidelines>`_ including tools available for immediate use as online services, or in a form which which you can download, install, configure and run yourself.  This includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions.

bio.tools development is supported by `ELIXIR <https://www.elixir-europe.org/>`_ - the European Research Infrastructure for life science information.



Technical components
--------------------
* `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ is a description model for bioinformatics software.  It is a formalised XML schema (XSD) which defines 50 important scientific, technical and administrative attributes.  It defines what attributes may be specified in a bio.tools entry, a precise syntax for those descriptions, and controlled vocabularies for consistent description of technical aspects such as software license and software type.
* `EDAM ontology <https://github.com/edamontology/edamontology>`_ is an ontology of well-established, familiar concepts that are prevalent within bioinformatics and computational biology, including types of data and data identifiers, data formats, operations and topics.  It defines precise semantics for the scientific description of software registered in bio.tools.

* `Curation Guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#>`_ describe how each attribute should be specified, *i.e.* concerning the quality of an entry. The guidelines go beyond the syntactic and semantic constraints defined by biotoolsSchema and EDAM, and are part of broader `tool information standards <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst>`_ being adopted by bio.tools.

* **Tool Cards** *e.g.* https://bio.tools/signalp provide key information at a glance for registered tools.  Tool cards have human-friendly, persistent URLs which include the unique tool identifier ("signalp" in this case).  The identifier is assigned upon registration is a URL-safe derivative of (normally identical to) the supplied tool name.

* **Query interfaces** help bio.tools end-users with tool discovery and include the search bar, a compact "mini-card" view and a detailed "grid" view available at https://bio.tools.  See the `Users Guide <http://biotools.readthedocs.io/en/latest/user_guide.html>`_.

* **Registration interface** enables manual creation of valid registry content and editing, including graphical editing via tabbed panes and an interactive JSON editor with inline error reporting.  It is available to logged-on users via "Menu ... Add content".  See the `Users Guide <http://biotools.readthedocs.io/en/latest/user_guide.html>`_.
  


