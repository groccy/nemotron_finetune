from nemo.collections.llm.api import LLM

# Assuming you have an initialized LLM instance called 'model'
# Replace with your actual model initialization
model = LLM(...)  # Initialize your LLM instance

# and a text prompt
prompt = "Your prompt here"

# Set max_length to 100 tokens
sampling_params = {"max_length": 100}
response = model.generate(prompt, sampling_params=sampling_params)
print(response)

# Set both max_length and min_length
sampling_params = {"max_length": 100, "min_length": 50}
response = model.generate(prompt, sampling_params=sampling_params)
print(response)

# If you want to experiment with the default settings, you can omit the sampling_params
# and the model will use its default settings for output length
response = model.generate(prompt)
print(response)
