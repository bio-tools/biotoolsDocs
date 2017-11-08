Hangouts
========

Monthly informal meetings to discuss all matters around bio.tools including ELIXIR EXCELERATE WP1 ("Tools Interoperability and Service Registry") tasks and activities of ELIXIR Denmark technical staff.

You are welcome to attend; please mail Henriette Husum Bak-Jensen (hhu@bio.ku.dk) cc Jon Ison (jison@bioinformatics.dtu.dk), including your gmail and skype addresses.  To understand how we organise tasks and projects, read the `Contributors Guide <http://biotools.readthedocs.io/en/latest/project_management.html>`_.


-------------
2017 Meetings
-------------

- No meeting in July, Aug
- POSTPONED (date TBD) Fri Sep 29, 11 AM CEST **WP1-focus**
- Fri Oct 27, 11 AM CET
- Thu Nov 23, 12.30 CET for 2 hours **WP1-focus**
- No meeting in Dec 

------------
Next meeting
------------

2017 Novmber 23, 12.30 CET 
---------------------------

Call details (*to be confirmed*)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

TC by DeIC platform (ensure Jon & Henriette have your email address)
Connect via Computer: http://v.deic.dk?ID=610026 (Windows / Mac)
Write your name and meeting ID: 610026.  Click Participate Now. 
Scopia Desktop client will be installed before entering the meeting room the first time. 
Installation guides: https://www.deic.dk/via_computer_dk


Attendeees
^^^^^^^^^^
Representatives of ELIXIR EXCELERATE WP1 partners are expected to attend.

Confirmed
^^^^^^^^^
Jon Ison (DTU, DK)
Matus Kalas (UiB, NO)
Dan Søndergaard (AU, DK) + student helpers
Hervé Menager and/or Kenzo Hillion1 (IP, FR)

Apologies
^^^^^^^^^^

Agenda
^^^^^^

