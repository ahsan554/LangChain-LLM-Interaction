import os
import openai
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv(find_dotenv())
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the default OpenAI model to use
DEFAULT_MODEL = "gpt-3.5-turbo"

# Initialize the OpenAI chat model with a low temperature for deterministic responses
chat = ChatOpenAI(temperature=0.0, model=DEFAULT_MODEL)

# Template for generating messages with style and text customization
template_string = """Translate the text delimited by triple backticks into a style that is {style}.
text: ```{text}```
"""

# Create a chat prompt template object from the defined template
prompt_template = ChatPromptTemplate.from_template(template_string)

# Check the structure and variables of the created template
# These lines verify the template configuration
print(prompt_template.messages[0].prompt)
print(prompt_template.messages[0].prompt.input_variables)

# Define the target style for the first message
customer_style = """American English in a calm and respectful tone"""

# Define the customer's original message with a specific tone and phrasing
customer_email = """
I am quite upset that my blender's lid flew off and made a mess of my kitchen walls with smoothie! 
To make matters worse, the warranty does not cover the cost of cleaning my kitchen. I need assistance right away, please!
"""

# Format the prompt for generating customer messages based on the template
customer_messages = prompt_template.format_messages(
    style=customer_style,
    text=customer_email
)

# Output the type of objects for debugging purposes
print(type(customer_messages))  # Type of the formatted messages (list)
print(type(customer_messages[0]))  # Type of the first message (Message object)

# Display the generated message content
print(customer_messages[0])

# Generate a response using the OpenAI model for the formatted message
customer_response = chat(customer_messages)

# Display the content of the generated customer response
print(customer_response.content)

# Define the service team's response in a standard tone
service_reply = """Hello, customer. The warranty does not cover cleaning expenses for your kitchen, 
as it appears the issue resulted from improper use of the blender, such as not securing the lid before use. 
We recommend reviewing the product manual for safe operation. Let us know if you need further assistance."""

# Define the style for translating the service response
service_style_pirate = """a polite tone that mimics English Pirate"""

# Format the prompt for generating service responses with the desired style
service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply
)

# Display the formatted service message for debugging
print(service_messages[0].content)

# Generate a pirate-styled response using the OpenAI model
service_response = chat(service_messages)

# Display the final pirate-style response
print(service_response.content)
