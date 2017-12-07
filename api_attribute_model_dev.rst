*****************************
Attribute model - development
*****************************
.. note:: This is the API documentation for upcoming features, already available on the dev server at https://dev.bio.tools.

This page documents the structure of a JSON object that describes a bio.tools tool.


Submission JSON
===============

To submit a tool via our bio.tools API you’ll need to POST a JSON / XML / YAML document to the ``tool`` endpoint. 

A sample JSON document may look like this:

.. code-block:: js

    {
      "name": "SignalP",
      "topic": [
        {
          "uri": "http://edamontology.org/topic_0003",
          "term": "Topic"
        }
      ],
      "function": [
        {
          "comment": "predicts the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms",
          "handle": "--someOption",
          "operation": [
            {
              "uri": "http://edamontology.org/operation_0418",
              "term": "Protein signal peptide detection"
            },
            {
              "uri": "http://edamontology.org/operation_0422",
              "term": "Protein cleavage site prediction"
            }
          ],
          "input": [
            {
              "data": {
                "uri": "http://edamontology.org/data_2044",
                "term": "Sequence"
              },
              "format": [
                {
                  "uri": "http://edamontology.org/format_1929",
                  "term": "FASTA"
                }
              ]
            }
          ],
          "output": [
            {
              "data": {
                "uri": "http://edamontology.org/data_1277",
                "term": "Protein features"
              },
              "format": [
                {
                  "uri": "http://edamontology.org/format_2305",
                  "term": "GFF"
                }
              ]
            },
            {
              "data": {
                "uri": "http://edamontology.org/data_2955",
                "term": "Sequence report"
              },
              "format": [
              	{
                  "uri": "http://edamontology.org/format_2305",
                  "term": "GFF"
                }
              	]
            }
          ]
        }
      ],
      "homepage": "http://cbs.dtu.dk/services/SignalP/",
      "description": "Prediction of the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms.",
      "cost": "Free of charge (with restrictions)",
      "maturity": "Mature",
      "credit": [
        {
          "name": "TN Petersen",
          "email": "test@email.com",
          "orcidid": "test",
          "gridid": "test",
          "typeEntity": "Person",
          "typeRole": "Developer",
          "comment": "test"
        }
      ],
      "link": [
        {
          "url": "http://www.cbs.dtu.dk/cgi-bin/sw_request?signalp",
          "type": "Repository",
          "comment": "test"
        }
      ],
      "download": [
        {
          "url": "http://www.cbs.dtu.dk/cgi-bin/sw_request?signalp",
          "type": "Source code",
          "comment": "test"
        },
        {
          "url": "http://www.cbs.dtu.dk/cgi-bin/sw_request?signalp",
          "type": "Binaries",
          "comment": "test"
        }
      ],
      "license": "Proprietary",
      "operatingSystem": [
        "Linux",
        "Mac"
      ],
      "toolType": [
        "Command-line tool",
        "Web application"
      ],
      "language": ["ActionScript"],
      "documentation": [
        {
          "url": "http://www.cbs.dtu.dk/services/SignalP",
          "type": "General",
          "comment": "test"
        }
      ],
      "publication": [
        {
          "pmcid": "21959131",
          "pmid": "21959131",
          "doi": "doi:10.1038/nmeth.1701",
          "type": "Primary"
        },
        {
          "pmcid": "21959131",
          "pmid": "21959131",
          "doi": "doi:10.1038/nmeth.1701",
          "type": "Other"
        }
      ],
      "collectionID": [
        "CBS"
      ],
      "contact": [
        {
          "email": "hnielsen@cbs.dtu.dk",
          "name": "Henrik Nielsen",
          "tel": "123456798",
          "url": "https://bio.tools"
        }
      ],
      "editPermission": {
        "type": "private",
        "authors": ["ekry"]
      }
    }

