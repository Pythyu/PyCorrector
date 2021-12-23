from Decompressor import *
from FileExplorer import *
import yaml
import sys

DEBUG = False

tests_functions = []

clean_up_after_run = False


def compareFunction(studentOut, registeredOut):
    return studentOut in registeredOut


def load_config():
    try:
        with open('config.yaml') as f:
            dt = yaml.load(f, Loader=yaml.FullLoader)
            for item in dt["functions"].keys():
                tests_functions.append((item, dt["functions"][item], dt["expected_outputs"][item]))
        return True
    except Exception as e:
        if DEBUG:
            print(e)
        print('/!\ config file couldn\'t be loaded properly. Please check config.yaml is correctly setup /!\\')
        return False


def rating_routine(module):
    score = 0
    for tests in tests_functions:
        testMethod = getattr(module, tests[0])
        studentOut = testMethod(*tests[1])
        if compareFunction(studentOut,tests[2]):
            score += 1
        if DEBUG:
            print("DEBUG routine : ",tests[0]," : ",studentOut, tests[2]," | actual score : ", score)
    return score







def main():

    outFile = open("ratings.txt","w")

    # Extract compressed files
    for file in get_files("./studentFiles"):
        dc = Decompressor(join("./studentFiles",file),"tmp/%s" % (file))
        dc.extract()
        sys.path.append("./tmp/%s" % (file))
        # Read each extracted files
        for pyfile in get_files_with_extension("tmp/%s" % (file), "py"):
            # import and rate it
            pym = __import__(pyfile[:-3])
            try:
                score = rating_routine(pym)
                # save the rating
                outFile.write("%s : %d/%d \n" % (file, score, len(tests_functions)))
            except Exception as e:
                print("Couldn't properly execute the rating routine to the student python code file")
                print("Reason :")
                print(e)

    outFile.close()



if __name__ == "__main__" and load_config():
    main()