1. **Purpose of this call** (Jon Ison)
2. **Deliverables & milestones due in 2018** (Jon Ison)

   2.1. Summary (https://biotools.sifterapp.com/projects/40459/issues?srt=milestone)

   2.2. M1.3 - literature integration (update)
   
   2.3. M1.6 - metacatalogue + synergy meetings (update)
   
   2.4. D1.5 - metrics in registry (update)
   
   2.5. D1.7 - user helpdesk / fora (action needed, see below)
   
   2.6. D1.8 - matchmaking service : (discussion needed - recommend to drop this)

3. **WP1 partner round-table presentations of what's been done and what's planned for 2018** (5' / partner)
   
   3.0.  Overall priorities and goals for WP1 for 2018 (DTU et al.)
   
   3.1.  ELIXIR-DK (DTU et al.)
   
   3.2.  ELIXIR-EE (UTARTU)
   
   3.3.  ELIXIR-ES (BSC, IRB)
   
   3.4.  ELIXIR-FR (IP, CNRS)
   
   3.5.  ELIXIR-CZ (MU)
   
   3.6.  ELIXIR-NO (UiB)
   
   3.7.  ELIXIR-EMBL (EBI)
   
   3.8.  ELIXIR-CH (SIB)
   
   3.9.  ELIXIR-UK (UOXF)
   
   3.10. ELIXIR-PT (INESC-ID)
   
4. **Framing a WP1 f2f meeting** early 2018, round-table contributions

   *add your suggested agenda items for the f2f here*
   
5. **Publication opportunities** (Jon Ison)
6. **AOB**



.. note::

   **D1.7 user helpdesk / fora**
   Excerpt from EXCELERATE proposal is below.  The idea was indicated as high-priority in the EXCELERATE mid-term review.  We need to identify leader(s) for this deliverable.

   This task will provide direct and indirect user support to deliver impact for ELIXIR end-users. Direct support will be achieved primarily by leveraging the existing and highly popular user bioinformatics forums (BioStars, BioPlanet etc.).  A User-support specialist will patrol such forums and respond to questions in one of four ways:

   1. Where resources answering to the Users needs exist in the registry, a link to them in the registry will be provided via our API.
   2. Where resources exist in the registry, but the registry API cannot be used to answer the question directly, they will request new features of the API and in so doing drive development of the Query Interface.
   3. Where an appropriate resource exists but has not been registered, they will request the appropriate registry curator add it to the registry.
   4. Where a registered resource exists that is close, but not quite what is required, they will forward feature requests to the appropriate developers, possibly via the Matchmaking Service (D1.5).


-------
Archive
-------

2017 June 16, 11 AM CEST
-----------------------



Attendeees
^^^^^^^^^^
WP-1 partners of which the following were present Anne Wenzel, Emil Rydza, Hans Ienasescu, Jon Ison, Matus Kalas, Piotr Chmura, Severine, Henriette Husum Bak-Jensen.

Apologies
^^^^^^^^^^
Vivi Raundahl Gregersen, Hedi Peterson, Veit Schwämmle, Vivi Gregersen, Ahto Salumets, Salva , Hervé Menager


Minutes
^^^^^^^
The goal of todays meeting was to go over the proposed standards for tools entries in bio.tools  (see https://github.com/bio-tools/biotoolsSchemaDocs/blob/master/information_requirement.rst ). 
The minutes also offer fundamental concerns – that prompt for consideration before launching the standards
Several comments were made at the meeting chat and also issues were brought up. Those can be found here https://github.com/bio-tools/biotoolsSchema/issues/77 and more can be added after the meeting, please.
The main points - constructive discussion points and actions points – at the meeting, were the following:

**The idea of 'revising the standards on an annual basis' is challenging**

Four standard tiers/labels are contemplated (OKAY, GOOD, VERY GOOD, EXCELLENT) that are all of 'acceptable' quality. A fifth label (NEEDS TO IMPROVE) is for entries which lack basic information. Each label is associated with a set of attributes. The set of attributes required to earn a label – or the list of allowed sub-domains to tick a particular attribute, could in principle be changed – if practical experience shows it would be valuable. And so we envision to revisit, with caution, the set of four (five) standards on an annual basis – with input from the community BUT - by all means, any future change in the standards must not bereave a tool of an 'earned' label, or lead to a 'greying' of an annotation void. Rather such changes should apply to future earning of labels, and be presented in the 'background guide info for curators' for verified-label tools, that now needs more annotation work.

**Annotation of Not applicable, None exists, Unknown, and Need Updating**

These terms are all valuable information, and should be carefully and individually assigned as annotation options, for all attributes. MK made the point that distinct tool types warrant a distinct set of attributes – in order to avoid numerous 'not applicable' annotation results. It was agreed that MK will draft a matrix (tool types vs attributes) that will help decide if some tool types should indeed be assigned a distinct set of attributes, and if not, at least will help capture the adequacy of annotating 'not applicable' for a given tool attribute. 

**Annotation metrics – assessing quantitative measures on the quality input**

This point was made by MK and wants to assess the registry's total number of annotated information on a given attribute. Other obvious quantitative measures include amount of information (most simply number of JSON/XML nodes); last modified (time since); last new version (time since); last scientific publication (time since). This will help us monitor the overall progress on quality of the registry as a supplement to tracking number of users and number of entries (quantity). 


**Date-stamps**

The annotation 'None exists' should be time stamped, because it may be relevant to update the information.
The annotation 'Not applicable' should not be Date-stamped, because it will never be relevant information.

**Verification of labels**

Several arguments were made for and against a Date-stamped verified label of a given tool. In particular if we're dealing with manual verification of earning a given label: 1) this could be seen as censure, by the developers, which would counteract his/her willingness to simply supply the best possible annotation/information on a given tool, 2) it is labour-intensive and possibly old-fashioned (not Wiki-like), 3) there is a danger of the verification process is of lower quality than the annotation process itself. On the other hand, the end user may better trust a manually verified date-stamped label. We need to consider the need of developers (the best provider of info) and of the end-user (trust issue). Including the possibility for developing a machine-learning-driven autocurator (Action Piotr Chmura). It is possible that the ressources spent of verification were better spent to improve the annotation.



2017, Apr 28 11 AM CEST
-----------------------

Attendees
^^^^^^^^^

Vivi Raundahl Gregersen, Anders Halager, Hans Ienasescu, Veit Schwämmle, Søren Brunak, Jon Ison, Frode Pedersen, Mathias Haudgaard, Arne Kratz, Anne Wenzel, Henriette Husum Bak-Jensen

Agenda and Minutes
^^^^^^^^^^^^^^^^^^

**1) Workplan for importing public domain information on 11.152 tools from MyBioSoftware to bio.tools (HH, 5’)https://biotools.sifterapp.com/issues/356**

HansI and HH will produce a work plan to ensure a staged import of public domain info on the 11.152 tools from MyBioSoftware, so that the entries will appear progressively month by month, to be completed by end of 2017. They will also plan the curation effort, which must take place in parallel.
HH will ask for renewal of volume and quality target for bio.tools entries at the next ELIXIR steering meeting (June XX) as current volume target (10.000 by end of 2017) will be reached ahead of time.

**2) Agenda outline for Bio.tools pre-meeting in Odense, August 23 2017 (JI, 10’)**

This is an open-day meeting for the bio.tools community and all are welcome. 

**Action:** JI will propose a draft agenda by May 5. 

**3) Bio.tools presentation at Odense Danish Bioinformatics Conference (JI, 5’)**

Yes, there should be a bio.tools presentation at the conference. The presentation could start by a general update by SB/JI on bio.tools achievements and ambitions, leading on to a talk on bio.tools’ scientific purpose: for example invite Magnus Palmblad to present case of using EDAM as basis for guided workflow composition. 

**Action:** JI & Veit to ensure time-slot on conference program (Rikke Stefansen) and once speaker list/titles are confirmed, to mature content of presentation in dialogue with SB.

**4) Update on bio.tools content #307: Bioinformatics Links Directory, 621 databases (Ahto Salumets, 5’)**

This was not covered, but Ahto reports from behind the scenes, that task is nearly completed.

**5) ‘Regate’ as means to harvest tools from local Galaxy servers – an option? Probable number of tools found? Timeline? (Hervé Menager, 5’)**

