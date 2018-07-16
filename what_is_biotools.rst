What is bio.tools?
==================

`bio.tools <https://bio.tools>`_ is a portal to bioinformatics resources worldwide, aimed to help bioinformaticians and scientists:

* find, understand, compare and select resources == **discovery**
* use and connect them in workflows == **(inter)operability**

Our **vision** is to be the sustainable primary archive for basic tool metadata, providing a persistent reference to high-quality (curated and verified) "canonical" descriptions of unique tools, with information about their provision via online services and various downloadable artefacts, and including entries for different versions of a tool, where these have major functional differences.
  
Objectives
----------
Our main objectives are:

* build and maintain a comprehensive **registry** of high-quality software metadata / descriptions 
* provide a **web portal** enabling registration, editing, search and discovery of the registry content
* support a **community** for the sustainable maintenance of the registry content and development of the portal features
* expose results of tool performance **benchmarking**, online service **monitoring** and other metrics of software and service quality
* integrate the registry with popular **workbench environments** in a way that improves resource interoperability
* **support** registry stakeholders including tool providers and end-users

Scope
-----
bio.tools scope is *application software* with well-defined data processing functions (inputs, outputs and operations).  bio.tools includes a broad range of `software types <http://biotools.readthedocs.io/en/latest/curators_guide.html#tool-type-guidelines>`_ including tools available for immediate use as online services, or in a form which which you can download, install, configure and run yourself.  This includes simple tools with one or a few closely related functions, and complex, multimodal tools with many functions.  It also includes executable workflows, database portals and Web APIs.

Technical components
--------------------
* `biotoolsSchema <https://github.com/bio-tools/biotoolsschema>`_ is a description model for bioinformatics software.  It is a formalised XML schema (XSD) which defines 50 important scientific, technical and administrative attributes.  It defines what attributes may be specified in a bio.tools entry, a precise syntax for those descriptions, and controlled vocabularies for consistent description of technical aspects such as software license and software type.
* `EDAM ontology <https://github.com/edamontology/edamontology>`_ is an ontology of well-established, familiar concepts that are prevalent within bioinformatics and computational biology, including types of data and data identifiers, data formats, operations and topics.  It defines precise semantics for the scientific description of software registered in bio.tools.

* `Curation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#>`_ describe how each attribute should be specified, *i.e.* concern the quality of an entry. The guidelines go beyond the syntactic and semantic constraints defined by biotoolsSchema and EDAM, and are part of broader `tool information standards <https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst>`_ being adopted by bio.tools.

* **Tool Cards** *e.g.* https://bio.tools/signalp provide key information at a glance for registered tools.  Tool cards have human-friendly, persistent URLs which include the unique tool identifier ("signalp" in this case).  The identifier is assigned upon registration is a URL-safe derivative of (normally identical to) the supplied tool name.

* **Query interfaces** available at https://bio.tools help bio.tools end-users with tool discovery and include the search bar, a compact "mini-card" view and a detailed "grid" view.  See the `Users Guide <http://biotools.readthedocs.io/en/latest/user_guide.html>`_.

* **Registration interface** enables manual creation of valid registry content and editing, including graphical editing via tabbed panes and an interactive JSON editor with inline error reporting.  It is available to logged-on users via "Menu ... Add content".  See the `Users Guide <http://biotools.readthedocs.io/en/latest/user_guide.html>`_.

* `bio.tools API <http://biotools.readthedocs.io/en/latest/api_reference.html>`_ provides programmatic means to query, add and edit registry content.
  
* **bio.tools metrics** available at https://bio.tools/stats include registry growth, contributors, annotation breakdown *etc.*

bio.tools Tool Identifiers
--------------------------

Each bio.tools entry is assigned a unique identifier (**biotoolsID**): a manually verified, URL-safe version of (normally identical to) the supplied tool name.  The IDs are used in persistent URLs, resolving to Tool Cards of essential information.  The recommended short-form is a compact URI (CURIE), which is resolvable in `Identifiers.org <http://identifiers.org/>`_.

