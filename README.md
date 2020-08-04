# Vehicle Collision in NYC
## Table of Contents
1. Demo
2. Overview
3. Motivation
4. Installation
## Demo
![Screenshot (50)](https://user-images.githubusercontent.com/48888895/89260186-672a3f00-d649-11ea-9fe1-b998c805e6a1.png)
![Screenshot (51)](https://user-images.githubusercontent.com/48888895/89260248-8923c180-d649-11ea-9d3c-8a87f14c741b.png)
![Screenshot (52)](https://user-images.githubusercontent.com/48888895/89260309-a48ecc80-d649-11ea-866b-303134ce20df.png)
![Screenshot (53)](https://user-images.githubusercontent.com/48888895/89260361-be301400-d649-11ea-8999-680700826013.png)
## Overview
This application is a dashboard made with streamlit library. It allows the users to explore vehicle collisions in New York City and shows not only the raw data in a tabular format but also plots the geographic location of those collisions in a map of NYC using plotly library.The dataset used in this application is of large size(87Mb) which can't be uploaded to github.You can find the dataset [here](https://www.kaggle.com/nypd/vehicle-collisions).
## Motivation
When I learnt about the streamlit library and came to know about it's wonderful features, I wanted to make an application using it.This was my first application using streamlit.
## Installation
The Code is written in Python 3.6.10. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after cloning the repository:

pip install -r requirements.txt

After installing all the required libraries run the following command in your command prompt in the project directory:

streamlit run app.py
