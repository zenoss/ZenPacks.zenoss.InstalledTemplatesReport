Installed Templates Report
==========================

The InstalledTemplatesReport ZenPack provides a report of all the Monitoring Templates installed in a Zenoss instance.

[zenoss-toc]

Releases
--------

Version 1.1.2- <a rel="nofollow" class="external" href="http://wiki.zenoss.org/download/zenpacks/ZenPacks.zenoss.InstalledTemplatesReport/1.1.2/ZenPacks.zenoss.InstalledTemplatesReport-1.1.2.egg">Download</a>
: Released on 2018/12/05
: Compatible with Zenoss 6.2.x, 6.3.x and Zenoss Cloud</dd>

Background
----------

The ZenPack provides a report of all the Monitoring Templates installed in a Zenoss instance, drawing together many different attributes that are not otherwise found in a text format such as:

- Template Name
- Device Class
- ZenPack Name
- Datasources
- Thresholds
- Graph Definitions

The user has the ability to view the templates by sorting through Template Name, Device Class or ZenPack Name.

## Usage

1. Click Reports
2. Under Reports, expand Monitoring Capabilities Reports
3. Select Installed Templates to generate a report for all Templates in your Zenoss instance

<br clear=all>

## Sample Report

[Report_Example.png]: /sites/default/files/zenpack/InstalledTemplateReports/Report_Example.png
[![][Report_Example.png]][Report_Example.png]

<br clear=all>

## Changes

1.1.2

-   Fixed scroll position in report's layout. (ZPS-4137)
-   Fix PDF export feature. (ZPS-4917)
-   Tested with Zenoss Resource Manager 6.3.0 and Zenoss Cloud.

1.1.1

-   Fixed PTRuntimeError in 4.2.5. (ZEN-24616)

1.1.0

-   Added ability to export Report to PDF.
