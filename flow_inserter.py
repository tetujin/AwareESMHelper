import json
import sys
import os

import template_generator as tg

if __name__ == '__main__':
    # python3 config_integrater.py new_master.json master.json esm_schedule_3_0_liker YES:likert,NO:slider
    argvs = sys.argv

    esm_flows = []
    answers = argvs[4].split(',')
    index = 0
    for answer in answers:
        answer_type = answer.split(':')
        answer = answer_type[0]
        type   = answer_type[1]
        aflow = {
            "user_answer":answer,
            "next_esm":tg.get_esm(type,"flow_"+str(index)+"_"+argvs[3])
        }
        esm_flows.append(aflow)
        index = index + 1


    # json.dump([esm_schedule], f, indent=4)
    f = open(argvs[2], 'r')
    temp_jsons = json.load(f)
    for tpj in temp_jsons:
        esms = tpj['esms']
        for esm in esms:
            print(esm['esm']['esm_trigger'])
            if esm['esm']['esm_trigger'] == argvs[3]:
                esm['esm']['esm_flows'] = esm_flows

    new_file = open(argvs[1], 'w')
    json.dump(temp_jsons, new_file, indent=4)

    print("Done!")
    os.system('open '+argvs[1])