# small utility to search python docs from cli 
# currently only supports firefox 

import sys
import subprocess
import os

url_base = "https://docs.python.org/3.8/search.html?q="

def call_fox(url):
    command = subprocess.run(['firefox','-new-window',url,'-foreground'],capture_output=False)
    #sys.stdout.buffer.write(command.stdout)
#    sys.stderr.buffer.write(command.stderr)
    sys.exit(command.returncode)
    

if __name__ == '__main__':


    #main func call
    try:
        search_term = sys.argv[1]
        call_fox(url_base+search_term)
        sys.exit(command.returncode)
    except IndexError:
        print(" Ugh... Pls give me a search term ('-')?") 
