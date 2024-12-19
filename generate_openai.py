from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
