# My Website

## Images aspect ratio

For the several images in the app apart from the profile picture, utilize `1:2.6` aspect ratio. To comply with it, following image dimensions are recommended:

* Height: 12.7 [cm]
* Width: 33 [cm]

## Cloud Run Deployment

It's recommended to test the Dockerfile build by deploying it locally. To do so, execute the following commands:

* Build container image:

```sh
docker build -t my-website .
```

* Run docker container

```sh
docker run -p 8080:8080 my-website
```

Once the Dockerfile builds the container properly, deploy to Cloud Run with the following commands:

* Load the container image to GCP Artifact Registry:

```sh
gcloud builds submit --tag gcr.io/project-portfolio-422515/my-website --project=project-portfolio-422515
```

* Deploy CloudRun Service:

```sh
gcloud run deploy --image gcr.io/project-portfolio-422515/my-website:latest --platform managed --project project-portfolio-422515 --allow-unauthenticated
```

# References

* [Íconos de Bootstrap](https://icons.getbootstrap.com/)
* [Generador de fotos de perfil](https://picofme.io/)
