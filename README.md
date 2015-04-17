# ZenPacks.zenoss.InstalledTemplatesReport

=====================
Installed Templates ZenPack 
=====================

Description
===========

The ZenPack provides a report of all the Monitoring Templates installed in you Zenoss Box, drawing together many different attributes that are not otherwise find in a text format such as:

Template Name
Device Class
ZenPack Name
Description
DataSources - DataPoints
Thresholds
GraphDefinitions

The user has the ability to view the Templates by sorting through Template Name, Device Class or ZenPack Name.


Requirements & Dependencies
===========================

    * Zenoss Versions Supported: 4.2 and above
    * External Dependencies: None
    * ZenPack Dependencies: None
    * Installation Notes: Restart zenhub and zopectl
    * Configuration:

Components
==========

No device clases or components are added.


General Comments
================

The ZenPack adds a report, Installed Templates, under REPORTS -> Monitoring Capabilites Report .


ZenPack installation
======================

Normal Installation (packaged egg)
----------------------------------
Copy the downloaded .egg to your Zenoss server and run the following commands as the zenoss
user::

   zenpack --install <package.egg>
   zenhub restart
   zopectl restart

Developer Installation (link mode)
----------------------------------
If you wish to further develop and possibly contribute back to this
ZenPack you should clone the git repository, then install the ZenPack in
developer mode::

   zenpack --link --install <package>
   zenhub restart
   zopectl restart



Screenshots
===========
|lotschy|


Acknowledgements
================
