#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#
# plugin to send the timely health beep to monitoring framework
# input : json: {service_name: check_method, service_owner}
# output: host: service: healthy = 1, critical = 0
#

import subprocess
import statsd
import sys
import json

NAGIOS_PLUGIN_PATH = "/usr/lib/nagios/plugins/"

c = statsd.StatsClient('localhost', 8125)
def main(sys):
    json_config = sys[1]
    with open(json_config) as json_data:
        json_config_obj = json.load(json_data)
        for service_name in json_config_obj:
            call_plugin = NAGIOS_PLUGIN_PATH + \
                    json_config_obj[service_name]["check"]
            params = json_config_obj[service_name]["params"]
            command = str(call_plugin) + " " + str(params)
            plugin_resp = subprocess.check_output(command, shell=True)
            resp_split_array = plugin_resp.split(":")
            service_status = resp_split_array[0][-2:]
            if service_status == "OK":
                c.gauge(service_name, 1)
            else:
                c.gauge(service_name, 0) 


if __name__ == "__main__":
    sys.exit(main(sys.argv))
