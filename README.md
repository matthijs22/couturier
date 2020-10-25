# couturier
Couturier is serving platform for machinelearning models.

## Project overview
Couturier provides a simple method to expose multiple machinelearning models through a REST api. It currently only provides a prediction endpoints.  

## Quickstart
* `git clone https://github.com/matthijs22/couturier.git`
* `pip install -r requirements.txt`
* rename models/example.py
* change the model class in exmample.py to match the file
* implement the methods
* place your scaler in model in the format
    * ./models/pickles/<modelname>.model.sav
    * ./models/pickles/<modelname>.scaler.sav

## Docker integration
docker build . --tag mymodel
docker run -p 8080:8080 mymodel