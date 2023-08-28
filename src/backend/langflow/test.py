from interface.loading import load_flow_from_json
# from langflow import load_flow_from_json
from interface.run import get_result_and_thought


flow = load_flow_from_json("/Users/lipeng/workspaces/github.com/logspace-ai/langflow/VectorStore.json")
print(flow("Hey, have you heard of LangFlow?"))
# result, thought = get_result_and_thought(flow, "Hey, have you heard of LangFlow?")
# print({"result": str(result), "thought": thought.strip()})