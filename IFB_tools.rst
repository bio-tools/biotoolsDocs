IFB tools
=========

.. warning::
   WORK IN PROGRESS - THESE GUIDELINES ARE CURRENTLY BEING WORKED ON / ARE IN A MESS. PLEASE COME BACK LATER.


These instructions will guide you through the steps to register your tools and databases in `bio.tools`_ and describe them to the standard required for inclusion in the next iteration of the `IFB Catalogue <https://www.france-bioinformatique.fr/en/ressources>`_ - the French national catalogue of bioinformatics resources.

There are various sources of information amd help:

* This document provides guidelines tailored to the IFB catalogue, highlighting key information and common pitfalls.
* The *bio.tools* `Curators Guide <https://biotools.readthedocs.io/en/latest/curators_guide.html>`_ provides in-depth curation guidelines. It's referred to a lot from here!
* The `biotoolsSchema documentation <https://biotoolsschema.readthedocs.io/en/latest/>`_ summarises the attributes, information model and controlled vocabularies, including the `EDAM ontology <https://edamontologydocs.readthedocs.io/en/latest/>`_, used to describe tools in *bio.tools*.

* To get help using *bio.tools*, or for general curation advice, please mail `registry-support <mailto:registry-support@elixir-dk.org>`_.  If you have questions specifically about the IFB catalogue curation process, you can mail `Jon Ison <mailto:jon.c.ison@gmail.com>`_ directly.
  
  
.. note::
    These instructions are tailored to the needs of IFB tool providers.  If you find a bug, or have any questions or suggestions about them, or any of the *bio.tools* documentation, please post them on `GitHub <https://github.com/bio-tools/biotoolsDocs/issues>`_.  

    
1. Get a bio.tools account
--------------------------

You'll need an account to create *bio.tools* entries or edit existing ones.  Creating an account is simple: just go to `bio.tools`_ and click on |Sign-up| at the top-right corner of the page.


.. |Sign-up| image:: _static/sign_up.png
   :width: 100px
   :height: 30px

You'll be asked for a username, email address and password.  Your account will be setup immediately.

.. note::
   *bio.tools* entries are owned by the individuals who created them. Owners may grant edit rights, or transfer ownership of their entries to other registered users. The rightful owner of a *bio.tools* entry is usually the person who developed the tool, or provides an online service, but it can be some other responsible person, *e.g.* a dedicated curator.



2. Claim your bio.tools entries
-------------------------------
As a software developer or service provider, you should own the *bio.tools* entries describing your tools, by claiming ownership of existing entries or creating new ones.    

You'll need to login first, by clicking on |Login| at the top-right corner of the page.

.. |Login| image:: _static/login.png
   :width: 100px
   :height: 30px

To see whether a tool is already registered, search for it by its name. Simply type the name in the search box. You may need to click on the *Name* facet to narrow-down the search:

.. image:: _static/find_tool.png


If you find yuur entry you can go ahead and update_ it.  If you can't find the entry, you'll need to create_ it. 

.. important::
   All tools that were submitted for consideration in the ELIXIR FR Service Delivery Plan should already be registered, but may have only very basic details. You will need to take ownerhsip and improve the entries.  Before starting work, please ensure you understand the `information requirement <https://biotools.readthedocs.io/en/latest/IFB_tools.html#understand-the-information-requirement>`_ and follow the guidelines_ below.


Existing entries
""""""""""""""""
.. _update:
To edit an existing entry, you need to click through to the Tool Card for the tool in question, *e.g.* https://bio.tools/signalp.  You'll see a one or two buttons at the bottom right of the Tool Card, depending on whether you're logged in, and own the entry or not. 

.. image:: _static/update.png
   :width: 200px
   :height: 35px

.. image:: _static/request_edit_rights.png
   :width: 200px
   :height: 35px

.. image:: _static/request_ownership.png
   :width: 200px
   :height: 35px	    	    
 

* Click on *Request ownership* if you want to claim ownership of the entry
* Click on *Request editing rights* if you want to get edit rights to the entry, but not own it 
* Click on *Update this record* (visible only if you own the entry or have editing rights) to edit the entry.

.. note::
   It can take a little while for other users to respond to requests for edit rights or ownership.  If these are not granted within a day or two, please mail `registry-support <mailto:registry-support@elixir-dk.org>`_.


New entries
"""""""""""
.. _create:
To create new entries you'll need to be logged onto *bio.tools*. Click on *Menu ... Add content*:


