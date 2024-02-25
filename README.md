# SDV_GettingStarted
- [About](#about)
    - [Company Description](#company_desc)
    - [Hack Coaches](#hack-coaches)
- [What do we bring](#what-we-provide)
- [Sample Hack Challenges](#sample-scenarios)
    - [Provided Sample Scenario](#provided-sample-hacks)
    - [Other Sample Scenarios](#other-sample-hacks)
- [Getting Started](#getting-started)
    - [Need to know](#need-to-know)
    - [Prebuilt Container Images](#prebuilt-container-images)


## About<a name="about"></a>

### Company Description<a name="company_desc"></a>

SDV combines a number of technologies and open source projects around the idea of Software Defined Vehicles. These activities mostly origniate from the Eclipse SDV working group or COVESA for connected vehicles.

### Hack Coaches<a name="hack-coaches"></a>

- <img src="img/Jeroschewski-teaser.JPG" alt="Image Sven" width="auto" height="200"> - @Sven Jeroschewski (Bosch Digital/ETAS)
- <img src="img/lukas.jpg" alt="Image Lukas" width="auto" height="200"> Lukas Mittag - @Lukas Mittag
- <img src="img/pavel.jpg" alt="Image Pavel" width="auto" height="200"> Pavel Simo - @Pavel Simo
- <img src="img/johannes.jpg" alt="Image Johannes" width="auto" height="200"> Johannes Kristan - @Johannes Kristan (Bosch)

## What do we bring<a name="what-we-provide"></a>

- [Eclipse Kuksa data broker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker)
- [Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/)
- VR Simulation of a single vehicle (see [SDV.Link Mixed Reality Kit](sdv-link-mixed-reality-kit.md) for more details)
- VR simulation of a city
- real moveable car seat

## Sample Scenarios<a name="sample-scenarios"></a>

### Provided Sample Hack Challenges<a name="provided-sample-hack"></a>

With the available technology and examples like a AR simulaiton and an actual car seat, hackers can develope and test applications which interact with the actuators and sensors in a vehicle.

### Other Sample hacks<a name="other-sample-hacks"></a>

One specific example is the implementation of a driver profile service which adjusts the seat according the user preference.

## Getting Started<a name="getting-started"></a>

We provide a number of building blocks that you can utilize to create your application and personal use case through the Kuksa databroker.
To get started we recommend that you familiarize yourself with the overall concepts and technologies in SDV, e.g., by going through the ["Introduction to SDV concepts"](https://eclipse-leda.github.io/leda/docs/general-usage/sdv-introduction/).

The central piece is the Kuksa data broker which manages and stores the current state of a vehicle. So your application will interact with the data broker. There is a full development tool chain which supports you during such an application by providing code templates, SDKs, pre-defined build, test and release pipelines, and deployment capabilities. This is described in the ["Companion Application Blueprint"](https://sdv-blueprints.eclipse.dev/docs/companion-application/). Once you setup described the blueprint, you are able to modify the example application, which adjusts a seat, to the signals of your hack idea.

As an alternative, you can skip the Companion Application Blueprint setup and instead use the Kuksa SDK for [Python](https://github.com/eclipse-kuksa/kuksa-python-sdk), [Android](https://github.com/eclipse-kuksa/kuksa-android-sdk) or [Rust](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker/lib) or generate your client library with the [gRPC](https://grpc.io) tooling from the [kuksa.val.v1 API definition](https://github.com/eclipse/kuksa.val/tree/master/proto/kuksa/val/v1) of the Kuksa data broker.

### Need to know<a name="need-to-know"></a>

The state in the databroker is expressed with the semantics defined in the Vehicle Signal Specification (VSS).
VSS defines a tree structure of signals in a vehicle and their semantics.
For instance, you can get the Vehicle Speed through the signal [Vehicle.Speed](https://github.com/COVESA/vehicle_signal_specification/blob/f28c3e7bc93be4d05babe103935d50af9d749653/spec/Vehicle/Vehicle.vspec#L199) which uses kilometer per hour as unit.
The [digital.auto Playground](https://digitalauto.netlify.app/model/STLWzk1WyqVVLbfymb4f/cvi/list) provides a very good visulization of the available signals. However, the Playground uses version 3.0 of VSS while the other components in our setup rely on version 4.0.
More details on the general SDV concepts are available in the guide .

As part of the BCX you can let your application interact through the Kuksa databroker with

- a [vehicle simulation in VR](simulation.md)
- an [actual car seat](seat.md).

In addition, we provide a setup to interface the data broker with Fetch.AI through a [corresponding agent](fetch-agent.md). This way you can control the data broker with natural language command like "Set Seat Position to 100". Fetch.AI is then able to interpret this command with an LLM and calls the corresponding agent.

### Prebuilt Container Images<a name="prebuilt-container-images"></a>

* Eclipse Kuksa [data broker](https://github.com/eclipse/kuksa.val/pkgs/container/kuksa.val%2Fdatabroker)
* [Eclipse Kuksa Client](https://github.com/eclipse/kuksa.val/pkgs/container/kuksa.val%2Fkuksa-client) which includes a CLI to interact with the Kuksa data broker
