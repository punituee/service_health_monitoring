# service_health_monitoring
This will send timely data of services to monitoring framework 1=>service running, 0=>service critical

###Requirements: 
pystatsd, statsd server, nagios plugins

###Usage: 
Update the location of nagios plugins in service_health_ping.py 
here NAGIOS_PLUGIN_PATH = "/usr/lib/nagios/plugins/libexec"

set a run-one cron python service_health_ping.py service_list.json every flush_interval