This was not covered.

**6) CONDA task proposal https://biotools.sifterapp.com/issues/100 , next steps (Dan S, 5’)**

Three student programmers have started.
First task is to create map of existing bio.tools ID’s to CONDA ID’s and identify un-matched entries in CONDA. The manual work associated with establishing links between CONDA ID’s and stable bio.tools ID’s must however await the nearly completed cleaning of the bio.tools ID list.
The CONDA task fits nicely with the biocontainers project (see `sifterapp 100 <https://biotools.sifterapp.com/issues/100 >`_
) a container package registry integration effort for container-ised tools found in e.g. dockr and CONDA. A studentship proposal describes in detail, what the CONDA task aims to achieve `here <https://docs.google.com/document/d/1w31T6w3j0JP7h2Ujp737RhiBcn-ywiBJ4VNGygdwAdY/edit#heading=h.ok40z7l1xy2h >`_

**7) WP-1 studentsships: new proposals (JI) and status of ongoing ones Proteomics tools annotation (Veit) and Utility to convert open-API configuration files to importable files (Herve) 15’)**

The work on the proteomics tools annotation is progressing well since it started 3 weeks ago.
Hervé could not attend this meeting due to a conflicting ELIXIR meeting. 
HansI and HH are recruiting on 3 studentships to assign publications on entries without a tool-specific publication or citation or proxy paper. Entries without any of the former curation will be subject to decision if to keep or delete from registry.
SB made the point that publications, alt-metrics, number of citations, de-duplications and consistent EDAM assignments, are key curation targets. In parallel, interface functionalities and search functions should be enabled on the development side, to make the most of this entry-information.

**Proposed action:** JI to please consider if ROADMAP reflects SB’s point above, and with what timeline, and share the plan on next SG meeting in June.

**8) AOB**

None.




2017, Mar 31 11 AM CEST
-----------------------

Attendees
^^^^^^^^^

Anne Wenzel, Emil Rydza, Hans Ienasescu, Jon Ison, Veit Schwämmle, Vivi Raundahl Gregersen, Salvador Capella-Gutierrez, Henriette Husum Bak-Jensen, Anders Halager, Dan Søndergård,Jaroslaw Kalinowski, Matus Kalas, Mikkel Schierup

Apologies 
^^^^^^^^^

Hervé Ménager, Vassilios Ioannidis

Agenda and Minutes
^^^^^^^^^^^^^^^^^^

**Ad 1) EXCELERATE WP 1 mid-term report (JI, 5 min).**
The 1st EXCELERATE WP1 periodic `report <http://tinyurl.com/WP1midterm2017>`_ was submitted on 31 march. It will be subject to scrutiny at the April mid-term ELIXIR review. The report is a reference document that compiles the work done so far on WP1. It is recommended reading for everyone involved on WP1, to get up to speed. 

**Ad 2) Urgency of bug fixes in preparation for a) EXCELERATE mid-term review, b) indexing of Tool Cards, c) in 2017 Q3 the “pivot to end users” (JI, 10 min).**

The DTU/KU team of Jon, Emil, Lukasz, and Piotr can handle the urgent tasks that needs doing before the mid-term review. We’re all encouraged to take a critical look at bio.tools and give feed-back via github on what we think is the most broken. Salva (ES) mentioned they will contribute a developer to this effort. On this note, please observe that github is the tracker for raising fine-grained issues/critique, while Sifter is used for high-level project management, while the `Roadmap <http://biotools.readthedocs.io/en/latest/changelog_roadmap.html>`_ addresses the question of ‘when’ planned bio.tools technical software development will happen.
**Action for JI**: to priority-label comments made in github in accordance priority-labelling used in sifter app (i.e. critical, high, normal, low, trivial) to acknowledge the community effort of raising issues in github.
Toolcards are about to be indexed in preparation for the coming ‘pivot to end-users’ task. 

**Ad 3) Introducing WP1 team from Aarhus Univ + options for WP1-EXCELERATE Milestone assignments (Mikkel Schierup, 10 min).**
A warm welcome to the WP1 team from AU, presented by Mikkel Schierup. The team is constituted by Anders Halager, Jaroslaw Kalinowski and Dan Søndergaard + three student programmers (10 hrs per week from April).

**CONDA task proposal (Dan Søndergaard and Anders Dannesboe)**
CONDA is ‘the standard’ open source software package manager. Bioconda is a ‘channel’ that already contains >3600 bioinformatics-related packages, that is maintained and expanded by a ‘serious’ open-source community (ContinuumIO). The AU-team proposes a task with the goal of making the maximum number of packages from bio.tools available as Conda packages, and distribute these via Bioconda. Furthermore, they propose to make Conda the official bio.tools approach for installing bio.tools curated software (i.e. bio.tools to inform/educate the end-user on how to install and update packages on different platforms via Conda/Bioconda). Several benefits could arise from such a collaboration including an improved search mechanism on bio.tools and improved understanding of end-users needs. Also, it would give bio.tools a competitive edge.
**Conclusion:** The idea is great, and should be written up as one or more studentship-like proposals (see next point) that also addresses the aspect of whether to include packages of single tools and workflows and the boundaries we then would share with parallel ELIXIR activities in the Biotools roadmap. **Action for JI and Dan** to shape project(s) via dialogue in `sifter task #100: Support pull of data from content providers <https://biotools.sifterapp.com/issues/100>`_.

