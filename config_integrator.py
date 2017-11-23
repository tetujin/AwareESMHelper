import json
import sys
import os

if __name__ == '__main__':
    # python3 config_integrator.py new_master.json master-1.json master-2.json master-3.json
    argvs = sys.argv
    new_esms = []
    if len(argvs) > 2:
        for i in range(2,len(argvs)):
            f = open(argvs[i], 'r')
            temp_jsons = json.load(f)
            for tpj in temp_jsons:
                new_esms.append(tpj)

    new_file = open(argvs[1], 'w')
    json.dump(new_esms, new_file, indent=4)

    print("Following config files are integrated into " + argvs[1] + ":")
    for i in range(2, len(argvs)):
        print("\t"+argvs[i])
    os.system('open '+argvs[1])