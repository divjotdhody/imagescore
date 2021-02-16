# imagescore
imagescore
![](images/image11.png)


## Tech Stack
#### BackEnd  : Flask
#### FrontEnd : Vue.js
#### Database : MongoDB

## Docker deployment steps
## Backend

### Build
                <. Yourdockerid  >/<  ImageName  >
docker build -t divjotdhodydocker/imagecounter:v13 .

### Push 
            <. Yourdockerid  >/<  ImageName  >
docker push divjotdhodydocker/imagecounter:v13

### Run
                            <. Yourdockerid. >/<. ImageName  >
docker run -td -p 5000:5000 divjotdhodydocker/imagecounter:v13

## Frontend

### Build
docker build -t divjotdhodydocker/frontimagecounter:v1 .

### Push 
docker push divjotdhodydocker/frontimagecounter:v1

### Run
docker run -td -p 8080:8080 divjotdhodydocker/frontimagecounter:v1





