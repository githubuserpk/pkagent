step-0: url for quickstart google documentation
https://cloud.google.com/logging/docs/write-query-log-entries-python#linux

download code: 
  git clone https://github.com/googleapis/python-logging

Note: actual code is in the snippets folder



step-1: install python logging library
pip install --upgrade google-cloud-logging


step-2: 
python snippets.py my-log write

output: 
I0000 00:00:1724681072.649615    2262 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
Wrote logs to my-log.


step-3: list the logs

output: 
pkdeltaai_06@cloudshell:~/python-logging/samples/snippets (pkdeltaai-06)$ python snippets.py my-log list
Listing entries for logger my-log:
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724681094.477912    2277 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
* 2024-08-26T14:04:35.801376+00:00: {'logging.googleapis.com/diagnostic': {'instrumentation_source': [{'version': '3.11.2', 'name': 'python'}]}}
* 2024-08-26T14:04:35.801376+00:00: Hello, world!
* 2024-08-26T14:04:35.923933+00:00: Goodbye, world!
* 2024-08-26T14:04:36.070830+00:00: {'favorite_color': 'Blue', 'quest': 'Find the Holy Grail', 'name': 'King Arthur'}


step-4: delete the log 

pkdeltaai_06@cloudshell:~/python-logging/samples/snippets (pkdeltaai-06)$ python snippets.py my-log delete
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724681106.936744    2290 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
Deleted all logging entries for my-log


step-5: create a bucket and make it privately accessible 


gsutil mb -l us-central1 -c standard -b on -p pkdeltaai-06 gs://bkt-my-loggingbucket/


gsutil defacl set private gs://bkt-my-loggingbucket/
Setting default object ACL on gs://bkt-my-loggingbucket/...


Step-5: create sink

python export.py create mysink bkt-my-loggingbucket "severity>=INFO"                                                    
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724682846.419824    3556 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
Created sink mysink



Step-6 export sink

pkdeltaai_06@cloudshell:~/python-logging/samples/snippets (pkdeltaai-06)$ python export.py list
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724682863.744668    3572 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
mysink: severity>=INFO -> storage.googleapis.com/bkt-my-loggingbucket
_Required: LOG_ID("cloudaudit.googleapis.com/activity") OR LOG_ID("externalaudit.googleapis.com/activity") OR LOG_ID("cloudaudit.googleapis.com/system_event") OR LOG_ID("externalaudit.googleapis.com/system_event") OR LOG_ID("cloudaudit.googleapis.com/access_transparency") OR LOG_ID("externalaudit.googleapis.com/access_transparency") -> logging.googleapis.com/projects/pkdeltaai-06/locations/global/buckets/_Required
_Default: NOT LOG_ID("cloudaudit.googleapis.com/activity") AND NOT LOG_ID("externalaudit.googleapis.com/activity") AND NOT LOG_ID("cloudaudit.googleapis.com/system_event") AND NOT LOG_ID("externalaudit.googleapis.com/system_event") AND NOT LOG_ID("cloudaudit.googleapis.com/access_transparency") AND NOT LOG_ID("externalaudit.googleapis.com/access_transparency") -> logging.googleapis.com/projects/pkdeltaai-06/locations/global/buckets/_Default


step-7: write logs
python snippets.py my-log write
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724683144.597424    3600 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
Wrote logs to my-log.

Step-8: delete my-log and delete mysink

python snippets.py my-log delete


python export.py delete mysink

output: 
pkdeltaai_06@cloudshell:~/python-logging/samples/snippets (pkdeltaai-06)$ python export.py delete mysink
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724683955.387970    3672 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache
Deleted sink mysink





