import sys  # モジュール属性 argv を取得するため
import json
from datetime import datetime as dt

def check_esm_fonfig(json_dict):
    for esm_set in json_dict:
        #####################################
        print('[schedule_id check]')
        if isinstance(esm_set['schedule_id'], str) is False:
            print('**error** schedule_id format is wrong. please use String.')
        print('schedule_id: ' + esm_set['schedule_id'] + '\n')

        #####################################
        print('[start_date format check: MM-dd-YYYY]')
        print('start:' + str(dt.strptime(esm_set['start_date'], '%m-%d-%Y')) + '\n') #MM-dd-yyyy

        #####################################
        print('[end_data format check: MM-dd-YYYY]')
        print('end:  ' + str(dt.strptime(esm_set['end_date'], '%m-%d-%Y')) + '\n')   #MM-dd-yyyy

        #####################################
        print('[randomize check]')
        if isinstance(esm_set['randomize'], int) is False:
            print('**error** randomize format is wrong. please use Int.')
        if esm_set['randomize'] < 0:
            print('**error** randomize format is wrong. The value should be taken >=0.')
        print('randomize: '+ str(esm_set['randomize']) + '\n')

        #####################################
        print('[expiration check]')
        if isinstance(esm_set['expiration'], int) is False:
            print('**error** expiration format is wrong. please use Int.')
        if esm_set['expiration'] < 0:
            print('\**error** expiration format is wrong. The value should be taken >=0.')
        if esm_set['expiration'] == 0:
            print('expiration: ' + str(esm_set['expiration']))
            print("NOTE: This ESM is never expired during a day because the expiration time is set 0 min.\n")
        else:
            print('expiration: ' + str(esm_set['expiration']) + '\n')
        ####################################
        print('[notification title]')
        if isinstance(esm_set['notification_title'], str) is False:
            print('**error** notification_title format is wrong. please use string.')
        print('notification_title: ' + str(esm_set['notification_title']) + '\n')

        ####################################
        print('[notification_body]')
        if isinstance(esm_set['notification_body'], str) is False:
            print('**error** notification_body format is wrong. please use string.')
        print('notification_body: ' + str(esm_set['notification_body']) + '\n')

        ####################################
        print("[hours]")
        if len(esm_set['hours']) <= 0:
            print('hours element needs more than 1 or more hours.')
        print('hours:')
        for h in esm_set['hours']:
            if h < 0 or h > 23:
                print('\t **error** ' + str(h) + ' is an wrong hour. Please set a different value between 0 and 23.');
            else:
                print('\t' + str(h))

        ####################################
        print("[esms]")
        if len(esm_set['esms']) <= 0:
            print('**error** esms element needs more than 1 or more esm elements.')
        index = 0
        for esm in esm_set['esms']:
            print("[" + str(index) + "]")
            index = index + 1

            check_common_esm_elements(esm)
            esm_type = esm['esm']['esm_type']

            if esm_type is 1:
                print('\tesm_type = (1) text input')
            elif esm_type is 2:
                print('\tesm_type = (2) radio button')
                check_radio_esm_elements(esm)
            elif esm_type is 3:
                print('\tesm_type = (3) check box')
                check_checkbox_esm_elements(esm)
            elif esm_type is 4:
                print('\tesm_type = (4) likert scale')
                check_likert_esm_elements(esm)
            elif esm_type is 5:
                print('\tesm_type = (5) quick answer')
                check_quickanswer_esm_elements(esm)
            elif esm_type is 6:
                print('\tesm_type = (6) slider')
                check_slider_esm_elements(esm)
            elif esm_type is 7:
                print('\tesm_type = (7) date/time picker')
            elif esm_type is 8:
                print('\tesm_type = (8) PAM')
            ########## ESMs under the line are prototypes (No. 9-16) ###########
            elif esm_type is 9:
                print('\tesm_type = (9) number')
            elif esm_type is 10:
                print('\tesm_type = (10) web')
            elif esm_type is 11:
                print('\tesm_type = (11) date')
            elif esm_type is 12:
                print('\tesm_type = (12) time')
            elif esm_type is 13:
                print('\tesm_type = (13) clock')
            elif esm_type is 14:
                print('\tesm_type = (14) picture')
            elif esm_type is 15:
                print('\tesm_type = (15) audio')
            elif esm_type is 16:
                print('\tesm_type = (16) video')
            else:
                print('\tthis esm_type('+str(esm_type)+') is not supported.')

