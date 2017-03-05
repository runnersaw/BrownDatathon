# BrownDatathon

Brown Datathon work. By Sawyer Vaughan, Ryan Louie, James Jang, and Chris Wallace

## Motivation

For the Brown Datathon, we decided to investigate the Global Terrorism Database (GTD). Obviously terrorism is a heavy subject and has been a large focus of our government and politics, especially within the last 15 years and the events of 9/11, the Afghanistan war, the Iraq war, and many of the terror attacks that have occured even within the past year.

We were interested in looking at this data because we feel that it is very important to understand if we want to make a positive change in this space. In addition, with much of the rhetoric in the most recent election campaign revolving around immigration and terrorism, we felt that it was important to challenge assumptions that we make about terrorism and why it happens.

## Work

### Determining Origin

We were interested in investigating the countries that terrorism originates from. To do this, we had to construct data about where attacks originate from. The GTD doesn't include this data, so we needed to determine where attacks originated from. 

First, the GTD includes a field indicating whether the attack was international or not. If the attack was not international, then that is the country of origin of the attack. Otherwise, we decided that we would use the group's location as the origin of the attack. Obviously it is not always correct that attackers are of the nationality of the group's location. However, we decided to investigate where the ideas responsible for the terrorism originated.

To determine the group's location, we used the median latitude and longitude of their attacks to determine the country of origin. The assumption that the median latitude and location are in the country of origin holds true if a majority of the group's attacks are in the country that it originates from. To prove this assumption correct, we plotted the amount of international and domestic attacks for each group. There were very few groups in which the number of international attacks was even close to the number of domestic attacks, so this assumption holds true for almost every group. 

*TODO: Plot here*

### Augmenting Data

In order to investigate the factors common in countries with high rates of terrorism, we needed to augment our data with other relevant data about the countries that attacks originate from. We chose the augmented data through a combination of what we believed would be relevant or correlated factors and which data was publicly available. We ended up augmenting our data with the following data about the origin country:

- GNI
- [Polity Score](http://www.systemicpeace.org/polity/polity4.htm)
- Recent Conflicts (Did the country have conflicts within the past 5 years?)



