import sys
import os
import json
import commands
import setup

class YAH():
    def _init_(self, file_path):
        self.file_path = file_path
    def read_config(self):
        
        with open(self.file_path, "r") as jsonfile:
            data = json.load(jsonfile)
        return data
if _name_ == '_main_':
    # In CLI pass config file path as argument
    # If config file not passed, select as default file
    if len(sys.argv)==1 :
        file_input = "config_default.json"
        print("Setting up using default Configuration File")
    else:
        file_input = sys.argv[1]
        print("Setting up using "+ file_input +" Configuration File")
    yah_object = YAH(file_input)
    config_dict = yah_object.read_config()

    #Initializing setup object and creating directory.
    setup_object = setup.Setup(config_dict)
    try:
        setup_object.create_direc()
    except FileExistsError:
        print("User already exits")
        os.chdir(setup_object.fs_path.split("/")[1]+"/"+setup_object.fs_path.split("/")[2])