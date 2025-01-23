import os
import openai
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the default OpenAI model
DEFAULT_MODEL = "gpt-3.5-turbo"

def generate_response(prompt, model=DEFAULT_MODEL):
    """
    Generate a response from OpenAI's Chat API.

    Args:
        prompt (str): Input text prompt for the model.
        model (str): OpenAI model to use. Default is 'gpt-3.5-turbo'.

    Returns:
        str: Generated text response from the model.
    """
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # Ensures consistent outputs
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example usage
    basic_response = generate_response("What is 1 + 1?")
    print(basic_response)

    # Sample customer email
    customer_email = """
    I’m frustrated because my blender lid flew off 
    and splattered smoothie all over my kitchen walls! 
    To make it worse, the warranty doesn’t cover 
    cleaning costs. I need your help right away!
    """

    # Define the tone and style for translation
    style = "American English in a calm and respectful tone"

    # Formulate the prompt for translation
    prompt = f"""
    Rewrite the text below in a style that is {style}:
    ---
    {customer_email}
    ---
    """

    translated_response = generate_response(prompt)
    print(translated_response)
