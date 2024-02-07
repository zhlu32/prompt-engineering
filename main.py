from utils import get_completion
from utils import Context


def call_prompt():
    system_prompt = "When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment in every paragraph."
    user_prompt = "Write a thank you note to my steel bolt vendor for getting the delivery in on time and in short notice. This made it possible for us to deliver an important order."

    c = Context()
    c.add_system_prompt_element(system_prompt)

    print(get_completion(c, user_prompt))


if __name__ == '__main__':
    call_prompt()



