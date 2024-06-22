
# File Organizer 

File Organizer is a powerful local application designed to simplify and streamline the management of digital files using Google's Gemini API. Tailored for ease of use, this application allows users to easily organize their files into categorized folders, all within a user-friendly interface powered by Flask.




## Important:

- #### It may take a bit to upload all the files so please wait for all files to completely upload

- #### Also, it may take a little bit to organize files after clicking organize so please wait and do not click out of website.

- #### It only accepts files (images, videos, audios, softwares, etc) to organize, and NOT folders. Dragging folders will add everything in that folder to be organized, which will lead to a different organization

- #### If you face any errors, kindly go to http://127.0.0.1:5000/ or refresh and then click Restart. Now reupload your files. 

## Installation
 - Ensure you have Python and Pip installed
 - Clone the repo and cd into it

```bash
  git clone https://github.com/dattpatel123/file-organizer.git
```

- Open into file-organizer directory
```bash
  cd file-organizer
```

- Get a Google Gemini API Key
- Create a .env file in the directory and put API key
```bash
  GOOGLE_API_KEY = "PASTE KEY HERE"
```
- Setup a virtual environment and activate in working directory
```bash
    macOS/Linux:
     1. python3 -m venv .venv
     2. source myenv/bin/activate

    Windows:
     1. python -m venv .venv
     2. .venv\Scripts\activate
```
- Install the dependencies
```bash
    pip install -r requirements.txt

```
- Run the project using:
```bash
    python main.py OR python3 main.py
```

- Now, simply goto http://127.0.0.1:5000 and follow instructions to get files organized

- Once you upload files, it will organize them and generate a zip to download which will contain categorized folders, inside which are your files 


## Features

- Intuitive Drag-and-Drop Interface: Seamlessly upload files by simply dragging them into the designated area, ensuring a smooth and intuitive user experience.

- Gemini API Integration: Uses the intelligent categorization capabilities of the Gemini API to automatically sort files into categories based on content analysis.

- Efficient Organization: Automatically creates structured folders within a downloadable zip archive, providing users with neatly organized collections of their files ready for storage or sharing.

- Secure and Private as It's All done On Your Local Computer 
