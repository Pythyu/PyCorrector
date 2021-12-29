from Decompressor import *
from FileExplorer import *
from AutoUpdate import *
from SecurityCheck import *
import yaml
import sys
import timeout_decorator
import collections.abc

DEBUG = False

ShowLogMessages = False

tests_functions = []
#clean_up_after_run = True

########### ALL SCORE FUNCTIONS ###############
#Fonction used to compare the student program output and the output registered in the config file
#|-> can be customized if needed
###############################################

def compareINFunction(studentOut, registeredOut):
    """
    If student output is into the output list
    """
    return studentOut in registeredOut

def compareEQFunction(studentOut, registeredOut):
    """
    if the student output is equal to the first in the output list
    """
    return studentOut == registeredOut[0]

score_functions = [compareINFunction,compareEQFunction]

################################################

def load_config():
    """
    Load the config file
    """
    try:
        with open('config.yaml') as f:
            dt = yaml.load(f, Loader=yaml.FullLoader)
            static_vars = dt["static"]
            for item in dt["functions"].keys():
                input = dt["functions"][item]
                if isinstance(input, collections.abc.Hashable) and static_vars.get(input, None) is not None:
                    input = static_vars[input]
                output = dt["expected_outputs"][item]
                if isinstance(output, collections.abc.Hashable) and static_vars.get(output, None) is not None:
                    output = static_vars[output]
                tests_functions.append((item, input, output, dt["score_functions"][item], dt["timeout_functions"][item]))
        return True
    except Exception as e:
        if DEBUG:
            print(e)
        print('/!\ config file couldn\'t be loaded properly. Please check config.yaml is correctly setup /!\\')
        return False


def rating_routine(module, file):
    """
    Rate each of the student's function from the config file data
    """
    score = 0
    for tests in tests_functions:
        try:
            testMethod = timeout_decorator.timeout(tests[4])(getattr(module, tests[0]))
            studentOut = testMethod(*tests[1])
            gain = 0
            if score_functions[tests[3]](studentOut,tests[2]):
                score += 1
                gain = 1
            file.write("     %s (%d) -> Expected %s got %s\n" % (tests[0], gain,tests[2], studentOut))
            if DEBUG:
                print("DEBUG routine : ",tests[0]," : ",studentOut, tests[2]," | actual score : ", score)
        except Exception as e:
            file.write("     %s (0) -> raised following error : %s\n" % (tests[0], e))

    return score

def local_import(pyfile,outFile, folders, length):
    pym = __import__(pyfile[:-3])
    try:
        outFile.write("%s >\n" % (underscore_format(folders)))
        score = rating_routine(pym, outFile)
        # save the rating
        outFile.write("%s : %d/%d \n" % (underscore_format(folders), score, length))
        outFile.write("\n"+"-="*10+"\n")
        if pyfile[:-3] in sys.modules:
            del sys.modules[pyfile[:-3]]
    except Exception as e:
        if pyfile[:-3] in sys.modules:
            del sys.modules[pyfile[:-3]]
        raise e



def main():
    """
    Main Application Logic
    """
    outFile = open("ratings.txt","w")

    # Extract compressed files
    for file in get_folders("./studentFiles"):
        if file[0] == ".":
            continue
        #dc = Decompressor(join("./studentFiles",file),"tmp/%s" % (file))
        #dc.extract()

        # Check the folder security
        RecursiveTreeCheck("./studentFiles/%s" % (file))

        # Read each extracted files
        for folders in get_folders("./studentFiles/%s" % (file)):
            sys.path.append("./studentFiles/%s/%s" % (file, folders))
            for pyfile in get_files_with_extension("./studentFiles/%s/%s" % (file, folders), "py"):
                # import and rate it
                try:
                    local_import(pyfile, outFile, folders, len(tests_functions))
                except Exception as e:
                    outFile.write("%s : Error( %s ) \n" % (underscore_format(folders), str(e)))
                    outFile.write("\n"+"-="*10+"\n")
                    if ShowLogMessages:
                        print("Couldn't properly execute the rating routine for the following student python code :", underscore_format(folders))
                        print("Reason :")
                        print(e)
            sys.path.remove("./studentFiles/%s/%s" % (file, folders))

    outFile.close()
    #if clean_up_after_run:
#        clean_folder_content("./tmp")



if __name__ == "__main__" and CheckUpdate() and load_config():
    main()
