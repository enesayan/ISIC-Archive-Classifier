import json
from pprint import pprint
import pandas as pd
import os
import shutil



def sparse_benign_malignant():
    
   path="/home/enes/PhD/Data/Descriptions"
   path_img="/home/enes/PhD/Data/Images"
   dest_img_benign="/home/enes/PhD/Data/ParsedData/Benigns/Images"
   dest_dscr_benign="/home/enes/PhD/Data/ParsedData/Benigns/Descriptions"
   dest_img_malignant="/home/enes/PhD/Data/ParsedData/Malignants/Images"
   dest_dscr_malignant="/home/enes/PhD/Data/ParsedData/Malignants/Descriptions"
   
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
           #benigns.append(data["meta"]["clinical"]["benign_malignant"])
           benigns.append(f)
        else:
           #malignants.append(data["meta"]["clinical"]["benign_malignant"])
           malignants.append(f)

      except Exception as e:
          #unknowns.append("unknown")
          unknowns.append(f)
          print "hata",e
          print "Hatali dosya=",f
   print len(benigns)
   print len(malignants)
   print len(unknowns)
   
   '''for b in benigns:
       b_img=path_img+"/"+b+".jpg"
       b_dscr=path+"/"+b
       shutil.copy2(b_dscr,dest_dscr_benign)
       shutil.copy2(b_img,dest_img_benign)'''

   for m in malignants:
       m_img=path_img+"/"+m+".jpg"
       m_dscr=path+"/"+m
       shutil.copy2(m_dscr,dest_dscr_malignant)
       shutil.copy2(m_img,dest_img_malignant)

   print "Copy operation is complated !!!"

     
   
   


#def sparse_ISBI_2017_Data():


def main():
    sparse_benign_malignant()
main()   

'''path="/home/enes/PhD/Data/Descriptions"
#path="Data/Descriptions"

os.chdir(path)
print os.getcwd()
listfolders=os.listdir(os.getcwd())
print len(listfolders)
#print listfolders


benigns=[]
malignants=[]
unknowns=[]

ISBI_2017_Train=[]
ISBI_2017_Test=[]
ISBI_2017_Validation=[]


for f in listfolders:
   try:
     data=pd.read_json(f)
     if data["meta"]["clinical"]["benign_malignant"]=="benign":
        benigns.append(data["meta"]["clinical"]["benign_malignant"])
     else:
        malignants.append(data["meta"]["clinical"]["benign_malignant"])
     if "ISBI 2017: Training" in data["notes"]["tags"]:
        ISBI_2017_Train.append(f)
     #elif "ISBI 2017: Test" in ["notes"]["tags"]:
	#ISBI_2017_Test.append(f)
     #labels.append(data["meta"]["clinical"]["benign_malignant"])
   except Exception as e:
     unknowns.append("unknown")
     print "hata",e
     print "Hatali dosya=",f

print len(benigns)
print len(malignants)
print len(unknowns)
print len(ISBI_2017_Train)
#print len(ISBI_2017_Test)

   

#data = json.load(open('ISIC_0000000.json'))

#data=pd.read_json("ISIC_0000000",typ='series')

#print data["meta"]["clinical"]["benign_malignant"]'''
