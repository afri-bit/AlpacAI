# Virtual City Payment


## Introduction

This README file serves as a guide for participants of the Hackathon project. It provides an overview of the project's purpose and functionality, as well as guidelines for implementing a payment use case using Blockchain.

## Project Description

The project is a Python-based application that leverages the Kuksa data broker to facilitate transactions in a Virtual City Metaverse. Users drive a virtual vehicle within this city and can visit two primary locations: a Fuel Station and a Parking Spot. Upon leaving location, the application emits signals using the Kuksa data broker. The signal payload varies based on the location:

Fuel Station: The signal includes information such as the date of the transaction, the driver's ID, and the amount of fuel purchased.

Parking Spot: The signal includes the date of the transaction, the driver's ID, and the duration of the parking.


| Signal                                                     | Type   | Payload			 														  	 | Trigger Point																					|
| ---------------------------------------------------------- | -----  | -------------------------------------------- | ------------------------------------------------------ |
| Vehicle.VehicleIdentification.VehicleSpecialUsage					 | String |>>> \|\${tx-date}\|${DriverId}\|Fuel\|\${liter}        | As soon as the vehicle left the Fuel Station           |
|																														 | String |>>> \|\${tx-date}\|${DriverId}\|Parking\|\${duration}  | As soon as the vehicle left the Parking                | 


## Implementation Guidelines

To implement the payment use case, participants should follow these steps:

1. **Smart Contract Creation**: Write a smart contract that defines the rules and conditions for the payment transactions in the Virtual City Metaverse. Include functions for initiating transactions, verifying data integrity, and updating payment statuses.

2. **Transaction Initiation**: Use the parsed data to initiate transactions on the Blockchain network. Ensure that the transactions are secure and follow the rules defined in the smart contract.

3. **Payment Verification**: Implement a mechanism for verifying payments based on the signals received. Use the smart contract to confirm that the transaction details match the data from the Kuksa data broker.

4. **Integration Testing**: Perform thorough testing of the payment use case to ensure its functionality and reliability within the Virtual City Metaverse.

5. **Documentation**: Provide detailed documentation of the implementation, including explanations of the Blockchain setup, smart contract design, and integration with the Python application.

6. **Presentation**: Prepare a presentation that highlights the key features and benefits of the payment use case. Include a demo of the application in action and explain how it addresses the challenges of secure and transparent transactions in a Virtual City Metaverse.




## Blockchain Infrastructure:

We have the Ethereum Besu network ready for use (Thanks to IBM for provding the VMs):

- JSON-RPC HTTP service endpoint: http://158.177.1.17:8545
- JSON-RPC WebSocket service endpoint: ws://158.177.1.17:8546
- Web block explorer address: http://158.177.1.17/25000/explorer/nodes


### Wallets: 
You can use the following Wallets to deploy and test: 
```json
"0xfe3b557e8fb62b89f4916b721be55ceb828dbd73" : {
		"privateKey" : "0x8f2a55949038a9610f50fb23b5883af3b4ecb3c3bb792cbcefbd1542c692be63",
		"balance" : "0x130EE8E7179044400000"
},
"0x627306090abaB3A6e1400e9345bC60c78a8BEf57" : {
		"privateKey" : "0xc87509a1c067bbde78beb793e6fa76530b6382a4c0241e5e4a9ec0a0f44dc0d3",
		"balance" : "90000000000000000000000"
},
"0xf17f52151EbEF6C7334FAD080c5704D77216b732" : {
		"privateKey" : "0xae6ae8e5ccbfb04590405997ee2d52d2b330726137b875053c36d94e974d162f",
		"balance" : "90000000000000000000000"
}
```


# Developing Tools:

 **Blockchain Smart Contract Development**:

[Hardhat Framework](https://hardhat.org/):

 Participants can use the Hardhat framework for developing smart contracts. The Hardhat framework is a development environment for Ethereum that allows developers to compile, test, and deploy smart contracts efficiently. It also provides debugging tools, and a local Ethereum network for testing.

 **Blockchain Interaction**:

[Web3.py](https://web3py.readthedocs.io/en/stable/):

 Use Web3.py for calling smart contracts from the Python project. Web3.py is a Python library that provides easy-to-use interfaces for interacting with Ethereum-based blockchains.



