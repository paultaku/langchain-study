from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
import os

# get open ai api key
OPENAI_API_KEY = os.getenv("OPENAI_API_TOKEN");

# initialize the model
chat = ChatOpenAI(temperature=0)

# load tools
tools = load_tools(["serpapi", "llm-math"], llm=chat);

# define system prompt
template = "You are a helpful assistant than translates text from {input_language} to {output_language}.";
system_message_prompt = SystemMessagePromptTemplate.from_template(template);

# define human prompt
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template);

# combine the prompts
chat_prompt = ChatPromptTemplate.from_messages([
    system_message_prompt,
    human_message_prompt
]);

# combine the model and the prompt
chain = LLMChain(llm=chat, prompt=chat_prompt);

# run the chain
chain.run(
    input_language="English",
    output_language="French",
    text="I love programming."
);


# result = chat_prompt.format_prompt(
#     input_language="English",
#     output_language="French",
#     text="I love programming."
# );

# print(result);  