**Sifter tasks proposals** The AU-WP1 team also proposed to contribute to sifter apps 240 (Expose bio.tools for indexing by Google), 106 (Enable sorting by citation rate matrics combined with recent citations somehow ) and 239 (field for content reviewed), which is warmly welcomed and much appreciated. 

**Ad 4) WP1-Studentships. Frame and how to apply for these + studentship proposals already made (HH+JI, 10 min).**

The Danish ELIXIR node has allocated funds for WP1-studentships. Only curation-focused mini-projects with a clear and quantifiable impact on bio.tools content will be considered for funding. In order to apply for a studentship, a one-page proposal must be written and submitted in accordance with the guidance found `here <https://github.com/bio-tools/Studentships>`_. Generally, a studentship is equivalent to maximum one month of full-time employment. Each project should target producing a mini publication and the project progress towards goals must be tracked in sifter. until now, two studentships have been granted with supervisors Veit Schwämmle (Proteomics tools annotation) and Hervé Menager (Utility to convert open-API configuration files to importable files), respectively. **Action point for Veit and Hervé:** please create sifter tracking for your studentships progress prior to next hangout.


**Ad 5) Recent discovery by Hans of ‘MyBioSoftware portal’ of 11.152 tools timeline for import to bio.tools (Tomas Racek/Jon Ison 5 min).""
Tomas Racek was invited with short notice, and could not join this call.** 
The discovery and work this far is described here `sifter task 356 <https://biotools.sifterapp.com/issues/356>`_. 

**Action for Jon and Tomas:** A timeline and work plan for importing the tools found in MyBioSoftware into bio.tools at standard annotation quality, is needed for the next hangout + the discovery of MyBioSoftware should be added to the monster list. **Action for HH:** The discovery calls for a revision of KPI targets.


**The remaining points could not be covered in time, and were postponed for the next hangout on April 28**






2017, Jan 27 11 AM CET
----------------------

Attendees
^^^^^^^^^

Anne Wenzel, Emil Rydza, Hans Ienasescu, Jon Ison, Veit Schwämmle, Vivi Raundahl Gregersen, Hervé Ménager, Kenzo Hugo, Anders Halager, Salvador Capella-Gutierrez, Henriette Husum Bak-Jensen, 



Thanks to everyone who managed to join this technically challenged meeting ! It seems that hangouts aren’t suitable for meetings of 10 participants or more, and so the next TC (Feb 24, 11:00 CET) will take place in another way (Action Henriette),

Please have a look at the revised (27/1 p.m.!) status report here `<http://biotools.readthedocs.io/en/latest/status_reports.html <http://>`_ 

 


Agenda and Minutes
^^^^^^^^^^^^^^^^^^

**Ad 1) Hackathon at Aarhus University Feb 2-3 2017: Outstanding issues (Vivi Gregersen) 10 min**

Currently 15 people have signed up to this hackathon, everyone is welcome to attend and can study the program AND register here https://docs.google.com/document/d/1tVemqzmus8BpQxfPZRmh5PGmIe64F9a72OKmPhfz1sk/edit#heading=h.p1b4r4t4pje3 
Jon will share a spreadsheet template with Vivi, to help define conceptual workflows, relevant tools and annotation (Action Jon)
Hans will demonstrate the Tool Annotator as requested – Jon should give directions to Hans as to timing and duration of this (Action Jon).

**Ad 2) Status on RTH - RNA tools (Anne Wenzel) 5 min** 

The upload of ~400 tools that were scheduled for end 2016 has been paused by RTH. This is due to concerns from RTH, as to how the ontology helps in finding the right tools, caused both by limitations in search function support and a non-implemented EDAM ontology extension that RTH plan to do. Anne, Emil and Jon will address these concerns off-line, update the list of critique points to address re: registry developments here https://biotools.sifterapp.com/issues/317 and identify a new plan for uploading the tools, involving Jan Gorodkin (Action Anne).


**Ad 3) Tool Annotator – status (Hans Ienasescu) 10 min**

The Tool Annotator is currently not integrated with bio.tools but it will be after user feed-back on the current version, at the hackathon in Aarhus Feb 2-3. Here the participants will compare and critique the difference in annotating using the Tool annotator, the bioportal and the current function in bio.tools and Hans will harvest the best modus and upgrade the Tool Annotator accordingly – and then settle on a plan, with Emil, Jon, to integrate it with bio.tools (Action Hans)


**Ad 4) Experience from Proteomics workshop Bio.tools outreach  (Veit Schwämmle) 10 min** 

