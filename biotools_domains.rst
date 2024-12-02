Domains in bio.tools
====================

*bio.tools* domains provide a way to "slice" the bio.tools content into subsets of tools. 

The name **"domain"** (or sometimes also referred as **"subdomain"**) comes from the fact that after creation the domains can be accessed via regular URL subdomains in bio.tools such as `proteomics <https://bio.tools/t?domain=proteomics>`_ or `rare-diseases <https://bio.tools/t?domain=rare-diseases>`_.

The advantage of creating and using bio.tools domains is that you can describe, link to, and search within a smaller subset (or "slice") of the bio.tools content which can help with the description and findability of tools relevant to a specific task.

Examples of bio.tools domains include:

- tools related to a specific bioinformatics area such as *Proteomics*, *Rare diseases*, *COVID* etc
- a subset or a collection of tools developed or used by a research group, lab or any other entity
- any other grouping, subset or collection of tools that serves a specific purpose or provides a certain value to researchers, curators, developers, tool users etc


A domain in bio.tools is a collection of tools along with metadata describing the domain itself. The metadata of the domain contains the following attributes:

Domain properties
^^^^^^^^^^^^^^^^^

Domain name
-----------
The unique name (or identifier) of a domain.

Note: the domain name can only be provided at the time of the domain creation. After the domain has been created the name cannot be changed,


- **REQUIRED** field: the domain name is the only metadata field required to create a bio.tools domain
- **MUST** be URL-safe, clean and intuitive
- **MUST** be related to the tools in the domain


Domain title
------------
The title of the domain.

- **MUST** be concise and descriptive. The domain title will appear at the top part of the domain page


Domain subtitle
---------------
The subtitle of the domain. 

- **SHOULD** be a longer version of the domain title. Not always needed as any other long description will be present in the **domain description** field


Domain tags
-----------
Tags associated with a domain.

- **MUST** be keywords that help with the search and discovery of the domain


Domain collections
------------------
Collections associated with the domain. 

When inputing a domain collection the user is presented with suggestions for tool collections. Domain collections are used as a matching mechanism between tools and domains. See the **Priate vs Public domains** section below for more.


Domain description
------------------
Longform description of the domain.

**SHOULD** contain any descriptive text about the domain that does not fit in any of the above fields.

Domain descriptions offer support for simple HTML tags such as **bold**, *italics* or `anchor tags <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a>`_.


Domain resources
----------------
Domain resources provide the tool content of the domain. Any tool entry in bio.tools can be added to a domain. 

A user can search for a tool by name, identifier, collection or credit entities.

Tools can be added or removed from a domain at any time. 
The tool content of a domain can change if a domain is public, see the **Private vs Public domains** section below.

**MUST** contain tools relevant to the domain


Private domain flag
-------------------
Indicates if the domain is private (true by default) to a user or public to the bio.tools registry.


Private vs Public domains
^^^^^^^^^^^^^^^^^^^^^^^^^

Private domains
---------------
With private domains only the creator of the domain can change the tools that belong to that specific domain.
By default domains are private.
This option is recommended when full control of the domain content is required. 

Public domains
--------------
A public domain is a domain in which other users can populate that domain by tagging tools with the same collections that are also present for that domain. If a domain is tagged with certain collections and tools are also tagged with the same collections then that tool will be added to the domain. In this way users can tag their tools as part of domains without needing permissions to that domain. 

Even if users can modify the tool content of a specific domain they cannot change the metadata of the domain (e.g. domain title, domain description etc)

Explore domains
^^^^^^^^^^^^^^^
All domains in bio.tools can be viewed and searched at `https://bio.tools/domains <https://bio.tools/domains>`_ or going to Explore -> Domains in the bio.tools page header.

Create a domain
^^^^^^^^^^^^^^^
In order to create a domain a user needs a bio.tools account and to be logged in. 
In the bio.tools page header go to Menu -> Manage domains or directly to `https://bio.tools/domain-manager <https://bio.tools/domain-manager>`_. 

This page will show all the domains (if any) a user has created. To create a new domain click on the *Add* button. This will take you to the domain create page. Fill in the fields described above (*only domain name required*) and click Save at the bottom right. This will validate and create your domain and redirect to the domain update page where tools can also be added to the domain.

Update a domain
^^^^^^^^^^^^^^^
From the `domain manager page <https://bio.tools/domain-manager>`_ click on the *Edit* button for any existing domains to update domain metadata or to add / remove tools associated to a domain.

Add-Remove tools
----------------
Tools can only be added after a domain has been created, on the domain update page. 
In the "*Search for tools*" section of the page use the searchbox to find the tools to add to the domain. Tools can be searched by tool name, tool identifier, tool collection and credits. Click on the Search button to find relevant tools. Results will appear below the searchbox. Add a tool by clicking the *Add to domain* button for a single tool or click *Add all tools* to add all tool results to the domain.

The tools added to the domain will show up below in the *Tools included the domain* section. In this section any included tools can also be removed. 

**Click the "Update" button at the bottom to save your changes.**
