import ollama
import os

# Ensure the current working directory is the script's directory 
script_dir = os.path.dirname(os.path.abspath(__file__)) 
os.chdir(script_dir)
#setting up constants

def model_prompt_vison(modelpass,prompt,filepath): #Passing three variables for identifying model,the promppt and path of image that goes with prompt.
        
        response = ollama.chat(
            model= modelpass,
            messages=[{
                'role': 'user',
                'content': prompt,
                'images': [filepath]

            }]
        )
        message = response.message.content
        return message


def model_prompt (modelpass,prompt):  
    if modelpass == 'llama3.2:3b':
        response = ollama.chat(
            model= modelpass,
            messages=[{
                'role': 'user',
                'content': prompt,
            }]
        )
        message = response.message.content
        return message

    elif modelpass == 'qwen2.5-coder:32b':
        response = ollama.chat(
            model= modelpass,
            messages=[{
                'role': 'user',
                'content': prompt,
            }]
        )
        message = response.message.content
        return message

    else:
         return 'Error'