Approximately 30 people attended the workshop. These were both Ph.D. students, postdocs and senior researchers. The main outcome was outreach i.e. to introduce ELIXIR and the bio.tools registry to the proteomics community. Another outcome was to define workflows in proteomics analysis, which is useful not only to the registry but also to the ELIXIR training platform, who attended as well (Niall Beard). The event could not have taken place without the ELIXIR-DK financial support, which was a little hard to come by. ELIXIR DK would benefit from an operational strategy that lowers the bar on resource decisions and executing these (Action Henriette).

**Ad 5) Highlights from ‘User feedback from the UI tests’ see here  (Kenzo Hugo Hillion) 10 min**

Several constructive points of critique were raised by the report. Salva also raised important points at this meeting. Jon and Emil are grateful for this helpful critique and kindly request these be noted in the sifter task here https://biotools.sifterapp.com/issues/317 where they will action them (i.e. link them with the roadmap) and solve them as soon as possible/feasible. Again – everyone is welcome (and needed) to help solve these issues – please coordinate with Jon, Emil. 

**Ad 6) Access to the code repository (Hervé Ménager) 10 min**

As a solution to some of the remaining software-level issues of bio.tools, HM and KHH have requested an access to the code repository for bio.tools. That would potentially enable to provide quickly corrections to some of the interface bugs for instance. JI would also like to get this access, in order to contribute to tasks such as QC. ER will provide this ASAP (week of jan. 30th). 

**Ad 7) New curator in DK (yea!) – roles and tasks, inspirational 5 min**

Hans Ienasescu has been hired at UCPH, Bioinformatics Centre, for 1 year as of Feb 15, 2017 as a full-time registry curator. Due to time constraints, this point has been postponed for the next meeting.

**Ad 8) AOB**
None





2016, Nov 25 11 AM CET
----------------------

Attendees
^^^^^^^^^
Anne Wenzel, Emil Rydza, Vivi Gregersen, Henriette Husum, Josep, Emil Rydza, Hervé Manager, Hans Ienasescu, Kenzo Hillion, Josep Gelpi, Vivi Gregersen, Henriette Husum


Apologies
^^^^^^^^^
Anders Dannesboe, Lukasz Berger, Jon Ison, Veit Schwämmle, Piotr Chmura, Christian Anthon


Our current primary focus is content, the secondary focus being quality of the content in bio.tools 
Current #entries 2664 
# affiliations 145. 
2016-Q4 target is 5000 entries.


Agenda / Minutes:
^^^^^^^^^^^^^^^^^
**Ad 1) Welcome everyone - especially to Hervé, Kenzo and Josep - brief sharing of plans regarding content expansion and more**
Kenzo joined Hervé’s team recently and will be focusing on the workbench integration enabler component for e.g. galaxy. 
Content-wise, Kenzo will be loading ~30 highly curated entries authored by Institute Pasteur on to Bio.tools and sponsor community engagement. 
Kenzo wishes to contribute to software development and is invited to do so by e-mail to registry-support@elixir-dk.org (John Ison, Emil Rydza, Lukasz Berger, Peter Løngren) in the first instance, with an option to set up a more formal structure if necessary.


**Ad 2) KPI monitoring: entry growth curve and contributors growth curve #72 (Emil Rydza, 2016-Q4)**

Good progress: The two curves have been constructed and will be made visible in November, here https://bio.tools/stats 

We will consider posting other statistics e.g. growth in number of users and number of views, when we launch the registry to enable community engagement.

**Ad 3) Settle on 'minimum information for content import to staging area #293' - any further input? (Henriette)**

We confirmed the following as the minimum information:

- Name
- Homepage
- Description
- EDAM Topic/descriptors

Additional information will be welcome but given default values i.e. not necessary/possible to fill in:

- Publications
- Type of service

**ADDENDUM Jon Ison 28/11/16**

Concerning the minimum information requirement for "beta" entries, see https://github.com/bio-tools/biotoolsSchema#information-requirements:

- name 
- toolID
- homepage
- description
- tool type
- topic
- function

topic and function can be assigned semi-automatically using `edamMap <https://github.com/edamontology/edammap>`_ and could default to "Topic" and "Operation" if necessary (undesirable).

All entries labelled as "beta" initially until manually inspected.  

ACTION: Jon & Emil to firm up validation / inforrmation requirement for labelling ("beta", "standard", "validated" etc.)

# end of addendnum

  
Anders Dannesboe is assuming a new position on Dec 1 and is nearly done with a script to transfer spreadsheets including tools for mass-import to XML - Anders will handover this task to be finalised/implemented by Jon and Hans for task #107. 

Jon should please close task 293 and release full steam on task #107 

**Ad 4) Status and plans concerning implementation of the staging area for mass-import and 'easy' community-driven content expansion #107 (Emil Rydza, 2017-Q1)** 

Not discussed in absence of John. It’s not clear if John or Emil is leading this critical task – please clarify between you.

**Ad 5) RNA tools upload progress #62 and  (Anne, Q4-2016)**

On track. 380 tools expected to be loaded onto bio.tools. Anne will discuss the RNA ontology list with Josep.

**Ad 6) MBG proposal for Bio.tools hackathon on crop and wild-stock tools and databases #178 (Vivi, milestone not assigned)**