.. image:: _static/add.png


bio.tools registration interface
""""""""""""""""""""""""""""""""
* The *bio.tools* registration interface helps you to create valid tool descriptions. It's organised into different tabs ("Summary", "Function", "Labels" *etc.*):

.. image:: _static/registration_interface.png


It provides some hints, and ensures that the information you set is in the right format. At any moment, you can click on |save| to save your edits, and immediately publish the changes online.  All the information you specified will be checked to ensure it's in the right syntax. To (optionally) force a manual syntax check, click on |validate|.
	   

.. |asterix| image:: _static/red_asterix.png
   :width: 15px
   :height: 20px

.. |save| image:: _static/save.png
   :width: 100px
   :height: 30px

.. |validate| image:: _static/validate.png
   :width: 100px
   :height: 30px	    

   
.. Important::
   The attributes required by *bio.tools* (tool name, description and homepage URL) are marked with a red asterix |asterix| in the registration interface, and must be given before an entry can be saved.  Much more information is required for the IFB catalogue, but this is not enforced by *bio.tools* ! 

.. note::
   It's possibe to create tool descriptions in JSON format directly in a text editor, and either paste these into the registration interface ("JSON" tab) or use the *bio.tools* API.  For guidance on using the API, see the `API Reference <https://biotools.readthedocs.io/en/latest/api_reference.html>`_ and the `API Usage Guide <https://biotools.readthedocs.io/en/latest/api_usage_guide.html>`_. 

    


	   

3. Understand the information requirement
-----------------------------------------

bio.tools
"""""""""
*bio.tools* requires only the name, description and homepage URL for a tool registration, but supports a comprehensive set of attributes for rich tool descriptions.

.. note::
   The attributes supported by *bio.tools*, their structure and their syntax are defined in formalised XML schema called `biotoolsSchema <https://biotoolsschema.readthedocs.io/en/latest/>`_.  If you'd like to learn more or contribute to this project, please head over to `GitHub <https://github.com/bio-tools/biotoolsSchema>`_.

The IFB catalogue
"""""""""""""""""

The information requirement of the IFB catalogue is more demanding than *bio.tools*, and depends upon the type of tool (command-line tool, database *etc.*) that is being registered.  In the guidelines_ that follow, tool attribute are described as *Mandatory*, *Recommended* or *Optional* for a given type of tool: 

* **Mandatory** attributes **MUST** be specified.
* **Recommended** attributes **SHOULD** be specified, but are not strictly required.
* **Optional** attributes **CAN** be specified, to produce a rich tool description.


.. image:: _static/ifb_info_standard.png

All tools in the IFB catalogue must have at least a minimal description, *i.e.* all *mandatory* attributes are specified. Tool providers are encouraged to provide an enhanced description which also includes all of the *recommended* attributes.
   
.. note::
   The above diagram is intended to give a quick overview of the information requirement.  Only the main types of tool and most important attributes are shown.  The guidelines_ below cover everything in more detail, and go through the curation process in a step-by-step way.


4. Plan your curation work 
---------------------------   

bio.tools enries
################

.. important::
   Before you use *bio.tools* to create and edit tool descriptions, it's important to plan carefully the entries with respect to the types of tool and the functions they perform. Be sure to understand:
   1. The type of tool being described - this determines the information requirement - and is covered in the section below on `tool type <#tool_type>`_. 
   2. The tool functionality and how it should be described  - covered in the section on `tool functions <#function>`_ below.
   3. Whether one or more entries are needed (covered below).

Tips when planning what new entries (if any) are required to adequately describe your tools:

* A discrete tool - one which is clearly an individual distinct entity - should have it's own entry. This is the case for most *command-line tools* and *desktop applications*.
* *bio.tools* aims to catalogue *unique* tool functionality. Different implementations but with esesentially the same functionality can be described by a sigle entity, *e.g.* a command-line tool that is later adapted into an R package for the Bioconductor suite, or which is served online via a Galaxy server.
* In some cases, *e.g.* complex software packages, it's not obvious whether to have one or multiple entries. Pick the option which mostly clearly illustrates the tool's functionality to end-users.
* Tool collections should be described by multiple entries. For example, an entry to describe a *suite*, and multple other entries to describe the individual tools within that suite. 
* Software with multiple interfaces should be described by a single entry. For example, a *command-line tool* whose functionality is also available via a *web application*, or a *database portal* with a *web API*.
* Many *database portals* provide multiple interfaces for the typical database functions (browse, deposit, search, visualise, analyse and download).  Usually one entry will suffice, but sometimes multiple entries are better, *e.g.* where there are multiple analysis tools.
* For very complex entities such as *Bioinformatics portals*, do not try to describe everything in a single entry.  Use a single entry for the portal, and multiple other entries for the things aggregated by the portal.

  

