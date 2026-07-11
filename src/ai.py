import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def generate_summary(report):

    prompt = f"""
You are a financial market analyst.

Write a short market summary (maximum 60 words).

Here is today's market data:

{report}

Keep it factual.
Do not invent information.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