def check_common_esm_elements(esm):
    esm_type = esm['esm']['esm_type']
    if isinstance(esm_type, int) is False:
        print('\t**error** esm_type should be set as int format.')
    ######## title ########
    esm_title = esm['esm']['esm_title']
    print('\tesm_title: '+esm_title)
    ######## instructions ########
    esm_instructions = esm['esm']['esm_instructions']
    print('\tesm_instructions: '+esm_instructions)
    ######## submit button name ########
    esm_submit = esm['esm']['esm_submit']
    print('\tesm_submit: '+esm_submit)
    ######## trigger ########
    esm_trigger = esm['esm']['esm_trigger']
    print('\tesm_trigger:' + esm_trigger)

def check_radio_esm_elements(esm):
    esm_radios = esm['esm']['esm_radios']
    if len(esm_radios) <= 0:
        print('\t**error** hours element needs more than 1 or more hours.')
    print('\tesm_radios:')
    for item in esm_radios:
        print('\t\t'+item)

def check_checkbox_esm_elements(esm):
    esm_checkboxes = esm['esm']['esm_checkboxes']
    if len(esm_checkboxes) <= 0:
        print('\t**error** hours element needs more than 1 or more hours.')
    print('\tesm_checkboxes:')
    for item in esm_checkboxes:
        print('\t\t'+item)

def check_likert_esm_elements(esm):
    ## int
    esm_likert_max = esm['esm']['esm_likert_max']
    if isinstance(esm_likert_max, int) is False:
        print('\t**error** esm_likert_max format is wrong. please use int.')

    esm_likert_step = esm['esm']['esm_likert_step']
    if isinstance(esm_likert_step, int) is False:
        print('\t**error** esm_likert_stop format is wrong. please use int.')

    ## str
    esm_likert_max_label = esm['esm']['esm_likert_max_label']
    if isinstance(esm_likert_max_label, str) is False:
        print('\t**error** esm_likert_max_label format is wrong. please use string.')

    esm_likert_min_label = esm['esm']['esm_likert_min_label']
    if isinstance(esm_likert_min_label, str) is False:
        print('\t**error** esm_likert_min_label format is wrong. please use string.')

def check_quickanswer_esm_elements(esm):
    esm_quick_answers = esm['esm']['esm_quick_answers']
    if len(esm_quick_answers) <= 0:
        print('\t**error** esm_quick_answers element needs more than 1 or more items.')
    print('\titems:')
    for item in esm_quick_answers:
        print('\t\t'+item)

def check_slider_esm_elements(esm):
    esm_scale_min = esm['esm']['esm_scale_min']
    if isinstance(esm_scale_min, int) is False:
        print('\t**error** esm_scale_min format is wrong. please use int.')
    ##################
    esm_scale_max = esm['esm']['esm_scale_max']
    if isinstance(esm_scale_max, int) is False:
        print('\t**error** esm_scale_max format is wrong. please use int.')
    ##################
    esm_scale_start = esm['esm']['esm_scale_start']
    if isinstance(esm_scale_start, int) is False:
        print('\t**error** esm_scale_start format is wrong. please use int.')
    ###########
    esm_scale_step  = esm['esm']['esm_scale_step']
    if isinstance(esm_scale_step, int) is False:
        print('\t**error** esm_scale_step format is wrong. please use int.')

    ###########
    esm_scale_max_label = esm['esm']['esm_scale_max_label']
    if isinstance(esm_scale_max_label, str) is False:
        print('\t**error** esm_scale_max_label format is wrong. please use str.')
    ###########
    esm_scale_min_label = esm['esm']['esm_scale_min_label']
    if isinstance(esm_scale_min_label, str) is False:
        print('\t**error** esm_scale_min_label format is wrong. please use str.')

if __name__ == '__main__':
    ### test ######
    # f = open('sample_config.json', 'r')
    # json_dict = json.load(f)
    # check_esm_fonfig(json_dict)

    ###############
    argvs = sys.argv
    if(len(argvs) < 2):
        print("Please add a path of the target AWARE ESM configuration file as a parameter.")
        print("EXAMPLE:")
        print("python3 format_checker.py sample_config.json")
    else:
        f = open(argvs[1], 'r')
        json_dict = json.load(f)
        check_esm_fonfig(json_dict)
