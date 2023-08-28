from langflow import CustomComponent
from langchain.chains import LLMChain
from langchain import PromptTemplate

from langchain.llms.base import BaseLLM

class PromptGenerator(CustomComponent):
    display_name = "Prompt Generator"
    description = "This component leverage llm to generator a prompt"

    def build_config(self) -> dict:
        return { "description": { "multiline": True, "required": True } }

    def build(self, description: str, llm: BaseLLM) -> PromptTemplate:
        prompt_template = "You are a great prompt generator, follow the description to generate a right prompt, description:  {description}. prompt format should be string, just print the prompt content"

        chain = LLMChain(
            llm=llm, 
            prompt=PromptTemplate.from_template(prompt_template))
        result = chain.run(description)

        prompt_template = PromptTemplate.from_template(str(result) + " {question}")
        return prompt_template