Familiarise yourself with EDAM
##############################

Terms are taken from and defined in the `EDAM ontology <https://github.com/edamontology/edamontology>`_:  
.. tip::
   The EDAM term picker currently implemented in *bio.tools* is not very powerful, for example, while it will find common synonyms on selectable terms, it does not display these to the user.  It's strongly recommended, especially if you can't find exactly the terms you need, to use other EDAM browsers (described below).



5. Describe your tools
----------------------
.. _guidelines:
The sections below match the tabs in the *bio.tools* registration interface.  

.. tip::
   The {`learn more <https://biotools.readthedocs.io/en/latest/curators_guide.html>`_} links take you to more detailed guidelines in the *bio.tools* Curators Guide. Follow these links whenever you're not sure about what information is needed.



   
Summary
"""""""
In the *Summary* tab you specify basic information about the software:

.. csv-table::
   :header: "Attribute", "Requirement"
   :widths: 25, 100
      
   "**Name**", "**Mandatory**"
   "**Description**", "**Mandatory**"
   "**Homepage URL**", "**Mandatory**"
   "Software version(s)", "*ignore*"

* **Name** is the short-form name by which the tool is commonly known, *e.g.* "BLAST" **not** "Basic Local Alignment Search Tool".  Database names should follow a pattern where the name and abbreviation are given *e.g.* "The Protein Databank (PDB)" {`learn more <https://biotools.readthedocs.io/en/latest/curators_guide.html#name-tool>`_}.
* **Description** is a *concise* summary of the *tool function or purpose*.  It can usually be copy-pasted from the tool homepage.  Do not include statements about performance, provenance, governance *etc.* {`learn more <https://biotools.readthedocs.io/en/latest/curators_guide.html#description>`_}.
* **Homepage URL** is the tool's homepage, or some URL that best serves this purpose {`learn more <https://biotools.readthedocs.io/en/latest/curators_guide.html#homepage>`_}.
   
.. Important::
   A `unique identifier <https://biotools.readthedocs.io/en/latest/curators_guide.html#id105>`_ - the *bio.tools* toolID - is created for a tool when a new entry is created. The ID value is a URL-safe version of the supplied tool name. The ID provides a persistent reference to the tool, used by bio.tools and other systems. The ID should therefore be sensible and intuitive.  In the case of databases, or tools with long names, the abbreviation should be used. For example, the `GnpIS tool <https://bio.tools/gnpis>`_ tool has the ID "gnpis" and *not* "Genetic and Genomic Information System". 


.. Tip::   
   The *bio.tools* toolID is **not** currently editable, so if you want the ID to differ from the name (*e.g.* an ID of "PDB" for the tool name "Protein databank (PDB)", you have to apply a workaround:
   
   1) create the entry giving a value for "Name" which is the desired ID value, *e.g.* "PDB"
   2) Save the entry.
   3) Edit the entry, resetting the name, *e.g.* to "Protein Databank (PDB)"

   To request an ID change post-registration (to be avoided!) you have to mail `Registry Support <mailto:registry-support@elixir-dk.org>`_.


Labels
""""""
In the *Labels* tab you specify miscellaneous scientific, technical and administrative details of the tool, expressed in terms from controlled vocabularies:

.. csv-table::
   :header: "Attribute", "Requirement"
   :widths: 25, 100
	    
   "**Tool type**", "**Mandatory**"
   "**Topic**", "**Mandatory**"
   "**Operating system**", "**Mandatory** (Desktop application), Recommended (Command-line tool)"
   "**Language**", "**Recommended** (Command-line tool)"
   "**Maturity**", "**Recommended**"
   "**License**", "**Mandatory** (Desktop application), Recommended (Command-line tool)"
   "**Cost**", "**Recommended** (Desktop application, Command-line tool)"
   "Collection", "*ignore*"
   "**Accessibility**", "**Mandatory** (Bioinformatics portal, Database portal, Web application)"
   "ELIXIRPlatform", "*ignore*"
   "ELIXIRNode", "*ignore*"
   "Other ID", "*ignore*"

