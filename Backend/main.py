from fastapi_microsoft_identity import initialize, requires_auth, AuthError, validate_scope
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, File, UploadFile, HTTPException, Query, Request,Response, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from story_book import create_story_themes,create_story,create_final_story,get_photos


app = FastAPI()
chat_history=[]
origins = ["*"]  # Update with your frontend URL(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)

@app.get("/create-story")
async def process_content(topic:str, num_pages:int):
    story_lines = create_story(topic)
    print("Created story")
    themes = create_story_themes(story_lines,num_pages)
    print("Split into themes")
    image_list=get_photos(themes)
    print("Recieved images")
    final_json = create_final_story(image_list, themes)
    print("final json created")
    return final_json


if __name__ == "__main__":
    uvicorn.run(app, port=9010)




