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


    model = ChatOpenAI(model_name="gpt-3.5-turbo", api_key="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")

    chain = LLMChain(prompt=prompt, llm=model)

    output = chain.run(input_data={})

    return output


if __name__ == "__main__":

    character_name, setting, theme = get_user_inputs()

    story = generate_story(character_name, setting, theme)

    print("\nGenerated Story:\n")
    print(story)