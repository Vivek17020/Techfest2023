# Currency Exchange Monitor & Alert Agent

## Overview

The Currency Exchange Monitor & Alert Agent is a Python-based application that allows users to monitor real-time currency exchange rates and receive alerts when the rates cross predefined thresholds. This project is built using the uAgent library and is designed to help users stay informed about currency exchange rate fluctuations.

## Features

- Real-time Currency Exchange Rate Monitoring: The agent connects to a currency exchange API to fetch real-time exchange rates, focusing on a specific base currency (e.g., USD).

- User-Defined Alert Thresholds: Users can specify currency pairs and set upper and lower thresholds for each pair. The agent continuously monitors exchange rates and triggers alerts when rates cross these thresholds.

- Notification System: The agent can send alerts or notifications to users when exchange rates meet or exceed the predefined thresholds. Currently, email notifications are supported, but other notification methods can be added as needed.

## Installation

1. Clone this repository to your local machine: git clone https://github.com/Vivek17020/Techfest2023.git

2.Install the required dependencies using pip:
pip install -r requirements.txt

3.Configure Agent Seed: Replace "your_agent_seed_here" with your actual agent seed in the main.py file.

4.Configure Email (Optional): If you plan to use email notifications, provide your email server details and credentials in the main.py file.

## Usage

1.Run the agent:
python main.py

2.Configure User Settings: Set your base currency and define currency pairs with alert thresholds in the main.py file. For example:

user_settings = UserSettings(
    base_currency="USD",
    alert_thresholds={
        "USD-INR": (82.60, 82.55),
        "USD-EUR": (0.85, 0.80),
        # Add more currency pairs and thresholds as needed
    }
)
'''
3. Monitor Exchange Rates: The agent will continuously monitor exchange rates and trigger alerts when they cross the specified thresholds.

4.Receive Notifications: When an alert is triggered, you will receive an email notification if configured.

## Customization
1.Adding Notification Methods: You can extend the project to support additional notification methods, such as SMS or push notifications, by modifying the send_alert function.

2.User Interface: Consider building a user interface for users to configure alert thresholds more conveniently.
