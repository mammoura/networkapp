import os.path
import sys

#checking IP address file and content validity
def ip_file_valid():

    #promting the user to input the file path
    ip_file = input("\n# Enter IP file path and name (e.g D:\python\ip.txt):")

    #checing if the file exists 

    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :")

    else:
        print ("\n* Fiel {} does not exist : (Please check and try again. \n)".format(ip_file))
        sys.exit()

    #Open the IP addresses file and save it in a list line by line 
    with open(ip_file) as f:
        ip_list = f.read().splitlines()

    
    return ip_list
