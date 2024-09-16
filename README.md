<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Apache License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/eslemkarakas/autoart-backend">
    <img src="images/autoart-logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">AutoArt: Automate, Innovate, Dominate</h3>

  <p align="center">
    <a href="https://github.com/eslemkarakas/autoart-backend/docs"><strong>Documentation »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#feedback">Contributing</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

AutoArt is a powerful open-source machine learning platform that builds learning models by supporting both regression and classification tasks with minimum provision from data scientists. This platform has a broad range of compatibility with cloud services and leverages their storage, database, security, and computing services. It retrieves the data from the source securely, extracts the significant features from the data, specifies which preprocessing and modeling techniques will be applied, trains the model with best parameters and deploys the container image and trained model into production in selected cloud provider.



<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Languages

* [![Python][Python.py]][Python-url]

### Packages
* [![NumPy][NumPy.io]][NumPy-url]
* [![Polars][Polars.io]][Polars-url]
* [![sklearn][sklearn.io]][sklearn-url]
* [![Poetry][Poetry.io]][Poetry-url]
* [![Docker][Docker.io]][Docker-url]
* [![MLFlow][MLFlow.io]][MLFlow-url]
* [![FastAPI][FastAPI.io]][FastAPI-url]
* [![PyTest][PyTest.io]][PyTest-url]
  
### Services
* [![S3][S3.io]][S3-url]
* [![Redshift][Redshift.io]][Redshift-url]
* [![SecretsManager][SecretsManager.io]][SecretsManager-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

You need to have Poetry installed. Here is how to install Poetry and verify the installation.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* poetry
  ```sh
  pip install poetry==1.6.0
  poetry --version # confirm the installation
  ```

### Installation

1. Clone the repository.
   ```sh
   git clone https://github.com/eslemkarakas/autoart-backend.git
   ```
2. Navigate to the project directory.
   ```sh
   cd autoart-backend
   ```
3. Create and activate the virtual environment with Poetry.
   ```sh
   poetry shell
   ```
4. Install development stage dependencies.
   ```sh
   poetry install --only dev
   ```
5. Change git remote url to avoid accidental pushes to base project.
   ```sh
   git remote set-url origin eslemkarakas/autoart-backend
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This provides a clear note that the usage details will be added later.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- FEEDBACK -->
## Feedback

We welcome your positive, negative, and constructive feedback to help shape a growth roadmap for AutoArt. Together, we aim to make AutoArt more effective and user-friendly for everyone.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing_feature`)
3. Commit your Changes (`git commit -m 'Enter your commit message here.'`)
4. Push to the Branch (`git push origin feature/amazing_feature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/eslemkarakas/autoart-backend/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=eslemkarakas/autoart-backend" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Eslem Karakaş - eslem.karakas.tr@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/eslemkarakas/autoart-backend.svg?style=for-the-badge
[contributors-url]: https://github.com/eslemkarakas/autoart-backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/eslemkarakas/autoart-backend.svg?style=for-the-badge
[forks-url]: https://github.com/eslemkarakas/autoart-backend/network/members
[stars-shield]: https://img.shields.io/github/stars/eslemkarakas/autoart-backend.svg?style=for-the-badge
[stars-url]: https://github.com/eslemkarakas/autoart-backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/eslemkarakas/autoart-backend.svg?style=for-the-badge
[issues-url]: https://github.com/eslemkarakas/autoart-backend/issues
[license-shield]: https://img.shields.io/github/license/eslemkarakas/auto-art.svg?style=for-the-badge
[license-url]: https://github.com/eslemkarakas/autoart-backend/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/eslemkarakas
[product-screenshot]: images/screenshot.png
[Python.py]: https://img.shields.io/badge/python-306998?style=for-the-badge&logo=python&logoColor=FFD343
[Python-url]: https://www.python.org/
[Poetry.io]: https://img.shields.io/badge/poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=FFFFFF
[Poetry-url]: https://python-poetry.org/docs/
[Polars.io]: https://img.shields.io/badge/polars-FFFFFF?style=for-the-badge&logo=polars&logoColor=0E76A8
[Polars-url]: https://pola.rs/
[Docker.io]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=FFFFFF
[Docker-url]: https://www.docker.com/
[MLFlow.io]: https://img.shields.io/badge/mlflow-0194E2?style=for-the-badge&logo=mlflow&logoColor=FFFFFF
[MLFlow-url]: https://mlflow.org/
[FastAPI.io]: https://img.shields.io/badge/fastapi-009688?style=for-the-badge&logo=fastapi&logoColor=FFFFFF
[FastAPI-url]: https://fastapi.tiangolo.com/
[PyTest.io]: https://img.shields.io/badge/pytest-000000?style=for-the-badge&logo=pytest&logoColor=white&color=black
[PyTest-url]: https://pypi.org/project/pytest/
[NumPy.io]: https://img.shields.io/badge/numpy-4F5D75?style=for-the-badge&logo=numpy&logoColor=FFFFFF
[NumPy-url]: https://numpy.org/
[sklearn.io]: https://img.shields.io/badge/sklearn-FABB00?style=for-the-badge&logo=scikit-learn&logoColor=000000
[sklearn-url]: https://scikit-learn.org/
[S3.io]: https://img.shields.io/badge/s3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=FFFFFF
[S3-url]: https://aws.amazon.com/s3/
[SecretsManager.io]: https://img.shields.io/badge/secretsmanager-E24C4C?style=for-the-badge&logo=aws-secrets-manager&logoColor=FFFFFF
[SecretsManager-url]: https://aws.amazon.com/secrets-manager/
[Redshift.io]: https://img.shields.io/badge/redshift-4053D6?style=for-the-badge&logo=amazon-redshift&logoColor=FFFFFF
[Redshift-url]: https://aws.amazon.com/redshift/
