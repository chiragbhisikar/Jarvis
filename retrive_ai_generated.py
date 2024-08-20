from openai import OpenAI
from apiKey import open_api_key


def aiProcess(command):
    client = OpenAI(
        api_key=open_api_key,
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You Are A Virtual Assistant In Jarvis."},
            {"role": "user", "content": command},
        ],
    )

    # print(completion.choices[0].message)
    return completion.choices[0].message
