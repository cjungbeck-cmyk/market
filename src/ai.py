import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def generate_summary(report):

    prompt = f"""
You are a financial analyst.

Write a short market summary in English.

{report}
"""

    try:

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

    except Exception:

        return (
            "AI summary unavailable "
            "(API quota exceeded or service unavailable)."
        )
