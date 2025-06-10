
from openai import OpenAI

BASE_URL = "https://openrouter.ai/api/v1"
API_KEY = "<------Add-your-API-KEY-here------>"

def chat_with_OpenAI(chat):
  client = OpenAI(
  base_url= BASE_URL,
  api_key = API_KEY
  )

  completion = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages=[
      {
        "role": "user",
        "content": f"{chat}"
      }
    ]
  )
  return completion.choices[0].message.content

