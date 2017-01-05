User Guide
==========

This user guide aims to help you through the different steps to register your own entry to `bio.tools`_.

.. Note::
    If you find a bug, have any questions or suggestions, please `get in touch with us <mailto:registry-support@elixir-dk.org>`_.

Create an account
-----------------
Creating an account on bio.tools is very quick and simple. Just click on the `sign up`_ button
at the top-right corner of the page.
Then you just need to give a username, your email address and a password to get your account done. 

.. _`sign up`: https://bio.tools/signup

Add content
-----------
Every user is welcome to register its own resource to `bio.tools`_. Once your account is
created, you can start adding your content by clicking on `add content`_:

The registration of an new entry is splitted in different parts that are described below.

.. Note::
    The minimum information required is marked with a red asterix |asterix|.

At every moment, you can check the validity of your information by clicking on Validate and
save it by clicking on Save |validate_save|.

.. Note::
    Saving the entry makes it directly available online.
    If you want to save what you have done without publishing it, the only
    way is to go to the :ref:`json` part and save the .json file locally.

.. _`add content`: https://bio.tools/register

.. |asterix| image:: _static/red_asterix.png
   :width: 15px
   :height: 20px

.. |validate_save| image:: _static/validate_save.png
   :width: 100px
   :height: 30px

Summary
"""""""
For this first part, you give the main descriptors of your entry. This includess the **name** 
of your resource with a **description**, its **version** and a **homepage URL**. A unique **ID**
is automatically generated from the name but it is still possible to change it.

.. Note::
    A unique URL on `bio.tools`_ will be generated for the entry with the following format:
    http://bio.tools/tool/ID/version/version_number

Function
""""""""
This is where you describe the functionnality of your entry based on the `EDAM ontology`_ [1]_.
The description is built on the following diagram:

|biotool_function| 

In each box, you can add as many fields as you want. You can also add a general comment about the function (*this is particularly useful when your entry has several functions*).

.. Note::
    It can be difficult to find the right ontology to describe your function(s), input(s) or output(s).
    Please visit `OLS EDAM`_ and `BioPortal EDAM`_ websites to find more information about the
    different ontologies and help you finding the best description.

.. _`EDAM ontology`: http://edamontology.org
.. _`OLS EDAM`: https://www.ebi.ac.uk/ols/ontologies/edam
.. _`BioPortal EDAM`: https://bioportal.bioontology.org/ontologies/EDAM/?p=classes&conceptid=root

.. |biotool_function| image:: _static/biotool_function.png

Labels
""""""
In this part, you can tell more about your tool:

* What **type** of tool it is (command line tool, library...).
* In which **topic(s)** the tool belongs to (based on `EDAM ontology`_ [1]_).
* In which **operating system** it is possible to use it.
* The **language** used to develop the tool, its **license** and **maturity**.
* The **accessibility** of your tool and its **cost**.

Contact
"""""""
At least one contact is required to register a tool but you can add as many contact as you want.

.. Note::
    If you wish to mention people that participated in the development of the tool, you can
    use the :ref:`credits` part.

Links
"""""
It is the place where your share links that do not belong to the other parts. For instance, it
can be link to a mailing list, mirror or repository.

Download
""""""""
You can here share all the different download links you want. It can be many different kind
such as binaries, source code, biological data, test data (full list available on the drop
down menu of **Download type**).

Documentation
"""""""""""""
Make your different documentations for your tool available here.

Publications
""""""""""""
Share the different publications of the tool which can be the primary publication but also
review or secondary references that are relevant to this tool. You can use either the **PubMed Central ID** (PMCID), the **PubMed ID** (PMID) or the **Digital Object ID** (DOI).

.. _credits:

Credits
"""""""
Credits represent all type of entities that participated in the tool. It can be a people, but
also an institution or a consortium.

.. _json:

JSON
""""
This is all the information you gave about your tool, formatted in JSON format.

Permissions
"""""""""""
You can decide to make the entry either editable only by yourself, a list of users or anyone.

Update a resource
-----------------
There is two way to update a resource from its tool card: |update|

* Click on update this record if it concerns minor changes
* Click on create a new version to register a new version. This allows to keep all the information concerning the previous version

.. |update| image:: _static/update.png
   :width: 255px
   :height: 45px

Remove a resource
-----------------
From the tool card, click on update this record. Then you can remove the entry by clicking on the remove button |remove|.

.. |remove| image:: _static/remove.png
   :width: 55px
   :height: 30px

.. warning::
    Removing an entry is definitive

Search for a tool
-----------------
Coming soon...

References
----------
.. [1] Ison, J., Kalaš, M., Jonassen, I., Bolser, D., Uludag, M., McWilliam, H., Malone, J., Lopez, R., Pettifer, S. and Rice, P. (2013). EDAM: an ontology of bioinformatics operations, types of data and identifiers, topics and formats. Bioinformatics, 29(10): 1325-1332.

.. _`bio.tools`: https://bio.tools
