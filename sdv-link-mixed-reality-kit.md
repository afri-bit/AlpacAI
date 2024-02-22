# SDV.Link Mixed Reality Kit

XIMAGE:SPLASHX

## Introduction

The SDV.Link App is an app preloaded on our VR headsets available at BCX (Meta Quest 3, Meta Quest 2 and Meta Quest Pro).

It is a controller-free application which visualizes and virtualizes a Virtual Car as well as a Mini map representing a Virtual City.

You're provided with an immersive environment with which you can develop car apps in lieu of an actual physical vehicle.

## What does it do and how does it work?

With SDV.Link, you are able to write applications based on Covesa and VSS signals. Applications emitting supported signals (listed below) can manipulate and visualize both the Virtual Car and how it works around the Virtual City. 

Interacting with the Virtual Car (e.g. opening doors, toggling switches, collisions to builidngs etc) also emits VSS signals so that your applications can react to these signals and write your use-cases.

## Is that all? What else is provided? What can i do with these?

So here is what is provided for you in order to take advantage of the SDV.Link app.

XIMAGE: ARCHITECTURE DIAGRAMX

**The SDV.Link App**
The Mixed Reality application which runs on our headsets available at BCX. 

**SDV.Link Companion App**
This is a python-based app which acts as a keyboard car controller. For one, It allows you to use WSAD keys for example for driving around (i..e emitting signals which tasks the car to move forward, back, etc). This is best paired with the SDV.Link VR App when used in City Mode. This will allow you to control the Mini City car and drive around the city. In turn, whatever events occuring within the city is also reported back (for example a car crash emits the IsBrokenDown signal). FUN!!

**Fetch.AI Cloud and Local Agent**
This is a pair of agents (One running on Fetch.AI and its DeltaV service) and the other is an agent which runs close to your broker (More about the broker later below). With such a setup you can have agents running on the cloud be able to communicate to your local setup. For example via DeltaV, you can use the LLM Chat service to send VSS commands to your vehicle. Not happy with that? Extend the code to put some fancy features in between!

**Smart Contracts**
There are some points in the Virtual City where it emits signals in order to perform payments. Maybe you can write a payment Smart Contract? Or maybe tap on the various other signals instead? (e.g. if the car breaks down, make a payment to a towing company and send for help!)

**The SDV Technology Stack**
This is a sizeable amount of frameworks and tools for you to write your applications such as Velocitas, Kuksa, Kuksa SDKs

**Any Covesa-compatible Hardware**

We provide, for example an actuating Smart Seat. The seat provides a Seat Service which you can develop apps against. Our Virtual car also has seats which are moveable, so you can have the seat move in the real and virtual at the same time. Imagine the next cool Passenger Welcome Use-case?

## Getting up and running



## Running a compatible stack or server (e.g. Kuksa DataBroker) 



## Install and Test the Kuksa Client



### Grab your VR and Set up the Guardian



## Run the SDV.Link App

In your VR headset, launch the 







# The SDV.Link App

## Getting around the app



#### Moving around and interacting



#### The Virtual Tablet

##### Configuring and Connecting to your broker



#### The Virtual Car





#### The Virtual City





# Writing SDV Apps

## The SDV.Link Companion App





### Writing Kuksa/Velocitas etc apps

##### Supported Signals by SDV.Link





## Fetch.AI and DeltaV Integration





## SmartContract Integration