.. csv-table::
   :header: "", "Example"
   :widths: 25, 50
	    
   "biotoolsID", "signalp"
   "CURIE", "biotools:signalp"
   "Identifiers.org", "http://identifiers.org/biotools/signalp"
   "Tool Card URL", "https://bio.tools/signalp"

Registered software which, for one reason or another, is no longer operational, retain their ID and URL but are marked as obsolete.  Hence, descriptions of legacy resources are archived.  

  
Docs overview
-------------
* `Contributors Guide <http://biotools.readthedocs.io/en/latest/contributors_guide.html>`_ - how to get involved (please do!)
* `User Guide <http://biotools.readthedocs.io/en/latest/user_guide.html>`_ - how to use the bio.tools user interfaces.
* `Curators Guide <http://biotools.readthedocs.io/en/latest/curators_guide.html>`_ - how to create a high quality bio.tools entry.
* `Editors Guide <http://biotools.readthedocs.io/en/latest/editors_guide.html>`_ - thematic editorships to improve bio.tools in scientific areas.
* `Documentors Guide <http://biotools.readthedocs.io/en/latest/documentors_guide.html>`_ - how to edit the bio.tools docs.
* `API reference <http://biotools.readthedocs.io/en/latest/api_reference.html>`_ - bio.tools API docs.
* `Hangouts <http://biotools.readthedocs.io/en/latest/hangouts.html>`_  - monthly coordination meetings (you're welcome to join!)
* `Roadmap <http://biotools.readthedocs.io/en/latest/roadmap.html>`_  - technical plans for the next year
* `Studentships <http://biotools.readthedocs.io/en/latest/studentships.html>`_ - bio.tools studentship scheme for curation-focussed mini-projects.
* `GitHub projects <http://biotools.readthedocs.io/en/latest/studentships.html>`_ - open projects of relevance to bio.tools.

bio.tools development is supported by `ELIXIR <https://www.elixir-europe.org/>`_ - the European Research Infrastructure for life science information. bio.tools content is freely available to all under `open license <http://biotools.readthedocs.io/en/latest/license.html>`_.


Getting involved : a quick-start guide
--------------------------------------
1. Read the `docs <http://biotools.readthedocs.io/en/latest/>`_ but especially the `contributors guide <http://biotools.readthedocs.io/en/latest/contributors_guide.html>`_.
2. All project / high-level task management is done in `sifter <https://biotools.sifterapp.com/>`_, email `Jon Ison <mailto:jison@bioinformatics.dtu.dk>`_ if you want in!
3. Join the `mailing lists <http://biotools.readthedocs.io/en/latest/contributors_guide.html#mailing-list>`_ but note that most of the discussion is done via sifter.  Important announcements and some discussion are done via registry-core (see below)
4. Members of `registry-core <http://biotools.readthedocs.io/en/latest/governance.html#registry-core>`_ share a mailing list and calendar, but there are some implications of joining.  Email `Jon <mailto:jison@bioinformatics.dtu.dk>`_ if you want to join.
5. GitHub is used heavily for public / fine-grained issue tracking, code *etc.*, see the `bio.tools <https://github.com/bio-tools/>`_ and `EDAM <https://github.com/edamontology/>`_ organisations, in particuar the `biotoolsregistry <https://github.com/bio-tools/biotoolsregistry>`_ and `edamontology <https://github.com/edamontology/edamontology>`_ projects. Email `Jon <mailto:jison@bioinformatics.dtu.dk>`_ if you want to join.
6. We run monthly `hangouts <http://biotools.readthedocs.io/en/latest/hangouts.html>`_ (coordination meetings) and - for technical people routinely involved with bio.tools curation or software development - weekely technical calls.  To join the hangouts email `Henriette <hhu@bio.ku.dk>`_ cc `Jon <mailto:jison@bioinformatics.dtu.dk>`_ or to join the weekly calls email `Emil <ekry@dtu.dk>`_ cc `Jon <mailto:jison@bioinformatics.dtu.dk>`_.
7. Dive in at the deep end!  There are no end of projects and tasks to get involved with, see `sifter <https://biotools.sifterapp.com/>`_ and email `Jon <mailto:jison@bioinformatics.dtu.dk>`_ in the 1st instance to get orientated.
