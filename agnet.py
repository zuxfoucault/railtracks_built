import railtracks as rt


# Define a tool (just a function!)
def get_weather(location: str) -> str:
    return f"It's sunny in {location}!"


# Create an agent with tools
agent = rt.agent_node(
    "Weather Assistant",
    tool_nodes=(rt.function_node(get_weather)),
    llm=rt.llm.OpenAILLM("gpt-4o"),
    system_message="You help users with weather information.",
)

# Run it
flow = rt.Flow(name="Weather Flow", entry_point=agent)
result = await flow.invoke("What's the weather in Paris?")
print(result.text)  # "Based on the current data, it's sunny in Paris!"
