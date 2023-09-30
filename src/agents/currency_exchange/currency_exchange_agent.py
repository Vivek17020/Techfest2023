import time
import requests
import smtplib
import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from uagents import Agent, Protocol, Context
from uagents.setup import fund_agent_if_low
from typing import Dict, List, Tuple

# Import message models
from message_models import UserSettings, ExchangeRateUpdate

class CurrencyExchangeAgent:
    exchange_protocol = Protocol("CurrencyExchange")
    def __init__(self):
        # Initialize the agent
        self.agent = Agent(name="currency_exchange_agent", seed="your_agent_seed_here")
        fund_agent_if_low(self.agent.wallet.address())

        # Define a protocol for communication
       
        self.exchange_protocol = Protocol("CurrencyExchange")
        # Initialize user settings
        self.user_settings = None

    # Function to fetch exchange rates from an API
    def fetch_exchange_rates(self):
        while True:
            try:
                # Make API call to fetch exchange rates.
                response = requests.get("d642dc5d879270bde3e772df2f8c9695", params={"base": "USD"})
                data = response.json()

                # Publish exchange rate updates using the exchange_protocol
                rates = data.get("rates", {})
                self.agent.publish(ExchangeRateUpdate(base_currency="USD", rates=rates), protocol=self.exchange_protocol)
            except Exception as e:
                print("Error fetching exchange rates:", str(e))

            # Fetch rates every hour
            time.sleep(3600)

    # Function to monitor exchange rates and send alerts
    async def monitor_exchange_rates(self, ctx: Context):
        while True:
            try:
                # Receive user settings from other agents
                if self.user_settings is None:
                    ctx.logger.info("Waiting for user settings...")
                    self.user_settings = await ctx.receive(UserSettings)
                    ctx.logger.info("Received user settings.")

                # Receive exchange rate updates
                update = await ctx.receive(ExchangeRateUpdate)

                # Check if any alerts need to be triggered
                if self.user_settings:
                    base_currency = self.user_settings.base_currency
                    thresholds = self.user_settings.alert_thresholds

                    for currency, (lower_threshold, upper_threshold) in thresholds.items():
                        if currency in update.rates:
                            rate = update.rates[currency]

                            if rate < lower_threshold:
                                self.send_alert(f"Alert: {base_currency} to {currency} rate is below {lower_threshold}")
                            elif rate > upper_threshold:
                                self.send_alert(f"Alert: {base_currency} to {currency} rate is above {upper_threshold}")

            except Exception as e:
                print("Error in monitoring exchange rates:", str(e))

            # Check rates every 10 minutes
            await asyncio.sleep(600)

    # Function to send notifications via email
    def send_alert(self, message):
        # Email configuration (replace with your email server and credentials)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "your_email@gmail.com"
        sender_password = "your_email_password"
        recipient_email = "recipient_email@example.com"

        try:
            # Create an SMTP connection
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Email content
            subject = "Currency Exchange Alert"
            body = message

            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print("Alert email sent successfully!")

            # Close the SMTP connection
            server.quit()
        except Exception as e:
            print("Error sending email:", str(e))

    # Register message handlers for the exchange_protocol
    @exchange_protocol.on_message(model=UserSettings)
    async def handle_user_settings(self, ctx: Context, sender: str, settings: UserSettings):
        # Receive and store user settings
        ctx.logger.info("Received user settings.")
        self.user_settings = settings

    # Include the exchange_protocol in the agent and start monitoring exchange rates
    def start(self):
        self.agent.include(self.exchange_protocol)
        
        # Start monitoring exchange rates
        loop = asyncio.get_event_loop()
        loop.create_task(self.monitor_exchange_rates(self.agent.context))
        loop.run_forever()
 