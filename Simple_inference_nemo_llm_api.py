from nemo.collections.llm.api import LLM

# Assuming you have already initialized your LLM
# Replace with your actual model initialization
llm = LLM(...)  # Initialize your LLM instance

sampling_params = {
    "max_length": 100  # Set the maximum length to 100 tokens
}

# Generate text with the specified sampling parameters
response = llm.generate(prompt="Your prompt here", sampling_params=sampling_params)

print(response)
