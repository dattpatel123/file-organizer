import shutil
import os
from groq import Groq
import json
import requests
from dotenv import load_dotenv, dotenv_values   
from collections import defaultdict
import random

load_dotenv()

def getDict():
    client = Groq(
        api_key=os.getenv('GROQ_API_KEY')
    )

    file_names = os.listdir('uploads') 
    random.shuffle(file_names)

    print(f"Original Count: {len(file_names)}\n")


    batch_size = 5  

    batches = [file_names[i:i + batch_size] for i in range(0, len(file_names), batch_size)]
    # 10 3   0-3, 3-6 6-9 9 12

    categoryList = ['Documents', 'Presentation', 'Images', 'Audios', 'Videos', 'Archives', 'Software']
    print(','.join(categoryList))
    finalDict = defaultdict(list)
    for index, batch in enumerate(batches):
        my_string = '\n'.join(batch)
        
        retries = 7
        attempt = 0
        
        response = {}
        while attempt < retries: 
            try: 
                attempt+=1
                """
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a API capable that responds with a single json object. The JSON object should use the format: {category1_name: list of file names, category2 name: list of files, ...}. I will give you file names. Categorize every single file name in that string looking for similarities AND File type. Keep the exact file name and each file should only go into JUST ONLY 1 category. Look at these preexisitng categories: {categoryList}. And if any file doesn't fit in them, create a new category with a new unique name. "
                        },
                        {
                            "role": "user",
                            "content": f"I will give you file names. Categorize every single file name in that string looking for similarities AND File type. Keep the exact file name and each file should only go into JUST ONLY 1 category. Look at these preexisitng categories: {categoryList}. And if any file doesn't fit in them, create a new category with a new unique name. This is the file string,  where the files are separated by \\n: {my_string}"
                        }
                    ],
                    model="llama3-8b-8192",
                    response_format={"type": "json_object"}

                    
                )"""

                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": f"You are a API capable that responds with a single json object. The JSON object should use the format: 'Category Name': [list of file names].... Keep the spaces in the file names and don't remove spaces. The file categories are: {categoryList}"
                        },
                        {
                            "role": "user",
                            "content": f"Categorize each and every single file name in the following string looking at file type and file names. Each file should have ONLY 1 CATEGORY and keep the EXACT file name even if it looks weird. Here is the file string, separated by \\n: {my_string}"
                        }
                    ],
                    model="llama3-8b-8192",
                    response_format={"type": "json_object"})
                
                # add keys to category list
                response = chat_completion.choices[0].message.content
                response = json.loads(response)
               
                """ Code for auto define 
                for key, values in list(response.items()):
                    if len(values) != 0:
                        categoryList.append(key)
                    if len(values) == 0:
                        response.pop(key)"""

                break            
            except Exception as e:
                    print(f"Error on attempt {attempt}: {e} for Batch {index}")
                    continue;

        # convert respones to python dictionary and append to existing final Dict
        
        
        
        print(f"\nBatch {index}'s Response: {json.dumps(response, indent=4)}\n")

        for key, value in response.items():
            for v in value:
                 finalDict[key].append(v) 
        
        

    return finalDict
  


def getFinalDict():
    finalDict = getDict()

    print('\n--------')
    print(json.dumps(finalDict, indent=4, sort_keys=True))
    print('--------\n')

   # while allFilesAccounted(finalDict) is False:
    #    finalDict = getDict() 
    
    return finalDict

def organize(response):

    
    # move files into folders
    for categoryName,files in response.items():

        try: os.mkdir('uploads/'+categoryName)
        except:
            shutil.rmtree('uploads/'+categoryName)
            os.mkdir('uploads/'+categoryName)

        for f in files:
            try: os.rename( 'uploads/' + f , 'uploads/' + categoryName + '/' + f)
            except Exception as e:
                #os.remove('uploads/' + categoryName)
               # os.rename( 'uploads/' + f , 'uploads/' + categoryName + '/' + f)
               
               #print(f"------------")
               print(f"\nError {e}\n")
               
    # remove empty folders        
    
    for f in os.listdir('uploads'):
        if os.path.isdir('uploads/'+f) and len(os.listdir('uploads/'+f)) == 0:
            shutil.rmtree('uploads/'+f)

    return 1




