Roadmap
=======
A summary of planned technical development of bio.tools software.  Developments are informed by the ELIXIR EXCELERATE application (granted in April 2015).  The roadmap is updated in light of community input (see `Contributors Guide <http://biotools.readthedocs.org/en/latest/hangouts.html>`_) and on-going developments.  As a rule we aim for quarterly registry feature releases with supporting EDAM releases.

- QC checks and reporting, built into my profile page
- enhanced content ownership / sharing features
- support for biotoolsSchema 2.0.0 XML format I/O
- extra enhancements to content reporting 
- subdomains
- labelling of entries following QC - beta, standard
- drive-by curation
- request edit rights
- request ownership
- similar tool suggestions
- ELIXIR EXCELERATE deliverables

  - D1.2 Registry release with comprehensive coverage of ELIXIR Node resources, including resource data format curation and analysis
  - D1.5 Incorporation of monitoring statistics and benchmarking results in registry releases
  - D1.6 Workbench integration enabler: implementation & evaluation of impact
  - M1.1.2 EDAM release with coverage of different resource categories and RIs. [2] Implementation of tooling for sustainable community development
  - M1.2 Implementation & evaluation of impact of Resource Pages on resource discoverability
  - M1.3 Implementation of registry-literature integration
  - M1.4 Implementation of support for “close to source” resource annotation in key documentation generators, and software development frameworks
  - M1.7.1 Implementation of novel highly usable interfaces from analysis of user experience and usability requirements
    
- finalised mass content imports
  
  - Tools used by EBI Training team (https://biotools.sifterapp.com/issues/70)
  - Tools used by ELIXIR trainers (https://biotools.sifterapp.com/issues/60)
  - BioConductor (https://biotools.sifterapp.com/issues/31)
  - msutils.org (https://biotools.sifterapp.com/issues/28) 
  - SEQwiki (https://biotools.sifterapp.com/issues/27) 
  - Ontologies from OBO Foundry  (https://biotools.sifterapp.com/issues/300)
  - Ontology metadata from OLS (https://biotools.sifterapp.com/issues/298)
  - Clean-up default EDAM Topic & Operation annotations (https://biotools.sifterapp.com/issues/156) 
  - GO tools (https://biotools.sifterapp.com/issues/58) 
    
2017 Q1
-------
- "sandbox" area for intermediate registrations
- "moderation interface" for mass content import
- improved QA/QC process
- improved admin interface for content management

2017 Q2
-------
- automated support for new EDAM releases
- improved content monitoring and reporting

2017 Q3
-------
- improved search and filtering

2017 Q4
-------


Changelog
=========

A summary of technical developments of bio.tools software to date.

December 2016
-------------
- stable data model, biotoolSchema 2.0.0 released (https://github.com/bio-tools/biotoolsSchema/tree/master/versions)

  - defines the stable bio.tools API
  - many major changes (new credit mechanism, cleaner aggregation of links, links (including for docs and downloads) can be typed etc.
  - breaking changes reserved to once/year from now on
  - incorporates very many community requests (tracked on https://github.com/bio-tools/biotoolsSchema/issues)
  - new schema docs (https://biotoolsschema.readthedocs.io/en/latest/)

- support for candidate stable schema (Stage 1/3) in backend & user interfaces, revised documentation

- content migration to stable schema

  - created system for semi-automated migration of content (future proofing)
  - migrated existing content (Stage 1/3), see https://docs.google.com/document/d/1tqw7FELV4F_qzrTA9KpVYoORAeFPyY1ZOjaGTPN2H1E/edit)

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
