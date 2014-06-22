# Introduction

[A recent article on TheStreet](http://www.thestreet.com/story/12747294/1/the-13-most-dangerous-cities-in-america.html), "The 13 Most Dangerous Cities in America", claimed that my hometown of Springfield, MO is the #1 most dangerous place to live in the country. That surprised a lot of people, and I certainly never thought of it as a particularly rough place. Having recently moved near Oakland, CA (which is only #4 on TheStreet's list) and driving through it every day, I was skeptical of their results and wanted to investigate for myself.

Although I no longer live in Springfield, I have family and many friends who do and I wanted to get an accurate idea of its crime rates.

# Methodology

I downloaded the FBI's report, [January to June 2013: Offenses Reported to Law Enforcement by State by City 100,000 and over in population](http://www.fbi.gov/about-us/cjis/ucr/crime-in-the-u.s/2013/preliminary-semiannual-uniform-crime-report-january-june-2013/tables/Table_4_January_to_June_2012-2013_Offenses_Reported_to_Law_Enforcement_by_State_by_City.xls/view), loaded it into Numbers 3.2, and exported it to a CSV (included in this repository) for easier analysis. City and state names are left unchanged from the spreadsheet for easy referencing.

My original goal was to use the FBI's numbers as-is with no modification, but that wasn't entirely possible:

## Phoenix

Phoenix, AZ didn't report aggravated assaults in 2013, so I copied their number from 2012 under the assumption that it probably wouldn't change drastically from year to year.

## Chicaco

Chicago, IL didn't report rapes in 2012 or 2013. I assumed (*please correct me if I'm wrong!*) that their rate would be similar to the national average, and filled in the missing value with the national rate (calculated from other cities in this table) multiplied by Chicago's population.

Without including rape in the statistics, Chicago ranks 115 overall. Estimating its rape count by the described method would result it in ranking #113 by rape rate, so that seems like a plausible first guess. In any case, Chicago is so far down in the rankings (both overall and only by rape) that the actual rate would have to be twice the estimate to make it into the top 20.

# Analysis

## Reproducing TheStreet's results

My first goal was to reproduce the results from TheStreet's report. That was easy: I just summed all crime rates and got an exact match with their numbers. The main difference was that their "total reported instances" seems to have double-counted all values (because they added the "violent crime" and "property crime" summary columns into the totals). However, since they did this for every city the relative rankings remain unchanged.

| Rank | City | State | TheStreet's rate |
| ---- | ---- | ----- | ------: |
| 1 | SPRINGFIELD | MISSOURI5 | 5032 |
| 2 | SPOKANE | WASHINGTON | 4751 |
| 3 | LITTLE ROCK | ARKANSAS5 | 4441 |
| 4 | OAKLAND | CALIFORNIA | 4095 |
| 5 | ST. LOUIS | MISSOURI5 | 3876 |
| 6 | DETROIT | MICHIGAN5 | 3785 |
| 7 | ORLANDO | FLORIDA5  | 3755 |
| 8 | MEMPHIS | TENNESSEE5 | 3731 |
| 9 | SALT LAKE CITY | UTAH5 | 3718 |
| 10 | ATLANTA | GEORGIA | 3715 |
| 11 | PUEBLO | COLORADO5 | 3692 |
| 12 | BIRMINGHAM3 | ALABAMA | 3668 |
| 13 | CHATTANOOGA | TENNESSEE5 | 3564 |
| 14 | TUCSON6, 8 | ARIZONA | 3528 |
| 15 | CLEVELAND5 | OHIO | 3449 |
| 16 | TACOMA5 | WASHINGTON | 3437 |
| 17 | KNOXVILLE | TENNESSEE5 | 3408 |
| 18 | LAFAYETTE | LOUISIANA | 3272 |
| 19 | EVERETT | WASHINGTON | 3241 |
| 20 | BEAUMONT | TEXAS | 3239 |

## By property crimes

Springfield, MO ranks #1 nationally in property crimes, competing only with Spokane, WA. Its reported property rate is about 50% higher than #20 Fayetteville, NC.

| Rank | City | State | Property crime rate |
| ---- | ---- | ----- | ------: |
| 1 | SPRINGFIELD | MISSOURI5 | 4468 |
| 2 | SPOKANE | WASHINGTON | 4412 |
| 3 | LITTLE ROCK | ARKANSAS5 | 3801 |
| 4 | SALT LAKE CITY | UTAH5 | 3341 |
| 5 | ORLANDO | FLORIDA5  | 3291 |
| 6 | PUEBLO | COLORADO5 | 3265 |
| 7 | TUCSON6, 8 | ARIZONA | 3211 |
| 8 | ST. LOUIS | MISSOURI5 | 3117 |
| 9 | ATLANTA | GEORGIA | 3099 |
| 10 | CHATTANOOGA | TENNESSEE5 | 3077 |
| 11 | OAKLAND | CALIFORNIA | 3068 |
| 12 | EVERETT | WASHINGTON | 3053 |
| 13 | KNOXVILLE | TENNESSEE5 | 3013 |
| 14 | TACOMA5 | WASHINGTON | 2987 |
| 15 | BIRMINGHAM3 | ALABAMA | 2980 |
| 16 | LAFAYETTE | LOUISIANA | 2929 |
| 17 | COLUMBUS | GEORGIA | 2926 |
| 18 | GLENDALE | ARIZONA | 2923 |
| 19 | MEMPHIS | TENNESSEE5 | 2907 |
| 20 | FAYETTEVILLE | NORTH CAROLINA | 2901 |

