import platform
import psutil
import argparse
import json
import socket
import getpass
import time
import sys
from logs import logger

parser = argparse.ArgumentParser()
parser.add_argument ("-p", "--parameter", type = str, required = False, help = "Choose between os_info/cpu_count/cpu_percent\
                     /total_memory, used_memory, free_memory/hd_info/local_time/boot_time/process/all")
parser.add_argument ("-f", "--format", type = str, required = False, help = "Choose between text or json")

parameter = parser.parse_args().parameter
format = parser.parse_args().format

if parameter == None:
    raise Exception('Enter at least one parameter')

class system_info():

    def __init__(self, parameter, format):
        self.parameter = parameter
        self.format = format
    
    # Determine the operating system
    def get_os_info(self):
        logger.info ("obtaining os info")
        os_info = platform.system()
        return os_info

    # Get CPU usage info
    def get_cpu_info(self):
        logger.info ("obtaining cpu info")
        cpu_count = psutil.cpu_count(logical=True)
        cpu_percent = psutil.cpu_percent(interval=1)
        return cpu_count, cpu_percent
    
    # Get memory usage info
    def get_memory_info(self):
        logger.info ("obtaining memory info")
        mem = psutil.virtual_memory()
        total_memory = mem.total / (1024 ** 3)  # Convert from bytes to GB
        used_memory = mem.used / (1024 ** 3)    
        free_memory = mem.free / (1024 ** 3)  
        return total_memory, used_memory, free_memory
    
    def get_hd_info(self):
        logger.info ("obtaining hd info")
        partitions = psutil.disk_partitions()
        hd_info = []
        for part in partitions:
            usage = psutil.disk_usage(part.mountpoint)
            hd_info.append({
                'device': part.device,
                'mountpoint': part.mountpoint,
                'fstype': part.fstype,
                'total': usage.total / (1024 ** 3),  # Convert from bytes to GB
                'used': usage.used / (1024 ** 3),
                'free': usage.free / (1024 ** 3),
                'percent': usage.percent
            })
        return hd_info

    # Get local time and boot time
    def get_time_info(self):
        logger.info ("obtaining time info")
        local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        boot_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(psutil.boot_time()))
        return local_time, boot_time

    # Main function to display all information
    def display_system_info(self):
        
        os_info = self.get_os_info()
        cpu_count, cpu_percent = self.get_cpu_info()
        total_memory = self.get_memory_info()
        used_memory = self.get_memory_info()        
        free_memory = self.get_memory_info()
        hd_info = self.get_hd_info()
        local_time = self.get_time_info()
        boot_time = self.get_time_info()

        dict = {"os_info":os_info, "cpu_count":cpu_count, "cpu_percent": cpu_percent, "total_memory":total_memory,\
                "used_memory": used_memory, "free_memory": free_memory, "hd_info": hd_info, "local_time": local_time,\
                "boot_time": boot_time}
        
        logger.info ("dictionary was created")
        
        with open('systeminfo.json', 'w') as f:
            json.dump (dict, f)
        
        if format == "text":
            for x in dict:
                if x == parameter:
                    print (dict[x])
        elif format == "json":
            print (dict)
        else:
            print ("choose format: text or json")

if __name__ == "__main__":
    my_os = system_info(parameter,format)
    my_os.display_system_info()