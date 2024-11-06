# import requests

# # Replace with your Hugging Face API key
# API_KEY = "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"
# API_URL = "https://api-inference.huggingface.co/models/gpt2"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# def query_huggingface(prompt, max_tokens=30, temperature=0.7, top_k=50, top_p=0.9):
#     payload = {
#         "inputs": prompt,
#         "parameters": {
#             "max_new_tokens": max_tokens,
#             "temperature": temperature,
#             "top_k": top_k,
#             "top_p": top_p
#         }
#     }

#     try:
#         response = requests.post(API_URL, headers=headers, json=payload)
#         response.raise_for_status()

#         output = response.json()

#         if isinstance(output, list) and "generated_text" in output[0]:
#             return output[0]["generated_text"]
#         else:
#             return "Unexpected response format: " + str(output)

#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

# # Main interaction loop
# print("Welcome to the AI assistant! Type 'exit' to end the conversation.")

# while True:
#     user_input = input("Ask a question: ")
    
#     # Check if user wants to exit
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
    
#     # Get response from the model
#     response = query_huggingface(user_input, max_tokens=50, temperature=0.8, top_k=40, top_p=0.95)
#     print("AI Response:", response)


# import requests


# API_KEY = "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"
# # API_URL = "https://api-inference.huggingface.co/models/gpt2"
# API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# def query_huggingface(prompt, max_tokens=30, temperature=2, top_k=1, top_p=0.20):
#     payload = {
#         "inputs": prompt,
#         "parameters": {
#             "max_new_tokens": max_tokens,
#             "temperature": temperature,
#             "top_k": top_k,
#             "top_p": top_p
#         }
#     }

#     try:
#         response = requests.post(API_URL, headers=headers, json=payload)
#         response.raise_for_status()

#         output = response.json()

#         if isinstance(output, list) and "generated_text" in output[0]:
#             return output[0]["generated_text"]
#         else:
#             return "Unexpected response format: " + str(output)

#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

# print("Welcome to the AI assistant! Type 'exit' to end the conversation.")

# while True:
#     user_input = input("Ask a question: ")

#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
    
#     response = query_huggingface(user_input, max_tokens=50, temperature=2, top_k=10, top_p=0.95)
#     print("AI Response:", response)






import requests
import random

API_KEY = "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"

# List of Hugging Face API model URLs for text generation
API_MODELS = [
    "https://api-inference.huggingface.co/models/gpt2",
    "https://api-inference.huggingface.co/models/t5-base"
]

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def query_huggingface(prompt, max_tokens=30, temperature=0.7, top_k=50, top_p=0.9):
    # Randomly select a model from the API_MODELS list
    api_url = random.choice(API_MODELS)
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens,
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()

        output = response.json()

        if isinstance(output, list) and "generated_text" in output[0]:
            return output[0]["generated_text"]
        else:
            return "Unexpected response format: " + str(output)

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"

print("Welcome to the AI assistant! Type 'exit' to end the conversation.")

while True:
    user_input = input("Ask a question: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    response = query_huggingface(user_input, max_tokens=50, temperature=0.8, top_k=40, top_p=0.95)
    print("AI Response:", response)