The date for this hackathon has been settled for 2.-3. February 2017 and will take place in Aarhus, Denmark. Henriette will look for budget coverage. Vivi and colleagues will continue to work to specify the conceptual workflows involved. 

**Ad 7) Issues on settled milestones - needs for revision ? (all)**

None

**Ad 8). Carry forward input concerning upcoming WP1/ELIXIR-DK partners TC on Dec 2nd at 10 a.m. UK / 11 a.m. DK**

None

**Ad 9) AOB**

None


**Next meeting will take place on January 27, 2017 (as December 30 is cancelled)** 



2016, Oct 26 11 AM CET
----------------------

Attendees
^^^^^^^^^
Anne Wenzel, Emil Rydza, Hans Ienasescu, Jon Ison, Veit S,Vivi Gregersen, Henriette Husum

Apologies
^^^^^^^^^
Anders Dannesboe, Christian Anthon, Lukasz Berger, Piotr Chmura

Agenda / Minutes:
^^^^^^^^^^^^^^^^^


**Ad 1) Plan for bio.tools content expansion (Jon Ison)**

We currently have ~2700 entries in bio.tools and - assuming additions in 2016 Q4 occur as scheduled - are about on track with the registry growth targets in the `top down plan <https://docs.google.com/document/d/1AM0iLimpT4ClybEKYYdWu52RzJ9GKqUpW2DZflS6_4c/edit>`_
which are:

- 2016 Q4 5000 entries
- 2017 Q1 6250 entries
- 2017 Q2 7500 entries
- 2017 Q3 8750 entries
- 2017 Q4 10000 entries

In the current phase, the primary focus is content, the secondary focus being quality of the content. With this in mind, we decided on two tasks:

**Task 1: Mass-import - (assigned to Emil & Jon to complete by Q1-2017):**

a) to define the minimum information required for a bio.tools mass-import that would result in a ‘beta-version’ entry in bio.tools.
   
b) to device a technical solution to implement this task.

c) to identify candidate collections suitable for import en masse

d) Immediate action: Emil and Jon to track this task in sifter.

Jon Ison note (1/11/2016)

- https://biotools.sifterapp.com/issues/107
- https://biotools.sifterapp.com/issues/107
- https://biotools.sifterapp.com/issues/295
  
**Criteria for mass-import task solution:**

- Minimum information includes at least Name; website; short description; EDAM descriptors

- The author/owner of the mass-imported tool must be notified by e-mail upon mass-import with guidance to qualify the content to production version.



**Task 2: Student helper – minimal annotation (assigned to Veit to complete with Jon by Q4-2016):**

a) to revisit the idea of minimal annotation of bio.tools content and define the minimum information required for a beta-version entry to upgrade to production version.

b) to write an instruction for student helpers (and for authors/owners see mass-import task) to perform the required annotation.

c) to present a plan for distributing the annotation task by student helpers across the Danish partners.

d) immediate action: Veit and Jon to track this task in sifter


Jon Ison note (1/11/2016)

- https://biotools.sifterapp.com/issues/294


**Ad 2) Sifter app tasks: Are milestones set - questions in this regard (All)**


Milestones for all sifter app tasks (except IDEAS) should be assigned and agreed on Jon Ison. Please keep an eye on your milestones and report at hangout meetings, if you want to change the assigned milestone.

**Ad 3) MBG proposal for bio.tools hackathon on crop and wild-stock tools and databases (Vivi)**

MBG wishes to host an international hackathon in w5 or w 11, 2017, which is great. We will discuss the concrete plans at the next hangout meeting on Nov 25. For that, Vivi will reach out to relevant others and

- define the conceptual workflows for research in the field, which will help to form work-groups at the hackathon, to develop EDAM ontology, as well as expand the list of tools/databases for import, which currently counts ~250 entries. Practically, up to 50 people can attend the event. -

- settle the date for the event by doodle to the registry core list, EDAM core list and this forum.

- settle the location for the event (which could be co-located to other relevant scientific event)

- draft a budget outline for the event


**Ad 4) RNA tools upload progress and emerged EDAM ontology issues (Anne)**

The plan to upload ~400 RNA tools in 2016 is on track. EDAM ontology challenges have emerged, as pointed out by Jan and Anne by email/progress report. 
Jon mentioned the opportunity to use synonyms for semantic enrichment of the EDAM ontology, and that some keywords can go to ‘operations’. Anne should send the ontology suggestions to Jon I, who will help making the EDAM vocabulary match the need from RNA tools field.

**Ad 5) AOB**
no issues were discussed.


2016 Sep 30 11 AM CET
---------------------

Attendeees
^^^^^^^^^^
Anders Dannesboe; Christian Anthon; Lukasz Berger; Emil Rydza; Jon Ison, Henriette Husum

Agenda / Minutes
^^^^^^^^^^^^^^^^
We deviated from the agenda and focused on the main issue raised by Jon : bio.tools content growth must happen faster. More tools and databases need to be loaded to bio.tools and this must be a critical focus until 1) we are on track with it and 2) practical content growth plan that has been endorsed by the Steering Group. To this end - we will consider the following actions to gear sifterapp:

