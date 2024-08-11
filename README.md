# Overview
This repository contains the data and code for the paper: _Mapping the Trust Terrain: LLMs in Software Engineering - Insights and Perspectives_. In this work, we aimed to understand how trust is defined, conceptualized, and measured in the context of using LLMs for SE. To this end, we first conducted a systematic literature review of 14 related papers from Software Engineering, Deep Learning, and Human-Computer Interaction to understand the current research status on trust concepts. We then surveyed 25 domain experts to understand practitioners' perceptions of trust.

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

The two authors conducted each step in this process independently and met after each step to ensure alignment and resolve any differences. The third author was consulted as needed to help settle any disputes. 

## Search for Primary Studies <a name="sfps"></a>
We focused on the period from January 1st, 2002 to February 1st, 2024, the time when we started our search. We chose 2002 as our starting period because this was when the method to model language using feed-forward neural networks was published by [Bengio et al.](https://proceedings.neurips.cc/paper_files/paper/2000/file/728f206c2a01bf572b5940d7d9a8fa4c-Paper.pdf). We then identified major venues in SE, Machine Learning, HCI, and DL that align with our research goals.

We considered the ACM Digital Library, IEEE Xplore, Springer Link, Google Scholar, and DBLP. We then formulated a search string to query these databases. We considered various combinations of search strings to get the best results. The search string `("trust" OR "distrust" OR "trustworthiness") AND ("SE" OR "Software Engineering") AND ("LLM" OR "Large Language Model" OR "LLMs" OR "Large Language Models" OR "Deep Learning" OR "Machine Learning")` worked best for us. Adding `"SE"` or `"Software Engineering"` to our search query helped return only relevant papers from DL-based venues while also not excluding any papers from SE venues.

We used different mechanisms to query each database. For IEEE Xplore, we used its advanced search feature to filter by date and venues and used their website to export the results as an Excel sheet. However, the ACM Digital Library does not have an export feature; thus, we wrote a simple Python program to query using a REST API and appropriate filters. After searching the databases with the specified search strings, we identified **4,143** potentially relevant papers.

The scripts and results related to the primary search can be found in the `1.Search for Primary Studies` folder.

## Screening <a name="screening"></a>

### Filter by Title <a name="fbt"></a>
We screened all search results by reviewing the titles first. In this step, any papers with titles containing the keywords `"trust"`, `"distrust"`, `"trustworthiness"`, `"Software Engineering"`, `"SE"`, `"Large Language Model"`, `"LLM"`, `"Deep Learning"`, or `"Machine Learning"` were considered for further screening. We included all of these keywords to ensure that we did not exclude any relevant papers. We were left with **1,125** papers for further screening after this step.

The scripts and results related to the title filtering can be found in the `2.Screening/2a.Filter by Title` folder.

### Filter by Abstract <a name="fba"></a>
Filtering by abstract was a manual effort conducted by two authors of this paper. The abstracts were systematically analyzed to confirm their relevance to our research goals. Papers that contained some indication of trust or trust-related concepts were included in this step. Specifically, if the abstract was related to trust in the context of using LLMs for SE, the papers were included for the next steps in the pipeline. From this step, we filtered out **1,105** papers, leaving us with **20** papers.

The results related to the abstract filtering can be found in `2.Screening/2b.Filter by Abstract.xlsx`.

### Full-text Screening <a name="fs"></a>
We carefully reviewed the **20** papers that passed the abstract filtering process to determine their final inclusion in our study. Papers that were at the intersection of trust-related concepts, SE, and LLMs were considered for the next steps of our literature review. From this step, we filtered out **11** papers, leaving us with **9** papers.

The results related to the full-text screening can be found in `2.Screening/2c.Full-text Screening.xlsx`.

## Snowballing and Manual Addition <a name="snowballing"></a>
To account for studies that we might have missed with our primary search keywords, we performed snowballing on the studies that met our inclusion criteria. We reviewed every reference cited by the selected papers.

The references were subjected to the same rigorous inclusion criteria as the original studies. We first screened them by title and then by abstract. Through this snowballing process, we identified and included an additional **5** papers.

Despite thorough efforts to locate further relevant research, no additional papers were identified through manual searching.

The results related to the snowballing can be found in the `3.Snowballing` folder.

## Data Extraction and Analysis <a name="deaa"></a>
We iteratively reviewed the collected papers to gather both general and specific information relevant to our RQs, following protocols suggested by [Levett et al.](https://guides.himmelfarb.gwu.edu/systematic_review/data-extraction). We created a dataset with the following data: authors, year of publication, RQs proposed, methodology, study population and characteristics (for user studies), definitions of trust, consequences of trust, the importance of trust, antecedents of trust, and metrics used for trust.

Both authors worked independently to extract information and populate the dataset. Any discrepancies were discussed with the third author. In the end, we achieved a high Inter-Rater Reliability (IRR), with a Cohen's kappa (κ) coefficient of 0.824.

The results related to the data extraction and analysis can be found in the `4.Data Extraction and Analysis` folder.

