*************
API Quickstart
*************

This page gets you productive with the bio.tools Web API in minutes.
For full details, see the :doc:`API Reference <api_reference>` and the
:doc:`API Usage Guide <api_usage_guide>`.

Base URL
--------
- **Production:** ``https://bio.tools/api``

Media types
-----------
- Responses: JSON by default. Use ``?format=json`` or ``?format=xml``.
- For human-readable output: ``?format=api``.

Authentication
--------------
Only endpoints that change data require authentication.
- Header: ``Authorization: Token <your_token>``
- Get a token from your bio.tools account. See :ref:`Token <api_reference>`.

List tools
----------
Retrieve paginated tool listings with optional search, filter, sort.

.. code-block:: bash

	# Basic list (first page, 50 per page by default)
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?format=json" | jq .

	# Pagination
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?page=2&per_page=25" | jq .

	# Search across many attributes
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?q=alignment" | jq .

	# Filter by specific attribute (see supported attributes in API Reference)
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?name=signalp" | jq .

	# Sort and order
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?q=alignment&sort=lastUpdate&ord=desc" | jq .


Common filters
--------------
Examples of frequently used filters (quote values when advised):

.. code-block:: bash

	# EDAM Operation (term)
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?operation=Sequence%20analysis" | jq .

	# EDAM Operation (ID)
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?operationID=\"operation_2403\"" | jq .

	# Data type
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?dataType=Protein%20sequence" | jq .

	# Domain
	curl -s -H "Accept: application/json" "https://bio.tools/api/t/?domain=proteomics" | jq .

Tool detail
-----------
Fetch a single tool by its ``biotoolsID``.

.. code-block:: bash

	curl -s "https://bio.tools/api/tool/SignalP?format=json" | jq .

Register a tool (POST)
----------------------
Create a new tool entry. Requires authentication.

.. code-block:: bash

	# Example using JSON file payload.json (biotoolsSchema-compatible)
	curl -s -X POST \
	  -H "Content-Type: application/json" \
	  -H "Authorization: Token <your_token>" \
	  -d @payload.json \
	  "https://bio.tools/api/tool/" | jq .

Validate a tool (POST)
----------------------
Validate the payload without saving it. Requires authentication.

.. code-block:: bash

	curl -s -X POST \
	  -H "Content-Type: application/json" \
	  -H "Authorization: Token <your_token>" \
	  -d @payload.json \
	  "https://bio.tools/api/validate/tool/" | jq .

Update a tool (PUT)
-------------------
Update an existing tool by ``biotoolsID``. Requires authentication.

.. code-block:: bash

	curl -s -X PUT \
	  -H "Content-Type: application/json" \
	  -H "Authorization: Token <your_token>" \
	  -d @payload.json \
	  "https://bio.tools/api/tool/SignalP/" | jq .

Response shape (list endpoint)
------------------------------
The list endpoint returns:

- ``count``: total results for the query
- ``previous``: link to previous page (or ``null``)
- ``next``: link to next page (or ``null``)
- ``list``: array of tool summaries

Tips
----
- Quote parameters exactly where the API requires it (see attribute table in :doc:`API Reference <api_reference>`).
- Use ``per_page`` and ``page`` to page through results; check ``next`` to continue.
- Prefer IDs (e.g. EDAM URIs) for exact matching; terms are fuzzy.
- For XML workflows, switch ``Content-Type`` and ``?format=xml`` accordingly.

Next steps
----------
- Explore all query attributes and headers in :doc:`API Reference <api_reference>`.
- Review payload rules and examples in :doc:`API Usage Guide <api_usage_guide>`.