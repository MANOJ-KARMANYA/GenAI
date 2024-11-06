# # import openai

# # # Replace with your OpenAI API key
# # openai.api_key = "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"

# # def query_openai(prompt):
# #     response = openai.ChatCompletion.create(
# #         model="gpt-3.5-turbo",
# #         messages=[{"role": "user", "content": prompt}],
# #         max_tokens=50,
# #         temperature=0.7
# #     )
# #     return response['choices'][0]['message']['content']

# # # Main interaction loop
# # print("Welcome to the AI assistant! Type 'exit' to end the conversation.")
# # while True:
# #     user_input = input("Ask a question: ")
# #     if user_input.lower() == "exit":
# #         print("Goodbye!")
# #         break
# #     response = query_openai(user_input)

# #     print("AI Response:", response)


# import openai

# # Set your API key
# openai.api_key = "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"  # Replace with your actual API key

# def query_openai(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # Updated model
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=50,
#         temperature=0.7
#     )
#     return response['choices'][0]['message']['content'].strip()

# print("Welcome to the AI assistant! Type 'exit' to end the conversation.")
# while True:
#     user_input = input("Ask a question: ")
#     if user_input.lower() == "exit":
#         print("Goodbye!")
#         break
#     response = query_openai(user_input)
#     print("AI Response:", response)


import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, world!"}]
)

print(response.choices[0].message['content'])
