import re, sys, os
from sys import argv

from . import screens, functions

def is_url(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return re.match(regex, string)

def exist(target):
    return os.path.exists(target)

def create_dir(target):
    if exist(target) == False:
        os.mkdir(target)

def file_to_list(file):
    with open(file) as f:
        links = f.readlines()

    listaux = []
    for line in links:
        lineAux = line.strip().replace(" ", "")
        if len(lineAux) > 0:
            listaux.append(line.strip().replace(" ", ""))

    links = listaux
    links = purge_list_links(links)
    return links

def purge_list_links(list):
    exit_while = False
    while exit_while == False:
        exit_while = True
        for link in list:
            if (is_url(link) == None):
                list.remove(link)  
                exit_while = False  
    return list

def validate_arguments(valid_arguments):
    to_music = False
    links = []
    arguments = argv[1:]
    
    if len(arguments) == 0 or len(arguments) > 2:
        screens.wrong_parameters()
        exit(1)

    for argument in arguments:
        if (argument in valid_arguments):
            if argument == "-h":
                screens.help_screen()
                exit(1)
            elif argument == "-m":
                to_music = True
        elif functions.is_url(argument) != None:
            links.append(argument)
        elif functions.exist(argument) == True:
            links = functions.file_to_list(argument)
        else:
            screens.resource_missed()
            exit(1)
    
    if len(links) == 0:
        screens.resource_missed()
        exit(1)
    
    return (links, to_music)