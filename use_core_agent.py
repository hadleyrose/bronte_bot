from rasa.core.agent import Agent
from rasa.core.utils import EndpointConfig
from rasa.core.interpreter import RasaNLUInterpreter
import asyncio

interpreter = RasaNLUInterpreter('models/20211104-133912_model/nlu')

agent = Agent.load('models/20211104-133912.tar.gz', interpreter=interpreter, action_endpoint=EndpointConfig(url='http://0.0.0.0:5055'))

loop = asyncio.get_event_loop()

results = loop.run_until_complete(agent.handle_text('hello'))
