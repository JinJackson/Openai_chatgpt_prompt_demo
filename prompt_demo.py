import openai
openai.api_key = "" # 将 YOUR_API_KEY 替换为您的 OpenAI API 密钥

prompt = "Hello, I'm ChatGPT. What can I help you with today?"

response = openai.Completion.create(
    engine="text-davinci-002", # 指定使用 ChatGPT 的 GPT 模型引擎
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.7,
)

import pdb; pdb.set_trace()

print(response.choices[0].text.strip())
