from llama_index.core.llms import ChatMessage
from llama_index.llms.openai_like import OpenAILike

# see: https://docs.llamaindex.ai/en/stable/examples/llm/localai/#llamaindex-interaction
model = OpenAILike(
    model="deepseek-chat",
    api_base='https://api.deepseek.com',
    api_key='sk-2142926dcf7f4d12aa0044e638c33bc9',
    is_chat_model=True,
    timeout=10*60,
)
response = model.chat(messages=[ChatMessage(content="你好")])
print(response)