- complete "top down" anaylsis of curation requirements + ELIXIR EXCELERATE WP1 deliverables and milestones due in 2017 (Jon)
- firm-up practical KPIs, metrics for assesment and propose sensible targets.  Map upload targets for WP1 partners & Danish Elixir DK satellite partners (Jon & Henriette)
- map requirements (curation and for milestone & deliverables) to available resources in DK + WP1 partners (Jon in 1st instance) 
- assign milestones (i.e. month-year completion needs) to all sifter tasks in "bio.tools content" tracker, this should reflect upload targets for WP1 partners & Danish Elixir DK satellite partners (Jon in 1st instance)
- clarify purpose of planned 'events' and how these each relate to KPI growth (Jon & Henriette)
- prioritise tooling that is essential for content growth, notably the 'moderation interface' (for mass content imports), 'sandbox' functionality (for intermediate registrations) and tool annotator
- organise a f2f meeting for the DK technical group and WP1 partners : 'content growth tactics' sign-off meeting early December 2016, coinciding with the big release (Jon & Henriette)

Henriette and Jon will continue the discussion off-line and come back by email.

Our next meeting is 28 October 2016 from 11:00 DK-time.


2016 July 1 11 AM CET
---------------------

Call details
^^^^^^^^^^^^
Hangouts - Jon initiates

Attendeees
^^^^^^^^^^

Jon, Henriette, Veit, Anders

Agenda
^^^^^^
1) *TASKS* : round-robin catch-up, people say what sifterapp they're working on, asking for help on tasks, reassignment of tasks, etc.
2) *FOCUS* : one person leads a presentation and discussions on a specific point.
3) *STATUS* : people are asked to review the Status Report http://biotools.readthedocs.io/en/latest/status_reports.html before the meeting and bring any points for discussion here, including points from partner institutions.
4) *PRIORITIES* : people are asked to review current priorities on sifterapp, for discussion here.
5) *EVENTS & DEADLINES* : people are asked to bring up items to be actioned in sifter 
6) *KPIs* (Emil): Track status of key performance indicators from https://bio.tools/stats. *User accounts* (affiliations); *Recurrent users* (recorded?); *Entries*; *Content changes/edits* (recorded?); *Publications* (bio.tools technical progress - ideas for future publications  - what's in progress (sifterapp)
7) *Update on agreed actions* :*Action* Henriette will contact Bernt Guldbrandsen for a representative from AU, QCG for the next meeting (DONE, see Ad 1 below)
8) *What else?* -Program for DKBC pre-meeting/hackathon in Odense (Jon)

Minutes
^^^^^^^
Ad 1) JI has made posters on ELIXIR, ELIXIR-DK, Computerome, Bio.tools to be presented at ISMB, ECCB, DK-BiC and more. Action: JI to please share the posters with the ELIXIR-DK partners and this forum. HH suggests ELIXIR-DK to define national strategy, including sub-strategy for Training and Outreach (Bio.tools-centered strategy for 1) Training Developers, 2) Training strategic segments of end-users in select tools and databases 3) Web-site communication of Danish training events and opportunities. Action: HH to raise issue at next Steering Group meeting (Sept 20th-2016) and to first get input from this forum at the 24 August technical meeting, Odense.

Ad 8) The Elixir Bio.tools OPEN DAY meeting will take place on August 24, the day before the DKBiC meeting. The agenda is found here https://docs.google.com/document/d/1srFDJF43yPGphP8j11DgseiTkaxs7pHeAcj2WyfzH34/edit#  and JI will advertise the meeting broadly, with a reminder to register themselves on a doodle.
Ad 8) Next two hangouts (end July and August) are cancelled due to holidays and the Open Day meeting, so we will have the next hangout meeting on Friday September 30th. 




2016 May 27 11AM CET
-------------------- 

Call details
^^^^^^^^^^^^
Hangouts - Jon initiates

Attendeees
^^^^^^^^^^
Veit S, Anne W, José Maria F, Emil R, Maria Maddalena S, Myhanh N, Jon I, Hans I, Henriette H,
apologies from Anders Dannesboe

Agenda
^^^^^^
1) *TASKS* : round-robin catch-up, people say what sifterapp they're working on, asking for help on tasks, reassignment of tasks, etc.
2) *FOCUS* : one person leads a presentation and discussions on a specific point.
3) *STATUS* : people are asked to review the Status Report http://biotools.readthedocs.io/en/latest/status_reports.html before the meeting and bring any points for discussion here, including points from partner institutions.
4) *PRIORITIES* : people are asked to review current priorities on sifterapp, for discussion here.
5) *EVENTS & DEADLINES* : people are asked to bring up items to be actioned in sifter 
6) *KPIs* : Track status of key performance indicators from https://bio.tools/stats  *User accounts* (affiliations); *Recurrent users* (recorded?); *Entries*; *Content changes/edits* (recorded?); *Publications* (bio.tools technical progress - ideas for future publications  - what's in progress (sifterapp)
7) *Update on agreed actions* : *Action* Henriette will contact Bernt Guldbrandsen for a representative from AU, QCG for the next meeting (DONE, see Ad 1 below) *Action* Maria Maddalena should please send the deadlines + events weekly alert to this quorum from now on. DONE.
8) *What else?*

