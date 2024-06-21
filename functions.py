import shutil
import os
import json
import requests
from dotenv import load_dotenv, dotenv_values   
from collections import defaultdict
import random
import google.generativeai as genai
from pprint import pprint

#Load env variables
load_dotenv()

# Using Google API, send dictionary of {category: [files]}

def getDict():
    
    # setup google api
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})

    # shuffle uploaded files
    file_names = os.listdir('uploads') 
    random.shuffle(file_names)

    print(f"Original Count: {len(file_names)}\n")


    # batch the uploaded files
    batch_size = 15  

    batches = [file_names[i:i + batch_size] for i in range(0, len(file_names), batch_size)]
    
    
    
    
    # Create empty dict and categories list
    finalDict = defaultdict(list)
    categories = set()

    # Call API to organize files in batches

    for index, batch in enumerate(batches):
        
        tries = 0

        while tries < 3:

            try:

                response = model.generate_content(f"""Organize these file names using category as key and list of file 
                                                names as values for that category. Keep exact file names and use 
                                                intuitive categories rather than just file types 
                                                Keep in mind these existing categories({categories})
                                                and use them if a file fits, otherwise create new category. 
                                                This is file list: {batch}""")
                
                
                categories.update(json.loads(response.text).keys())
                print(f"\nBatch {index}'s Response: {response.text}\n\nCategories: {categories}\n")
                
                # Add the organized batch into final dict
                for key, value in json.loads(response.text).items():
                    for v in value:
                            finalDict[key].append(v)
                break
            # Failed Batch
            except Exception as e:
                print(f"{e}")
                print("Failed on Try: {tries}. Retrying...")
            
            tries+=1
        
        
    # Show me Final Dictionary and Categories
    pprint(finalDict)
    pprint(categories)

    return finalDict
  

def organize():

    finalDict = getDict()
    
    # move files into folders
    for categoryName,files in finalDict.items():

        #try: os.mkdir('uploads/'+categoryName)
        #except:
        #    shutil.rmtree('uploads/'+categoryName)
        #    os.mkdir('uploads/'+categoryName)
        os.mkdir('uploads/'+categoryName)

        for f in files:
            try: os.rename( 'uploads/' + f , 'uploads/' + categoryName + '/' + f)
            except Exception as e:
                #os.remove('uploads/' + categoryName)
               # os.rename( 'uploads/' + f , 'uploads/' + categoryName + '/' + f)
               
               #print(f"------------")
               print(f"\nError {e} w/ File: {f}\n")
               
          
    
    

 




