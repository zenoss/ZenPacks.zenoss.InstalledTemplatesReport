# ZenReports.Utils contains some useful helpers for creating records to return.
from Products.ZenReports.Utils import Record


# The class name must match the filename.
class installedTemplatesPlugin(object):

    """
    def index_mapping(self, sort_index, unsorted_list):

        sorted_list = [unsorted_list[x] for x in index]

        return sorted_list
    """

    def sort_template_list(self, primary_sort, secondary_sort, tertiary,
                           description, dsmap, thmap, gdmap, url):
        output = []
        temp_list = []
        sort_index = []
        pre_primary = []
        primary = []
        secondary = []

        temp_list = [x + '!' + y for x, y in zip(primary_sort, secondary_sort)]
        sort_index = sorted(range(len(temp_list)), key=lambda k: temp_list[k])
        temp_list.sort()

        for element in temp_list:
            pre_primary.append(element.split("!", 1)[0])
            secondary.append(element.split("!", 1)[1])

        for item in pre_primary:
            if item not in primary:
                primary.append(item)
            else:
                primary.append(None)

        tertiary = [tertiary[x] for x in sort_index]
        description = [description[x] for x in sort_index]
        dsmap = [dsmap[x] for x in sort_index]
        thmap = [thmap[x] for x in sort_index]
        gdmap = [gdmap[x] for x in sort_index]
        url = [url[x] for x in sort_index]

        for x in xrange(len(primary)):
            output.append(Record(
                primary=primary[x],
                secondary=secondary[x],
                tertiary=tertiary[x],
                template_description=description[x],
                datasources_info=dsmap[x],
                thresholds_info=thmap[x],
                graphdefs_info=gdmap[x],
                zenpack_url=url[x],
            ))

        return output

    # The run method will be executed when your report calls the plugin.
    def run(self, dmd, args):
        report = []

        # Place template, device and zenpack in list to help categorize in
        # future (by sorting)
        template_list = []
        device_list = []
        zenpack_list = []

        description_map = []
        datasource_map = []
        threshold_map = []
        graphdef_map = []

        datasources_list = []
        thresholds_list = []
        graphdefs_list = []

        zenpack_url_list = []

        for template in dmd.Devices.getAllRRDTemplates():
            datasources_list = []
            thresholds_list = []
            graphdefs_list = []

            if (template.pack() == None):
                zenpack_name = "Core"
                zenpack_url = None
            else:
                zenpack_name = template.pack().id
                zenpack_url = template.pack().urlLink()

            for datasource in template.datasources():
                datapoints_list = []
                if datasource is None:
                    datasources_list = None
                else:
                    for datapoint in datasource.datapoints():
                        datapoints_list.append(Record(
                            datapoint_id=datapoint.id,
                            datapoint_type=datapoint.rrdtype,
                            datapoint_alias=datapoint.aliases(),
                            datapoint_description=datapoint.description,
                        ))

                    datasources_list.append(Record(
                        datasource_id=datasource.id,
                        datasource_ssh_enabled=datasource.enabled,
                        datasource_type=datasource.sourcetype,
                        datasource_description=datasource.description,
                        datapoints_info=datapoints_list,
                    ))

            for threshold in template.thresholds():
                if threshold is None:
                    thresholds_list = None
                else:
                    try:
                        threshold_min = threshold.minval
                    except:
                        threshold_min = None

                    try:
                        threshold_max = threshold.maxval
                    except:
                        threshold_max = None

                    try:
                        threshold_type = threshold.factory_type_information[0]['actions'][0]['name']
                    except:
                        threshold_type = None

                    thresholds_list.append(Record(
                        threshold_id=threshold.id,
                        threshold_type=threshold_type,
                        threshold_min=threshold_min,
                        threshold_max=threshold_max,
                        threshold_description=threshold.description,
                    ))

            for graphDef in template.graphDefs():
                graphpoints_list = []
                if graphDef is None:
                    graphdefs_list = None
                else:
                    for graphPoint in graphDef.graphPoints():
                        graphpoints_list.append(Record(
                            graphPoint_id=graphPoint.id,
                            graphPoint_type=graphPoint.getType(),
                            graphPoint_associated="<--Place Holder-->",
                            graphPoint_description=graphPoint.description,
                        ))

                    graphdefs_list.append(Record(
                        graphDef_id=graphDef.id,
                        graphDef_unit=graphDef.units,
                        graphDef_description=graphDef.description,
                        graphpoints_info=graphpoints_list,
                    ))

            template_list.append(template.id)
            device_list.append(template.getOrganizerName())
            zenpack_list.append(zenpack_name)
            zenpack_url_list.append(zenpack_url)
            description_map.append(template.description)
            datasource_map.append(datasources_list)
            threshold_map.append(thresholds_list)
            graphdef_map.append(graphdefs_list)

        template_srt = self.sort_template_list(
            template_list, device_list, zenpack_list, description_map,
            datasource_map, threshold_map, graphdef_map, zenpack_url_list)
        device_srt = self.sort_template_list(
            device_list, template_list, zenpack_list, description_map,
            datasource_map, threshold_map, graphdef_map, zenpack_url_list)
        zenpack_srt = self.sort_template_list(
            zenpack_list, template_list, device_list, description_map,
            datasource_map, threshold_map, graphdef_map, zenpack_url_list)

        report.append(Record(
            template_sort=template_srt,
            device_sort=device_srt,
            zenpack_sort=zenpack_srt,
        ))

        return report