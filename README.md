# nyc_dob_analysis

## Overview

This repository corresponds to the open-source analysis conducted by [NewTrails Data Science](http://newtrails.io) that covers the New York City Department of Buildings, and contains:
- a Python library, `pydob`, which we've written for downloading, ingesting, and analyzing the DoB data
- a collection of Jupyter notebooks that were used to generate the charts in our report
- the figures that we chose to include in our report
- the report itself, in markdown form

Below you will find the [executive summary](#executive-summary) for our report and the [setup instructions](#setup-instructions) for making use of our Python code.

## Executive Summary

#### Overview

This is an initial analysis of _New York City Department of Buildings_ data performed by Abe Lerman and Xiaofeng Cao of [NewTrails Data Science](https://newtrails.io).

The date of publication of our report is March 2nd, 2020 - our research was conducted over several preceding months, primarily during the fourth calendar quarter of 2019. The executive summary will provide some context on various aspects of the project, each of which - and more - will be discussed in greater detail throughout the remainder of this report. For more information, you can visit the GitHub repo for this project, where you can:

- download our code and analysis notebooks
- contribute directly to the materials
- notify us of any issues

You can also reach out to us over [email](mailto:contact@newtrails.io).

#### Problem Statement

Facing an onslaught of construction-related, quality-of-life issues and earning little in the way of respite through filing complaints with the city, we set out to study building and construction trends in NYC. Our hope was to gain a better understanding of the NYC real-estate construction landscape. Specifically, we sought to answer the following questions:

1. is NYC currently over-indexing, compared to historical trends, with respect to construction activity?
2. is the construction that's going on of a more harmful nature, and / or less respectful to residents' quality of life?
3. is the city enforcing building-code adherence with the same level of rigor as it has historically?

#### Methodology

In trying to answer these questions, we ingested several datasets publicly released by the New York City Department of Buildings (DoB) through the [OpenData](https://opendata.cityofnewyork.us/) platform and performed our own analysis on this data. We call this an _initial analysis_ because there's plenty more to do: in this report, we take a high-level look at certain corners of the available data, focusing only slightly on other corners and ignoring some others altogether. A key constraint to note is that we looked exclusively at NYC-level data - i.e. we did not drill down to the level of a neighborhood, or even a borough. Another is that, unless otherwise noted, we focused our analysis on the years 2000 through 2019.

#### Analysis Findings

*1: An Increase in Construction Activity?*

Regarding recent construction activity as compared to historical trends, NYC saw a tremendous run-up in applications and permits in the post-recession years, with 2016 and 2017 exceeding[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-1-data) any of their respective prior yearly totals. As is described [below](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#data-overview) in _Application Filings_, we could not really study permit applications beyond 2016. But, we were able, to some extent, to study permit issuances, for which 2018 was a peak. "Construction equipment" was, far and away, the most-issued permit type[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-4) over the time-frame we studied.

We reiterate that we are painting in broad strokes - construction activity almost-assuredly varies throughout different boroughs and neighborhoods, both in terms of the raw number of construction projects, as well as in the magnitude of such projects. That said, it would be correct to say that New York City, on the aggregate, has seen unprecedented levels of permit issuance in the last few years. With that in mind, we have likely (in one way or another) been feeling the effects of of such issuance activity in recent years.

*2: An Increase in the Harmfulness of Construction Activity?*

As for the second question - both complaints and violations are at all-time highs[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-1-data). This could very well be a result of the fact that construction activity in general is at record levels. However, it should be noted that both complaints and violations, proportionate to the number of permits issued, have been on the rise[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-5-data). This annually tabulated complaints-to-permits ratio bottomed out at 56% in 2015 but has since risen, hitting 74% in 2019. Ditto for the similarly tabulated violations-to-permits ratio, which after hovering around 28% from 2013 - 2015 and has since also risen, coming in at 48% last year. Neither of these KPIs have reached their records highs (posted in 2008 and 2009, respectively) but the increases each has seen in the past 4 years are, nonetheless, large. You can find more on this [below](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#complaints-and-violations). Additionally, construction-related violations have sky-rocketed over the last several years, more than doubling since 2014[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-6-data) - there were 71.5k _construction-related_, DoB-issued ECB violations issued last year. For reference, there were 5.4k _elevator-related_ DoB-issued ECB violations issued in 2019, and an even-smaller 1.5k of these violations tagged with _quality-of-life_.

It's hard to answer this question definitively, given the potential for confounding. Has it gotten easier, at least in the last 10 years, to file a complaint against a landlord or nearby construction project? The city has certainly made updates to its 311 program. Is it possible that constituents have become less tolerant of construction, even if the relative harmfulness of that construction hasn't really gone anywhere? Given the increases in rental costs, along with the increases in construction-related activity, yes. And, to reiterate, we took a very high-level view in this analysis - the real answer to this question would probably vary over different areas of the city. But with all that said, there do seem to be indications that construction activity has in recent years taken a turn that is more harmful to NYC residents.

*3: Is the City Rigorously Enforcing the Building Code?*

Finally, is the city rigorously enforcing the building code? The answer is complicated. After refusing to really climb for the greater part of the last decade, the median annual ECB penalty issued (explained in more detail below) did rise in 2019[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-8). (This rise, by the way, holds true when grouping by the year in which the penalty was issued, not by when the hearing was held - the latter of these methodologies yields results that lag those the former.) This could obviously mean a number of things; for instance, that:

- the city is trying to make more severe the consequences for violating important aspects of the building code
- there are just more, severe violations of the building code
- more people are being caught for violating the building code
- this rise in median annual penalty was a statistical blip, and we will eventually revert to the mean (or median)

The truth may very well lie in some combination of these factors.

The allocation of responsibility for the issuance, assessment, and collection of violations and penalties is not entirely straightforward. The DoB handles the issuance of violations, which can be either "DoB" or "ECB" (Environmental Control Board) violations. The DoB's own violations tend to be more administrative in nature, while ECB violations that the DoB may issue tend to cover the more severe and "quality-of-life" impacting issues, as per our own research and what we were told by folks we spoke with in the NYC government. The ECB is a subdivision of the Office of Administrative Trials and Hearings, which [operates](https://en.wikipedia.org/wiki/New_York_City_Office_of_Administrative_Trials_and_Hearings) laterally to other agencies (like the DoB) who rely on it for adjudication. Depending on the severity of the ECB violation, a respondent may be able to avoid a hearing and / or reduce the ultimate penalty imposed at that hearing, through either correcting the issues that led to the violation, pre-paying by mail, or agreeing to some other set of stipulations. If none of that happens, the ECB administers a hearing on the violation, which may result in the imposition of a penalty. If a penalty is imposed it would likely be due immediately, unless otherwise stipulated, and the ECB would be responsible for collecting said penalty[<sup>\*</sup>](http://www.nyc.gov/html/dob/downloads/ppt/resolving_ecb_violations.pdf).

With all of that out of the way, we can note the following:

- the median annual paid ECB penalty, even when grouping by hearing date, has spent the last 3 years at $0[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-9-data)
- as the number of issued ECB violations has sky-rocketed over the last few years, the annual ratio of paid-to-imposed penalties has plummeted[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-10-data)
- despite starting the previous decade at around 25%, the ratio of the total $-value for in-default (no-show at hearing with an outstanding balance) ECB violations, proportionate to the total $-value of all imposed ECB violations, has held at over 50% for several years[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-11-data)
- the median difference in days between dates of hearing and issuance for DoB-issued ECB violations last year breached 100 for the first time (in our data, since 2000) and is up 88% from 2013 [<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-12-data)
- the temporality with which the DoB issues its own, administrative violations, which may be a part of the procedure for enforcing penalty payment, is surprising in its irregularity[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-17-data)
- the balance of unpaid DoB-issued ECB violations last year measured out at 42% of the DoB's total annual expenses[<sup>\*</sup>](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#figure-18-data)

More analysis on DoB-issued ECB penalties can be found [below](https://github.com/lermana/nyc_dob_analysis/blob/master/report.md#violation-penalties), but suffice it to say that the ECB looks to be overwhelmed by the increase in issued violations over the last few years, and that it may be having a hard time collecting the penalties for those violations.

In a relevant argument, Danielle Chaim recently [noted](https://clsbluesky.law.columbia.edu/2020/02/20/how-common-ownership-can-lead-to-tax-avoidance/) in Columbia Law School's _CLS Blue Sky Blog_ that a large number of firms all committing tax avoidance at the same increases the likelihood of the government becoming overwhelmed in its enforcement, thus decreasing the probability of enforcement action. It is important that the city engage in, and have the proper resources to engage in, rigorous enforcement of its building code, lest developers, landlords, and others come to believe that there are only light consequences for flouting the building code. Even those industry practitioners who hold themselves to a higher standard may face pressure to cut corners if their competitors are repeatedly able to get away with delivering faster or cheaper solutions through kicking the metaphorical "consequence" can down the road. As we've already seen, such a culture can produce [severe consequences](https://www.nytimes.com/2019/12/30/nyregion/nyc-building-violations.html).

#### Recommendations - Summary

The city needs to be more systematic in its enforcement of the building code, which includes ensuring that:
- penalty payment is enforced
- ECB hearings are held in a timely manner
- penalty values grow at a reasonable rate

#### Next Steps - Summary

We could further extend this analysis to borough-level and neighborhood-level. Moreover, roping in additional, economic variables could provide additional context. Finally, linking applications and permits to complaints and violations could help the city keep a handle on bad actors and preempt the types of work that are at a high-risk of heading in the wrong direction.

## Setup Instructions

#### `pydob`

To install `pydob` simply run the following, once you've cloned this repository:
 ```
 cd pydob
 pip install .
 ```
 
You can see find the required and auto-installed dependencies [here](pydob/setup.py#L10).

#### `DOB_DATA_DIR`

This code relies upon the setting of an environment variable named `DOB_DATA_DIR`, whose value is assumed to be the location in which should be kept all the data generated by and required for, the running of our code.

The default behavior - which the program will notify you of once it is running - can be avoided through setting this variable prior to running the code (you can also see the default behavior for yourself, [here](pydob/pydob/settings.py#L13)). If you do not set this variable in your environment, the program will ask for permission before doing anything, providing you with the opportunity to kill the program, set this variable, and run again.

Finally, the program will create a new folder (a sub-directory of `DOB_DATA_DIR`) to store the programmatically generated figures in - we've left our final figures where they are in this repo so that they are conveniently viewable.

#### `build`

Once `pydob` has been installed and `DOB_DATA_DIR` set to your liking, you are ready to run the setup program:
```
from pydob.build import build
build()
```
This program will download all the requisite data (saving these files to your machine) and then process it so that it's ready for analysis, depositing the results in a SQLite database.

Note that, if you choose to rerun at some point (maybe due to network issues or your making of modifications to the code) you can pass `use_existing=True` to `build` to avoid re-downloading any DoB data that is already available in `DOB_DATA_DIR`.

Also note that the DoB datasets each span roughly 1-2+M rows and 20-50 columns, which means that running `build` may take upwards of an hour and may require significant computational capacity from your local machine.

#### Notebooks

To actually generate the charts in our report, you will have to run our Jupyter notebooks, which you can find [here](https://github.com/lermana/nyc_dob_analysis/tree/master/notebooks).