.. note::
   The API supports XML and YAML format uploads and will (soon!) support XML comatible with biotoolsSchema (https://github.com/bio-tools/biotoolsschema).  Example files will be added here soon.
    
    
Data model
==========

Name
----
*Canonical software name assigned by the software developer or service provider, e.g. "SignalP"*

Attribute name
  name

Required
  Yes

Type
  String

Restrictions
  Min length: 1  
  Max length: 100  
  Pattern: [\p{Zs}A-Za-z0-9+\.,\-_:;()]*  

Example

.. code-block:: js
		
  # JSON
  "name": "SignalP"

  # XML
  <name>SignalP</name>



.. note::
   - the name has a 100 character limit and may only contain space, uppercase and lowercase letters, decimal digits, plus symbol, period, comma, dash, underscore, colon, semicolon and parentheses.
   - line feeds, carriage returns, tabs, leading and trailing spaces, and multiple spaces are not allowed / will be removed.
   - see the `curation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#id18>`_



  
Short description
-----------------
*Short and concise textual description of the software function, e.g. "Detect and visualise single-nucleotide polymorphisms (SNPs)."*

Attribute name
  shortDescription

Required
  No

Type
  String

Restrictions
  Min length: 10

  Max length: 100

Example

.. code-block:: js

  "shortDescription": "Detect and visualise single-nucleotide polymorphisms (SNPs)."

.. note::
  - see the `curation guidelines <http://biotools.readthedocs.io/en/latest/curators_guide.html#shortdescription>`_

  
Description
-----------
Attribute name
  description

Required
  Yes

Type
  String

Restrictions
  Max length: 1000

Example

.. code-block:: js

  "description": "Prediction of the presence and location of signal
  peptide cleavage sites in amino acid sequences from different organisms."
  
Current version
---------------
Attribute name
  currentVersion

Required
  No

Type
  String

Restrictions
  Max length: 50

Example

.. code-block:: js

  "currentVersion": "4.1"

Topic
-----
Attribute name
  topic

Required
  Yes

Type
  List of EDAM objects (1 or more)

EDAM object definition
  Content
    * uri
        * Required: No (if term present)
        * Type: URL
    * term
        * Required: No (if URI present)
        * Type: String
  Notes
    Either term or URI can be provided, or both. 

    URI and term are validated against EDAM ontology.
    
    If term does not match URI an error will be returned.

    Synonym terms are accepted, however, **the synonym will be replaced with main term**.

Example

.. code-block:: js

  "topic": [
        {
            "uri": "http://edamontology.org/topic_0605",
            "term": "Informatics"
        },
        {
            "uri": "http://edamontology.org/topic_3303",
            "term": "Medicine"
        }
    ]

.. _function:

Function
--------
Attribute name
  function

Required
  Yes

Type
  List of function objects (1 or more)

Function object definition
  Content
    * :ref:`operation`
        * Required: Yes
        * Type: List of EDAM objects
    * input
        * Required: No
        * Type: List of input objects
    * output
        * Required: No
        * Type: List of output objects
    * comment
        * Required: No
        * Type: String
        * Restrictions: max length: 1000

Example

.. code-block:: js

  "function": [
    {
      "comment": "predicts the presence and location of signal peptide cleavage sites in amino acid sequences from different organisms",
      "operation": [
        {
          "uri": "http://edamontology.org/operation_0418",
          "term": "Protein signal peptide detection"
        },
        {
          "uri": "http://edamontology.org/operation_0422",
          "term": "Protein cleavage site prediction"
        }
      ],
      "input": [
        {
          "data": {
            "uri": "http://edamontology.org/data_2044",
            "term": "Sequence"
          },
          "format": [
            {
              "uri": "http://edamontology.org/format_1929",
              "term": "FASTA"
            }
          ]
        }
      ],
      "output": [
        {
          "data": {
            "uri": "http://edamontology.org/data_1277",
            "term": "Protein features"
          },
          "format": [
            {
              "uri": "http://edamontology.org/format_2305",
              "term": "GFF"
            }
          ]
        },
        {
          "data": {
            "uri": "http://edamontology.org/data_2955",
            "term": "Sequence report"
          },
          "format": [
            {
              "uri": "http://edamontology.org/format_1929",
              "term": "FASTA"
            }
          ]
        }
      ]
    }
  ]

.. _operation:

Operation
---------
Attribute name
  operation

Required
  Yes

Child of
  :ref:`function`

Type
  List of EDAM objects (1 or more)

EDAM object definition
  Content
    * uri
        * Required: No (if term present)
        * Type: URL
    * term
        * Required: No (if URI present)
        * Type: String
  Notes
    Either term or URI can be provided, or both. 

    URI and term are validated against EDAM ontology.
    
    If term does not match URI an error will be returned.

    Synonym terms are accepted, however, **the synonym will be replaced with main term**.

Example

.. code-block:: js

  "operation": [
      {
          "uri": "http://edamontology.org/operation_0418",
          "term": "Protein signal peptide detection"
      },
      {
          "uri": "http://edamontology.org/operation_0422",
          "term": "Protein cleavage site prediction"
      }
  ]

.. _input:

Input
--------
Attribute name
  input

Required
  No

Child of
  :ref:`function`

Type
  List of input objects (0 or more)

Input object definition
  Content
    * data
        * Required: Yes
        * Type: EDAM object
    * format
        * Required: No
        * Type: List of EDAM objects

Example

.. code-block:: js

  "input": [
    {
      "data": {
        "uri": "http://edamontology.org/data_2044",
        "term": "Sequence"
      },
      "format": [
        {
          "uri": "http://edamontology.org/format_1929",
          "term": "FASTA"
        }
      ]
    }
  ]

.. _output:

Output
--------
Attribute name
  output

Required
  No

Child of
  :ref:`function`

Type
  List of output objects (0 or more)

Output object definition
  Content
    * data
        * Required: Yes
        * Type: EDAM object
    * format
        * Required: No
        * Type: List of EDAM objects

Example

.. code-block:: js

  "output": [
    {
      "data": {
        "uri": "http://edamontology.org/data_2044",
        "term": "Sequence"
      },
      "format": [
        {
          "uri": "http://edamontology.org/format_1929",
          "term": "FASTA"
        }
      ]
    }
  ]

.. _data:

Data
--------
Attribute name
  data

Required
  Yes

Child of
  :ref:`input` or :ref:`output`

Type
  EDAM object

EDAM object definition
  Content
    * uri
        * Required: No (if term present)
        * Type: URL
    * term
        * Required: No (if URI present)
        * Type: String
  Notes
    Either term or URI can be provided, or both. 

    URI and term are validated against EDAM ontology.
    
    If term does not match URI an error will be returned.

    Synonym terms are accepted, however, **the synonym will be replaced with main term**.

Example

.. code-block:: js

  "data": {
    "uri": "http://edamontology.org/data_2044",
    "term": "Sequence"
  }

.. _format:

Format
--------
Attribute name
  format

Required
  No

Child of
  :ref:`input` or :ref:`output`

Type
  List of EDAM objects (0 or more)

EDAM object definition
  Content
    * uri
        * Required: No (if term present)
        * Type: URL
    * term
        * Required: No (if URI present)
        * Type: String
  Notes
    Either term or URI can be provided, or both. 

    URI and term are validated against EDAM ontology.
    
    If term does not match URI an error will be returned.

    Synonym terms are accepted, however, **the synonym will be replaced with main term**.

Example

.. code-block:: js

  "format": [
    {
      "uri": "http://edamontology.org/format_1929",
      "term": "FASTA"
    }
  ]

Homepage
--------
Attribute name
  homepage

Required
  Yes

Type
  URL

Restrictions
  Max length: 300

  Pattern: ^https?:\/\/[^\s\/$.?#].[^\s]*$

Example

.. code-block:: js

  "homepage": "http://cbs.dtu.dk/services/SignalP/"

Cost
-----------
Attribute name
  cost

Required
  No

Type
  ENUM

Allowed values
  - ``Free of charge``
  - ``Free of charge (with restrictions)``
  - ``Commercial``

Example

.. code-block:: js

  "cost": "Free of charge (with restrictions)"

Maturity
-----------
Attribute name
  maturity

Required
  No

Type
  ENUM

Allowed values
  - ``Emerging``
  - ``Mature``
  - ``Legacy``

Example

.. code-block:: js

  "maturity": "Mature"

.. _credit:

Credit
--------
Attribute name
  credit

Required
  No

Type
  List of credit objects (0 or more)

Credit object definition
  Content
    * name
        * Required: Yes
        * Type: String
        * Restrictions: max length: 100
    * url
        * Required: No
        * Type: URL
        * Restrictions: max length: 300
    * email
        * Required: No
        * Type: Email
        * Restrictions: max length: 300
    * orcidId
        * Required: No
        * Type: String
        * Restrictions: max length: 100
    * gridId
        * Required: No
        * Type: String
        * Restrictions: max length: 100
    * typeEntity
        * Required: No
        * Type: ENUM
        * Allowed values: ``Person``, ``Project``, ``Division``, ``Institute``, ``Consortium``, ``Funding agency``
    * typeRole
        * Required: No
        * Type: ENUM
        * Allowed values: ``Developer``, ``Maintainer``, ``Provider``, ``Documentor``, ``Contributor``, ``Support``
    * comment
        * Required: No
        * Type: String
        * Restrictions: max length: 1000

Example

.. code-block:: js

  "credit": [
    {
      "name": "TN Petersen",
      "url": "http://cbs.dtu.dk",
      "email": "test@cbs.dtu.dk",
      "orcidId":"test",
      "gridId": "test",
      "typeEntity": "Person",
      "typeRole": "Developer",
      "comment": "test"
    }
  ]

Link
--------
Attribute name
  link

Required
  No

Type
  List of link objects (0 or more)

Link object definition
  Content
    * url
        * Required: Yes
        * Type: URL
        * Restrictions: max length: 300
    * type
        * Required: Yes
        * Type: ENUM
        * Allowed values: ``Browser``, ``Helpdesk``, ``Issue tracker``, ``Mailinglist``, ``Mirror``, ``Registry``, ``Repository``, ``Social media``
    * comment
        * Required: No
        * Type: String
        * Restrictions: max length: 1000

Example

.. code-block:: js

  "link": [
    {
      "url": "http://www.cbs.dtu.dk/cgi-bin/sw_request?signalp",
      "type": "Repository",
      "comment": "test"
    }
  ]

Download
--------
Attribute name
  download

Required
  No

Type
  List of download objects (0 or more)

Download object definition
  Content
    * url
        * Required: Yes
        * Type: URL
        * Restrictions: max length: 300
    * type
        * Required: Yes
        * Type: ENUM
        * Allowed values: ``API specification``, ``Biological data``, ``Binaries``, ``Binary package``, ``Command-line specification``, ``Container file``, ``CWL file``, ``Icon``, ``Ontology``, ``Screenshot``, ``Source code``, ``Source package``, ``Test data``, ``Test script``, ``Tool wrapper (galaxy)``, ``Tool wrapper (taverna)``, ``Tool wrapper (other)``, ``VM image``
    * comment
        * Required: No
        * Type: String
        * Restrictions: max length: 1000

Example

.. code-block:: js

  "download": [
    {
      "url": "http://www.cbs.dtu.dk/cgi-bin/sw_request?signalp",
      "type": "Source code",
      "comment": "test"
    }
  ]

Documentation
--------------

Attribute name
  documentation

Required
  No

Type
  List of documentation objects (0 or more)

Documentation object definition
  Content
    * url
        * Required: Yes
        * Type: URL
        * Restrictions: max length: 300
    * type
        * Required: Yes
        * Type: ENUM
        * Allowed values: ``API documentation``, ``Citation instructions``, ``General``, ``Manual``, ``Terms of use``, ``Training material``, ``Other``
    * comment
        * Required: No
        * Type: String
        * Restrictions: max length: 1000

Example

.. code-block:: js

  "documentation": [
    {
      "url": "http://www.cbs.dtu.dk/services/SignalP",
      "type": "General",
      "comment": "test"
    }
  ]

License
-----------
Attribute name
  license

Required
  No

Type
  ENUM

Allowed values
  ``0BSD``, ``AAL``, ``ADSL``, ``AFL-1.1``, ``AFL-1.2``, ``AFL-2.0``, ``AFL-2.1``, ``AFL-3.0``, ``AGPL-1.0``, ``AGPL-3.0``, ``AMDPLPA``, ``AML``, ``AMPAS``, ``ANTLR-PD``, ``APAFML``, ``APL-1.0``, ``APSL-1.0``, ``APSL-1.1``, ``APSL-1.2``, ``APSL-2.0``, ``Abstyles``, ``Adobe-2006``, ``Adobe-Glyph``, ``Afmparse``, ``Aladdin``, ``Apache-1.0``, ``Apache-1.1``, ``Apache-2.0``, ``Artistic-1.0``, ``Artistic-1.0-Perl``, ``Artistic-1.0-cl8``, ``Artistic-2.0``, ``BSD-2-Clause``, ``BSD-2-Clause-FreeBSD``, ``BSD-2-Clause-NetBSD``, ``BSD-3-Clause``, ``BSD-3-Clause-Attribution``, ``BSD-3-Clause-Clear``, ``BSD-3-Clause-LBNL``, ``BSD-3-Clause-No-Nuclear-License``, ``BSD-3-Clause-No-Nuclear-License-2014``, ``BSD-3-Clause-No-Nuclear-Warranty``, ``BSD-4-Clause``, ``BSD-4-Clause-UC``, ``BSD-Protection``, ``BSD-Source-Code``, ``BSL-1.0``, ``Bahyph``, ``Barr``, ``Beerware``, ``BitTorrent-1.0``, ``BitTorrent-1.1``, ``Borceux``, ``CATOSL-1.1``, ``CC-BY-1.0``, ``CC-BY-2.0``, ``CC-BY-2.5``, ``CC-BY-3.0``, ``CC-BY-4.0``, ``CC-BY-NC-1.0``, ``CC-BY-NC-2.0``, ``CC-BY-NC-2.5``, ``CC-BY-NC-3.0``, ``CC-BY-NC-4.0``, ``CC-BY-NC-ND-1.0``, ``CC-BY-NC-ND-2.0``, ``CC-BY-NC-ND-2.5``, ``CC-BY-NC-ND-3.0``, ``CC-BY-NC-ND-4.0``, ``CC-BY-NC-SA-1.0``, ``CC-BY-NC-SA-2.0``, ``CC-BY-NC-SA-2.5``, ``CC-BY-NC-SA-3.0``, ``CC-BY-NC-SA-4.0``, ``CC-BY-ND-1.0``, ``CC-BY-ND-2.0``, ``CC-BY-ND-2.5``, ``CC-BY-ND-3.0``, ``CC-BY-ND-4.0``, ``CC-BY-SA-1.0``, ``CC-BY-SA-2.0``, ``CC-BY-SA-2.5``, ``CC-BY-SA-3.0``, ``CC-BY-SA-4.0``, ``CC0-1.0``, ``CDDL-1.0``, ``CDDL-1.1``, ``CECILL-1.0``, ``CECILL-1.1``, ``CECILL-2.0``, ``CECILL-2.1``, ``CECILL-B``, ``CECILL-C``, ``CNRI-Jython``, ``CNRI-Python``, ``CNRI-Python-GPL-Compatible``, ``CPAL-1.0``, ``CPL-1.0``, ``CPOL-1.02``, ``CUA-OPL-1.0``, ``Caldera``, ``ClArtistic``, ``Condor-1.1``, ``Crossword``, ``CrystalStacker``, ``Cube``, ``D-FSL-1.0``, ``DOC``, ``DSDP``, ``Dotseqn``, ``ECL-1.0``, ``ECL-2.0``, ``EFL-1.0``, ``EFL-2.0``, ``EPL-1.0``, ``EUDatagrid``, ``EUPL-1.0``, ``EUPL-1.1``, ``Entessa``, ``ErlPL-1.1``, ``Eurosym``, ``FSFAP``, ``FSFUL``, ``FSFULLR``, ``FTL``, ``Fair``, ``Frameworx-1.0``, ``FreeImage``, ``GFDL-1.1``, ``GFDL-1.2``, ``GFDL-1.3``, ``GL2PS``, ``GPL-1.0``, ``GPL-2.0``, ``GPL-3.0``, ``Giftware``, ``Glide``, ``Glulxe``, ``HPND``, ``HaskellReport``, ``IBM-pibs``, ``IJG``, ``IPA``, ``IPL-1.0``, ``ISC``, ``ImageMagick``, ``Imlib2``, ``Info-ZIP``, ``Intel``, ``Intel-ACPI``, ``Interbase-1.0``, ``JSON``, ``JasPer-2.0``, ``LAL-1.2``, ``LAL-1.3``, ``LGPL-2.0``, ``LGPL-2.1``, ``LGPL-3.0``, ``LGPLLR``, ``LPL-1.0``, ``LPL-1.02``, ``LPPL-1.0``, ``LPPL-1.1``, ``LPPL-1.2``, ``LPPL-1.3a``, ``LPPL-1.3c``, ``Latex2e``, ``Leptonica``, ``LiLiQ-P-1.1``, ``LiLiQ-R-1.1``, ``LiLiQ-Rplus-1.1``, ``Libpng``, ``MIT``, ``MIT``, ``MIT-advertising``, ``MIT-enna``, ``MIT-feh``, ``MITNFA``, ``MPL-1.0``, ``MPL-1.1``, ``MPL-2.0``, ``MPL-2.0-no-copyleft-exception``, ``MS-PL``, ``MS-RL``, ``MTLL``, ``MakeIndex``, ``MirOS``, ``Motosoto``, ``Multics``, ``Mup``, ``NASA-1.3``, ``NBPL-1.0``, ``NCSA``, ``NGPL``, ``NLOD-1.0``, ``NLPL``, ``NOSL``, ``NPL-1.0``, ``NPL-1.1``, ``NPOSL-3.0``, ``NRL``, ``NTP``, ``Naumen``, ``NetCDF``, ``Newsletr``, ``Nokia``, ``Noweb``, ``Nunit``, ``OCCT-PL``, ``OCLC-2.0``, ``ODbL-1.0``, ``OFL-1.0``, ``OFL-1.1``, ``OGTSL``, ``OLDAP-1.1``, ``OLDAP-1.2``, ``OLDAP-1.3``, ``OLDAP-1.4``, ``OLDAP-2.0``, ``OLDAP-2.0.1``, ``OLDAP-2.1``, ``OLDAP-2.2``, ``OLDAP-2.2.1``, ``OLDAP-2.2.2``, ``OLDAP-2.3``, ``OLDAP-2.4``, ``OLDAP-2.5``, ``OLDAP-2.6``, ``OLDAP-2.7``, ``OLDAP-2.8``, ``OML``, ``OPL-1.0``, ``OSET-PL-2.1``, ``OSL-1.0``, ``OSL-1.1``, ``OSL-2.0``, ``OSL-2.1``, ``OSL-3.0``, ``OpenSSL``, ``PDDL-1.0``, ``PHP-3.0``, ``PHP-3.01``, ``Plexus``, ``PostgreSQL``, ``Python-2.0``, ``QPL-1.0``, ``Qhull``, ``RHeCos-1.1``, ``RPL-1.1``, ``RPL-1.5``, ``RPSL-1.0``, ``RSA-MD``, ``RSCPL``, ``Rdisc``, ``Ruby``, ``SAX-PD``, ``SCEA``, ``SGI-B-1.0``, ``SGI-B-1.1``, ``SGI-B-2.0``, ``SISSL``, ``SISSL-1.2``, ``SMLNJ``, ``SMPPL``, ``SNIA``, ``SPL-1.0``, ``SWL``, ``Saxpath``, ``Sendmail``, ``SimPL-2.0``, ``Sleepycat``, ``Spencer-86``, ``Spencer-94``, ``Spencer-99``, ``SugarCRM-1.1.3``, ``TCL``, ``TMate``, ``TORQUE-1.1``, ``TOSL``, ``UPL-1.0``, ``Unicode``, ``Unlicense``, ``VOSTROM``, ``VSL-1.0``, ``Vim``, ``W3C``, ``W3C-19980720``, ``WTFPL``, ``Watcom-1.0``, ``Wsuipa``, ``X11``, ``XFree86-1.1``, ``XSkat``, ``Xerox``, ``Xnet``, ``YPL-1.0``, ``YPL-1.1``, ``ZPL-1.1``, ``ZPL-2.0``, ``ZPL-2.1``, ``Zed``, ``Zend-2.0``, ``Zimbra-1.3``, ``Zimbra-1.4``, ``Zlib``, ``bzip2-1.0.5``, ``bzip2-1.0.6``, ``curl``, ``diffmark``, ``dvipdfm``, ``eGenix``, ``gSOAP-1.3b``, ``gnuplot``, ``iMatix``, ``libtiff``, ``mpich2``, ``psfrag``, ``psutils``, ``xinetd``, ``xpp``, ``zlib-acknowledgement``, ``Proprietary``, ``Other``

Example

.. code-block:: js

  "license": "Proprietary"


Operating system
----------------
Attribute name
  operatingSystem

Required
  No

Type
  List of ENUMs

Allowed values
  - ``Mac``
  - ``Linux``
  - ``Windows``

Example

.. code-block:: js

  "operatingSystem": [
    "Linux",
    "Mac"
  ]

Tool type
----------------
Attribute name
  toolType

Required
  Yes

Type
  ENUM

Allowed values
  ``Command-line tool``, ``Web application``, ``Desktop application``, ``Script``, ``Suite``, ``Workbench``, ``Database portal``, ``Ontology``, ``Workflow``, ``Plug-in``, ``Library``, ``Web API``, ``Web service``, ``SPARQL endpoint``

Example

.. code-block:: js

  "toolType": [
    "Command-line tool",
    "Web application"
  ]

Language
----------------
Attribute name
  language

Required
  No

Type
  ENUM

Allowed values
  ``ActionScript``, ``Ada``, ``AppleScript``, ``Assembly language``, ``AWK``, ``Bash``, ``C``, ``C#``, ``C++``, ``COBOL``, ``ColdFusion``, ``CWL``, ``D``, ``Delphi``, ``Dylan``, ``Eiffel``, ``Forth``, ``Fortran``, ``Groovy``, ``Haskell``, ``Icarus``, ``Java``, ``Javascript``, ``JSP``, ``LabVIEW``, ``Lisp``, ``Lua``, ``Maple``, ``Mathematica``, ``MATLAB``, ``MLXTRAN``, ``NMTRAN``, ``Pascal``, ``Perl``, ``PHP``, ``Prolog``, ``PyMOL``, ``Python``, ``R``, ``Racket``, ``REXX``, ``Ruby``, ``SAS``, ``Scala``, ``Scheme``, ``Shell``, ``Smalltalk``, ``SQL``, ``Turing``, ``Verilog``, ``VHDL``, ``Visual Basic``, ``Other``

Example

.. code-block:: js

  "language": [
    "ActionScript"
  ]

.. _publication:

Publication
-----------
Attribute name
  publication

Required
  Yes

Type
  List of publication objects (1 or more)

Publication object definition
  Content
    * pmcid
        * Required: No
        * Type: PMCID
    * pmid
        * Required: No
        * Type: PMID
    * doi
        * Required: No
        * Type: DOI
    * type
        * Required: No
        * Type: ENUM
        * Allowed values: ``Primary``, ``Benchmark``, ``Review``, ``Other``
    * version
        * Required: No
        * Type: String
        * Restrictions: max length: 300

Example

.. code-block:: js

  "publication": [
    {
      "pmcid": "21959131",
      "pmid": "21959131",
      "doi": "doi:10.1038/nmeth.1701",
      "type": "Primary",
      "version": "4.0"
    }
  ]

Collection
----------------
Attribute name
  collectionID

Required
  No

Type
  List of strings

Restrictions
  Max length: 300

Example

.. code-block:: js

  "collectionID": [
    "CBS"
  ]

.. _contact:

Contact
--------
Attribute name
  contact

Required
  No

Type
  List of contact objects (0 or more)

Contact object definition
  Content
    * name
        * Required: Yes
        * Type: String
        * Restrictions: max length: 100
    * url
        * Required: No
        * Type: URL
        * Restrictions: max length: 300
    * email
        * Required: No
        * Type: Email
        * Restrictions: max length: 300
    * tel
        * Required: No
        * Type: String
        * Restrictions: max length: 30


Example

.. code-block:: js

  "contact": [
    {
      "name": "Henrik Nielsen",
      "url": "http://cbs.dtu.dk",
      "email": "test@cbs.dtu.dk",
      "tel": "123456798"
    }
  ]

.. _editPermission:

Permissions
-------------------
Attribute name
  editPermission

Required
  No

Type
  Permission object

Permission object definition
  Content
    * type
        * Required: Yes
        * Type: ENUM
        * Allowed values: ``private``, ``public``, ``group``
    * authors
        * Required: No
        * Type: List of usernames

  Notes
    'authors' only need to be provided when type is set to ``group``.

Example

.. code-block:: js

  "editPermission": {
    "type": "group",
    "authors": [
      "ekry", 
      "lukbe"
    ]
  }
