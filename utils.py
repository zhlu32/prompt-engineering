import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


class Context:
    def __init__(self):
        self.my_list = []

    def add_element(self, element):
        self.my_list.append(element)

    def remove_element(self, element):
        if element in self.my_list:
            self.my_list.remove(element)
        else:
            print(f"{element} 不存在于列表中")

    def get_list(self):
        return self.my_list

    def clear_list(self):
        self.my_list.clear()

    def add_system_prompt_element(self, system_prompt):
        self.my_list.append({
            "role": "system",
            "content": system_prompt,
        })


def get_completion(c: Context, prompt, model="gpt-4", temperature=0):
    add_prompt = {
        "role": "user",
        "content": prompt,
    }
    c.add_element(add_prompt)
    print(f"===========Before Request===========")
    print(c.get_list())

    response = client.chat.completions.create(
        model=model,
        messages=c.get_list(),
        temperature=temperature,
    )
    ret = response.choices[0].message.content

    c.add_element({
        "role": "assistant",
        "content": ret
    })
    print(f"===========After Request===========")
    print(c.get_list())

    return ret

