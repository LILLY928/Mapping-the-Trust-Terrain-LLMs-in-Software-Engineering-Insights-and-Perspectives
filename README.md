# Overview
This repository contains the data and code for the paper: _Mapping the Trust Terrain: LLMs in Software Engineering - Insights and Perspectives_. In this work, we aimed to understand how trust is defined, conceptualized, and measured in the context of using LLMs for SE. To this end, we first conducted a systematic literature review of 18 related papers from Software Engineering, Deep Learning, and Human-Computer Interaction to understand the current research status on trust concepts. We then surveyed 25 domain experts to understand practitioners' perceptions of trust.

This repository contains all of our data to facilitate reproducibility and to encourage contributions from the community to promote trust in LLMs in SE.

# Systematic Literature Review
We conducted a systematic literature review (SLR) following the approach by [Kitchenham et al.](https://dl.acm.org/doi/10.1145/2372233.2372235). Before starting the review process, we developed research questions (RQs) according to Kitchenham's guidelines. This helped us systematically identify papers relevant to our research goals. We then performed the following steps: 

1. [Search for Primary Studies](#sfps)
2. [Screening](#screening)

   2.a. [Filter by Title](#fbt)

   2.b. [Filter by Abstract](#fba)

   2.c. [Full-text Screening](#fs)
4. [Snowballing and Manual Addition](#snowballing)
5. [Data Extraction and Analysis](#deaa)

The two authors conducted each step in this process independently and met after each step to ensure alignment and resolve any differences. The third author was consulted as needed to help settle any disputes. The image below provides a visual representation of our complete pipeline. A detailed record of each step can be found in `Number Record.xlsx`.
![Pipeline for Survey](./Literature%20Review/Pipeline%20for%20Survey.png)

## Search for Primary Studies <a name="sfps"></a>
We focused on the period from January 1st, 2002 to November 1st, 2024, the time when we started our search. We chose 2002 as our starting period because this was when the method to model language using feed-forward neural networks was published by [Bengio et al.](https://proceedings.neurips.cc/paper_files/paper/2000/file/728f206c2a01bf572b5940d7d9a8fa4c-Paper.pdf). We then identified major venues in SE, Machine Learning, HCI, and DL that align with our research goals.

We considered the ACM Digital Library, IEEE Xplore, Springer Link, Google Scholar, and DBLP. We then formulated a search string to query these databases. We considered various combinations of search strings to get the best results. The search string `(“trust” OR “distrust” OR “trustworthiness”) AND (“SE” OR “Software Engineering”
OR “Software Development” OR “Code Generation” OR “Program Repair” OR "Automatic Program
Repair" OR “Software Testing” OR “Test Generation”) AND (“LLM” OR “Large Language Model” OR
“LLMs” OR “Large Language Models” OR “Deep Learning” OR “Machine Learning”)` worked best for us. Adding `"SE"` or `"Software Engineering"` to our search query helped return only relevant papers from DL-based venues while also not excluding any papers from SE venues.

We used different mechanisms to query each database. For IEEE Xplore, we used its advanced search feature to filter by date and venues and used their website to export the results as an Excel sheet. However, the ACM Digital Library does not have an export feature; thus, we wrote a simple Python program to query using a REST API and appropriate filters. After searching the databases with the specified search strings, we identified **4,472** potentially relevant papers.

The scripts and results related to the primary search can be found in the `1.Search for Primary Studies` folder.

## Screening <a name="screening"></a>

### Filter by Title <a name="fbt"></a>
 We selected all search results by reviewing the title first. In this step, any
papers with titles that contained keywords "trust" OR "distrust" OR "trustworthiness" OR "SE"
OR "Software Engineering" OR "Software Development" OR "Code Generation" OR "Program
Repair" OR "Automatic Program Repair" OR "Software Testing" OR "Test Generation" OR "LLM"
OR "Large Language Model" OR "LLMs" OR "Large Language Models" OR "Deep Learning" OR
"Machine Learning" were considered for further screening. We kept all these keywords to
ensure that we did not lose any relevant papers. We were left with **3,186** papers for further
screening from this step.

The scripts and results related to the title filtering can be found in the `2.Screening/2a.Filter by Title` folder.

### Filter by Abstract <a name="fba"></a>
Filtering by abstract was a manual effort conducted by two authors of this paper. The abstracts were systematically analyzed to confirm their relevance to our research goals. Papers that contained some indication of trust or trust-related concepts were included in this step. Specifically, if the abstract was related to trust in the context of using LLMs for SE, the papers were included for the next steps in the pipeline. From this step, we filtered out **3,163** papers, leaving us with **23** papers.

The results related to the abstract filtering can be found in `2.Screening/2b.Filter by Abstract.xlsx`.

### Full-text Screening <a name="fs"></a>
We carefully reviewed the **23** papers that passed the abstract filtering process to determine their final inclusion in our study. Papers that were at the intersection of trust-related concepts, SE, and LLMs were considered for the next steps of our literature review. From this step, we filtered out **11** papers, leaving us with **12** papers.

The results related to the full-text screening can be found in `2.Screening/2c.Full-text Screening.xlsx`.

## Snowballing and Manual Addition <a name="snowballing"></a>
To account for studies that we might have missed with our primary search keywords, we performed snowballing on the studies that met our inclusion criteria. We reviewed every reference cited by the selected papers.

The references were subjected to the same rigorous inclusion criteria as the original studies. We first screened them by title and then by abstract. Through this snowballing process, we identified and included an additional **6** papers.

Despite thorough efforts to locate further relevant research, no additional papers were identified through manual searching.

The results related to the snowballing can be found in the `3.Snowballing` folder.

## Data Extraction and Analysis <a name="deaa"></a>
We iteratively reviewed the **18** collected papers to gather both general and specific information relevant to our RQs, following protocols suggested by [Levett et al.](https://guides.himmelfarb.gwu.edu/systematic_review/data-extraction). We created a dataset with the following data: authors, year of publication, RQs proposed, methodology, study population and characteristics (for user studies), definitions of trust, consequences of trust, the importance of trust, antecedents of trust, and metrics used for trust.

Both authors worked independently to extract information and populate the dataset. Any discrepancies were discussed with the third author. In the end, we achieved a high Inter-Rater Reliability (IRR), with a Cohen's kappa (κ) coefficient of 0.824.

The results related to the data extraction and analysis can be found in the `4.Data Extraction and Analysis` folder.

# Survey Study

Upon approval from our Institutional Review Board (IRB), we conducted a survey study to investigate practitioners' perceptions of trust-related concepts when using LLMs for SE tasks. Specifically, we explored definitions of trust, its antecedents, and metrics, complementing our systematic literature review with insights from both expert and novice practitioners. We employed [purposive sampling](https://link.springer.com/article/10.1007/s10664-021-10072-8) to reach practitioners with varying levels of SE and machine learning expertise, including industry experts, researchers, students, and software engineers. Participation was voluntary with no incentives offered, and participants were informed of the voluntary nature of the study during solicitation.

* [Survey Structure](#survey-structure)
* [Participant Demographics](#participant-demographics)
* [Qualitative Metrics](#qualitative-metrics)
* [Trust Antecedents Selection](#trust-antecedents-selection)
* [Data Collection](#data-collection)
* [Survey Validity](#survey-validity)

## Survey Structure <a name="survey-structure"></a>

The survey consists of four sections, detailed below:

* _Section 1_ assesses the practitioner's familiarity with using LLMs for various SE tasks. It qualifies practitioners for the rest of the survey, ensuring valid feedback by excluding those who have never used LLMs for the subsequent tasks.
* _Section 2_ includes blocks of questions investigating practitioners' insights into trust-related concepts in Test Case Generation, Code Generation, and Program Repair. Blocks are presented in random order to avoid bias. Each block covers trust definitions, antecedents, and metrics. Only practitioners with experience in using LLMs for these tasks answer these questions.
* _Section 3_ captures general perceptions of the importance of trust, the desired metrics for trust, and whether practitioners value the significance of these topics.
* _Section 4_ collects demographic information about participants, such as sex, job title, and years of experience. The data is used to categorize trust-related concepts by expertise during data analysis.

The original responses captured from the survey study are documented in `Survey Responses Raw Data from Qualtrics.csv`. Our coding of the free-response questions can be found in the `Open-ended Qs Coding` folder.

## Participant Demographics <a name="participant-demographics"></a>

The table below presents the demographic characteristics of the 25 participants who completed the survey. The majority of participants were between 25–34 years of age, most identified as male, and the majority reported having graduate or professional degrees. Participants represented a mix of students, researchers, engineers, and professors.

| Characteristic        | Category                                      | n  | %     |
|-----------------------|-----------------------------------------------|----|-------|
| Age                   | 18–24                                         | 4  | 16.0  |
|                       | 25–34                                         | 17 | 68.0  |
|                       | 35–44                                         | 3  | 12.0  |
|                       | 55–64                                         | 1  | 4.0   |
|                       | **Total**                                     | 25 |  |
| Sex / Gender          | Male                                          | 19 | 76.0  |
|                       | Female                                        | 5  | 20.0  |
|                       | Non-binary                                    | 1  | 4.0   |
|                       | **Total**                                     | 25 |  |
| Hispanic / Latino     | None of these                                 | 25 | 100.0 |
|                       | **Total**                                     | 25 |  |
| Race / Ethnicity      | Asian                                         | 15 | 60.0  |
|                       | White                                         | 6  | 24.0  |
|                       | Prefer not to answer                          | 2  | 8.0   |
|                       | Native Hawaiian or Pacific Islander + White   | 1  | 4.0   |
|                       | Black or African American                     | 1  | 4.0   |
|                       | **Total**                                     | 25 |  |
| Education             | Graduate or professional degree               | 15 | 60.0  |
|                       | Bachelor’s degree                             | 9  | 36.0  |
|                       | High school diploma or equivalent             | 1  | 4.0   |
|                       | **Total**                                     | 25 |  |
| Job Title             | Student                                       | 10 | 40.0  |
|                       | Researcher                                    | 5  | 20.0  |
|                       | Engineer                                      | 4  | 16.0  |
|                       | Professor                                     | 3  | 12.0  |
|                       | Freelancer                                    | 1  | 4.0   |
|                       | Other                                         | 1  | 4.0   |
|                       | Manager                                       | 1  | 4.0   |
|                       | **Total**                                     | 25 |  |


## Qualitative Metrics <a name="qualitative-metrics"></a>

We derived survey metrics based on our SLR to complement it with participants' perceptions. We captured trust definitions, antecedents, and metrics.

* _Definition_: We asked practitioners with experience in using LLMs for specific tasks to define trust in code generation, test-case generation, and program repair.
* _Antecedents of Trust_: We gathered practitioners' views on useful trust antecedents for specific downstream SE tasks. This metric allows us to investigate whether trust antecedents are consistent across different tasks.
* _Trust Metrics_: We collected information on how practitioners measure trust in specific tasks through open-ended questions. This helped us compare practitioners' trust measurement methods with those in the literature. We also inquired about their code review processes for both human-written and LLM-generated code to identify similarities and differences.

The organization of survey questions according to our research questions can be found in `Survey Questions Organized by RQs.xlsx`.

## Trust Antecedents Selection <a name="trust-antecedents-selection"></a>

The survey asked participants to select trust antecedents for each downstream task. We identified model-related and community-related attributes from SE, HCI, and ML literature. One author compiled all the documented antecedents, and then two authors independently categorized them, resolving disagreements through discussion. We selected the nine most popular antecedents for our survey, allowing participants to add any additional ones not originally listed.

More detailed documentation of the trust antecedents we extracted can be found in `Trust factor source.xlsx`.

## Data Collection <a name="data-collection"></a>

We reached out to **96** potential participants with varying expertise and from different backgrounds, who were not involved in or aware of the purpose of this work. Of these, **48** participants completed the survey. However, we discarded the responses from **23** participants due to incomplete or poor-quality answers, leaving **25** valid responses. The study was conducted using Qualtrics.

## Survey Validity <a name="survey-validity"></a>

To enhance the validity of our survey, we conducted two pilot studies: the first with **5** participants and the second with **2** participants who were not invited to the main survey. Based on the results of these pilot studies, we eliminated leading questions, corrected minor errors, and made improvements to our trust antecedents selection. Our survey study was also informed by findings from our literature review. Additionally, data analysis for the survey was independently conducted by two of the authors to minimize bias and human error.
