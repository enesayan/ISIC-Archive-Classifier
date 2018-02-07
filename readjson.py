import json
from pprint import pprint
import pandas as pd
import os
import shutil



def sparse_benign_malignant():
   #  
   path="~/Data/Descriptions"
   path_img="~/Data/Images"
   dest_img_benign="~/Data/ParsedData/Benigns/Images"
   dest_dscr_benign="~/Data/ParsedData/Benigns/Descriptions"
   dest_img_malignant="~/Data/ParsedData/Malignants/Images"
   dest_dscr_malignant="~/Data/ParsedData/Malignants/Descriptions"
   
   # change destination directort
   os.chdir(path)
   print os.getcwd()
   #get list of file names
   listfilenames=os.listdir(os.getcwd())
   print len(listfilenames)
   
   benigns=[]
   malignants=[]
   unknowns=[]
   
   for f in listfilenames:
      try:
        data=pd.read_json(f)
        if data["meta"]["clinical"]["benign_malignant"]=="benign":
           benigns.append(f)
        else:
           malignants.append(f)

      except Exception as e:
          unknowns.append(f)
          print "Error:",e
          print "Error File Name:",f
   print len(benigns)
   print len(malignants)
   print len(unknowns)
   
   for b in benigns:
       b_img=path_img+"/"+b+".jpg"
       b_dscr=path+"/"+b
       shutil.copy2(b_dscr,dest_dscr_benign)
       shutil.copy2(b_img,dest_img_benign)

   for m in malignants:
       m_img=path_img+"/"+m+".jpg"
       m_dscr=path+"/"+m
       shutil.copy2(m_dscr,dest_dscr_malignant)
       shutil.copy2(m_img,dest_img_malignant)

   print "Copy operation is complated !!!"

def main():
    sparse_benign_malignant()
main()   

