from os import system, listdir, path

from colorama import Fore, Style

from cfg import LOG, DEST_DIR
from utils import log_it, check_dir, check_file, kill_drivers


def live_download(server, destination):
    if path:
        command = 'curl ' + server + ' --max-time 2400 -o ' + destination
        #test_command = 'touch '+ destination
    else:
        return
    print(Fore.MAGENTA + command+Style.RESET_ALL)
    log_it(command)
    system(command)
    #log_it(test_command)
    #system(test_command)
    check_download(destination)
    msg = 'success senpai... '+destination+" downloaded"
    print(Fore.BLUE +msg+Style.RESET_ALL)
    log_it(msg)
        
def check_download(d_file):
    d_size = path.getsize(d_file)/(2**20)
    status = ''
    if d_size > 200:
        status = status +  "download met size requirement"
        print(status)
        log_it(status)
        return True
    else:
        status = status +  "download possibly incomplete"
        print(status)
        log_it(status)

