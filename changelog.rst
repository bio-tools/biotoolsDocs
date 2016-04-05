Changelog
=========

A summary of technical developments of bio.tools software to date.

December 2015
-------------
- Created URL links to various registry related resources, such as bio.tools/events
- Displaying date added as ¡®X time ago¡¯
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
