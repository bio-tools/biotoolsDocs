Roadmap
=======
A summary of planned technical development of bio.tools software.  Developments are informed by the ELIXIR EXCELERATE application (granted in April 2015).  The roadmap is updated in light of community input (see `Contributors Guide <http://biotools.readthedocs.org/en/latest/hangouts.html>`_) and on-going developments.  As a rule we aim for quarterly registry feature releases with supporting EDAM releases.

October 2016
------------
- moving dev.bio.tools into production (consolidation of dev.bio.tools & bio.tools content)
- QC checks 

  - auto-checks for redundancy in content (tool name, homepage URL)
  - link checking

- stable tool ID / URL scheme including tool version number
- content ownership / sharing of edit rights (Google docs style)
- improved bio.tools auto-mailer (using admin email address)
- release of bio.tools source code under open license

December 2016
-------------
- support for candidate stable schema (Stage 1 / 3) in backend & user interfaces, with support for XML & documentation
- content migration to stable schema
- graphs of content growth
- Google indexing of bio.tools
- enhanced content reporting
- subdomains

2017 Q1
-------
- "sandbox" area for intermediate registrations
- “moderation interface” for mass content import
- improved QA/QC process

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
- Made JSON interactively editable in the ¡®Resource registration¡¯ interface
- Continuous debugging and improvements

September 2015
--------------
- New domain bio.tools
- New advanced filtering widget and mechanism
- Improvements to the EDAM widget
- Tooltips redone
- Updated the contact tab in ¡®Resource registration¡¯ to make it obvious that either email or URL is required instead of both
- Continuous debugging and improvements

August 2015
-----------
- Major release with focus on improved interface usability:
  - Removed splashscreen
  - Refactored menus
  - New browsing interface: added new ¡®pill¡¯ view, new sorting capabilities, storing search state in the URL etc.
  - New registration interface: new ontology browsing widget, restructured to improve look and feel
  - New editing interface (for existing resources)
  - Added ¡®compact view¡¯ to query interface
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
  - Enforced ¡®description' length limit
  - Enforced other 'description' fields¡¯ length limits
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
