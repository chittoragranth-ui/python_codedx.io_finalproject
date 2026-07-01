import openai

openai.api_key = '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'

def generate_blog(paragraph_topic):
  response = openai.completions.create(
    model = 'gpt-3.5-turbo-instruct',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog

print(generate_blog('The impact of artificial intelligence on society.'))


# Multiple Paragraphs

keep_writing = True

while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False

