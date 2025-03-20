import openai

# Set OpenAI API key
# Make sure to replace YOuR_API_KEY with your actual OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define prompt
prompt = (
    "Given the following entities and their known relationships:\n"
    "1. John Doe is the CEO of Acme Corporation.\n"
    "2. Acme Corporation acquired Beta LLC.\n"
    "Infer any additional relationships or ownership structures between these entities."
)

# Generate response
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.7,
)

# Output generated text
print(response.choices[0].text.strip())
