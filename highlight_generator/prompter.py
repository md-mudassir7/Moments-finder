from api.config.config import Settings
from openai import OpenAI
import re

from utility.logger import get_logger
settings = Settings.get_settings()

logger = get_logger(__name__)
class Prompter:
    def __init__(self,genre,transcription):
        self.genre = genre
        self.transcription = transcription
        self.client = OpenAI(api_key=settings.openapi_key)
        
    def generate_prompts(self,genre,transcription):
        prompts = [
            {
                "role": "user", 
                "content": f"extremely carefully analyse below transcription and give me just one exact timestamp in seconds format where you feel it is an {genre} scene,\
                if you don't find anything related to the genre {genre}, then don't return any timesatamp and give a proper message\
                            Transcription: {transcription} \
                            "
             }
        ]
        return prompts

    def extract_numbers(self,input_string):
        pattern = r'\d+\.\d+|\d+'
        matches = re.findall(pattern, input_string)
        numbers = [float(match) if '.' in match else int(match) for match in matches]
        return numbers[0]
    
    def create_chat(self):
        logger.info("Creating a prompt for chatgpt")
        prompts = self.generate_prompts(self.genre,self.transcription)
        
        # logger.info(f"prompt generated {prompts}")
        
        chat_completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=prompts,
        )            
        logger.info(f"Prompt response : {chat_completion.choices[0].message.content}")
        
        try:
            resp = self.extract_numbers(chat_completion.choices[0].message.content)
        except Exception as e:
            logger.error(f"Error while prompting : {e}")
            resp = chat_completion.choices[0].message.content
        return resp