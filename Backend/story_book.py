import google.generativeai as genai
from dotenv import load_dotenv
import os 

import pandas as pd
import ast as ast
import requests

load_dotenv()

genai.configure(api_key=os.environ.get("API_KEY"))




def get_src_original_url(query):
    url = 'https://api.pexels.com/v1/search'
    headers = {
        'Authorization':os.environ.get("PEXEL_API_KEY"),
    }

    params = {
        'query': query,
        'per_page': 1,
    }

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        photos = data.get('photos', [])
        if photos:
            src_original_url = photos[0]['src']['original']
            return src_original_url
        else:
           return "No url found"
    else:
        return f"Error: {response.status_code}, {response.text}"

   

def create_story_themes(story,pages):
    model = genai.GenerativeModel(
        model_name='gemini-1.5-pro')
        # tools='code_execution')
    
    prompt=f"""
    1. Break the given story {story} into {pages} themes. The themes should be children-friendly and should not exceed 5 words.
    2. Split the pages only into {pages}. It should not exceed {pages}.
    3. Create ONE single LIST of JSON format of themes and the part of stories as the output.
    4. Make sure the complete story is incorporated. Do not miss any information. Give output in the following json format only.
    5. Give only one single output. Do not give multiple outputs
    """
    response = model.generate_content(prompt)
    # print(response)
    output=response.text
    start = output.find("```json") 
    end=output.find("```",start+len("```json"))
  
    extracted_output = output[start+len("```json"):end].strip()
    extracted_output=ast.literal_eval(extracted_output)
    return extracted_output

def create_story(topic):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt=f"""
    Create a story using the following topic: {topic} for children. The story should not exceed 1000 words and should be minimum of 500 words.
    It should be a friendly story and should have a happy ending.


    """
    response = model.generate_content(prompt)
    return response.text

def create_final_story(image_list, themes):
    for i in range(len(themes)):
        themes[i]['image']=image_list[i]
    return themes

def get_photos(themes):
    image_list=[]
    for t in themes:
        print(t)
        image_list.append(get_src_original_url(t['theme']))
    return image_list
        


# topic="butterflies"

# story_lines = create_story(topic)
# themes = create_story_themes(story_lines,5)
# image_list=get_photos(themes)
# final_json = create_final_story(image_list, themes)
# print(final_json)



