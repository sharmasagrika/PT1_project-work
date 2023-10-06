print("""  #####                                                                
 #     # #    # #####  #####   ####  #    #   ##   # #    #            
 #       #    # #    # #    # #    # ##  ##  #  #  # ##   #            
  #####  #    # #####  #    # #    # # ## # #    # # # #  #            
       # #    # #    # #    # #    # #    # ###### # #  # #            
 #     # #    # #    # #    # #    # #    # #    # # #   ##            
  #####   ####  #####  #####   ####  #    # #    # # #    #            
                                                                       
 #######                                                               
 #       #    # #    # #    # ###### #####    ##   #####  ####  #####  
 #       ##   # #    # ##  ## #      #    #  #  #    #   #    # #    # 
 #####   # #  # #    # # ## # #####  #    # #    #   #   #    # #    # 
 #       #  # # #    # #    # #      #####  ######   #   #    # #####  
 #       #   ## #    # #    # #      #   #  #    #   #   #    # #   #  
 ####### #    #  ####  #    # ###### #    # #    #   #    ####  #    #""")

print("\n------------------------------------------------------------------\n")

import requests
import sys
subdomains = open("subdomains.txt").read().splitlines()
target = sys.argv[1]
targ = target.split(",")
for tar in targ:
    for sub in subdomains:
        sub_domain = f"http://{sub}.{tar}"
        try:
            requests.get(sub_domain)
        except requests.ConnectionError:
            pass

        else:
            print("Valid Domain: ", sub_domain)
        
    print("-----------------------------------------\n")
