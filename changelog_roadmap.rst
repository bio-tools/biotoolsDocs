Roadmap
=======
A summary of planned technical development of bio.tools software.  Developments are informed by the ELIXIR EXCELERATE application (granted in April 2015).  The roadmap is updated in light of community input (see `Contributors Guide <http://biotools.readthedocs.org/en/latest/hangouts.html>`_) and on-going developments.  As a rule we aim for quarterly registry feature releases with supporting EDAM releases.


2017 Q2
-------

- clean-up of `toold IDs <https://biotools.sifterapp.com/issues/401>`_ and consolidation of `duplicates <https://biotools.sifterapp.com/issues/297>`_

- indexing of whole site following clean-up of duplicates and tool IDs
      
- M1.7.1 `novel users interfacs <https://biotools.sifterapp.com/issues/255>`_

   - new `Tool Annotator <https://biotools.sifterapp.com/issues/211>`_ UI
   - proof-of-principle of `interactive diagrams <https://biotools.sifterapp.com/issues/65>`_ of published workflows / tool-specific diagrams (https://bio.tools/worklows)
   - scoping the `Icon / topic-based view <https://biotools.sifterapp.com/issues/172>`_ for browsing bio.tools

- M1.3 `Registry-literature integration <https://biotools.sifterapp.com/issues/253>`_ 

  - systematic annotation of tool publications, via  `studentship <https://biotools.sifterapp.com/issues/224>`_
  - expose #citations, altmetrics etc. with sorting
  - copy-pastable citation information etc.

- "drive-by curation" (suggestions from non-account holders)

- mass content imports

  - `Bioinformatics Links Directory - databases <https://biotools.sifterapp.com/issues/307>`_

- curation of select tool collections to “gold-standard” (Q2-Q3)

  - for tools from msutils.org via `studentship <https://biotools.sifterapp.com/issues/177>`_ 

- systematic identification of rightful entry owners (Q2-Q4)

  - mailshot / requesting adoption of entries
  - requesting new tools

- systematic improvement of entries following QC checks (Q2-Q4)

- **rolled over from 2017 Q1**

  - support for biotoolsSchema 2.0.0 XML format I/O
  - "disown" entry button (My Profile)
  - import of tools from `NAR Web servers <https://biotools.sifterapp.com/issues/245>`_
  - import of tools from `Bioinformatics Links Directory - software <https://biotools.sifterapp.com/issues/242>`_
  - drop mandatory requirement for email or URL in credits (non-breaking change in biotoolsSchema and UI for 2.1.0)


  
2017 Q3
-------
*"pivot to end-users" begins in earnest @ end 2017 Q3*

- systematic `annotation of tool publication IDs <https://biotools.sifterapp.com/issues/224>`_

- D1.2 Registry release (report)
    
- D1.5 Incorporate monitoring statistics & benchmarking results

  - connect to ELIXIR EXCELERATE WP2 metrics datastore, expose available data
  - proof of principle!

- D1.6 Workbench integration enabler: implement & evaluate

  - generate Galaxy tool wrapper & CWL file from registry entry
  - proof-of-principle!

- entry quality metrics

  - LinkedIn-style entry completion percentage

- M1.1.2 EDAM release & tooling (report)

- M1.4 Suppport “close to source” resource annotation 

  - biotoosSchema-compatible YAML format (tbd) for tool descriptions in GitHub 
  - periodic pull of YAML-format tool descriptions, hook (metadata file in repo changes, bio.tools updated), needs read-only bio.tools entries (also for e.g. EBI, SIB)
  - integration with BioShadock, BioContainers etc. (containers), IFB cloud (VMs, workflows)
  - tooling to support new entries, or annotations on existing entries (across the board)
  - needs some admin privilege for named fields

- extra enhancements to content reporting (tbd)
    
- mass content imports

  - `NAR databases edition <https://biotools.sifterapp.com/issues/246>`_
  - `DebianMed <https://biotools.sifterapp.com/issues/32>`_
  - others (tbd)
	  
    
2017 Q4
-------
- "tools similar to these" feature (using EDAM annotations)

- improved search and filtering

- planning of comprehensive coverage & systematic improvment in scientific areas

  - assignment of thematic editors responsible for overseeing content coverage & quality
  - thematic workshops (EDAM developments, tool lists, visual workflows)
  - refactoring existing content for consistency & other improvment
  - *provisional on additional funding*    

- evaluate user impact

  - assess tool discoverability (tool cards, tool homepage URLs) via Google
  - add BioSchema Tool Specification mark-up, assess impact on presentation of search results
  - provide metadata as service (tbd)  



Beyond 2017
-----------
- M1.1.3 EDAM release with coverage of different resource categories and RIs. Implementation of tooling for sustainable community development
- M1.5 Good Practice Guidelines
- M1.6 Implementation of resource metadata catalogue & evaluation of impact of Resource Synergy Meeting series
- M1.7.2 Implementation of novel highly usable interfaces from analysis of user experience and usability requirements
- D1.3 Registry release with comprehensive coverage of ELIXIR Node resources, including resource data format curation and analysis (Task 1)
- D1.7 Description of the registry user helpdesk & impact on user support via community forums (Task 4)
- D1.8 Matchmaking service: implementation & evaluation of impact
- M1.1.4 EDAM release with coverage of different resource categories and RIs. Implementation of tooling for sustainable community development
- D1.4 Registry release with comprehensive coverage of ELIXIR Node resources, including resource data format curation and analysis (Task 1)


NOTE
----

- Things mentioned previously that will **not** be done

  - "sandbox" area for intermediate registrations.  The information requirement is now lower for `beta entries <https://github.com/bio-tools/biotoolsSchema#information-requirements>`_ , "sandbox" (staging area) is not needed
  - "moderation interface" for mass content import.  Instead there will be enhanced QA/QC with features for improving entries (see below)
  - improved admin interface for content management.  Instead an admin will be able to edit any entry via the UI, also programmatically via Python notebooks (see below)
  

      
Changelog
=========

A summary of technical developments of bio.tools software to date.

April 2017
----------


March 2017
----------
- subdomains

  - pilot for de.NBI, others
  - subdomain management in My Profile

February 2017
-------------
- enhanced content ownership / sharing features

  - "request edit rights" button (Tool Card)
  - "request ownership" button (Tool Card, My Profile)

- improved search

  - support "Collection" and "Credit" in search bar, with drop-down of suggestions
  - tweak search behaviour to address most critical issues from https://biotools.sifterapp.com/issues/274


    
January 2017
------------
- Admin tooling

  - admin editing via UI
  - admin editing programmatically via Python notebooks
  
- improved QA/QC process (content monitoring & reporting)

  - comprehensive basic checks (see `technical proposal <https://docs.google.com/document/d/1ATj2zJOlbR3Edk6QyGvPX5HStZBknqfx1Fwqk4k0kqE/edit#heading=h.fffoc8urhpt8>`_)
  - labelling of entries with "has issues" **will not be done**  
  - reporting to admin page.  Reporting to Tool Cards & My Profile **will not be done**

- mass content imports  
  
  - `Tools used by EBI Training team <https://biotools.sifterapp.com/issues/70>`_
  - `Tools used by ELIXIR trainers <https://biotools.sifterapp.com/issues/60>`_
  - `BioConductor <https://biotools.sifterapp.com/issues/31>`_
  - `msutils.org <https://biotools.sifterapp.com/issues/28>`_
  - `SEQwiki <https://biotools.sifterapp.com/issues/27>`_
  - `Ontologies from OBO Foundry  <https://biotools.sifterapp.com/issues/300>`_
  - `Ontology metadata from OLS <https://biotools.sifterapp.com/issues/298>`_



December 2016
-------------
- stable data model, `biotoolSchema 2.0.0  <https://github.com/bio-tools/biotoolsSchema/tree/master/versions>`_ released

  - defines the stable bio.tools API
  - many major changes (new credit mechanism, cleaner aggregation of links, links (including for docs and downloads) can be typed etc.
  - breaking changes reserved to once/year from now on
  - incorporates very many community requests (tracked on https://github.com/bio-tools/biotoolsSchema/issues)
  - new `schema docs <https://biotoolsschema.readthedocs.io/en/latest/>`_

- support for candidate stable schema (Stage 1/3) in backend & user interfaces, revised documentation

- content migration to stable schema

  - created system for semi-automated migration of content (future proofing)
  - migrated existing content (Stage 1/3), see `Data model docs <https://docs.google.com/document/d/1tqw7FELV4F_qzrTA9KpVYoORAeFPyY1ZOjaGTPN2H1E/edit>`_

- labelling of all entries as "beta"

  - beta entries will require QC / user verification before being indexed

- Google indexing of bio.tools

  - new indexing system (keywords and metadata representation), no longer uses prerender, Google can now index single-page applications (Javascript)
  - main site is indexed, individual Tool Cards will be indexed as we migrate from "beta" entries

- new look Tool Cards

- bio.tools updated for EDAM_16

- support for EDAM synonyms for registration via API
  
November 2016
-------------

- revised https://bio.tools/stats pages with new graphs, cleaner look and feel etc.
- revised search mechanism, now performs exact and fuzzy searches
- revised Registration Interface, now provides inline error reporting
- feature to send verification (for account creation) and password reset emails
- features to share resources moved to "my profile" page
- scheduling system for housekeeping, e.g. gathering stats for https://bio.tools/stats
- misc. bug fixes  

October 2016
------------
- moved dev.bio.tools into production (consolidation of dev.bio.tools & bio.tools content) with QC check for redundant tool names 

- content ownership / sharing of edit rights (Google docs style)

  - ownership is not based on affiliation anymore, 1 owner / tool, edit rights can be shared with selected account holder, or with all account holders

- stable tool ID / URL scheme including tool version number

  - moved away from affiliation-name-version triplet for identifying entries, tools now identified by toolID, specific versions of a tool identified by versionID.  IDs have syntax constraints (defined in https://github.com/bio-tools/biotoolsSchema/).
  - IDs and therefore Tool Card URLs will be user-verifiable (implementation tbd)

- improved bio.tools auto-mailer (using admin email address)

- added historical stats to bio.tools/stats

  
July 2016
---------
- rewrite bio.tools software to pay off technical debt (completed)

June 2016
---------
- ~750 automated unit tests
- new and improved grid view
- "my profile" page, with account information and list of tools registered by this account
- Curation admin interface (content edition) (beta)
- General admin interface (account management, password change, reset etc) (beta)

May 2016
--------
- robust validation of incoming tool descriptions
- new URL / persistent ID scheme
- unit tests for EDAM topics, operations, data types and formats


April 2016
----------
- bio.tools/stats page
- improved load time
- added Elasticsearch support for improved search
- user authentication support for password change, reset, etc
- new improved and simplified search and filtering interface (neXtProt style)

March 2016
----------
- bio.tools documentation framework: https://biotools.readthedocs.org
- rewrite bio.tools software to pay off technical debt (on-going)

December 2015
-------------
- Created URL links to various registry related resources, such as bio.tools/events
- Displaying date added as 'time ago'
- Improvements to the pagination
- Added a nightly validator that ensures that the existing contents of the registry validate against the XSD schema
- EDAM release
- Continuous debugging and improvements

November 2015
-------------
- Created a mechanism for gathering stats of the current content of the registry
- API now returns date of last update
- Sorting entries by last added
- Improvements to the account creation
- Schema release
- Continuous debugging and improvements

October 2015
------------
- Rework of all interfaces to make website mobile friendly
- Improved error handling, messages and display when registering a resource
- Made JSON interactively editable in the Â¡Â®Resource registrationÂ¡Â¯ interface
- Continuous debugging and improvements

September 2015
--------------
- New domain bio.tools
- New advanced filtering widget and mechanism
- Improvements to the EDAM widget
- Tooltips redone
- Updated the contact tab in Â¡Â®Resource registrationÂ¡Â¯ to make it obvious that either email or URL is required instead of both
- Continuous debugging and improvements

August 2015
-----------
- Major release with focus on improved interface usability:
  - Removed splashscreen
  - Refactored menus
  - New browsing interface: added new Â¡Â®pillÂ¡Â¯ view, new sorting capabilities, storing search state in the URL etc.
  - New registration interface: new ontology browsing widget, restructured to improve look and feel
  - New editing interface (for existing resources)
  - Added Â¡Â®compact viewÂ¡Â¯ to query interface
  - Improved search bar with search suggestions
- Finalizing search API intended to prepare for growth in content and usage of the registry (scalability)
- New transferable search URL - same syntax for filtering both via GUI and API
- Continuous debugging and improvements

July 2015
--------- 
- Work on a search API intended to prepare for growth in content and usage of the registry (scalability)
- Implemented Resource Pages (mature)
  - New look: compactified, visualisation of functions and in/outputs
- Work on major enhancements to interface usability
- Continuous debugging and improvements

June 2015
---------
- biotoolsXSD-1.2 released
  - https://github.com/jongithub/biotoolsxsd/blob/master/CHANGELOG.md
- Registry software updated to accommodate the new release (ongoing)
- Continuous debugging

May 2015
--------
- Created new demo server
- Created replacement page for use upon releases
- Set up Google Indexing
- Enabled Google Analytics
- Implemented Resource Pages (beta)
- Made publication attribute mandatory
- Created biotoolsXSD project in Github
- biotoolsXSD-1.1 released
  - https://github.com/jongithub/biotoolsxsd/blob/master/CHANGELOG.md 
  - Updated schema docs for "Name" standards
  - Updated schema docs to include simple table of attributes (optional, recommended, mandatory) PLUS reference Google Doc with this info
- Continuous debugging

April 2015
----------
- Added ability to adjust column width 
- Added ability to sort columns
- Outlined technical implementation of Resource Pages
- Enforced "name" standards in registration interface
- Prepare for Google Indexing
- Added whole VM deployment and provisioning setup
- Various schema updates, e.g.
  - Improved dataType, dataFormat element docs
  - Extended URL with support for FTP 
  - Enforced Â¡Â®description' length limit
  - Enforced other 'description' fieldsÂ¡Â¯ length limits
  - Made publication ID mandatory
  - Updated sample JSON with "null" value of "uri"
- Continuous debugging

March 2015
----------
- Batch registration to support XML format, & support multi-resource JSON / XML upload
- Fixed the interface not to direct the user to the splash screen all the time
- Various schema updates, e.g.
  - Harmonize "Maturity" in software description schema
  - Updated comment in schema docs for "contact"
  - Removed URI from softwareType and resourceType
  - Updated schema for missing AppDB languages
  - Updated schema for missing AppDB licenses
- Continuous debugging

February 2015
-------------
- Released EDAM 1.9 with corresponding registry updates
- Splash page updated to accept full term before redirecting
- Various schema updates, e.g.
  - Added "virtual appliance" to enum for interfaceType
  - Removed URLs from simple enums in schema (old SWO terms)
  - Changed "Accessibility" element to support "private" tools 
  - Added "Dataset" to enum for resourceType
- Continuous debugging
