key = "user_api_key_here"  # Replace with your actual OpenAI API key

from openai import OpenAI   

client = OpenAI(api_key=key)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that provides information about the OpenAI API."
        },
    ],
    response_format={"type": "text"},
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

for choice in response.choices:
    print(f"Response: {choice.message.content}")
# Note: The API key is sensitive information and should not be shared publicly.
# Ensure you have the OpenAI Python package installed: