from uagents import Bureau, Agent

# Import your CurrencyExchangeAgent class
from agents.currency_exchange.currency_exchange_agent import CurrencyExchangeAgent

if __name__== "__main__":
    # Initialize the CurrencyExchangeAgent
    currency_exchange_agent = CurrencyExchangeAgent()

    # Create a uagents.Agent instance
    agent = Agent(name="currency_exchange_agent_wrapper", seed="2271d3282d8c8f2a49999e6b9e8a0fa277c458646415815090ccb3d93e7e9e94")

    # Add your CurrencyExchangeAgent as a protocol to the uagents.Agent
    agent.include(currency_exchange_agent.exchange_protocol)

    # Create a Bureau and add the uagents.Agent
    bureau = Bureau(endpoint="http://127.0.0.1:8000/submit", port=8000)
    bureau.add(agent)

    # Run the bureau
    bureau.run()