#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

'''
Chemin du répertoire où je souhaite récupérer mes vidéos --> à modifier en fonction des MOOCS
'''

path="/home/amandine/compu_neurosciences/"

LectureList = os.listdir(path) # current directory


# In[29]:


'''
Définition de la fonction permettant d'obtenir la durée d'une vidéo
'''

import subprocess

def getLength(filename):
  result = subprocess.Popen(["ffprobe", filename],
    stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
  return [x for x in result.stdout.readlines() if b"Duration" in x]


# In[45]:


''' 
Ouverture fichier dans lequel 
les résultats de durées des vidéos s'enregistreront 
'''

fh=open("video_duration_results.csv", "w")


for i in LectureList:
    LectureVideos=os.listdir(path+i)
    print("le dossier "+i+" contient", LectureVideos)
    for folder in LectureVideos:
        FileList=os.listdir(path+i+"/"+folder)
        print("Dans "+folder+ " on a:", FileList)
        
        for file in FileList:
            filename, file_extension = os.path.splitext(file)
            if file_extension==".mp4":
                #dans la 1ere colonne je veux les numéros de lecture 2.2, 2.3 = LectureVideos... et dans la 2e je veux la duration correspondante
                fh.write(folder +","+ str((getLength(chemin))[0]) +'\n')
fh.close()

