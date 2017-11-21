# About ConfigFormatChecker
This Python program supports to generating/checking the format of ESM configuration file
 for AWARE client.

By using the *template_generator.py*, you can generate a template of the ESM configuration
 file through a command with some options.
You just need to polish the generated template for making your ESMs.

*format_checker.py* allows us to easily checking the format of the configuration file
 before releasing it to AWARE client iOS. This program checks formats of the file
 automatically and indicates errors just giving a link to the file.


## Required Software/Library
- Python3
- JSON library on Python

## How to Use

### template_generator.py
For generating the template, you need to give an export file name, notification hours, and ESM types.
HOURS valus should select between 0 and 23. In addition, you can choose ESMs from 9 types of ESM: text(1),
radio(2), checkbox(3), likert(4), quick answer(5), slider(6), datetime(7), PAM(8), and WEB(10).
```
$ python3 template_generator.py EXPORT_FILE HOURS TYPES [options]
```

Example-1:
Generally, you can generate a configuration file using the following command.
```
$ python3 template_generator.py master.json 9,12,15,18 text,radio,checkbox,likert,quick,slider,datetime,pam,web
```

Example-2:
* -s = start date
* -e = end date
* -i = id
```
$ python3 template_generator.py master.json 9,12,15 likert,likert,likert -s 06-22-2017 -e 06-22-2020 -i test_id
```

Example-3:
-r = randomize
-p = expiration
-m = interface mode (0=one-by-one interface, 1=single line interface)
```
$ python3 template_generator.py master.json 9,12,15 likert,likert,likert -r 15 -p 15 -m 1
```


### format_checker.py
You just give a link to the target configuration file for checking the file is valid or invalid.

```
$ python3 format_checker.py sample_config.json
```

## AWARE ESM format
Please refer the following link.
http://www.awareframework.com/schedule-esms-for-aware-ios-client/



