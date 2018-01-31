# About ConfigFormatChecker
ConfigFormatChecker allows generating/checking the format of
ESM configuration file for AWARE client by easy steps.
The programs are composed of Python and you can utilize it as like a command.

ConfigFormatChecker has following functions:

|Programs|Note|
|:---------:|--------|
|*template_generator.py*|Generating a template ESM configuration for AWARE client|
|*flow_inserter.py*|Inserting esm_flows into an ESM configuration file|
|*config_integrator.py*|Integrating ESM configuration files into an file|
|*format_checker.py*|Checking a format for an ESM configuration file|


## Required Software/Library
- Python3
- JSON library on Python

## How to Use

### template_generator.py
For generating the template, you need to give an export file name, notification hours, and ESM types.
HOURS valus should select between 0 and 23. In addition, you can choose ESMs from 9 types of ESM: text(1),
radio(2), checkbox(3), likert(4), quick answer(5), slider(6), datetime(7), PAM(8), and WEB(10).
```
$ python3 template_generator.py NEW_CONFIG SCHEDULE_ID HOURS TYPES [options]
```

Options:

|Option|Means|Default|Options|
|:-------:|-------|-------|-------|
|-s | start date| 06-23-2014 | any Time |
|-e | end date  | 06-23-2050 | any Time |
|-r | randomize min | 0 | more than 0 |
|-p | expiration min | 0  | more than 0 |
|-m | interface mode | 0 | 0(=one-by-one mode) or 1(=single-line mode) |

Actual Examples:
```
$ python3 template_generator.py master.json schedule1 9,12,15,18 text,radio,checkbox,likert,quick,slider,datetime,pam,web
```


```
$ python3 template_generator.py master.json schedule2 9,12,15 likert,likert,likert -s 06-22-2017 -e 06-22-2020 -i test_id
```


```
$ python3 template_generator.py master.json schedule3 9,12,15 likert,likert,likert -r 15 -p 15 -m 1
```

---

### flow_inserter.py
AWARE ESM supports to switch ESM by user answer.
We call the function as esm_flows.
*flow_inserter.py* allows inserting the logic into an ESM configuration file.
The sample command is follow

```
$ python3 flow_inserter.py NEW_CONFIG TARGET_CONFIG TARGET_ESM_TRIGGER ANSWER:ESM_TYPE,ANSWER:ESM_TYPE
```

Actual example:
```
$ python3 flow_inserter.py new_master.json master.json esm_schedule_3_0_liker YES:likert,NO:slider
```


### config_integrator.py
ESM configuration file can have multiple ESM scedules in an configuration file.
*config_integrator.py* allows integrating multiple ESM schedules into an new configuration file.

```
$ python3 config_integrator.py NEW_CONFIG CONFIG_1 CONFIG_2 CONFIG_3
```

Actual Example:
```
$ python3 config_integrator.py new_master.json master-1.json master-2.json master-3.json
```


### format_checker.py
You just give a link to the target configuration file for checking the file is valid or invalid.


```
$ python3 format_checker.py CONFIG_1
```

Actual Example:
```
$ python3 format_checker.py master.json
```

## AWARE ESM format
Please refer the following link.
http://www.awareframework.com/schedule-esms-for-aware-ios-client/