Minutes
^^^^^^^
Ad 1) 
Outreach to TESS (sifter 140, Henriette): Henriette is helping organise a workshop (Fall, 2016) between Bio.tools and TeSS on how to enable cross-links between the two ressources. 

MBG partner involvement (sifter 178, Henriette): Bernt Guldbrandsen will shortly assign a technical member to help the bio.tools expansion (wild stock and plant breeding) and to participate in our meetings.

Training platform (sifter 141, Henriette): It will be valuable to understand which E-learning ressources (online files, videos, slide decks etc) are available from the satellites. Henriette will ask this information from everyone. Hans I is willing to help make a video tutorial on 'how to load tools into Bio.tools' or 'how to get started, using COMPUTEROME'.

Anne Wenzel is in the process of loading 400 RNA-bioinformatics tools onto Bio.tools, and to adjust EDAM ontology accordingly.

Text mining tool (sifter 99, name edamMap, Veit and Jon): This project uses text mining of software descriptions/abstracts/full texts to extract associated EDAM terms. Among other applications, the results can be used for automatic tool annotation.

Workflow generation (sifter 119, Veit and Jon): EDAM provides powerful information to create pipelines for e.g. data analysis involving multiple tools. The study shows how to find applicable pipelines and presents several use cases for the analysis of mass spectrometry data. The work will be presented at ASMS 2016 (mass spectrometry conference) and a paper draft is being prepared.

EDAM Tool Annotator (sifter 46): Improved annotation of tools using EDAM terms. The tool aims to peform a "smart" term search and picking on EDAM in the effort to provide the best exisiting tool annotations; alternatively term suggestions will also be available

Tools used by ELIXIR trainers (sifter 60): finish curration for high-value tools to trainers.

Ad 2) No volunteer today. But great opportunity if needing input/bounce off idea
Ad 3) Credits to Emil for expanding the bio.tools statistics to comprise more parameters. The report could perhaps be made to contain the 'priority' dimension (Henriette and Jon to liase before the meeting, about this)
ad 4) Not done. We really should.
ad 5) Not covered, due to time pressure.
ad 6) Henriette will contact Emil about KPIs and tracking these


2016 April 29 11AM CET
---------------------- 

Call details
^^^^^^^^^^^^
tbd

Attendeees
^^^^^^^^^^

Agenda
^^^^^^
1. Scope & purpose of these hangouts
2. Format

   - *Google hangout ?*
   - *skype ?*

3. Quorum 

   - *formal or informal ?*
4. Fixed agenda items

   - discussion of bio.tools status report (Emil and Jon will publish, on the last Thu of each month) including status on key performance indicators:

    - #User accounts
    - #Entries
    - #Content changes/edits
    - #Publications on technical progress
   
   - forthcoming deadlines
   
   - forthcoming events

     - ECCB2016 3-7 Sept 2016
     - ELIXIR-DK technical get-together and bio.tools workshop in one event 24. August 2016
   
   - *what else ?*

Minutes
^^^^^^^
Ad 1) These hangouts should have a practical focus (defined by fixed agenda items) but in-depth technical discussions should be taken elsewhere. We agreed on a set of fixed agenda items, see under 4.

Ad 2) Google hangout worked well today, and we will use this going forward.

Ad 3) All DK partners are expected to provide a representative to these meetings. Currently, we don't expect representatives from industry partners.


Ad 4) 
The fixed agenda items were agreed to be the following:
1) *TASKS* : round-robin catch-up, people say what sifterapp they're working on, asking for help on tasks, reassignment of tasks, etc.
2) *FOCUS* : one person leads a presentation and discussions on a specific point.
3) *STATUS* : people are asked to review the Status Report before the meeting and bring any points for discussion here, including points from partner institutions.
4) *PRIORITIES* : people are asked to review current priorities on sifterapp, for discussion here.
5) *EVENTS & DEADLINES* : people are asked to bring up items to be actioned -> sifter 
6) *KPI's* : Track status of key performance indicators from https://bio.tools/stats 

The fixed agenda items will enable the hangouts to serve three overall purposes
1) To surface if Elixir-DK activities are progressing as planned, and if not, what changes/resources are needed? 
2) To surface information/results (from Elixir-HUB, -events, -meetings) that need to go to the DK-partners or to the HUB. 
3) The meetings serve as a feeder for Elixir-DK Steering group meetings, and similarly, activities/decisions from the Elixir-DK Steering group can be channeled to the agenda of the hangout meetings

Today's actions were:
*Action* Henriette will contact Bernt Guldbrandsen for a representative from AU, QCG for the next meeting (ad 3)
*Action* Maria Maddalena should please send the deadlines + events weekly alert to this quorum from now on (ad 4)

Today's KPI records were:
#User accounts (affiliations) = 262
#Recurrent users = not sure (not recorded?)
#Entries = 2403
#Content changes/edits = not sure (not recorded?)
#Publications : bio.tools technical progress - ideas for future publications  - what's in progress (sifterapp)








