# couturier
Couturier is serving platform for machinelearning models.

## Project overview
Couturier provides a simple method to expose multiple machinelearning models through a REST api. It currently only provides a prediction endpoint.  

## Quickstart
```
git clone https://github.com/matthijs22/couturier.git
pip install -r requirements.txt
```
* rename or copy models/example.py
* change the model class in each of the model files should match the filename
* implement the methods in example.py
* place your scaler in and models/picle folder in the following format:
    * ./models/pickles/<modelname>.model.sav
    * ./models/pickles/<modelname>.scaler.sav

## Docker integration
```
docker build . --tag mymodel-couturier
docker run -p 8080:8080 mymodel-couturier
```
