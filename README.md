# onlinequakermeetings.com
Source code for an directory of online Quaker meetings.

The first goal for this website is to be a simple list of online meetings and discussion groups.

**To-do** (in terms of priority!)
* Add **time/date data** for meetings. This needs some engineering work because Meetings happen across time zones.
 * A solution might start with a list of days of the week and times in UTC.
* Revise existing code for improvements.
* Create pages filtering the websites in different ways.
* Add other types of social group, discussion groups.
* Guides to using chat software used for meetings (Zoom, Discord, Skype, etc.)
* Search functionality

**Already done**
* Write HTML template for listing meetings in categories
* Write CSS to make things look good & be usable
* Migrate site to Flask, replicating initial functionality, but allowing me to update the website through updating a CSV.

**Flask site features**
* HTML minifying through a build script
* Build script creates static site using Frozen-Flask
* Ways to represent and manipulate collections of meetings
* Load meetings data from CSV

It should contain information like the physical 'locality' of the online meeting/discussion group, what software is used to run meetings, and when those meetings take place.

Want to contribute? Please make sure any code contributions work on old devices and slow connections (standards pending) and keep an eye on [WCAG accessibility standards](https://www.w3.org/TR/WCAG20/) (this project aims to reach AAA standards, the standard set for government websites).

The website should work fine without Javascript.

To get your meeting added or suggest features, make an issue on Github or email me at clarkseanor@gmail.com.
