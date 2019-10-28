## Topic Intro
A Interactive Restful API developed in Python Flask with Swagger UI using Ensembl public database for getting genes list result.

## Running Local
```
# Clone 
git clone https://github.com/yogeshrana18/Search-Gene.git
cd Search-Gene

# Create virtual Env.
pip3 install pipenv
pipenv shell

# Install app dependencies
pip3 install -r requirements.txt
```

## Start App
```
python3 app.py
```

## Testing
```
python3 test_app.py
```

## Docker process to launch
Building docker image using Dockerfile
```
docker build -t flaskapp:latest .
```
Run 
```
docker run -it -d -p 5000:5000 flaskapp
```

## Use this UI home at port 5000: http://127.0.0.1/

1. Choose search_gene and click
2. Choose Get Api 
3. Click Try it out
4. Fill parameter 
5. Execute and Enjoy !!
