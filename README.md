# Electric Vehicles as Mobile Batteries: dataset generation
This repository contains the code used to generate the synthetic electric vehicle (EV) mobility and charging dataset used in the study.
Because no open vehicle-centric EV datasets capture complete trip sequences and charging behavior, profiles were generated using emobpy and driver-specific constraints at a 15-minute resolution.
The repository focuses exclusively on reproducible dataset generation.

## Overview

This repository contains the dataset generation pipeline, prediction models, and simulation framework used to evaluate EVs as **mobile batteries** within Renewable Energy Communities (RECs) under a **Community-to-Vehicle-to-Community (C2V2C)** paradigm .

The framework:

* Predicts EV mobility and charging behavior
* Infers energy needs (not delivered energy)
* Recommends charging and discharging actions
* Maximizes REC self-consumption under regulatory constraints


## Dataset generation

Because open vehicle-centric EV datasets are unavailable, synthetic EV profiles were generated using the **emobpy** open source tool ([Gaete-Morales et al., 2021](https://doi.org/10.1038/s41597-021-00932-9)). 

For each EV, emobpy generates:

* Vehicle mobility
* Driving electricity consumption
* Grid availability
* Grid electricity demand

A Monte Carlo approach ensures variability across vehicles .


## Driver Typologies

Five driver profiles (200 EVs each, total 1000 EVs) :

* Delivery person
* Commuter
* Parents
* Unemployed
* Remote worker

Profiles are parameterized using European mobility studies.

## Dataset Characteristics

* 1,000 EVs
* 15-minute resolution
* 53 weeks training data
* 5 weeks testing data 


## Data Availability
The dataset is publicly available on [Dataverse](https://doi.org/10.14428/DVN/6GUFM9)


## Citation

If you use this repository, please cite:

> Van Rillaer, V., de Schietere de Lophem, M., Verhaeghe, H. *Electric Vehicles as Mobile Batteries: Automating Charge and Discharge Using Machine Learning Predictions* 

