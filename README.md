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
  ![ScreenShot](https://github.com/yogeshrana18/Search-Gene/blob/master/Scr_shots/gene1.png?raw=true){:height="36px" width="36px"}
2. Choose Get Api 
  ![ScreenShot](https://github.com/yogeshrana18/Search-Gene/blob/master/Scr_shots/gene2.png?raw=true)
3. Click Try it out
  ![ScreenShot](https://github.com/yogeshrana18/Search-Gene/blob/master/Scr_shots/gene3.png?raw=true)
4. Fill parameter 
  ![ScreenShot](https://github.com/yogeshrana18/Search-Gene/blob/master/Scr_shots/gene4.png?raw=true)
5. Execute and Enjoy !!