* **Tool type** describes the type of the tool: a *bio.tools* entry can have more than one type.  {`learn more <http://biotools.readthedocs.io/en/latest/curators_guide.html#tool-type>`_}.
* **Topic** is the general scientific domain the tool serves, or other general category {`learn more <https://biotools.readthedocs.io/en/latest/curators_guide.html#topic>`_}.
* **Operating system** is the operating system supported by a downloadable software package {`learn more <http://biotools.readthedocs.io/en/latest/curators_guide.html#operating-system>`_}.
* **Language** is the name of a programming language the tool source code was written in. {`learn more <http://biotools.readthedocs.io/en/latest/curators_guide.html#programming-language/>`_}.
* **License** is a software or data usage license {`learn more <http://biotoolsschema.readthedocs.io/en/latest/controlled_vocabularies.html#license>`_}.
* **Maturity** is how mature the software product is {`learn more <http://biotoolsschema.readthedocs.io/en/latest/controlled_vocabularies.html#maturity>`_}.
* **Cost** is the monetary cost of acquiring the software {`learn more <http://biotoolsschema.readthedocs.io/en/latest/controlled_vocabularies.html#cost>`_}.
* **Accessibility** is whether the software is freely available for use {`learn more <http://biotools.readthedocs.io/en/latest/curators_guide.html#accessibility>`_}.

.. tip:: 
   You can use **Collection** to assign tools which are somehow related to one or more groups. These collections can have any names you like. Other ways to group tools are by creating a *bio.tools* subdomain (from *Menu...Manage subdomains*) and by defining `relations <https://biotools.readthedocs.io/en/latest/curators_guide.html#relation-group>`_ between tools.

.. note::
  **ELIXIRNode** and **ELIXIRPlatform** define the name of an ELIXIR node or ELIXIR platform, respectively, that is credited for the tool. These are not normally be set by *bio.tools* users (see `docs <http://biotools.readthedocs.io/en/latest/curators_guide.html#elixir-node>`_).
  All tools in the IFB catalogue will have the ELIXIRNode credit set to "France" by *bio.tools* admin in due course. 


Tool type
^^^^^^^^^
The scope of *bio.tools* is very broad, ranging from simple scripts to comprehensive bioinformatics portals, defined by 15 different `tool types <https://biotoolsschema.readthedocs.io/en/latest/controlled_vocabularies.html#tool-type>`_.  The vast majority of entries are of the following types:

.. csv-table::
   :header: "Type", "Description"
   :widths: 25, 100

   "**Bioinformatics portal**", "A web site providing a platform/portal to multiple resources used for research in a focused area, including biological databases, web applications, training resources and so on."
   "**Database portal**", "A Web site providing a portal to a biological database, typically allowing a user to browse, deposit, search, visualise, analyse or download data."
   "**Web application**", "A tool with a graphical user interface that runs in your Web browser."
   "**Desktop application**", "A tool with a graphical user interface that runs on your desktop environment, *e.g.* on a PC or mobile device."
   "**Command-line tool**", "A tool with a text-based (command-line) interface."

Other common types incude:

.. csv-table::
   :header: "Type", "Description"
   :widths: 25, 100
	    
   "**Web API**", "An application programming interface (API) consisting of endpoints to a request-response message system accessible via HTTP.  Includes everything from simple data-access URLs to RESTful APIs."
   "**Workflow**", "A set of tools which have been composed together into a pipeline of some sort.  Such tools are (typically) standalone, but are composed for convenience, for instance for batch execution via some workflow engine or script."
    "**Suite**", "A collection of tools which are bundled together into a convenient toolkit.  Such tools typically share related functionality, a common user interface and can exchange data conveniently.  This includes collections of stand-alone command-line tools, or Web applications within a common portal."
   "**Workbench**", "An application or suite with a graphical user interface, providing an integrated environment for data analysis which includes or may be extended with any number of functions or tools.  Includes workflow systems, platforms, frameworks etc."
    "**Workflow**", "A set of tools which have been composed together into a pipeline of some sort.  Such tools are (typically) standalone, but are composed for convenience, for instance for batch execution via some workflow engine or script."
   "**Library**", "A collection of components that are used to construct other tools.  bio.tools scope includes component libraries performing high-level bioinformatics functions but excludes lower-level programming libraries."

A single *bio.tools* entry is annotated with one or more types, reflecting different facets of the tool described by the entry. Be sure to understand the type(s) of tool you have, because it determines the information that's expected.  A few suggestions:

