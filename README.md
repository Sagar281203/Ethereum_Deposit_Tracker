# Ethereum Deposit Tracker

This repository contains a script designed to monitor and log Ethereum deposits. It connects to the Ethereum network, fetches deposit information, and maintains logs for both successful deposits and errors.

## Overview

The Ethereum Deposit Tracker is composed of several key components:

### Core Components

#### Main Script (main.py)
The main script orchestrates the deposit tracking:
- *Logging Setup*: Configures logging for tracking events and errors.
- *Web3 Initialization*: Establishes a connection to Ethereum using Web3.
- *Deposit Retrieval and Processing*: Fetches deposit logs, processes them, and updates the log file.

#### Deposit Processor (deposit_processor.py)
Handles the specifics of deposit management:
- *Deposit Retrieval*: Retrieves deposit data from the blockchain.
- *Data Processing*: Extracts necessary details from deposit logs and updates the log file. Manages error handling as well.

### Logging
Logs are categorized as follows:
- *Deposit Logs*: Stored in logs/deposit_logs.json.
- *Error Logs*: Stored in logs/error_logs.json.

## Setup Instructions

1. *Install Dependencies*
   Create a requirements.txt file with the following content and install the packages using pip:
    text
    web3==6.0.0
    requests==2.28.1
    

2. *Configure the Script*
   Edit config.py to include your Alchemy API key, the Beacon Contract address, and any other required settings.

3. *Execute the Script*
   Run the following command to start monitoring Ethereum deposits:
    bash
    python main.py
    
   The script will continuously monitor for new deposits and update the log files accordingly.

## Troubleshooting

- *Connection Issues*: If you encounter issues connecting to Ethereum, double-check your Alchemy URL and network settings.
- *Logging Problems*: Ensure that the file paths and permissions for log files are correctly set in your configuration.

For any additional help, feel free to open an issue or consult the [documentation](#).