## By violent crimes (overall)

There are no surprises here. Cities with violent reputations top the list.

| Rank | City | State | Violent crime rate |
| ---- | ---- | ----- | ------: |
| 1 | OAKLAND | CALIFORNIA | 1027 |
| 2 | FLINT | MICHIGAN5 | 1021 |
| 3 | DETROIT | MICHIGAN5 | 969 |
| 4 | MEMPHIS | TENNESSEE5 | 824 |
| 5 | ST. LOUIS | MISSOURI5 | 759 |
| 6 | BALTIMORE | MARYLAND | 692 |
| 7 | BIRMINGHAM3 | ALABAMA | 688 |
| 8 | CLEVELAND5 | OHIO | 685 |
| 9 | ROCKFORD5 | ILLINOIS | 646 |
| 10 | LITTLE ROCK | ARKANSAS5 | 640 |
| 11 | STOCKTON | CALIFORNIA | 634 |
| 12 | MILWAUKEE | WISCONSIN5 | 623 |
| 13 | ATLANTA | GEORGIA | 616 |
| 14 | RICHMOND | CALIFORNIA | 615 |
| 15 | NEW HAVEN5 | CONNECTICUT | 610 |
| 16 | KANSAS CITY | MISSOURI5 | 604 |
| 17 | NEWARK | NEW JERSEY | 597 |
| 18 | BUFFALO | NEW YORK6 | 592 |
| 19 | HARTFORD | CONNECTICUT | 584 |
| 20 | INDIANAPOLIS5 | INDIANA | 582 |

## By assault and robbery

Because assault and robbery are so much more common than murder and rape, ranking by only those statistics added together yields almost the same list as when ordering by all violent crimes.

| Rank | City | State | Assault and robbery rate |
| ---- | ---- | ----- | ------: |
| 1 | OAKLAND | CALIFORNIA | 993 |
| 2 | FLINT | MICHIGAN5 | 915 |
| 3 | DETROIT | MICHIGAN5 | 903 |
| 4 | MEMPHIS | TENNESSEE5 | 783 |
| 5 | ST. LOUIS | MISSOURI5 | 692 |
| 6 | BALTIMORE | MARYLAND | 649 |
| 7 | BIRMINGHAM3 | ALABAMA | 632 |
| 8 | CLEVELAND5 | OHIO | 626 |
| 9 | STOCKTON | CALIFORNIA | 613 |
| 10 | LITTLE ROCK | ARKANSAS5 | 602 |
| 11 | ATLANTA | GEORGIA | 595 |
| 12 | ROCKFORD5 | ILLINOIS | 594 |
| 13 | RICHMOND | CALIFORNIA | 586 |
| 14 | MILWAUKEE | WISCONSIN5 | 582 |
| 15 | NEWARK | NEW JERSEY | 573 |
| 16 | NEW HAVEN5 | CONNECTICUT | 570 |
| 17 | HARTFORD | CONNECTICUT | 561 |
| 18 | BUFFALO | NEW YORK6 | 557 |
| 19 | MIAMI | FLORIDA5  | 555 |
| 20 | KANSAS CITY | MISSOURI5 | 551 |

## By rape and murder

When considering only the most violent crimes - rape and murder - the rankings change quite a bit. Springfield, MO jumps to near the top and a few new cities appear.

| Rank | City | State | Rape and murders rate |
| ---- | ---- | ----- | ------: |
| 1 | FLINT | MICHIGAN5 | 104 |
| 2 | SPRINGFIELD | MISSOURI5 | 85 |
| 3 | PUEBLO | COLORADO5 | 77 |
| 4 | ANCHORAGE5 | ALASKA | 69 |
| 5 | LANSING | MICHIGAN5 | 68 |
| 6 | DETROIT | MICHIGAN5 | 65 |
| 7 | ST. LOUIS | MISSOURI5 | 65 |
| 8 | CLEVELAND5 | OHIO | 57 |
| 9 | BIRMINGHAM3 | ALABAMA | 55 |
| 10 | SALT LAKE CITY | UTAH5 | 54 |
| 11 | MINNEAPOLIS | MINNESOTA5 | 52 |
| 12 | ROCKFORD5 | ILLINOIS | 51 |
| 13 | KANSAS CITY | MISSOURI5 | 51 |
| 14 | TULSA | OKLAHOMA | 51 |
| 15 | TALLAHASSEE  | FLORIDA5  | 49 |
| 16 | WARREN | MICHIGAN5 | 46 |
| 17 | PHILADELPHIA | PENNSYLVANIA5 | 46 |
| 18 | SOUTH BEND5 | INDIANA | 45 |
| 19 | COLORADO SPRINGS | COLORADO5 | 44 |
| 20 | AKRON5 | OHIO | 44 |

