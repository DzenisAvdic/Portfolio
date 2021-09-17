# Portfolio
#### Dženis Avdić
Summary for **ETH** *Zurich*

### 1 :: DATA MINING :: WEB SCRAPING

-	Created a script that runs locally to read and store weather data i CSV format
-	Data obtained from Federal Hydrometeorological Institute for Sarajevo, Bosnia and Herzegovina
-	Windrose plot is being updated with every new value and stored as PNG image
-	CSV data is used for analysis of daytime winds in Sarajevo for specific periods


*Sarajevo windrose based on dataset collected from september 2020 to september 2021*

### 2 :: DATA MINING :: SENSOR LOGGER AND WEB API DATA

-	[Data logger][1] is made with open electronics components to collect data inside observed architectural spaces
-	15-minute logs are being stored to microSD card in CSV format for later analyses
-	Available meteorological and air quality data from web APIs is being stored simultaneously
-	Long term monitoring and data collecting for scientific research in building physics and energy efficiency

[1]: https://github.com/DzenisAvdic/Air-Quality-and-Meteorology-Data-Logger

### 3 :: DATA PREPROCESSING AND OBSERVATIONS

-	Based on [collected data][2] specific analyses were conducted
-	Missing values and sensor misreadings were recognised and filled in with neighbouring values average
-	Physical phenomena were analysed for wind movement, natural ventilation and infiltration

*Infiltration air change rate based on collected data - Python plot*

[2]: LINK

### 4 :: DATA VERIFICATION AND VALIDATION USING CFD SIMULATIONS

-	2D and 3D CFD simulations were conducted for typologicaly specific building form

*Building block with courtyard typology*


*'Marijin dvor' building air change rate simulations*


-	Based on real data (weather stations data), natural ventilation potential was estimated for neighbourhood (urban area ventilation) and single apartment (interior ventilation air flow)


-	Pedestrian and street level air movement phenomena was analysed for arguably misplaced high rise building in Sarajevo area

### 5 :: MACHINE LEARNING :: TIME SERIES FORECASTING

-	Tensorflow Recurrent Neural Network (RNN) with Gated Recurrent Units (GRUs) for time series forecasting was deployed to Arduino Nano 33 BLE Sense using TinyML
-	Three different prediction algorithms were discussed and compared (ARIMA, facebook Prophet and Tensorflow RNN)
-	Low-energy consumption [AI assisted system is proposed][3] for natural ventilation control and predictive maintenance

[3]: https://github.com/DzenisAvdic/Air-Quality-and-Meteorology-Data-Logger/tree/main/Journal%20of%20Pervasive%20Technology%20reference%20files

### 6 :: LOW-POLY 3D MODELING :: OPTIMISATION FOR UNITY AND UNREAL ENGINE

-	Worflow includes various software for 3D modeling, retoplogy and texturing
-	Optimisation of highly detailed 3D models for web and UI/UX integration




