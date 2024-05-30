from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os


load_dotenv()

key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(
    temperature=0.7,
    openai_api_key=key,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

def get_name(resturant_type):
    prompt_template_name = PromptTemplate(
        input_variables=['resturant_type'],
        template="I want to open resturant for {resturant_type} food. Suggest me  a fancy name for this "
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key='resturant_name')
    prompt_template_items = PromptTemplate(
        input_variables=['resturant_name'],
        template="Suggest me some menu items for {resturant_name} resturant. send them in comma separated format"
    )
    chain = LLMChain(llm=llm, prompt=prompt_template_items,  output_key='menu_items')

    chains = SequentialChain(
        chains=[name_chain, chain],
        input_variables=['resturant_type'],
        output_variables=['resturant_name', 'menu_items']
        )
    return chains.invoke({'resturant_type': resturant_type})