* Only use *Bioinformatics portal* for sites that cover multiple other resources, each which have their own distinct entity (and should have their own *bio.tools* entries).  Good examples include `IMGT <http://www.imgt.org/>`_ and `wheatIS <http://www.wheatis.org/index.php>`_.  *Bioinformatics portals* provide an unmbrella to other tools and databases, but don't (typically) directly serve them.
* *Suite* might be more applicable than *Bioinformatics portal*.  Example include Web application suites such as `CRISRP-Cas++ <https://crisprcas.i2bc.paris-saclay.fr/>`_ and `EvryRNA <https://evryrna.ibisc.univ-evry.fr/evryrna/evryrna/evryrna_home>`_, and suites of command-line tools such as `BioConductor <http://www.bioconductor.org/>`_.
*  *Workbench* might be also be more applicable than *Bioinformatics portal*.  This includes online and desktop integrated environements. Example include the general-purpose `Galaxy <https://usegalaxy.org/>`_ workbench and domain-specific ones such as `MetExplore <http://www.metexplore.fr/>`_ and `MicroScope <https://www.genoscope.cns.fr/agc/microscope/home/index.php>`_.
* Typically use only one of *Bioinformatics portal*, *Database portal* or *Web application* in a single entry.  If the resource is providing a database, then just go with *Database portal*, a good example being `Norine <https://bioinfo.lifl.fr/norine/>`_.
* In general, often a singe tool type will do. For example, `LoRDEC <http://atgc.lirmm.fr/lordec/>`_ (a *Command-line tool*), `GINsim <http://ginsim.org/>`_ (a *Desktop application*), and `Ocean Gene Atlas <http://tara-oceans.mio.osupytheas.fr/ocean-gene-atlas/>`_ or `Genomicus <http://www.genomicus.biologie.ens.fr/genomicus-97.01/cgi-bin/search.pl>`_ (both are *Web application*).  
* But do pick all the types that apply.  For example the `BOOSTER <https://booster.pasteur.fr/>`_ *Command-line tool* is also available as a *Web application* (and if these implementations have essentially the same functionality, they'd be described in a single *bio.tools* entry).
* If a database has an API (most do!) then use both *Database portal* and *Web API*, for example `aNISEED <https://www.aniseed.cnrs.fr/>`_.
* Use the more specialised tool types where they are applicable, for example *Workflow* for `Workflow4Metabolomics <https://workflow4metabolomics.org/>`_ and *Library* for any R pacages.


.. tip::
   Software is complex and it can be tricky to assign a type.  Make sure you understand the `tool type definitions <https://biotoolsschema.readthedocs.io/en/latest/controlled_vocabularies.html#tool-type>`_ before you use them. For example, in *bio.tools* a *Web service* is specifically a SOAP+WSDL implementation. Mmost likely you need *Web API* (which covers most APIs nowadays) or just *Web application* (for a tool delivered via the Web but without an API).  
  

   
License
^^^^^^^
All downloadable software should be licensed.  If you can't find your license in the list:

.  use "Proprietary" in cases where the software is under some license whereby it can be obtained from the provider (e.g. for money), and then owned, i.e. definitely not an open-source or free software license!
4. use "Other" if the software is available under a license not listed by biotoolsSchema and which is not "Proprietary" - please `request <https://github.com/bio-tools/biotoolsschema/issues>`_ the license is added.
3. use "Unlicensed" for software which is not licensed and is not "Proprietary" (this is bad - license your software!)

.. note::
   There are many good reasons why you should license your software, ideally picking a FOSS-license (Free and Open Source Software).  Read ` <A Quick Guide to Software Licensing for the Scientist-Programmer <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002598>`_.  Some types of tools *e.g.* *Web application" are not licensed, but instead, should have a `Terms of use <>`_ document. 


Topic
^^^^^
**Topic** is the place to tag your tool with terms describing the scientific domain the tool serves, or other general category.  

* specify the most important and relevant scientific topic; up to 3 topics will suffice
* don't exhaustively specify all the topics of lower or secondary relevance

   
 
Function
""""""""
In the *bio.tools* software model, a tool has one or more basic functions, or modes of operation.  Each function performs at least one specific operation, and has one or more primary inputs and outputs, each of a defined type of data and listing supported format(s).

This is visualised in a diagram on the Tool Cards that look like this:

|biotool_function|

.. |biotool_function| image:: _static/biotool_function.png

For example, the tool `signalp <https://bio.tools/signalp>`_ has a single function performing two operations, with a single input and two outputs:

.. image:: _static/signalp_function.png

Whereas the tool `HMMER3 <https://bio.tools/hmmer3>`_ has multiple functions (only 3 shown here):

.. image:: _static/hmmer3_function.png


.. note:: The `HMMER3 <https://bio.tools/hmmer3>`_ entry has very nicely annotated functionality, but is a good example of where the entry would be easier for users to understand if the functionality was described in separate entries - retaining the existing entry for the suite, but creating a new entry for each of the HMMER programs (alimask, hmmalign, hmmbuid *etc.*).
  
	   
Before describing your tools, you should carefully identify the distinct functions and the individual operations associated with each one. This is often straighforward, as different functions (modes) typically perform distinct operations:

* if a tool has an option between doing one thing or another, then you should annotate the operations as distinct functions
* if in contrast a tool always does one or more things, then you should annotate these as distinct operations within a single function
* only specify the primary functions and operations, from a typical end-user perspective - tools often do many things to its central, advertised purpose - you don't need to describe everything!
* this holds for input and output too, *e.g.* a sequence alignment tool would be annotated as reading sequences (input), and writing a sequence alignment (output), but not with gap insertion and extension penalties, or other parameters.

.. tip::
   When deciding how to describe your tools, in terms of *bio.tools* entries, their functions and operations, always keep the end-user in mind and try to describe your tools in a way that will be clear to them. If you're not sure, mail `registry-support <mailto:registry-support@elixir-dk.org>`_ for help.
   

This is where you describe the functionality of the tool based on the `EDAM ontology`_ [1]_.


In each box, you can add as many fields as you want. You can also add a general comment about the function (*this is particularly useful when your entry has several functions*).  It's highly recommended to read up about `tool functions <https://biotools.readthedocs.io/en/latest/curators_guide.html#toolfunctions>`_ before filling this section.

.. Note::
   It can be difficult to find the right terms to describe a tools operation(s), input(s) or output(s).  You can use `OLS EDAM`_, `BioPortal`_ and `EDAM Browser`_ to browse EDAM and find the terms you need, or request new terms via `GitHub <https://github.com/edamontology/edamontology/issues>`_.  Improvements (including term requests) to the term picker in *bio.tools* are planned.
    
.. _`EDAM ontology`: http://github.com/edamontology/edamontology/
.. _`OLS EDAM`: https://www.ebi.ac.uk/ols/ontologies/edam
.. _`BioPortal`: https://bioportal.bioontology.org/ontologies/EDAM/?p=classes&conceptid=root
.. _`EDAM Browser`: https://ifb-elixirfr.github.io/edam-browser/



Links
"""""
It is the place where your add links that do not belong to Download or Documentation.  For instance, a link to a mailing list, mirror or repository (full list available on the drop-down menu of **Link type**).

Download
""""""""
You can here share all the different download links you want. It can be many different kind such as binaries, source code, biological data, test data *etc.* (see the **Download type** drop-down menu).

Documentation
"""""""""""""
Make your different documentations for your tool available here. Again, you can assign type of documentation using **Documentation type**.

Publications
""""""""""""
Share the different publications of the tool, which can be the primary publication (the one to cite when the tool is used), but also
reviews or secondary references (see **Publication type**). You can use either the **PubMed Central ID** (PMCID), the **PubMed ID** (PMID) or the **Digital Object ID** (DOI) - DOI is preferred.

.. _credits:

Credits & Support
"""""""""""""""""
Credits include all type of entities that contributed to the development, maintenance or provision of the resource. Credits can have an **Entity type** (Person, Institute *etc.*) and an **Entity role** (Developer, Documentor *etc.*).  Use the role of *Primary contact* to indicate preferred contact details.

.. _json:

Relations
"""""""""

JSON
""""
This is all the information you gave about your tool, formatted in JSON format.

Permissions
"""""""""""
You can decide to make the entry either editable only by yourself, a list of users or anyone.


6. Maintaining your entries
---------------------------

Remove a resource
"""""""""""""""""
From the tool card, click on update this record. Then you can remove the entry by clicking on the remove button |remove|.

.. |remove| image:: _static/remove.png
   :width: 55px
   :height: 30px

.. warning::
    Removing an entry is definitive.  There's no way back (other than emailing `Registry Support <mailto:registry-support@elixir-dk.org>`_).





