import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# Load the environment variables
load_dotenv()
aoai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
aoai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
aoai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
aoai_deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")


#client = openai.AzureOpenAI(
client = AzureOpenAI(
    azure_endpoint = aoai_endpoint,
    api_key = aoai_api_key,
    api_version = "2024-02-01") # aoai_api_version

completion = client.chat.completions.create(
    #deployment_name=aoai_deployment_name,
    model=aoai_deployment_name, #"gpt-4o",
    messages=[
        { "role": "user", 
         "content": "What should I know about generating structured output data from latest OpenAI GPT-4o available?"}
        ]
    )

# Prints only the Natural Language response answer from Azure OpenAI
print("Direct Answer to the question: ", completion.choices[0].message.content.strip())

# Print the completion full response from Azure OpenAI
#print("Full response back from the Azure OpenAI with all attributes is: ",completion)
