import json
import sys
import os
import time
from datetime import datetime

def get_common_esm_elements():
    return {"esm_type":0,
            "esm_title":"EDIT HERE",
            "esm_instructions": "EDIT HERE",
            "esm_submit": "Submit",
            "esm_expiration_threshold": 60,
            "esm_trigger":"EDIT HERE",
            "esm_na": 0
            }

def get_text_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 1
    return {"esm":esm_elements}

def get_radio_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 2
    esm_elements['esm_radios'] = ['YES','NO']
    return {"esm":esm_elements}

def get_checkbox_elemtns():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 3
    esm_elements['esm_checkboxes'] = ['One','Two','Other']
    return {"esm":esm_elements}

def get_likert_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 4
    esm_elements['esm_likert_max'] = 5
    esm_elements['esm_likert_max_label'] = 'Good'
    esm_elements['esm_likert_min_label'] = 'Bad'
    esm_elements['esm_likert_step'] = 1
    return {"esm":esm_elements}

def get_quick_answer_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 5
    esm_elements['esm_quick_answers'] = ['Yes','No','Maybe']
    return {"esm":esm_elements}

def get_slider_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 6
    esm_elements['esm_scale_min'] = 0
    esm_elements['esm_scale_max'] = 10
    esm_elements['esm_scale_start'] = 5
    esm_elements['esm_scale_max_label'] = '10'
    esm_elements['esm_scale_min_label'] = '0'
    esm_elements['esm_scale_step'] = 1
    return {"esm":esm_elements}

def get_datetime_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 7
    return {"esm":esm_elements}

def get_pam_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 8
    return {"esm":esm_elements}

def get_web_elements():
    esm_elements = get_common_esm_elements()
    esm_elements['esm_type'] = 10
    esm_elements['esm_url'] = 'https://xxxx.xxxx.xxxx'
    return {"esm":esm_elements}


def is_valid_date_format(str):
    mdy = [int(n) for n in str.split('-')]
    if len(mdy) == 3:
        if mdy[0]>12:
            return False
        if mdy[1]>24:
            return False
        if mdy[2]<999 or mdy[2]>9999:
            return False
    else:
        return False
    return True


if __name__ == '__main__':
    # python3 template_generator.py -f master.json -s 06-23-2017 -e 07-23-2017 -i hello_id -h 13,15,18 -r 15 -p 15 -t 1,2,3,4,5 -m 0

    export_file = 'master.json' # -f
    start_date = '06-23-2014'   # -s
    end_date = '06-23-2050'     # -e
    schedule_id = 'EDIT HERE"'
    hours = []
    randomize = 0
    expiration = 0
    esms = []
    interface = 0

    ###############
    argvs = sys.argv

    ######### export_file ########
    export_file = argvs[1]

    ######### hours ########
    temp_hours = [int(n) for n in argvs[2].split(',')]
    for h in temp_hours:
        if h < 24 and h >= 0:
            hours.append(h)
        else:
            print('**error** ' + str(h) + ' is invalid number. Please select the number between 0 and 23.')

    ######### types ########
    types = argvs[3].split(',')
    for esm_type in types:
        if (esm_type == "1" or esm_type == "text"):
            esms.append(get_text_elements())
        elif (esm_type == "2" or esm_type == "radio"):
            esms.append(get_radio_elements())
        elif (esm_type == "3" or esm_type == "checkbox"):
            esms.append(get_checkbox_elemtns())
        elif (esm_type == "4" or esm_type == "likert"):
            esms.append(get_likert_elements())
        elif (esm_type == "5" or esm_type == "quick"):
            esms.append(get_quick_answer_elements())
        elif (esm_type == "6" or esm_type == "slider"):
            esms.append(get_slider_elements())
        elif (esm_type == "7" or esm_type == "datetime"):
            esms.append(get_datetime_elements())
        elif (esm_type == "8" or esm_type == "pam"):
            esms.append(get_pam_elements())
        elif (esm_type == "10" or esm_type == "web"):
            esms.append(get_web_elements())
        else:
            print('**error** ' + esm_type + ' is unsupported.')


    for i in range(len(argvs)):
        if(argvs[i] == '-s'):
            if is_valid_date_format(argvs[i + 1]):
                start_date = argvs[i + 1]
            else:
                print("**error** please check the format of start_date.")
        elif(argvs[i] == '-e'):
            if is_valid_date_format(argvs[i + 1]):
                end_date = argvs[i + 1]
            else:
                print("**error** please check the format of end_date.")
        elif(argvs[i] == '-i'):
            schedule_id = argvs[i+1]
        elif(argvs[i] == '-r'):
            randomize = int(argvs[i+1])
        elif(argvs[i] == '-p'):
            expiration = int(argvs[i+1])
        elif(argvs[i] == '-m'):
            interface = int(argvs[i+1])


    esm_schedule = {'schedule_id':schedule_id,
                    "hours": hours,
                    "randomize": randomize,
                    "start_date": start_date,
                    "expiration": expiration,
                    "end_date":  end_date,
                    "notification_title": "EDIT HERE",
                    "notification_body": "EDIT HERE",
                    "interface": interface,
                    "esms":esms}

    f = open(export_file, 'w')
    json.dump([esm_schedule], f, indent=4, sort_keys=True)

    print(export_file + " is generated correctly. Please modify the configuration file for your study.")
    os.system('open '+export_file)