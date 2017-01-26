Status reports
==============

2017 January
------------

See the `changelog and roadmap <http://biotoolsschema.readthedocs.io/en/latest/>`_

  - ELIXIR Hackathon @ EuBIC Winter School, Jan 10 2017 (https://tinyurl.com/registryhackathon11)

  - ELIXIR bio.tools Curation Workshop: Genomics Tools and Databases in Agricultural Science Feb 2-3 2017 (https://tinyurl.com/registryhackathon12)

  - First draft of "registry pillar" of `ELIXIR Tools Platform roadmap <https://docs.google.com/document/d/1rWzWdxMJvSkDRWEfdyMSu8EMO0LfV_UXwsG86JZmIZ0/edit#heading=h.j77fai7pe4sc>`_  : *open for comments*


2016 December
-------------
Actions (November)
^^^^^^^^^^^^^^^^^^
  - Technical developments

     - stable schema `biotoolsSchema 2.0.0 <https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-2.0.0>`_ released.  It will define the scope and potential functionality of bio.tools for years to come.   Future versions will follow the MAJOR.MINOR.PATCH pattern (http://semver.org), with major changes that could break bio.tools API dependencies restricted to once/year.  
     - EDAM_1.16 released and available on `BioPortal <http://bioportal.bioontology.org/ontologies/EDAM?p=classes>`_ and `OLS <https://www.ebi.ac.uk/ols/ontologies/edam>`_.
       
  - Documentation
    
     - new schema docs on http://biotoolsschema.readthedocs.io/en/latest/
     - information requirement for "beta" and "standard" bio.tools entries `defined here <https://github.com/bio-tools/biotoolsSchema#information-requirements>`_.
    
     
Plans (December)
^^^^^^^^^^^^^^^^

  - Technical work towards the Dec release, see  `roadmap <http://biotools.readthedocs.io/en/latest/changelog_roadmap.html>`_ of registry software developments
  - Various content additions listed on `sifterapp <https://biotools.sifterapp.com/projects/39503/issues?srt=priority>`_  
  - WP 1 / ELIXIR-DK partners telcon 10AM UK, Fri Dec 2

2016 October
------------

Actions (October)
^^^^^^^^^^^^^^^^^
  - Technical developments

     - `dev.bio.tools <https://dev.bio.tools>`_ has been moved into production on https://bio.tools.  Including new content ownership model whereby edit rights on entries can be shared amongst bio.tools users.
     - candidate stable schema `biotoolsSchema 2.0-beta02 <https://github.com/bio-tools/biotoolsSchema/tree/master/biotools-2.0-beta-02>`_ released.
     - prototype EDAM extension for bioimaging analysis concepts released : `EDAM-Bioimaging_alpha01 <http://bioportal.bioontology.org/ontologies/EDAM-BIOIMAGING?p=classes>`_. 

  - Outreach actions

     - Bioschema specification for schema.org mark-up for tools on the Semantic Web, worked on during `NETTAB hackathon <http://tinyurl.com/registryhackathon10>`_.  Such mark-up will be added to bio.tools Tool Cards in due course.
     - revision / extension of `bio.tools documentation <biotools.readthedocs.io/en/latest/>`_
     - new `EDAM documentation <http://edamontologydocs.readthedocs.io/en/latest/>`_ and revamp of https://edamontology.org.
     - bio.tools `studenstship scheme <http://biotools.readthedocs.io/en/latest/studentships.html>`_ now available

  - Content

     - consolidation of content from dev.bio.tools and bio.tools : 2885 entries, 376 contributors (registered users)
     - top-down plan for content expansion now `available <https://docs.google.com/document/d/1AM0iLimpT4ClybEKYYdWu52RzJ9GKqUpW2DZflS6_4c/edit>`_ for comment.  See `sifterapp issue <https://biotools.sifterapp.com/issues/241>`_. 


Plans (November)
^^^^^^^^^^^^^^^^
  - Technical work towards the Dec release, see  `roadmap <http://biotools.readthedocs.io/en/latest/changelog_roadmap.html>`_ of registry software developments 
  - import of SEQwiki (see `sifterapp issue <https://biotools.sifterapp.com/issues/27>`_.)
  - EDAM 1.16 including requests via GitHub and addition of data format concepts


2016 September
--------------

Actions (September)
^^^^^^^^^^^^^^^^^^^
 
  - Major recent work highlights
     - finished rewrite of registry software (see https://dev.bio.tools) 
     - major revision of underlying data model (biotoolsXSD) producing candidate stable schema (https://github.com/bio-tools/biotoolsxsd/)
     - Deliverable D1.1 submitted on time
     - Presentation of work at ISMB, ECCB and DKBC
     - improved & extended `bio.tools docs <http://biotools.readthedocs.io/en/latest/>`_
     - detailed `roadmap <http://biotools.readthedocs.io/en/latest/changelog_roadmap.html>`_ for registry software developments 
     - paper submitted   "ReGaTE, Registration of Galaxy Tools in Elixir" Olivia Doppelt-Azeroual, Ph.D.; Fabien Mareuil, Ph.D.; Eric Deveaud; Matus Kalas, Ph.D.; Nicola Soranzo; Marius van den Beek, Ph.D.; Björn Grüning; Jon Ison; Hervé Ménager

Plans (October)
^^^^^^^^^^^^^^^

     - moving dev.bio.tools into production, see  `roadmap <http://biotools.readthedocs.io/en/latest/changelog_roadmap.html>`_ for registry software developments 
     - `top-down plan for content expansion <https://biotools.sifterapp.com/issues/241>`_


2016 June
---------- 

Actions (June)
^^^^^^^^^^^^^^^
  - Content
     - Mapping of OLS tags : EDAM (proposal), hopefully OLS will adopt EDAM.  See https://biotools.sifterapp.com/issues/186.

  - Outreach actions

    - ASMS/IMSC conference
      - Magnus Palmblad (LUMC, NL) et al - member of registry-core - submitted a poster on workflow composition using EDAM / bio.tools annotations.

    - ISMB
      - Prepare 5 posters (ELIXIR & ELIXIR-DK, ELIXIR EXCELERATE WP1, bio.tools, EDAM, biotoolsXSD, computerome)
      - Booth preparations (freebies, dressing etc.) & logistics

    - Meeting with representatives of `The Open Microscopy Environment <https://www.openmicroscopy.org/>`_ and `Euro-BioImaging <www.eurobioimaging.eu/>`_  (including Gloabl-BioImaging) scope technical for collaboration with bio.tools.  See https://biotools.sifterapp.com/issues/166.


  - Technical specification documents

    - "Tool types and relations" (1st draft) to inform biotoolsXSD 2.0 development and support re-use of tool descriptions, and reduce duplications and inconsistencies in bio.tools.

  - Technical developments

    -          ~750 automated unit tests
    -          new and improved grid view
    -          ‘my profile’ page, with account information and list of tools registered by this account
    -          admin / curation interface (work ongoing)

    - Continue bio.tools rewrite to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_, with a focus on user interfaces and unit tests
    - Curation admin interface (content edition) (beta)
    - General admin interface (account management, password change, reset etc)

- Tasks **not** completed

  - Prepare new slide deck for Tech Track including software demo

Plans (July)
^^^^^^^^^^^^^^^^

  - Technical developments
     - migrating and consolidating the content from the production database to the new system
     - testing improvements to the search (so that it returns more relevant results)
     - quality of life improvements to the registration interface (error handling)
     - work towards release new system for testing by registry-core 

  - Outreach actions
     - ISMB

  - Technical specification documents
     - Settle these in prep for EXCELERATE WP1 D1.1
       - API specs
       - Tool types and relations
       - Content ownership model
       - Improved tool annotator mock-up 



Notes
^^^^^^^^^^^

  The “Tools, Workflows and Workbenches” hackathon (Institut Pasteur, May 18-20) was co-organized by the French and Danish ELIXIR nodes.  The event brought together over 40 representatives from 21 academic institutions and companies, with projects including Galaxy, bio.tools, Common Workflow Language, biotoolsXSD, EDAM, Debian Med, BioShadock and more.  The delegates enjoyed a series of talks, lively discussions and breakout hacking sessions including bio.tools entry relationships, Galaxy to bio.tools publishing, CWL specification, workflow specification interoperability, and training workflows.  In addition to concrete outcomes including various technical documents, new CWL bindings and enabling support for EDAM annotations in Galaxy, the hackathon provided a boost to various ongoing collaborations between the projects and institutes.  We look forward to a re-run soon!




2016 May
---------- 

Actions (May)
^^^^^^^^^^^^^^^
- Outreach actions (see https://bio.tools/events)

  - At ISMB, ELIXIR-DK will have a booth a give a technology track presentation
  - The “Tools, Workflows and Workbenches” hackathon (Institut Pasteur, May 18-20) was attended by over 40 people.  See `tinyurl.com/registryhackathon8 <tinyurl.com/registryhackathon8>`_ and the summary (below).

- Development of the improved tool annotator is being led by Hans-Ioan Ienasescu, based on the `mockup <https://docs.google.com/document/d/1IJLMu_5WSJmFa6ePmL034ju7mPG8GBYMYxLixmiRDMI/edit#>`_

- Content

    - EDAM 1.15 is out
        It includes new community-requested concepts and terms, including for metagenomics and biodiversity, structural improvements and fixes (synonyms clean-ups etc.), format updates, and implification of some concepts.  See the `Change log <https://github.com/edamontology/edamontology/blob/master/changelog.md>`_. Browse EDAM on `BioPortal <http://bioportal.bioontology.org/ontologies/EDAM?p=classes>`_ and in the new `OLS <http://www.ebi.ac.uk/ols/ontologies/edam>`_.

- bio.tools rewrite to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_ . Features done but not yet in production:

  - **back-end** development

    - robust validation of incoming tool descriptions
    - new URL / persistent ID scheme
    - unit tests for EDAM topics, operations, data types and formats

  - **front-end** development

    - ongoing work on the admin / curator interface
    - ongoing work on the improved grid view


Plans (June)
^^^^^^^^^^^^^^^^

  - Outreach actions

    - ISMB
      - Prepare 5 posters (computerome, ELIXIR-DK, bio.tools, EDAM, biotoolsXSD)
      - Prepare new slide deck for Tech Track
      - Booth preparations (freebies, dressing etc.)
      - Plan logistics

    - Meeting with representatives of `The Open Microscopy Environment <https://www.openmicroscopy.org/>`_ and `Euro-BioImaging <www.eurobioimaging.eu/>`_ to scope out technical collaboration with bio.tools.


  - Technical specification documents

    - "Tool types and relations" (1st draft) to inform biotoolsXSD 2.0 development and support re-use of tool descriptions, and reduce duplications and inconsistencies in bio.tools.

  - Technical developments

    - Continue bio.tools rewrite to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_, with a focus on user interfaces and unit tests
    - Curation admin interface (content edition) (beta)
    - General admin interface (account management, password change, reset etc)

- Tasks **not** completed in May

  - General admin interface (account management, password change, reset etc) - postponed for now



2016 April
---------- 

Actions (April)
^^^^^^^^^^^^^^^
- Outreach actions (see https://bio.tools/events)

  - Metagenomics Thematic Hackathon (7-8)
  - Slovenian Tools Curation Hackathon (8)
  - Preparations for `ECCB 2016 <https://biotools.sifterapp.com/issues/154>`_:
 
    - ELIXIR-DK booth
    - ELIXIR Application Track submissions
 
      - bio.tools - status and plans
      - The EDAM Ontology of bioinformatics data and methods
      - Bioschemas: Structured Data for Life Science using Schema.org
      - Defining A Community-Based Open Source Policy for Research Software in Life Sciences


- Collaborations
 
  - **BioExcel:bio.tools** meeting: technical `groundwork and planning <https://biotools.sifterapp.com/issues/114>`_
  - **DK partner** meetings. Work ongoing on various fronts: 
  
    - `RNA analysis tool annotation <https://biotools.sifterapp.com/issues/62>`_
    - `msutils.org tools import <https://biotools.sifterapp.com/issues/28>`_
    - `Improved tool annotator <https://biotools.sifterapp.com/issues/46>`_
    - multiple opportunities concerning ELIXIR Training Platform were discussed (see sifterapp).

  - **CZ partner** discussions: they will assist with content consolidation of `EDAM Operation <https://biotools.sifterapp.com/issues/156>`_ and `EDAM Topics <https://biotools.sifterapp.com/issues/155>`_ in all bio.tools entries.

- Technical specification documents

  - `Settle bio.tools entry ID / URL format (API) <https://biotools.sifterapp.com/issues/36>`_ : a `first draft <https://docs.google.com/document/d/1vDxejS7MWluSm8EXK3y7jCd39trEmtMhq8cGNodYQeA/edit#>`_ is available
  - `Fully featured API (planning) <https://biotools.sifterapp.com/issues/112>`_ : a `first draft <https://docs.google.com/document/d/1vDxejS7MWluSm8EXK3y7jCd39trEmtMhq8cGNodYQeA/edit#>`_ is available

  - Mock-up of `Improved tool annotator <https://biotools.sifterapp.com/issues/46>`_ : a `first draft <https://docs.google.com/document/d/1IJLMu_5WSJmFa6ePmL034ju7mPG8GBYMYxLixmiRDMI/edit#>`_ is available.

- Created bio.tools `stats page <https://bio.tools/stats>`_ .

- bio.tools rewrite to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_ . Features done but not yet in production:

  - **back-end** development

    - improved load time 
    - added Elasticsearch support for improved search
    - user authentication support for password change, reset, etc

  - **front-end** development

    - support for the new fast backend, user authentication, validation endpoints
    - new improved and simplified search and filtering interface (UniProt), aligned with Elasticsearch

Plans (May)
^^^^^^^^^^^
  - Technical Hackathon 3 : Tools, Workflows and Workbenches (see `bio.tools/events <https://bio.tools/events>`_ )
  - Technical documents (consult and consolidate) 

    - mock-up of `Improved tool annotator <https://docs.google.com/document/d/1IJLMu_5WSJmFa6ePmL034ju7mPG8GBYMYxLixmiRDMI/edit#>`_ 
    - `bio.tools entry ID / URL format (API) <https://docs.google.com/document/d/1vDxejS7MWluSm8EXK3y7jCd39trEmtMhq8cGNodYQeA/edit#>`_
    - `Fully featured API <https://docs.google.com/document/d/1vDxejS7MWluSm8EXK3y7jCd39trEmtMhq8cGNodYQeA/edit#>`_ 
    - API documentation 

  - Technical developments

    - Continue bio.tools rewrite to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_, with a focus on more robust validation of content and supporting new URL sheme
    - Curation admin interface (content edition) (beta)
    - General admin interface (account management, password change, reset etc)

- Tasks **not** completed in April

    - Preparations for `ISMB 2016 <https://biotools.sifterapp.com/issues/160>`_
    - Release of EDAM 1.15 addressing multiple requests logged on `GitHub <https://github.com/edamontology/edamontology/issues>`_


2016 March
---------- 

Actions (March)
^^^^^^^^^^^^^^^
- Outreach events (see https://bio.tools/events)

  - ELIXIR All-hands (7-10) 
  - Norwegian Tools Hackathon (17-18)
  - French Tools Hackathon (24-25)
- Setup and configuration of project management software (sifterapp): https://biotools.sifterapp.com/
- Setup and configuration of software issue management software (JIRA)
- Setup bio.tools documentation framework: https://biotools.readthedocs.org
- Setup bio.tools basic content reporting: https://bio.tools/stats
- Rewrite bio.tools software to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_ (on-going)

Plans (April)
^^^^^^^^^^^^^
- Outreach & collaborations

  - Preparations for `ISMB 2016 <https://biotools.sifterapp.com/issues/160>`_ and `ECCB 2016 <https://biotools.sifterapp.com/issues/154>`_ 
  - `Activate ELIXIR-DK partners <https://biotools.sifterapp.com/issues/161>`_, esp. ensure everyone has ELIXIR-relevant tasks
- Technical specification documents:

  - `Settle bio.tools entry ID / URL format (API) <https://biotools.sifterapp.com/issues/36>`_
  - `Fully featured API (planning) <https://biotools.sifterapp.com/issues/112>`_
- Release of EDAM 1.15 addressing multiple requests logged on `GitHub <https://github.com/edamontology/edamontology/issues>`_
- Continue bio.tools rewrite to `pay off technical debt <https://biotools.sifterapp.com/issues/94>`_, with a focus on `improving load time <https://biotools.sifterapp.com/issues/53>`_ and more `robust validation <https://biotools.sifterapp.com/issues/117>`_ of incoming tool descriptions



