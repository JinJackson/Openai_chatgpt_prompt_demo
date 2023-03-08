import openai

openai.api_key = ""



message = []

user = {'user': "用户",
        'system': "预设内容",
        'assistant': "Chat回复"}

def logout(message):
    for m in message:
        role = user[m['role']]
        content = m['content']
        print(role + "  -->  " + content)
        print("-------------------------SEP------------------------")



while True:
    content = input("用户请输入--->")
    message.append({"role": "user", "content": content})
    logout(message)

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message,
    temperature=0.2, # higher, randomer [0, 2]
    )
#     import pdb; pdb.set_trace()

    chat_resp = response.choices[0].message.content.strip()
    message.append({"role": "assistant", "content": chat_resp})
    logout(message)