## By rape alone

Surprisingly (to me), the lists for rape alone and murder alone are quite different. Different cities have distinctly different crime profiles. Unfortunately, Springfield rises to the top of the rape alone list.

| Rank | City | State | Rape alone rate |
| ---- | ---- | ----- | ------: |
| 1 | SPRINGFIELD | MISSOURI5 | 82 |
| 2 | FLINT | MICHIGAN5 | 81 |
| 3 | PUEBLO | COLORADO5 | 77 |
| 4 | ANCHORAGE5 | ALASKA | 66 |
| 5 | LANSING | MICHIGAN5 | 63 |
| 6 | SALT LAKE CITY | UTAH5 | 53 |
| 7 | CLEVELAND5 | OHIO | 51 |
| 8 | ST. LOUIS | MISSOURI5 | 50 |
| 9 | MINNEAPOLIS | MINNESOTA5 | 49 |
| 10 | ROCKFORD5 | ILLINOIS | 48 |
| 11 | TALLAHASSEE  | FLORIDA5  | 46 |
| 12 | WARREN | MICHIGAN5 | 46 |
| 13 | DETROIT | MICHIGAN5 | 44 |
| 14 | SOUTH BEND5 | INDIANA | 43 |
| 15 | TULSA | OKLAHOMA | 43 |
| 16 | KANSAS CITY | MISSOURI5 | 42 |
| 17 | COLORADO SPRINGS | COLORADO5 | 41 |
| 18 | MANCHESTER | NEW HAMPSHIRE5 | 41 |
| 19 | LAKEWOOD | COLORADO5 | 40 |
| 20 | PHILADELPHIA | PENNSYLVANIA5 | 39 |

## Murder alone

With 3 murders per 100,000, Springfield isn't anywhere near the top 20 murderingest cities.

| Rank | City | State | Murder alone rate |
| ---- | ---- | ----- | ------: |
| 1 | FLINT | MICHIGAN5 | 23 |
| 2 | NEW ORLEANS | LOUISIANA | 21 |
| 3 | DETROIT | MICHIGAN5 | 21 |
| 4 | BIRMINGHAM3 | ALABAMA | 18 |
| 5 | BALTIMORE | MARYLAND | 18 |
| 6 | ST. LOUIS | MISSOURI5 | 15 |
| 7 | NEWARK | NEW JERSEY | 15 |
| 8 | MONTGOMERY | ALABAMA | 11 |
| 9 | OAKLAND | CALIFORNIA | 11 |
| 10 | BATON ROUGE | LOUISIANA | 11 |
| 11 | RICHMOND | CALIFORNIA | 10 |
| 12 | SAN BERNARDINO  | CALIFORNIA | 10 |
| 13 | VALLEJO | CALIFORNIA | 10 |
| 14 | JACKSON | MISSISSIPPI | 10 |
| 15 | CINCINNATI5 | OHIO | 10 |
| 16 | LITTLE ROCK | ARKANSAS5 | 9 |
| 17 | POMONA | CALIFORNIA | 9 |
| 18 | KANSAS CITY | KANSAS | 9 |
| 19 | KANSAS CITY | MISSOURI5 | 9 |
| 20 | MEMPHIS | TENNESSEE5 | 9 |

# Rankings for Springfield, MO by statistic

These are where Springfield, MO is ranked by each tracked statistic:

| Statistic | Rank |
| --------- | ---: |
| murder | 101 |
| aggravated assault | 13 |
| robbery | 64 |
| burglary | 24 |
| motor-vehicle-theft | 31 |
| rape | 1 |
| larceny-theft | 1 |
| murder, aggravated assault, robbery, burglary, motor-vehicle-theft, larceny-theft | 1 |
| murder, aggravated assault, robbery | 27 |
| murder, aggravated assault, robbery, rape | 22 |

Springfield's murder rates are about average, but rape, larceny, and assault rates are astonishingly high.

# Discussion

Several factors could potentially affect the numbers significantly. I'm not a sociologist so I don't personally know if (or how much) these factors could change the results.

## Reporting rates

It's possible that some residents of some cities are more likely to report crimes than those in other places, probably if they believe police are likely to do something about it. I have no idea how Springfield would fare here.

## Collecting accuracy

Cities have incentives to under-report actual crime rates to appear as safer than they really are. They also have incentives to over-report crime rates to demonstrate that they need to increase police budgets. I would suspect (but have no evidence) that Springfield would likely be in the former category and that actual crime rates would be higher.

# Conclusion

TheStreet wasn't *exactly* correct in calling Springfield, MO the most dangerous city in America, but it wasn't exactly wrong. According to FBI statistics, Springfield has an alarmingly high property crime rate. The overall violent crime rate there would rank it #22 nationally (#27 nationally if rape is excluded), but it wins the dishonor of having the highest rape ranking in the country.

# Reporting bugs

If I've made mistakes, please clone this repo, fix the problems you find, and submit a pull request. I want these results to be as accurate as possible and would appreciate the help.

# Author

This analysis was written by Kirk Strauser <[kirk@strauser.com](mailto:kirk@strauser.com)>.	
