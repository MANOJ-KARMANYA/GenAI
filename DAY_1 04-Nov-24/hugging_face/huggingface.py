import requests

# Replace with your Hugging Face API key
API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/gpt2"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def query_huggingface(prompt, max_tokens=30):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_tokens  # Limit the response length
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Test the function with limited response length
result = query_huggingface("what do you know about Japan?", max_tokens=30)
print(result)




# import requests

# # Replace with your Hugging Face API key
# API_KEY = "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"
# API_URL = "https://api-inference.huggingface.co/models/gpt2"

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# def query_huggingface(prompt, max_tokens=30, temperature=0.7, top_k=50, top_p=0.9):
#     # Set up the payload with customizable parameters
#     payload = {
#         "inputs": prompt,
#         "parameters": {
#             "max_new_tokens": max_tokens,  # Limit the response length
#             "temperature": temperature,    # Control randomness (higher is more random)
#             "top_k": top_k,                # Top-k sampling for diversity
#             "top_p": top_p                 # Top-p sampling for more control
#         }
#     }

#     # Perform the API request
#     try:
#         response = requests.post(API_URL, headers=headers, json=payload)
#         response.raise_for_status()  # Raise an error for bad status codes

#         # Parse JSON response
#         output = response.json()

#         # Check if the response contains the generated text
#         if isinstance(output, list) and "generated_text" in output[0]:
#             return output[0]["generated_text"]
#         else:
#             return "Unexpected response format: " + str(output)

#     except requests.exceptions.RequestException as e:
#         return f"An error occurred: {e}"

# # Test the function with advanced parameters
# result = query_huggingface("What do you know about France?", max_tokens=50, temperature=0.8, top_k=40, top_p=0.95)
# print(result)
