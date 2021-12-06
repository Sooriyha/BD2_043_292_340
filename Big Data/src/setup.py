import sys
import os
import json
import main
import commands
class Setup():
        def _init_(self, config_dict):
            #Extraction of configuration details 
            self.block_size = config_dict["block_size"]
            self.path_to_datanode = config_dict["path_to_datanode"]
            self.path_to_namenode = config_dict["path_to_namenode"]
            self.replication_factors = config_dict["replication_factors"]
            self.num_datanode = config_dict["num_datanode"]
            self.datanodes_size = config_dict["datanodes_size"]
            self.sync_period = config_dict["sync_period"]
            self.datanode_log_paths = config_dict["datanode_log_paths"]
            self.namenode_log_paths = config_dict["namenode_log_paths"]
            self.namenode_checkpoints = config_dict["namenode_checkpoints"]
            self.fs_path = config_dict["fs_path"]
            self.dfs_setup_config = config_dict["dfs_setup_config"]
            self.datanode_list = []

        def create_direc(self):
            #Creating a directory for each user
            user = self.fs_path.split("/")[2]
            home_dir = self.fs_path.split("/")[1]
            os.mkdir(home_dir+"/"+user)
            print("created directory for"+user)

            #Creating datanode dir
            datanode_dir = self.path_to_datanode.split("/")[3]
            os.mkdir(home_dir+"/"+user+"/"+datanode_dir)

            #creating namenode dir
            namenode_dir = self.path_to_namenode.split("/")[3]
            os.mkdir(home_dir+"/"+user+"/"+namenode_dir)

            #creating datanodes within the datanode directory
            create_datanodes(self.num_datanode,self.datanodes_size,user,datanode_dir,home_dir,self.datanode_list)
            print("Succesfully Created Datanodes")

            #creating namenode within the namenode directory
            create_namenode(namenode_dir)
            print("Succesfully Created Namenode")

            #Success
            print('Setup Complete')

def create_datanodes(num_datanode, datanodes_size, user,datanode_dir,home_dir,datanode_list):
    os.chdir(home_dir+"/"+user+"/"+datanode_dir)
    for i in range(1,num_datanode+1):
        s = str(i)
        os.mkdir("datanode"+s)
        datanode_list.append("datanode"+s)
    print(datanode_list)
    

def create_namenode(namenode_dir):
    os.chdir("../"+namenode_dir)
    namenode_dict = {
        "key":"value"
    }
    json_object = json.dumps(namenode_dict)
    with open("namenode.json", "w") as outfile:
        outfile.write(json_object)
    os.chdir("../")

def setup_cat():
    print("In setup_cat")