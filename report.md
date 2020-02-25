<font family="helios" color="#231F20">
<style>
	a {
		color: #008AD9;
	}
 </style>

# Why All the Ruckus?

## Table of Contents

<!-- MarkdownTOC autolink="true" markdown_preview="markdown" levels="1,2" -->

- [Executive Summary](#executive-summary)
- [Acknowledgments](#acknowledgments)
- [Background](#background)
- [Data Overview](#data-overview)
- [High-Level Trends](#high-level-trends)
- [Applications and Permits](#applications-and-permits)
- [Complaints and Violations](#complaints-and-violations)
- [Violation Penalties](#violation-penalties)
- [Recommendations](#recommendations)
- [Next Steps](#next-steps)
- [Appendix](#appendix)

<!-- /MarkdownTOC -->

## Executive Summary

#### Overview

This is an initial analysis of _New York City Department of Buildings_ data performed by Abe Lerman and Xiaofeng Cao of [NewTrails Data Science](https://newtrails.io).

The date of publication of our report is March 2nd, 2020 - our research was conducted over several preceding months, primarily during the fourth calendar quarter of 2019. The executive summary will provide some context on various aspects of the project, each of which - and more - will be discussed in greater detail throughout the remainder of this report. For more information, you can visit the GitHub repo for this project, where you can:

- download our code and analysis notebooks
- contribute directly to the materials
- notify us of any issues

You can also reach out to us over [email](mailto:contact@newtrails.io).

#### Problem Statement

Spurred by personal encounters with construction-related, quality-of-life issues, we set out to study building and construction trends in NYC. Our hope was to gain a better understanding of the NYC real-estate construction landscape. Specifically, we sought to answer the following questions:

1. is NYC currently over-indexing, compared to historical trends, with respect to construction activity?
2. is the construction that's going on of a more harmful nature, and / or less respectful to residents' quality of life?
3. is the city enforcing building-code adherence with the same level of rigor as it has historically?

#### Methodology

In trying to answer these questions, we ingested several datasets publicly released by the New York City Department of Buildings (DoB) through the [OpenData](https://opendata.cityofnewyork.us/) platform and performed our own analysis on this data. We call this an _initial analysis_ because there's plenty more to do: in this report, we take a high-level look at certain corners of the available data, focusing only slightly on other corners and ignoring some others altogether. A key constraint to note is that we looked exclusively at NYC-level data - i.e. we did not drill down to the level of a neighborhood, or even a borough. Another is that, unless otherwise noted, we focused our analysis on the years 2000 through 2019.

#### Analysis Findings

*1: An Increase in Construction Activity?*

Regarding recent construction activity as compared to historical trends, NYC saw a tremendous run-up in applications and permits in the post-recession years, with 2016 and 2017 exceeding[<sup>\*</sup>](#figure-1-data) any of their respective prior yearly totals. As is described [below](#data-overview) in _Application Filings_, we could not really study permit applications beyond 2016. But, we were able, to some extent, to study permit issuances, for which 2018 was a peak. "Construction equipment" was, by far and away, the most-issued permit type[<sup>\*</sup>](#figure-4) over the time-frame we studied.

We reiterate that we are painting in broad strokes - construction activity almost-assuredly varies throughout different boroughs and neighborhoods, both in terms of the raw number of construction projects, as well as in the magnitude or size of such projects. That said, it would be correct to say that New York City, on the aggregate, has seen unprecedented levels of permit issuance in the last few years. With that in mind, we have likely (in one way or another) been feeling the effects of of such issuance activity in recent years.

*2: An Increase in the Harmfulness of Construction Activity?*

As for the second question - both complaints and violations are at all-time highs[<sup>\*</sup>](#figure-1-data). This could very well be a result of the fact that construction activity in general is at record levels. However, it should be noted that both complaints and violations, proportionate to the number of permits issued, have been on the rise[<sup>\*</sup>](#figure-5-data). This annually tabulated complaints-to-permits ratio bottomed out at 56% in 2015 but has since risen, hitting 74% in 2019. Ditto for the similarly tabulated violations-to-permits raio, which after hovering around 28% from 2013 - 2015 and has since also risen, coming in at 48% last year. Neither of these KPIs have reached their records highs (posted in 2008 and 2009, respectively) but the increases each has seen in the past 4 years are, nonetheless, large. You can find more on this [below](#complaints-and-violations). Additionally, construction-related violations have sky-rocketed over the last several years, more than doubling since 2014[<sup>\*</sup>](#figure-6-data) - there were 71.5k _construction-related_, DoB-issued ECB violations issued last year. For reference, there were 5.4k _elevator-related_ DoB-issued ECB violations issued in 2019, and an even-smaller 1.5k of these violations tagged with _quality-of-life_.

It's hard to answer this question definitively, given the potential for confounding. Has it gotten easier, at least in the last 10 years, to file a complaint against a landlord or nearby construction project? The city has certainly made updates to its 311 program. Is it possible that constituents have become less tolerant of construction, even if the relative harmfulness of that construction hasn't really gone anywhere? Given the increases in rental costs, along with the increases in construction-related activity, yes. And, to reiterate, we took a very high-level view in this analysis - the real answer to this question would probably vary over different areas of the city. But with all that said, there do seem to be indications that construction activity has in recent years taken a turn that is more harmful to NYC residents.

*3: Is the City Rigorously Enforcing the Building Code?*

Finally, is the city rigorously enforcing the building code? The answer is complicated. After refusing to really climb for the greater part of the last decade, the median annual ECB penalty issued (explained in more detail below) did rise in 2019[<sup>\*</sup>](#figure-8). (This rise, by the way, holds true when grouping by the year in which the penalty was issued, not by when the hearing was held - the latter of these methodologies yields results that lag those the former.) This could obviously mean a number of things; for instance, that:

- the city is trying to make more severe the consequences for violating important aspects of the building code
- there are just more, severe violations of the building code
- more people are being caught for violating the building code
- this rise in median annual penalty was a statistical blip, and we will eventually revert to the mean (or median)

The truth may very well lie in some combination of these factors.

The allocation of responsibility for the issuance, assessment, and collection of violations and penalties is not entirely straightforward. The DoB handles the issuance of violations, which can be either "DoB" or "ECB" (Environmental Control Board) violations. The DoB's own violations tend to be more administrative in nature, while ECB violations that the DoB may issue tend to cover the more severe and "quality-of-life" impacting issues, as per our own research and what we were told by folks we spoke with in the NYC government. The ECB is a subdivision of the Office of Administrative Trials and Hearings, which [operates](https://en.wikipedia.org/wiki/New_York_City_Office_of_Administrative_Trials_and_Hearings) laterally to other agencies (like the DoB) who rely on it for adjudication. Depending on the severity of the ECB violation, a respondent may be able to avoid a hearing and / or reduce the ultimate penalty imposed at that hearing, through either correcting the issues that led to the violation, pre-paying by mail, or agreeing to some other set of stipulations. If none of that happens, the ECB administers a hearing on the violation, which may result in the imposition of a penalty. If a penalty is imposed it would likely be due immediately, unless otherwise stipulated, and the ECB would be responsible for collecting said penalty[<sup>\*</sup>](http://www.nyc.gov/html/dob/downloads/ppt/resolving_ecb_violations.pdf).

With all of that out of the way, we can note the following:

- the median annual paid ECB penalty, even when grouping by hearing date, has spent the last 3 years at $0[<sup>\*</sup>](#figure-9-data)
- as the number of issued ECB violations has sky-rocketed over the last few years, the annual ratio of paid-to-imposed penalties has plummeted[<sup>\*</sup>](#figure-10-data)
- despite starting the previous decade at around 25%, the ratio of the total $-value for in-default (no-show at hearing with an outstanding balance) ECB violations, proportionate to the total $-value of all imposed ECB violations, has held at over 50% for several years[<sup>\*</sup>](#figure-11-data)
- despite the average number of days between violation imposition and ECB hearing date falling to under 100 back in 2013, this metric (albeit with less standard deviation around it) has risen to over 125 days[<sup>\*</sup>](#figure-12-data)
- the temporality with which the DoB issues its own, administrative violations, which may be a part of the procedure for enforcing penalty payment, is surprising in its irregularity[<sup>\*</sup>](#figure-17-data)

More analysis on DoB-issued ECB penalties can be found [below](#violation-penalties), but suffice it to say that the ECB looks to be overwhelmed by the increase in issued violations over the last few years, and it may be having a hard time collecting the penalties for those violations.

In a relevant argument, Danielle Chaim recently [noted](https://clsbluesky.law.columbia.edu/2020/02/20/how-common-ownership-can-lead-to-tax-avoidance/) in Columbia Law School's _CLS Blue Sky Blog_ that a large number of firms all committing tax avoidance at the same increases the likelihood of the government becoming overwhelmed in its enforcement, thus descreasing the probability of enforcement action. It is important that the city engage in, and have the proper resources to engage in, rigorous enforcement of its building code, lest developers, landlords, and others come to believe that there are only light consequences for flouting the building code. Even those industry practitioners who hold themselves to a higher standard may face pressure to cut corners if their competitors are repeatedly able to get away with delivering faster or cheaper solutions through kicking the metaphorical "consequence" can down the road. As we've already seen, such a culture can produce [severe consequences](https://www.nytimes.com/2019/12/30/nyregion/nyc-building-violations.html).


#### Recommendations

The city needs to be more systematic in its enforcement of the building code, which includes ensuring that:
- penalty payment is enforced
- ECB hearings are held in a timely manner
- penalty values grow at a reasonable rate

#### Next steps

We could further extend this analysis to borough-level and neighborhood-level. Moreover, roping in additional, economic variables could provide additional context. Finally, linking applications and permits to complaints and violations could help the city keep a handle on bad actors and preempt the types of work that are at a high-risk of heading in the wrpng direction.

[^](#table-of-contents)
## Acknowledgments

- come back to this

[^](#table-of-contents)
## Background

To offer a brief history of _NewTrails_, we were founded last year in the hope of being able to offer flexible but robust data engineering and machine learning services to a variety of different types of organizations. The work last year was carried out primarily by Abe but we are now a team of three. Xiaofeng - who started working on this report as an intern - has joined as a Data Scientist, and Andriy Noble has joined as our Principal Security Engineer, enabling us to enhance our offering with a suite of cyber-security-oriented data science solutions. We also maintain an, if you will, distributed network of on-demand talent to help out as necessary, and we plan on adding additional, full-time capacity this year.

The idea for this project came about towards the end of last summer - we were brainstorming on what Xiaofeng's next project should be, as she had just successfully completed an audit of some of our analysis programs, and she was looking for a real-world, gnarly, data wrangling problem. We stumbled into what would become the underlying idea for this report by means of having our conversation interrupted by some incredible construction noise right outside the window.

Abe had spent months dealing with a variety of problems at his apartment. First, there was the late-night construction across the street. Finding little in return for the 311 complaints he'd made, he reached out to his councilwoman's office, who was responsive and empathetic, but ultimately just encouraged him to continue calling 311. This construction went on for some time and was severe enough that it, along with his and his neighbor's complaints, was all picked up by the [New York Times](https://www.nytimes.com/2019/09/27/nyregion/noise-construction-sleep-nyc.html). There was also the construction for the restaurant downstairs, some of which was taking place - illegally - on the weekends. And, of course, there were the myriad maintenance problems inside the apartment itself. As all of this continued to happen, right in the heart of the Flatiron district, we wondered whether this was a localized suite of issues, or a representation of a larger problem?

It had long been a hope that NewTrails would occasionally carve out time for interesting open-source work. Plus, what better way to gain familiarity with the new (to us) and exciting industry of real estate construction? And so it was that we set out to put our data science abilities to use in gaining an understanding of NYC's building codes and the DoB's enforcement of them. An early theory was that key, problematic actors were working as force multipliers in the construction space, engaging in bad behavior that would allow them to get through certain work-flows at higher speeds and / or lower costs, thus encouraging competitors to degrade their standards lest they lose market share. Given the level of depth and data-access required in order to properly solve such a problem, and our correspondingly limited time and lack of access to any non-public data, we whittled our ambitions down to answering the three, core questions laid out in our [problem statement](#problem-statement) over the course of a few months of part-time work.

[^](#table-of-contents)
## Data Overview

#### Application Filings

- [data](https://data.cityofnewyork.us/Housing-Development/DoB-Job-Application-Filings/ic3t-wcy2)
- assumed primary key: `job`
- assumed primary date column: `pre_filing_date`

This dataset corresponds to the applications filed, applications which - if approved - would yield permit(s), generally one permit for each type of work performed (e.g. electrical, plumbing, etc.). Unfortunately, this dataset was unusable for us post-2017 (and even somewhat for 2017) due to the fact that it does not include applications submitted through the _DoB NOW_ platform, and cannot be deterministically linked to those jobs, at least in any sort of way that would have fit with the level of granularity we have tried to achieve in this report. See the _DoB NOW: Build – Job Application Filings_ [dataset](https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd) for DoB NOW jobs. 

The DoB has released a new system for permit application and issuance that it calls _DoB NOW_, which as of 2018 had already been used for issuing a majority of permits and which last year was responsible for almost all permits issued. The data (which we've linked to in the above paragraph) corresponding to the applications filed through this system, at the time of this writing, included neither any sort of application identifier that would have allowed us to link to applications filed in the other system, nor even _any sort of date field_. After making multiple requests for a date field, we were told that a ticket had been filed, and that there was no time estimate corresponding to when this field would be added.

#### Permit Issuance

Old system:

- [data](https://data.cityofnewyork.us/Housing-Development/DoB-Permit-Issuance/ipu4-2q9a)
- assumed primary key: combination of `permit_si_no` and 
- assumed primary date column: `issuance_date`

This dataset corresponds to permits issued by the Department of Buildings since 1989. Same as the application dataset, we have limitation on using this dataset later than 2017 because the new system DoB NOW was implemented that year. 

New system:

- [data](https://data.cityofnewyork.us/Housing-Development/DoB-NOW-Build-Approved-Permits/rbx6-tga4)
- assumed primary key: `job_filing_number`
- assumed primary date column: `issued_date`

_DOB NOW: Build – Approved Permits_ [dataset](https://data.cityofnewyork.us/Housing-Development/DoB-NOW-Build-Approved-Permits/rbx6-tga4) provides list of all approved permits in DOB NOW since 2016. The new system was put in use from 2017. We were able to aggregate this data to the old dataset and to find total permit issue in each year by the date field `issued_date`. However, when it comes to aggregate the types of permits, we are very much limited since the type fields in DoB NOW do not reconcile the types in old system.

#### Complaints Received

- [data](https://data.cityofnewyork.us/Housing-Development/DoB-Complaints-Received/eabe-havv)
- assumed primary key: `complaint_number`
- assumed primary date column: `date_entered`
- de-duplicate on `complaint_number`

Complaints received dataset corresponds complaints received by Department of Buildings (DoB). It includes complaints that come from 311, that are called in to DoB's Customer Service Center, and that are entered into the system by DoB staff. After communicating with the stakeholder from DoB, we dropped the duplicates in `complaint_number`. 

#### ECB Violations

- [data](https://data.cityofnewyork.us/Housing-Development/DoB-ECB-Violations/6bgk-3dad)
- assumed primary key: `isn_dob_bis_extract`
- assumed primary date column: `issue_date`
- de-null `issue_date`

The Department of Buildings issues [ECB/OATH](https://www1.nyc.gov/site/buildings/business/environmental-control-board-violations.page) violations when a property is not in compliance with either New York City construction codes or zoning resolutions[<sup>\*</sup>](https://www.propertyshark.com/Real-Estate-Reports/2018/11/26/breaking-down-new-york-city-violations-hpd-dob-ecb/). These violations are adjudicated by OATH and generally apply to offenses that are more harmful in nature than those covered by the more-administrative, non-ECB DoB violations. This dataset includes details of ECB violations going back to the 1990s. We dropped violations with null `issue_date` values, as this date field was core to our analysis and these values accounted for less than 0.005% of all values `issue_date`.

#### DoB Violations
- [data](https://data.cityofnewyork.us/Housing-Development/DOB-Violations/3h2n-5cm9)
- assumed primary date column: `issue_date`
- de-null `issue_date`

DoB Violations dataset provides the violations information that are less harmful than ECB violations. There are no penalty imposed or no need to go to court for adjudication. What deserve to mention is that some of violations, e.g. failure to file a Boiler or Elevator compliance filing with DoB, would be generated by computer periodically. This is part of the reason why there are many surprising spikes in figure 16.

[^](#table-of-contents)
## High-Level Trends

For one, as many in real estate already know, there's a cyclical nature to construction activity in the city. We saw large increases in permit applications and issuances in the years immediately preceding the Great Recession (mid-aughts), and we saw another large run up from 2009 to around 2016 or 2017.

#### Figure 1
- [data](#figure-1-data)
![ ](figures/percent_change_all.png  "percent_change_all")

We also saw that, on the aggregate, complaints and violations seemed to track each other pretty well. However, we saw that these two (complaints and violations) seem to lag behind permit applications and issuances by about two years. We look to be in the midst of a downswing in construction-related activity. (quantify the lag, and use this as the basis for price predictions later)

What deserve to be mentioned is that there are more permits than applications for each year. Since a job application to DoB could potentially leads to different types of works, DoB would issue several work permits for one application. 

Since around 2016, DoB started to put DoB NOW in use. [DoB NOW](https://www1.nyc.gov/site/buildings/industry/dob-now.page) is the Department of Building's self-service online tool that enables applicants to do all business with DoB online. We included the DoB NOW permits issuance here. However, we are limited in how we can make use of DoB NOW applications data, due to there (at the time of this writing) not being a date column in that data set. In this case, we estimated the total applications from 2017 to 2019 based on the applications-to-permits ratio in 2016. We assumed the rate to be constant in these three years for simplicity. The estimated numbers are showed in dotted line.

#### Figure 2
- [data](#figure-2-data)
![ ](figures/autocorrelations_all_yearly.png  "autocorrelations_all_yearly")

Autocorrelation represents the relationship between a variable's current value and its past value. Figure 2 shows the autocorrelation in monthly changes in permits, complaints and violations. Autocorrelation of 1 indicates a perfect positive correlation and -1 shows a perfect negative correlation. In this research, we are interested in 30 months autocorrelations.

The permits autocorrelations shows that there appears to be a strong relationship between permits issued in the current month and the same month in the previous year, since the autocorrelation of permits issuance at lag 12 reaches to 0.71. The autocorrelations in complaints also reached to the highest point 0.45 at lag 12, indicating similar relation as in permits. In violations, we are not able to identify this pattern as strong as it is in permits. The autocorrelation is 0.3 at lag 12 which could represent there is some auto-regression in violations. 

[^](#table-of-contents)
## Applications and Permits

#### Figure 3
- [data](#figure-3-data)
![ ](figures/percent_change_appli_permits.png  "pct_change_application_and_permits_yearly")

**Xiaofeng**
New York City issued 197,556, 195,817 and 192,399 permits each year from 2017 to 2019, including the regular DoB permits as well as the ones issued by DoB NOW. With in that, 195,343, 169,377 and 152,212 permits were issued by regular. DoB NOW contributed 2,213, 26,440 and 40,187 on the other hand. The DoB has been pushing its DoB NOW system as the desired standard and the system has been accounting for a non-negligible portion activity since 2018. 

#### Figure 4
- [data](#figure-4-data)
![ ](figures/permit_types.png  "permit_types")

Applications and permits tracks each other pretty well since 2000. In 2017, there are 94% more permits issued comparing to the number in 2000. The climb in permit issuance after recession shows that the real estate market was recovering since then and reached its all time high in 2017. The heat in real estate clams down a little after 2017 and decreased to slightly below 90%. 

**Abe**
It's worth noting that, to very thoroughly consider whether the city has _over-indexed_ on construction, it would be worth exploring applications and permits against additional variables. For instance, what is the relationship between permitting rates and population density, in different parts of the city? Manhattan is geographically constrained by water on all four sides. So, outside of maybe the Hudson Yards project, where a no-so-inhabited nook of the city was developed freshly in new ways.

The city has become somewhat more selective in terms of what jobs it approves. that permit applications and issuances were closely linkedPermit issuance rates peaked at around 86% back in 2006, and are now at around 75%. The number of complaints for _illegal conversions_ and _operating without a permit_ - top complaint categories - have decreased, while the number of elevator-related complaints has held steady for the last decade or so, and is close to its all-time high.

[^](#table-of-contents)
## Complaints and Violations

#### Figure 5
- [data](#figure-5-data)
![ ](figures/ratios.png  "ratios")

Complaints-to-permits and violations-to-permits both evaluate the percentage of permits issued that lead to complaints and violations. Complaints-to-permits reached 74% at the end of 2019. This is horrific for resident in NYC since 7 out of 10 jobs has been filed for complaints. 

#### Figure 6
- [data](#figure-6-data)
![ ](figures/complaint_types.png  "complaint_types")

We grouped the complaints by their types by issuance year. The complete complaints types can be found [here](https://www1.nyc.gov/assets/buildings/pdf/complaint_category.pdf). The city modified the type `63` _Elevator-Danger Condition/Shaft Open/Unguarded_ to `6S` in recent years. `6S` counts for critical elevator issues, e.g. a particular elevator is out of order. `6M` on the contrary, is similar to `6S` but less severe. 

The top 3 complaints have been `45`: illegal conversion, `05`: no permit, and `63`: elevator in danger condition since 2006. These 3 types of complaints stay on a similar pattern with a little fluctuation in recent years.

#### Figure 7
- [data](#figure-7-data)
![ ](figures/violation_types.png  "ecb_violation_types")

In figure 6 we measure the number of ECB violations for each type and year. We show the top 3 ECB violations for each year from 2006 to 2019. Construction violations has been the the most prevailing since 2006. It increased from around 25,000 to 70,000 in 7 years from 2012 to 2019 and reached its all time high in 2019 at 71,532.

ECB violation types include construction, elevators, quality of life, boilers, local law, site safety, zoning, signs, plumbing, public assembly, HPD, cranes and derricks, administrative, padlock, non-hazardous. 


[^](#table-of-contents)
## Violation Penalties

Unless otherwise noted, all charts here refer to DoB-issued ECB violations.

#### Figure 8
- [data](#figure-8-data)
![ ](figures/penalty_imposed_y_hearing_issue.png  "penalty_imposed")

In statistics, mean and median are two main measures of central tendency. They could help us better understand the distribution of data. Since mean measures the average of a set of data, its value will be more affected by outliers than median. 

To better understand the underlying penalty data, we grouped the data by two date fields (hearing date and issue date) by year and to calculate mean and median for each year. Note that _issue date_ is the date on which a violation is issued, and _hearing date_ is the date of the most recent scheduled hearing. A hearing presents an opportunity for the respondent named on the violation to either admit to it or contest it. 

A hearing occurs after the issuance of a ECB violation. The mean grouped by issue date tracks pretty well with the mean grouped by issue date with a few months lag. The medians are pretty comparable in their moves. While the medians of imposed penalties stayed within a roughly $500-750 range from 2008 to 2018, the means increased greatly, eventually settling within a range of $1,500-3,500. This positive difference between mean and median indicates that the data is positively skewed, i.e. the data has a long right tail. Surprisingly, at the end of 2018 to 2019, both means and medians of imposed penalties sharply increased, indicating that the city issued many expensive ECB violations. 

#### Figure 9
- [data](#figure-9-data)
![ ](figures/penalty_paid_y_hearing_issue.png  "penalty_paid")

The means and medians of paid penalties followed a similar pattern as the imposed penalties, with the exception of 2018 and 2019. The means of paid penalties has tumbled since the end of 2018, which when compared to the above data on imposed penalties indicates that many ECB penalties issued in the last two years have not been paid. 


#### Figure 10
- [data](#figure-10-data)
![ ](figures/penalty_paid_to_imposed_yearly.png  "penalty_paid_to_imposed")

The paid-to-imposed ratio measures the proportion of penalties paid by building owners to penalties imposed to them by DoB. The paid-to-imposed ratio went down from approximately 50% to 30% after the recession until 2012. The ratio arose thereafter and reached 47% in 2016. However, the paid-to-imposed ratio has plunged 76% since then and fell to 11.64%. 

The blue bar shows the amount of ECB violations was issue from 2000 to 2019. Violations issued declined since the recession and rebound to its all time high at 2019. The total number of violations has increased 55% from 59,838 to 92,800 since 2019. The city may just overwhelmed by the surprising climb in the violations and need more support on collecting penalty.

#### Figure 11

- [data](#figure-11-data)
![ ](figures/normalized_and_paid_to_imposed_hearing.png  "normalized_and_paid_to_imposed")

To further analyze paid to imposed ratio, we grouped the ECB violations by its hearing status by hearing year. Normalized penalty imposed represents the proportion of penalty imposed for each type of hearing status for each year. We mainly looked at two types of hearings, default and in violation, because they count for the top two highest amount of imposed penalty. 

*Violation Status:* `DEFAULT`

A hearing status of `DEFAULT` indicates that the respondent failed to appear for scheduled hearing and did not pay the summons prior to the hearing. ECB may add additional penalties on top the existing one(s).

We can see that violations with a status of `DEFAULT` have each year, since 2012, accounted for about *50-60% of the total dollar-value* of all DoB-issued ECB violations, while the paid-to-imposed ratio over this period of time has typically stayed *below 20%*. Moreover, given that it usually takes less than a year for the city to hold an ECB hearing for a given violation, the 2018 paid-to-imposed ratio of .073 for `DEFAULT` violations (which accounted for 52% of the total dollar-value of Dob-issued ECB violations that year) is just outrageous.

Stronger default penalties could make a real impact on the timeliness with which these violations are paid off. And, with such a high % of penalty dollar-value in default each year, is there any way that the city is tracking all of these down? With that, an impact of payment timeliness probably means a real impact both to the city's bottom line, and to the behavior of the various players in its ecosystem.

*Violation Status:* `IN VIOLATION`

ECB violations with hearing status `IN VIOLATION` in the last decade typically accounted for around around 40% of the total dollar-value of all DoB ECB penalties imposed each year. The paid-to-imposed ratio for penalties peaked at 76% in 2016 and has since fallen - to 75% in 2017, 67% in 2018, and 48% last year. One reason for this decline could be the massive increase in ECB Violations issued over the last few years. 

*Violation Status: All*
There are nine types of hearing status as following: 

- `IN VIOLATION`: Definition unknown.
- `CURED/IN-VIO`: Enforcement agency notes indicate that the violating conditions have been corrected prior to hearing.
- `POP/IN-VIO`: Definition unknown.
- `STIPULATION/IN-VIO`: Admission of guilt – extends compliance time by an additional 75 days from the first scheduled hearing date.
- `PENDING`: Definition unknown. Penalties of this status couldn't be found for most of the last decade, but exhibited a strangely high paid-to-imposed-ratio of 66% in 2017 and accounted for 0.15% of all DoB ECB penalties imposed that year.
- `DEFAULT`: Respondent failed to appear for scheduled hearing and did not pay the summons prior to the hearing.
- `WRITTEN OFF`: Summons has been written off and nothing is due.
- `DEFAULT`: Respondent failed to appear for scheduled hearing and did not pay the summons prior to the hearing.
- `DISMISSED`: Dismissal – No Penalty Imposed; If you prevail in contesting your violation, you will not owe any penalties and your violation will be dismissed. However, the Department may re-inspect, reissue a violation, or appeal the decision.

#### Figure 12
- [data](#figure-12-data)
![ ](figures/ecb_hearing_imposed_daysdelta.png  "hearing_issue_days_delta")

All ECB violations need to be adjudicated by the Office of Administrative Trials and Hearings (OATH), so we analyzed the day differences between hearing and issue dates across all issued ECB violations, broken out by year. The above chart shows us the average number of days that it took for OATH/ECB to hold a hearing (days delta between hearing and issue date) from 2000 to 2019 (issue date year). The blue bar represents the average days and the black line is the standard deviation of the days delta in each year. A higher error bar indicates more volatility in days delta for the year. The average of days decreased from 206 days in 2008 to 97 days in 2013. There has been a slightly increase since then. However, the standard deviation has been decreasing since the recession, which means that OATH/ECB is getting more and more consistent on its violations hearing. 

#### Figure 13

|Quantiles (%) | 2017 (days) |2018 (days)  |
|:-------:     |:-------:    |:--------:|
|0.00	       |12           |  1
|5.00	       |45           |  47
|10.00	       |47           |  49
|25.00	       |50           |  56
|50.00	       |84           |  89
|75.00	       |161          |  155
|90.00	       |247          |  230
|**95.00**     |**308**      |**291**
|99.00	       |486          |  409
|99.90	       |811          |  576
|99.99	       |965          |	656

We further analyze on percentile of days delta between hearing days and issue days for 2017 and 2018. We specifically look at 95% percentile as representation that most of ECB violations have been heard in the year. In 2017, 95% of issued ECB violations in have no more than 310 days delta between hearing date and issue date. The 95% percentile of days delta stays similar in 2018. Penalty is imposed after the hearing. 

In an effort to provide a greater buffer window, we decide to bucket by year given 95% days delta between issued date and hearing date. We further adding two months to the 95% days delta to allow the City to collect penalties since we have no payment date of penalty in the ECB violations data to have a better understanding on the speed of collecting. Therefore, we give approximately a year to collect the penalty after the violation was issued.

#### Figure 14
- [data](#figure-14-data)
![ ](figures/active_resolved_ecb.png  "active_and_resolved_ecbs")

Active ECB violations are violations that still needs to be addressed whereas resolved ECB violations are the ones that was either fixed with DOB or dismissed by OATH. The above graph shows the status of ECB violations that have been heard as of 2019 (grouping by hearing date). There are still many active ECB violations in this decade. We can tell that the DoB is truly overwhelmed by the increase in number of violations issued.

#### Figure 15
- [data](#figure-15-data)
![ ](figures/paid_to_imposed_bins.png  "paid_to_imposed_bins")

We further grouped the paid-to-imposed ratio into 6 bins of imposed penalty's dollar value. They are 0-500, 500-1,000, 1,000-5,000, 5,000-10,000, 10,000-50,000, 50,000-100,000. From 2016 to 2019, DoB paid-to-imposed ratio went down as the dollar imposed penalty increased. DoB reached 80% on paid-to-imposed ratio when penalties were within 1,000 dollars. However, the ratio went below 20% for penalties higher than 10,000 dollars. We can conclude that DoB has trouble on collecting higher imposed penalties. 

#### Figure 16
 
|ECB Violation Type	 |Year            |Normalized Violation Counts|Normalized Imposed Penalty|Paid to Imposed
|:------------------:|:-------------: |:------------------: |:----------------:  |:-----------:
|Boilers             |2017            |0.04                 |    0.02            |0.43
|                    |2018            |0.03                 |    0.01            |0.41
|                    |2019            |0.02                 |    0.01            |0.25
|**Construction**    |**2017**        |**0.74**             |    **0.77**        |**0.43**
|                    |**2018**        |**0.77**             |    **0.78**        |**0.30**
|                    |**2019**        |**0.77**             |    **0.68**        |**0.12**
|Cranes and Derricks |2017            |0.00                 |    0.01            |0.90
|                    |2018            |0.01                 |    0.01            |0.62
|                    |2019            |0.00                 |    0.01            |0.17
|Elevators	         |2017            |0.09                 |    0.04            |0.70
|                    |2018            |0.07                 |    0.03            |0.44
|                    |2019            |0.06                 |    0.02            |0.33
|Local Law	         |2017            |0.00                 |    0.00            |0.68
|                    |2018            |0.04                 |    0.02            |0.50
|                    |2019            |0.00                 |    0.00            |0.14
|Plumbing	         |2017            |0.03                 |    0.02            |0.58
|                    |2018            |0.01                 |    0.01            |0.40
|                    |2019            |0.01                 |    0.01            |0.15
|Public Assembly	 |2017            |0.00                 |    0.00            |0.13
|                    |2018            |0.00                 |    0.00            |0.41
|                    |2019            |0.00                 |    0.00            |0.00
|**Quality of Life** |**2017**        |**0.01**             |    **0.03**        |**0.52**
|                    |**2018**        |**0.01**             |    **0.07**        |**0.14**
|                    |**2019**        |**0.02**             |    **0.16**        |**0.01**
|Signs	             |2017            |0.01                 |    0.03            |0.35
|                    |2018            |0.01                 |    0.01            |0.31
|                    |2019            |0.01                 |    0.01            |0.01
|Site Safety	     |2017            |0.00                 |    0.00            |0.80
|                    |2018            |0.00                 |    0.00            |0.24
|                    |2019            |0.01                 |    0.02            |0.08
|Unknown	         |2017            |0.07                 |    0.08            |0.61
|                    |2018            |0.04                 |    0.05            |0.53
|                    |2019            |0.09                 |    0.08            |0.21
|Zoning	             |2017            |0.01                 |    0.01            |0.65
|                    |2018            |0.02                 |    0.00            |0.64
|                    |2019            |0.01                 |    0.00            |0.33

This table shows percentage of ECB Violation counts, percentage of imposed penalty, percentage of paid penalty, and paid-to-imposed penalty for year 2017, 2018 and 2019 for each type of ECB violations. For example in 2017 for construction type, 74% of ECB violation issued in that year contributed to construction and 77% of dollar amount of penalty imposed was towards to construction. However, the paid to imposed ratio for construction in 2017 is only 0.43, which means 57% of penalty imposed for construction in 2017 has not been paid with in 2017. It is also interesting to see the normalized penalty imposed increase in dollars from 7% in 2018 to 16% in 2019, but the normalized violation counts only increased 1%. Furthermore, the paid to imposed ratio was only 0.14 and 0.01 in 2018 and 2019. The city should definitely to investigate on these two types of ECB violations to improve their collection of penalty. 


#### Figure 17
- [data](#figure-17-data)
![ ](figures/violation_spikes.png  "dob_violation_counts")

We grouped DoB violations by issued year and month from 2000 to 2019 to understand the trend in violation issuance over years. DoB Violation is a notice without penalty, which is very different from ECB violation. The periodic spikes for each year are most likely the computer generated violations from time to time. 

--

[^](#table-of-contents)
## Recommendations

Successfully executing on penalty collection is critical to the New York City government's protection of its residents' quality of life. As we have already discussed, a failure to execute can lead to more corner cutting, unsafe conditions - more in-violation activity.

Rigorous enforcement of DoB-issued ECB penalty collection would likely reduce the number of violations in default, thus:

- reducing the outstanding balance owed to the city
- increasing the likelihood of penalty payment
- discouraging bad behavior that may be driven by the opportunity for low-cost penalty default

Additionally, the maintenance of a reasonable gap between issuance and hearing dates for DoB-issued ECB penalties would ensure that developers and landlords could realize their harmful behavior immediately and would also reduce backlog in ECB violations cases.

These achievement of these goals may require additional human resources, since it seems that the increases in penalty collection delay or laxness are well-correlated to increases in penalty issuance volumes. That said, automated and possibly statistical tools could allow for a more efficient and manageable path to execution.

Finally, the City need to ensure that violation penalties do not stay stagnant in competitive real state markets. The profit from arising in residential housing price should be priced in penalty to avoid building owners and developers are careless on their violations. 


[^](#table-of-contents)
## Next Steps

We have reiterated that we are painting in broad strokes. Construction activity varies from neighborhood to neighborhood, and further analysis at the borough and neighborhood levels would be very interesting to see. It would also be helpful to see measures of population density compared to construction activity, as the various "effects" of construction activity are surely felt differently, depending on how dense the surrounding area is. 

Additionally, analysis on the relationships between economic factors (e.g. [REIT valuations](https://www.reit.com/what-reit?gclid=Cj0KCQiAqNPyBRCjARIsAKA-WFzmxqJWaTebuH8MXvH0l2T5_Qkix2Fus-tDbNk8rRArIU8SujMA8x4aAj7TEALw_wcB), [residential rental prices](https://streeteasy.com/blog/data-dashboard/?agg=Median&metric=Asking%20Rent&type=Rentals&bedrooms=Any%20Bedrooms&property=Any%20Property%20Type&minDate=2010-01-01&maxDate=2020-01-01&area=Flatiron,Brooklyn%20Heights), [residential sales prices](https://streeteasy.com/blog/data-dashboard/?agg=Median&metric=Asking%20Price&type=Sales&bedrooms=Any%20Bedrooms&property=Any%20Property%20Type&minDate=2010-01-01&maxDate=2020-01-01&area=Flatiron,Brooklyn%20Heights)) and the data we've analyzed here would be interesting to see. For instance, a capEx-heavy industry such as real estate will surely exhibit cyclical tendencies - we did in fact see this in the DoB data[<sup>\*</sup>](#figure-2). Comparing these tendencies to pricing trends, an understanding of which could benefit developers' sense of market timing, was something that we'd hoped to do, but didn't have time for. And, regarding ECB violations - it would be interesting to flesh out whether there is, or whether there should be, any relationship between the real estate market's economic health and the city's penalty imposition or collection.

Finally, our initial and ambitious hope for this project was to understand if there were certain, key developers or landlords who were regularly flouting the building codes and who had thus far managed to escape real punishment and / or exclusion from the NYC real estate landscape. A lack of punishment for persistent rule flouting essentially green-lights violating the building code in the name of cost cutting or project expediency. Taken further, a lack of enforcement effectively implements rule flouting as a de facto _requirement_ for any developer or landlord who wishes to seriously compete in the marketplace.

As such, we had envisioned trying to link violations to their perpetrating landlords or developers, and to the permit applications that ultimately led to the problematic behavior. Setting aside the various obfuscations practiced by many landlords and developers (including the use of LLCs and / or shell companies) and considering only the data that we had access to, the permit application and issuance datasets did not directly (i.e. at the level of a record) link to either complaints or violations. Even complaints and violations did not directly link to each other. Executing on a "record linkage" project is well within the scope of our abilities but was not something that we were able to invest the time into completing. That said, we had been of the mind that such a linkage could have enabled us to answer questions like:

- what types of projects are most prone to in-violation activities?
- which permit applicants can be traced to the most violations?
- how do the answers to each of the above questions change over time?

Answering such questions would better arm the city to weed out problematic actors from its buildings ecosystem.

[^](#table-of-contents)
## Appendix

#### Figure 1 Data
- *Growth in Yearly Figures: Applications, Permits, Complaints, and Violations*
- \* in below table indicates estimated value, due to the data issues explained [here](#application-filings)
- total annual applications from 2017 to 2019 were estimated based on the applications-to-permits ratio in 2016
- [back to figure](#figure-1)

| Year | Applications          | Permits | Complaints | Violations (ECB) |
| :--: | -----------:          | ------: | ---------: | ---------------: |
| 2000 |    67,735             | 101,496 |   43,520   |      41,030      |
| 2001 |    67,320             | 105,728 |   45,124   |      42,059      |
| 2002 |    70,045             | 111,931 |   51,991   |      40,566      |
| 2003 |    72,817             | 122,595 |   62,542   |      45,041      |
| 2004 |    80,833             | 137,618 |   78,212   |      44,962      |
| 2005 |    86,264             | 150,087 |  108,873   |      49,196      |
| 2006 |    86,896             | 155,861 |  112,953   |      51,687      |
| 2007 |    90,201             | 158,250 |  129,247   |      58,225      |
| 2008 |    84,548             | 150,370 |  142,991   |      76,940      |
| 2009 |    70,726             | 135,770 |  127,278   |      78,540      |
| 2010 |    74,889             | 136,243 |  113,516   |      69,054      |
| 2011 |    77,847             | 143,943 |  103,800   |      57,781      |
| 2012 |    81,843             | 148,534 |  100,377   |      47,173      |
| 2013 |    93,195             | 161,322 |   95,242   |      45,773      |
| 2014 |   107,943             | 170,787 |  101,680   |      52,095      |
| 2015 |   107,544             | 182,714 |  101,984   |      52,582      |
| 2016 |   109,527             | 191,006 |  114,679   |      59,838      |
| 2017 |   113,287<sup>*</sup> | 197,556 |  126,587   |      79,105      |
| 2018 |   112,290<sup>*</sup> | 195,817 |  129,562   |      88,482      |
| 2019 |   110,330<sup>*</sup> | 192,399 |  142,873   |      92,800      |

--

#### Figure 2 Data
- *Autocorrelation in Monthly Percent Changes*
- [back to figure](#figure-2)

| Lags| Permits | Complaints   | Violations (ECB) |
| :--:| ------: | ---------:   | ---------------: |
| 1   | -0.382373 | -0.313691  |  -0.291068       |
| 2   | -0.008993 |  0.194009  |   0.025308       |
| 3   |  0.146137 |  0.038190  |   0.068256       |
| 4   | -0.259690 | -0.223919  |  -0.107328       |
| 5   |  0.148509 |  0.075229  |   0.099334       |
| 6   | -0.182140 | -0.225010  |  -0.139810       |
| 7   |  0.089662 | -0.064170  |   0.056295       |
| 8   | -0.176381 | -0.063100  |  -0.116743       |
| 9   |  0.147122 | -0.047402  |   0.122574       |
| 10  | -0.159407 | -0.025230  |  -0.069506       |
| 11  | -0.143229 | -0.017490  |  -0.085073       |
| 12  |  0.707353 |  0.415345  |   0.236153       |
| 13  | -0.362506 | -0.215213  |  -0.130263       |
| 14  |  0.162864 |  0.336686  |   0.134334       |
| 15  |  0.026297 | -0.058940  |  -0.007688       |
| 16  | -0.247162 | -0.103298  |  -0.096528       |
| 17  |  0.242613 |  0.055483  |   0.010223       |
| 18  | -0.336469 | -0.324666  |  -0.064154       |
| 19  |  0.134917 | -0.009868  |   0.108028       |
| 20  | -0.121456 | -0.060456  |  -0.180632       |
| 21  |  0.049985 | -0.112659  |   0.093528       |
| 22  | -0.115574 |  0.167879  |  -0.054410       |
| 23  | -0.040642 | -0.102237  |  -0.011686       |
| 24  |  0.499464 |  0.383696  |   0.236234       |
| 25  | -0.177592 | -0.094395  |  -0.137769       |
| 26  |  0.118807 |  0.335357  |   0.008371       |
| 27  | -0.060310 | -0.129620  |  -0.012436       |
| 28  | -0.106392 | -0.099436  |   0.004337       |
| 29  |  0.187828 |  0.083418  |   0.079013       |
| 30  | -0.370341 | -0.331938  |  -0.146401       |


--

#### Figure 3 Data
- *Growth in Yearly Figures: Applications and Permits*
- [back to figure](#figure-3)

|Year|applications |permits
|:--:|:-------:    |:---------:
|2000|0.00000      | 0.000000
|2001|-0.61268     | 4.169622
|2002|3.410349     | 10.28119
|2003|7.502768     | 20.78801
|2004|19.337123    | 35.58958
|2005|27.355134    | 47.87479
|2006|28.288182    | 53.56368
|2007|33.167491    | 55.91747
|2008|24.821732    | 48.15362
|2009|4.415738     | 33.76881
|2010|10.561748    | 34.23484
|2011|14.928767    | 41.82135
|2012|20.828228    | 46.34468
|2013|37.587658    | 58.94419
|2014|59.360744    | 68.26968
|2015|58.771684    | 80.02088
|2016|61.699269    | 88.19066
|2017|67.251284    | 94.64412
|2018|65.779044    | 92.93075
|2019|62.885358    | 89.56313


--

#### Figure 4 Data
- *Top 3 Permit Types Issued, Yearly*
- [back to figure](#figure-4)

| Year  | Construction Equipment | Equipment Work |  Plumbing|
| :--:  | -----:                 | -----:         | ---:     |          
|2000   |13.569                  |          44.797|  20.807
|2001   |14.418                  |          44.733|  21.625
|2002   |16.969                  |          44.827|  22.798
|2003   |19.812                  |          45.836|  25.495
|2004   |23.701                  |          50.635|  27.585
|2005   |28.524                  |          53.444|  29.536
|2006   |32.166                  |          53.891|  30.14
|2007   |34.315                  |          58.221|  29.496
|2008   |29.978                  |          60.043|  30.445
|2009   |24.86                   |          57.115|  29.677
|2010   |24.361                  |          59.017|  28.937
|2011   |25.051                  |          66.12 |  30.004
|2012   |26.38                   |          68.324|  29.076
|2013   |28.199                  |          75.961|  31.998
|2014   |28.746                  |          80.712|  33.718
|2015   |29.4                    |          85.193|  35.743
|2016   |30.295                  |          91.03 |  36.585
|2017   |29.511                  |          92.948|  38.22





--

#### Figure 5 Data
- *Yearly Ratios, Over Time: Complaints, Violations; to Permits*
- [back to figure](#figure-5)

| Year | Complaints to Permits | Violations (ECB) to Permits |
| :--: | --------------------: | --------------------------: |
| 2000 |       0.428785        |       0.404252              |
| 2001 |       0.426793        |       0.397804              |
| 2002 |       0.464492        |       0.362420              |
| 2003 |       0.510151        |       0.367397              |
| 2004 |       0.568327        |       0.326716              |
| 2005 |       0.725399        |       0.327783              |
| 2006 |       0.724703        |       0.331622              |
| 2007 |       0.816727        |       0.367930              |
| 2008 |       0.950928        |       0.511671              |
| 2009 |       0.937453        |       0.578478              |
| 2010 |       0.833188        |       0.506844              |
| 2011 |       0.721119        |       0.401416              |
| 2012 |       0.675785        |       0.317591              |
| 2013 |       0.590384        |       0.283737              |
| 2014 |       0.595361        |       0.305029              |
| 2015 |       0.558162        |       0.287783              |
| 2016 |       0.600395        |       0.313278              |
| 2017 |       0.640765        |       0.400418              |
| 2018 |       0.661648        |       0.451861              |
| 2019 |       0.742623        |       0.482331              |

--

#### Figure 6 Data
- *Top 3 Complaint Types, Yearly*
- [back to figure](#figure-6)

| Year | Illegal Conversion | Permit – None | Elevator (Old Category) | Elevator (New Category)    |
| :--: | -----------------: | ------------: | ----------------------: | -------------------------: |
| 2006 |   19.424           |     15.571    |     9.281               |   NaN                      |
| 2007 |   22.739           |     18.483    |     9.413               |   NaN                      |
| 2008 |   21.966           |     19.855    |     9.431               |   NaN                      |
| 2009 |   23.409           |     16.396    |     8.250               |   NaN                      |
| 2010 |   18.370           |     18.454    |     7.082               |   NaN                      |
| 2011 |   15.745           |     19.580    |     6.433               |   NaN                      |
| 2012 |   13.977           |     15.190    |     7.002               |   NaN                      |
| 2013 |   14.273           |     12.143    |     7.520               |   NaN                      |
| 2014 |   14.568           |     13.508    |     8.034               |   NaN                      |
| 2015 |   13.527           |     13.366    |     8.952               |   NaN                      |
| 2016 |   14.622           |     15.110    |     11.572              |   NaN                      |
| 2017 |   17.179           |     15.566    |     11.992              |   NaN                      |
| 2018 |   17.107           |     14.370    |     NaN                 |   9.674                    |
| 2019 |   15.603           |     15.916    |     NaN                 |   10.643                   |

--

#### Figure 7 Data
- *Top 3 ECB Violation Types, Yearly*
- [back to figure](#figure-7)

| Year | Construction | Elevators | Quality of Life | Unknown   |
| :--: | ---------:   | --------: | -------------:  | --------: |
| 2006 |   25.230     |  6.217    |     5.475       |   2.040   |
| 2007 |   26.208     |  7.923    |     5.385       |   4.113   |
| 2008 |   40.431     |  10.373   |     3.161       |   9.052   |
| 2009 |   45.217     |  7.888    |     0.627       |   15.514  |
| 2010 |   40.791     |  5.757    |     0.604       |   14.334  |
| 2011 |   31.625     |  4.972    |     0.363       |   15.344  |
| 2012 |   24.287     |  4.065    |     0.163       |   14.305  |
| 2013 |   24.700     |  4.276    |     0.252       |   13.566  |
| 2014 |   30.764     |  4.216    |     0.429       |   12.234  |
| 2015 |   38.801     |  3.957    |     0.633       |   4.648   |
| 2016 |   44.424     |  6.653    |     0.807       |   2.095   |
| 2017 |   58.225     |  6.925    |     1.058       |   5.405   |
| 2018 |   67.900     |  6.088    |     0.922       |   3.980   |
| 2019 |   71.532     |  5.439    |     1.491       |   8.614   |

--

#### Figure 8 Data
- *Imposed ECB Penalties, Yearly: Mean vs. Median*
- [back to figure](#figure-8)

|Issue Year| Mean       |Median|Hearing Year | Mean             |Median|
|:-------: |:----------:|:---: |:----------: |:----------------:|:---: |
|2000      | 822.829466 |250.0 |    2000     |843.5884788478850	| 250.0
|2001      | 692.964526 |200.0 |    2001     |678.3566753627170	| 180.0
|2002      | 729.038357 |250.0 |    2002     |745.3990105936440	| 250.0
|2003      | 700.333407 |250.0 |    2003     |701.9465517621390	| 240.0
|2004      | 802.410591 |350.0 |    2004     |762.2334090558210	| 250.0
|2005      | 957.911172 |350.0 |    2005     |881.2444449247800	| 350.0
|2006      | 1138.404550|480.0 |    2006     |1058.6154163742200| 400.0
|2007      | 1175.498205|500.0 |    2007     |1149.1942861513700| 500.0
|2008      | 1308.193930|500.0 |    2008     |1210.7764213892600| 500.0
|2009      | 1859.663222|500.0 |    2009     |1542.9416647181100| 500.0
|2010      | 2380.383830|500.0 |    2010     |2315.5780727143900| 800.0
|2011      | 2620.992368|800.0 |    2011     |2546.2986676269400| 800.0
|2012      | 2661.495654|500.0 |    2012     |2497.6836732759600| 500.0
|2013      | 2310.251285|500.0 |    2013     |2416.036066691030	| 500.0
|2014      | 2367.043118|800.0 |    2014     |2349.4754807673100| 800.0
|2015      | 2366.361085|800.0 |    2015     |2459.605247914740	| 800.0
|2016      | 1871.004867|800.0 |    2016     |1956.63924582552	| 800.0
|2017      | 1762.884373|800.0 |    2017     |1710.841972509570	| 600.0
|2018      | 2387.357734|800.0 |    2018     |2134.2540692700700| 800.0
|2019      | 2622.369828|1250.0|    2019     |2476.1035762572300| 800.0


#### Figure 9 Data
- *Paid ECB Penalties, Yearly: Mean vs. Median*
- [back to figure](#figure-9)

|Issue Year| Mean               |Median|Hearing Year | Mean             |Median|
|:-------: |:------------------:|:---: |:----------: |:----------------:|:---: |
|2000      | 420.31777187424    |0.0   |    2000     |418.9148069949860	| 0.0
|2001      | 392.00367364892200 |0.0   |    2001     |379.6388663096720	| 0.0
|2002      | 418.0449115022440  |0.0   |    2002     |430.89797971217300| 0.0
|2003      | 404.7831588996700  |0.0   |    2003     |411.7189105375680	| 0.0
|2004      | 449.83422356656800 |130.0 |    2004     |426.1413630047870	| 130.0
|2005      | 524.0713415724850  |130.0 |    2005     |488.05953224969800| 130.0
|2006      | 553.7166212006900  |180.0 |    2006     |537.31712831840200| 130.0
|2007      | 570.222657277802   |180.0 |    2007     |551.35253317780200| 180.0
|2008      | 653.3622019755650  |200.05|    2008     |568.10924556440300| 180.0
|2009      | 817.5204583651650  |200.0 |    2009     |696.82715263704900| 200.0
|2010      | 865.5988876821020  |100.0 |    2010     |896.39615858518100| 250.0
|2011      | 847.4791803534040  |0.0   |    2011     |897.44453510983300| 200.0
|2012      | 835.1980980645720  |0.0   |    2012     |835.44033324487500| 0.0
|2013      | 822.7347117296220  |200.0 |    2013     |837.3819082837040	| 100.0
|2014      | 893.4595888281020  |250.0 |    2014     |882.41543356069800| 250.0
|2015      | 947.3545804647990  |400.0 |    2015     |966.5381605267200	| 400.0
|2016      | 894.4359687823770  |250.0 |    2016     |918.3032983302060 | 250.0
|2017      | 819.444093040896   |0.0   |    2017     |818.7907139010900	| 0.0
|2018      | 748.740919622064   |0.0   |    2018     |795.53807542021900| 0.0
|2019      | 305.1469738146550  |0.00  |    2019     |579.71646015236200| 0.0

#### Figure 10 Data
- *ECB Penalties Yearly: Number Issued, by Issue Date; Paid-to-Imposed Ratio, by Hearing Date*
- [back to figure](#figure-10)

|Year| Ratio (%)|  Violations (K)|
|:--:|:--------:|  :------------:|
|2000| 51.082003|	41.030       |    
|2001| 56.569082|	42.059       |    
|2002| 57.341964|	40.566       |   
|2003| 57.798636|	45.041       |   
|2004| 56.060355|	44.962       |    
|2005| 54.709806|	49.196       |
|2006| 48.639706|	51.687       |
|2007| 48.509020|	58.225       |
|2008| 49.943834|	76.940       |
|2009| 43.960672|	78.540       |
|2010| 36.363837|	69.054       |
|2011| 32.334286|	57.781       |
|2012| 31.380780|	47.173       |
|2013| 35.612347|	45.773       |
|2014| 37.745810|	52.095       |
|2015| 40.034236|	52.582       |
|2016| 47.805112|	59.838       |
|2017| 46.483145|	79.105       |
|2018| 31.362745|	88.482       |
|2019| 11.636306|	92.800       |

#### Figure 11 Data
- *Normalized Penalty Imposed Vs. Paid-to-Imposed Ratio, by Hearing Date, 2010 - 2020*
- [back to figure](#figure-11)

- Normalized Penalty Imposed  	

|Year |DEFAULT | IN VIOLATION |PENDING
|:---:|:------:|:------------:|:-----:
|2010 | 0.2551 |  0.2801      |0.0000 
|2011 | 0.2781 |  0.3061      |0.0000 
|2012 | 0.6381 |  0.3448      |NaN    
|2013 | 0.6153 |  0.3599      |0.0000 
|2014 | 0.5849 |  0.3880      |NaN    
|2015 | 0.5691 |  0.4068      |NaN    
|2016 | 0.5547 |  0.4058      |NaN    
|2017 | 0.5055 |  0.4449      |0.0015 
|2018 | 0.5220 |  0.4393      |0.0000 
|2019 | 0.5598 |  0.4103      |0.0002 

- Paid to Imposed Ratio

|Year |DEFAULT| IN VIOLATION| PENDING
|:---:|:-------:|:---------:|:--------:
|2010 |0.473319 | 0.838798  |0.000000
|2011 |0.322927 | 0.765718  |NaN
|2012 |0.129904 | 0.661808  |NaN
|2013 |0.132598 | 0.651158  |NaN
|2014 |0.151629 | 0.654419  |NaN
|2015 |0.173058 | 0.652355  |NaN
|2016 |0.203692 | 0.764692  |NaN
|2017 |0.174569 | 0.753715  |0.663402
|2018 |0.072933 | 0.668929  |NaN
|2019 |0.019203 | 0.480588  |0.022704


#### Figure 12 Data
- *Average Days for ECB to Hear a Violation: 2000 - 2019*
- [back to figure](#figure-12)


|Year | Mean     |Standard Deviation|Lower Bound|Upper Bound|
|:---:|:--------:|:----------:      |:--------: |:----------:|
|2000 |188.270972|	296.101184      |0          |  484.372157|
|2001 |167.616634|	254.693650      |0          |  419.692124|
|2002 |145.663659|	235.309539      |0          |  378.611099|
|2003 |139.183433|	212.915329      |0          |  352.098762|
|2004 |149.926249|	253.512591      |0          |  400.921935|
|2005 |164.968392|	263.639294      |0          |  428.607685|
|2006 |191.379515|	293.646556      |0          |  485.026071|
|2007 |200.772417|	288.510108      |0          |  488.59077 |
|2008 |205.966584|	278.333494      |0          |  484.300078|
|2009 |197.040387|	262.903058      |0          |  458.89321 | 
|2010 |167.696194|	261.700278      |0          |  429.047844|
|2011 |127.232758|	227.973652      |0          |  349.426485|
|2012 |113.836983|	195.856683      |0          |  300.167791|
|2013 |96.521071 |	146.241080      |0          |  237.947153|
|2014 |106.425972|	139.687556      |0          |  233.12733 |
|2015 |109.598323|	124.949972      |0          |  225.392506|
|2016 |108.916190|	108.286981      |4.268722   |  212.043781|
|2017 |123.004791|	105.602715      |21.932161  |  221.237261|
|2018 |122.736749|	92.508119       |34.920681  |  202.236819|
|2019 |126.714278|	74.348205       |47.913788  |  159.882269|


#### Figure 14 Data
- *Active and Resolved ECB Violations as of 2019, by Hearing Date*
- [back to figure](#figure-14)


|Year| Active |Resolved|Active to Total|	
|:--:|:------:|:------:|:-------------:|
|2000|3.228   |22.966  |12.32343284721690
|2001|4.864   |36.838  |11.663709174619900
|2002|4.985   |34.199  |12.722029399755000
|2003|5.275   |39.635  |11.745713649521300
|2004|5.585   |39.426  |12.408078025371600
|2005|6.124   |39.98   |13.283012319972200
|2006|7.175   |41.188  |14.835721522651600
|2007|8.572   |43.698  |16.39946431987760
|2008|11.047  |53.985  |16.98702177389590
|2009|12.52   |64.457  |16.264598516440000
|2010|14.146  |64.896  |17.896814351863600
|2011|14.177  |55.241  |20.42265694776570
|2012|10.77   |41.983  |20.415900517506100
|2013|9.454   |37.056  |20.326811438400300
|2014|10.361  |39.63   |20.725730631513700
|2015|12.11   |39.679  |23.38334395334920
|2016|13.87   |42.122  |24.77139591370200
|2017|18.659  |51.903  |26.443411467928900
|2018|26.092  |60.397  |30.167998242551100
|2019|32.187  |54.054  |37.32215535534140



#### Figure 15 Data
- *Paid-to-Imposed Ratio, Binned: 2016 - 2019*
- [back to figure](#figure-15)

|issue_date_year  |(0, 500] |(500, 1000] |(1000, 5000] |(5000, 10000]   |(10000, 50000] |(50000, 100000]|
|:---------------:|:-------:|:----------:|:-----------:|:-------------:|:-------------:|:--------------:|		
|2016	          |0.883693	|0.855209	 |0.620740	   |0.442213	   | 0.206192	   |     0.087941
|2017	          |0.850331	|0.792443	 |0.575757	   |0.409464	   | 0.203460	   |     0.083333
|2018	          |0.782018	|0.773744	 |0.598378	   |0.234511	   | 0.086297	   |     0.020094
|2019	          |0.562664	|0.501429	 |0.224271	   |0.088075	   | 0.026535	   |     0.000000


#### Figure 17 Data
- *DoB Violation Issuances, Monthly*
- [back to figure](#figure-16)

| Date (2000 - 2009) | Issuances (k) | Date (2010 - 2019) | Issuances (k) |
| :----------------- | ------------: | :----------------- | ------------: |
| 2000-1             |  2.123        | 2010-1             |  2.690        |
| 2000-2             |  33.905       | 2010-2             |  2.576        |
| 2000-3             |  5.972        | 2010-3             |  4.211        |
| 2000-4             |  2.193        | 2010-4             |  4.916        |
| 2000-5             |  2.546        | 2010-5             |  4.319        |
| 2000-6             |  2.603        | 2010-6             |  4.946        |
| 2000-7             |  2.243        | 2010-7             |  5.077        |
| 2000-8             |  2.683        | 2010-8             |  4.835        |
| 2000-9             |  2.225        | 2010-9             |  4.981        |
| 2000-10            |  2.532        | 2010-10            |  10.466       |
| 2000-11            |  1.861        | 2010-11            |  5.184        |
| 2000-12            |  1.685        | 2010-12            |  7.405        |
| 2001-1             |  2.449        | 2011-1             |  6.142        |
| 2001-2             |  34.193       | 2011-2             |  4.131        |
| 2001-3             |  6.380        | 2011-3             |  4.874        |
| 2001-4             |  3.300        | 2011-4             |  4.309        |
| 2001-5             |  3.172        | 2011-5             |  4.740        |
| 2001-6             |  3.178        | 2011-6             |  5.733        |
| 2001-7             |  2.752        | 2011-7             |  5.183        |
| 2001-8             |  2.854        | 2011-8             |  5.535        |
| 2001-9             |  1.736        | 2011-9             |  4.844        |
| 2001-10            |  2.314        | 2011-10            |  4.756        |
| 2001-11            |  1.995        | 2011-11            |  4.885        |
| 2001-12            |  1.950        | 2011-12            |  33.762       |
| 2002-1             |  2.549        | 2012-1             |  7.807        |
| 2002-2             |  5.907        | 2012-2             |  4.969        |
| 2002-3             |  34.725       | 2012-3             |  4.796        |
| 2002-4             |  1.782        | 2012-4             |  4.183        |
| 2002-5             |  1.966        | 2012-5             |  7.824        |
| 2002-6             |  1.575        | 2012-6             |  3.891        |
| 2002-7             |  1.729        | 2012-7             |  3.756        |
| 2002-8             |  6.001        | 2012-8             |  6.442        |
| 2002-9             |  1.450        | 2012-9             |  3.931        |
| 2002-10            |  2.181        | 2012-10            |  9.046        |
| 2002-11            |  1.797        | 2012-11            |  3.596        |
| 2002-12            |  1.939        | 2012-12            |  3.546        |
| 2003-1             |  2.357        | 2013-1             |  8.039        |
| 2003-2             |  1.519        | 2013-2             |  3.929        |
| 2003-3             |  35.990       | 2013-3             |  22.026       |
| 2003-4             |  1.904        | 2013-4             |  3.803        |
| 2003-5             |  1.970        | 2013-5             |  3.862        |
| 2003-6             |  2.252        | 2013-6             |  5.713        |
| 2003-7             |  2.181        | 2013-7             |  4.694        |
| 2003-8             |  2.297        | 2013-8             |  6.075        |
| 2003-9             |  2.569        | 2013-9             |  4.409        |
| 2003-10            |  2.561        | 2013-10            |  4.618        |
| 2003-11            |  2.015        | 2013-11            |  3.551        |
| 2003-12            |  2.323        | 2013-12            |  4.939        |
| 2004-1             |  2.809        | 2014-1             |  5.804        |
| 2004-2             |  31.794       | 2014-2             |  3.417        |
| 2004-3             |  2.881        | 2014-3             |  13.461       |
| 2004-4             |  6.278        | 2014-4             |  3.982        |
| 2004-5             |  2.078        | 2014-5             |  39.463       |
| 2004-6             |  2.392        | 2014-6             |  5.096        |
| 2004-7             |  1.830        | 2014-7             |  4.481        |
| 2004-8             |  2.185        | 2014-8             |  3.479        |
| 2004-9             |  2.569        | 2014-9             |  3.829        |
| 2004-10            |  2.721        | 2014-10            |  10.635       |
| 2004-11            |  6.155        | 2014-11            |  3.662        |
| 2004-12            |  2.698        | 2014-12            |  4.469        |
| 2005-1             |  30.441       | 2015-1             |  2.780        |
| 2005-2             |  2.739        | 2015-2             |  3.261        |
| 2005-3             |  3.263        | 2015-3             |  22.767       |
| 2005-4             |  3.797        | 2015-4             |  3.530        |
| 2005-5             |  3.671        | 2015-5             |  4.936        |
| 2005-6             |  3.533        | 2015-6             |  10.186       |
| 2005-7             |  2.922        | 2015-7             |  4.228        |
| 2005-8             |  3.662        | 2015-8             |  4.492        |
| 2005-9             |  3.188        | 2015-9             |  3.300        |
| 2005-10            |  7.880        | 2015-10            |  18.763       |
| 2005-11            |  2.811        | 2015-11            |  4.159        |
| 2005-12            |  2.685        | 2015-12            |  4.091        |
| 2006-1             |  29.530       | 2016-1             |  4.141        |
| 2006-2             |  2.848        | 2016-2             |  5.454        |
| 2006-3             |  3.111        | 2016-3             |  5.441        |
| 2006-4             |  2.435        | 2016-4             |  4.433        |
| 2006-5             |  3.072        | 2016-5             |  4.399        |
| 2006-6             |  3.470        | 2016-6             |  11.082       |
| 2006-7             |  3.616        | 2016-7             |  3.842        |
| 2006-8             |  4.221        | 2016-8             |  5.005        |
| 2006-9             |  4.380        | 2016-9             |  3.931        |
| 2006-10            |  4.596        | 2016-10            |  3.388        |
| 2006-11            |  4.786        | 2016-11            |  18.943       |
| 2006-12            |  3.649        | 2016-12            |  10.193       |
| 2007-1             |  31.684       | 2017-1             |  18.253       |
| 2007-2             |  3.541        | 2017-2             |  22.102       |
| 2007-3             |  4.939        | 2017-3             |  3.955        |
| 2007-4             |  8.444        | 2017-4             |  3.274        |
| 2007-5             |  4.312        | 2017-5             |  5.571        |
| 2007-6             |  5.269        | 2017-6             |  4.494        |
| 2007-7             |  4.442        | 2017-7             |  4.046        |
| 2007-8             |  5.107        | 2017-8             |  4.788        |
| 2007-9             |  5.060        | 2017-9             |  10.928       |
| 2007-10            |  5.140        | 2017-10            |  4.157        |
| 2007-11            |  10.118       | 2017-11            |  4.720        |
| 2007-12            |  4.617        | 2017-12            |  4.084        |
| 2008-1             |  32.876       | 2018-1             |  17.802       |
| 2008-2             |  5.238        | 2018-2             |  4.370        |
| 2008-3             |  11.259       | 2018-3             |  5.077        |
| 2008-4             |  6.257        | 2018-4             |  23.655       |
| 2008-5             |  6.160        | 2018-5             |  6.861        |
| 2008-6             |  5.919        | 2018-6             |  4.272        |
| 2008-7             |  5.457        | 2018-7             |  5.544        |
| 2008-8             |  4.910        | 2018-8             |  3.754        |
| 2008-9             |  4.543        | 2018-9             |  3.565        |
| 2008-10            |  4.857        | 2018-10            |  4.149        |
| 2008-11            |  3.940        | 2018-11            |  3.090        |
| 2008-12            |  3.982        | 2018-12            |  2.711        |
| 2009-1             |  31.115       | 2019-1             |  4.668        |
| 2009-2             |  6.654        | 2019-2             |  4.457        |
| 2009-3             |  3.607        | 2019-3             |  6.024        |
| 2009-4             |  3.440        | 2019-4             |  11.889       |
| 2009-5             |  3.129        | 2019-5             |  13.596       |
| 2009-6             |  3.662        | 2019-6             |  4.210        |
| 2009-7             |  3.509        | 2019-7             |  4.242        |
| 2009-8             |  3.250        | 2019-8             |  7.003        |
| 2009-9             |  3.159        | 2019-9             |  16.927       |
| 2009-10            |  2.996        | 2019-10            |  6.355        |
| 2009-11            |  2.525        | 2019-11            |  21.825       |
| 2009-12            |  29.633       | 2019-12            |  3.924        |




</font>
