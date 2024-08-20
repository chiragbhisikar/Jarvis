# OPENAI_API_KEY="sk-7ZXbYw0wcu58AKa6szJcQUGCOlsl5Uz9G3Pm7BmF8PT3BlbkFJiN0ZrEYa_K0EELGLzJX6DLApEeBs5lu4cOHybIrZAA"
from openai import OpenAI


def aiProcess(command):
    client = OpenAI(
        api_key="sk-7ZXbYw0wcu58AKa6szJcQUGCOlsl5Uz9G3Pm7BmF8PT3BlbkFJiN0ZrEYa_K0EELGLzJX6DLApEeBs5lu4cOHybIrZAA",
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
