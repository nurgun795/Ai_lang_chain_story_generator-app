from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


from user_input import get_user_inputs


def generate_story(character_name, setting, theme):
    prompt_template = f"Create a story with the following details:\n\n" \
                        f"Main Character: {character_name}\n" \
                        f"Setting: {setting}\n" \
                        f"Theme: {theme}\n\n" \
                        f"Story:\n"
    
    prompt = PromptTemplate(template=prompt_template)


    model = ChatOpenAI(model_name="gpt-3.5-turbo", api_key="API_KEY")

    chain = LLMChain(prompt=prompt, llm=model)

    output = chain.run(input_data={})

    return output


if __name__ == "__main__":

    character_name, setting, theme = get_user_inputs()

    story = generate_story(character_name, setting, theme)

    print("\nGenerated Story:\n")
    print(story)
