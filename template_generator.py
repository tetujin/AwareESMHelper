import json
import sys
import os
import time
from datetime import datetime

def get_common_esm_elements(esm_trigger):
    return {"esm_type":0,
            "esm_title":"EDIT HERE",
            "esm_instructions": "EDIT HERE",
            "esm_submit": "Submit",
            "esm_expiration_threshold": 60,
            "esm_trigger":esm_trigger,
            "esm_na": 0
            }

def get_text_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 1
    return {"esm":esm_elements}

def get_radio_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 2
    esm_elements['esm_radios'] = ['YES','NO']
    return {"esm":esm_elements}

def get_checkbox_elemtns(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 3
    esm_elements['esm_checkboxes'] = ['One','Two','Other']
    return {"esm":esm_elements}

def get_likert_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 4
    esm_elements['esm_likert_max'] = 5
    esm_elements['esm_likert_max_label'] = 'Good'
    esm_elements['esm_likert_min_label'] = 'Bad'
    esm_elements['esm_likert_step'] = 1
    return {"esm":esm_elements}

def get_quick_answer_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 5
    esm_elements['esm_quick_answers'] = ['Yes','No','Maybe']
    return {"esm":esm_elements}

def get_slider_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 6
    esm_elements['esm_scale_min'] = 0
    esm_elements['esm_scale_max'] = 10
    esm_elements['esm_scale_start'] = 5
    esm_elements['esm_scale_max_label'] = '10'
    esm_elements['esm_scale_min_label'] = '0'
    esm_elements['esm_scale_step'] = 1
    return {"esm":esm_elements}

def get_datetime_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 7
    return {"esm":esm_elements}

def get_pam_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 8
    return {"esm":esm_elements}

def get_number_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 9
    return {"esm":esm_elements}

def get_web_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 10
    esm_elements['esm_url'] = 'https://xxxx.xxxx.xxxx'
    return {"esm":esm_elements}

def get_date_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 11
    return {"esm":esm_elements}

def get_time_elements(ems_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 12
    return {"esm":esm_elements}

def get_clock_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 13
    return {"esm":esm_elements}

def get_picture_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 14
    esm_elements['esm_camera'] = 0 # 0=front camera, 1=back camera
    return {"esm":esm_elements}

def get_audio_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 15
    return {"esm":esm_elements}

def get_video_elements(esm_trigger):
    esm_elements = get_common_esm_elements(esm_trigger)
    esm_elements['esm_type'] = 16
    esm_elements['esm_camera'] = 0 # 0=front camera, 1=back camera
    return {"esm":esm_elements}


######

def get_esm(esm_type, esm_trigger):
    esm = None
    if (esm_type == "1" or esm_type == "text"):
        esm = get_text_elements(esm_trigger + "_text")
    elif (esm_type == "2" or esm_type == "radio"):
        esm = get_radio_elements(esm_trigger + "_radio")
    elif (esm_type == "3" or esm_type == "checkbox"):
        esm = get_checkbox_elemtns(esm_trigger + "_checkbox")
    elif (esm_type == "4" or esm_type == "likert"):
        esm = get_likert_elements(esm_trigger + "_liker")
    elif (esm_type == "5" or esm_type == "quick"):
        esm = get_quick_answer_elements(esm_trigger + "_quick")
    elif (esm_type == "6" or esm_type == "slider"):
        esm = get_slider_elements(esm_trigger + "_slider")
    elif (esm_type == "7" or esm_type == "datetime"):
        esm = get_datetime_elements(esm_trigger + "_datetime")
    elif (esm_type == "8" or esm_type == "pam"):
        esm = get_pam_elements(esm_trigger + "_pam")
    elif (esm_type == "9" or esm_type == "number"):
        esm = get_number_elements(esm_trigger + "_number")
    elif (esm_type == "10" or esm_type == "web"):
        esm = get_web_elements(esm_trigger + "_web")
    elif (esm_type == "11" or esm_type == "date"):
        esm = get_date_elements(esm_trigger + "_date")
    elif (esm_type == "12" or esm_type == "time"):
        esm = get_date_elements(esm_trigger + "_time")
    elif (esm_type == "13" or esm_type == "clock"):
        esm = get_clock_elements(esm_trigger + "_clock")
    elif (esm_type == "14" or esm_type == "picture"):
        esm = get_picture_elements(esm_trigger + "_picture")
    elif (esm_type == "15" or esm_type == "audio"):
        esm = get_audio_elements(esm_trigger + "_audio")
    elif (esm_type == "16" or esm_type == "video"):
        esm = get_video_elements(esm_trigger + "_video")
    else:
        print('**error** ' + esm_type + ' is unsupported.')
    return esm

######

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
    schedule_id = 'EDIT HERE'
    hours = []
    randomize = 0
    expiration = 0
    esms = []
    interface = 0

    ###############
    argvs = sys.argv

    ######### export_file ########
    export_file = argvs[1]

    ######### schedule_id ########
    schedule_id = argvs[2]

    ######### hours ########
    temp_hours = [int(n) for n in argvs[3].split(',')]
    for h in temp_hours:
        if h < 24 and h >= 0:
            hours.append(h)
        else:
            print('**error** ' + str(h) + ' is invalid number. Please select the number between 0 and 23.')

    ######### types ########
    types = argvs[4].split(',')
    index = 0
    for esm_type in types:
        esm_trigger = schedule_id +"_" +str(index)
        esm = get_esm(esm_type,esm_trigger)
        if esm is not None:
            esms.append(esm)
        index = index + 1

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
        elif(argvs[i] == '-r'):
            randomize = int(argvs[i+1])
        elif(argvs[i] == '-p'):
            expiration = int(argvs[i+1])
        elif(argvs[i] == '-m'):
            interface = int(argvs[i+1])


    esm_schedule = {"schedule_id":schedule_id,
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

