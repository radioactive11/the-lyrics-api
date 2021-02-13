<p float="left">

[![forthebadge](https://forthebadge.com/images/badges/contains-tasty-spaghetti-code.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://forthebadge.com)
</p>

<!-- PROJECT LOGO -->
<br/>
<p align="center">
  <a href="https://github.com/radioactive11/the-lyrics-api">
    <img src="STATIC_IMG/header1.svg" alt="Logo" width="420" height="420">

    
  </a>

  <h1 align="center">The Lyrics API</h1>

  <p align="center">
    Get lyrics for English and Hindi songs
    <br />
    <br />
    <a href="https://the-lyrics-api.herokuapp.com/lyrics">View Demo</a>
    ·
    <a href="https://github.com/radioactive11/the-lyrics-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/radioactive11/the-lyrics-api/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Product Screenshots](#Product-Screenshots)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Contact](#contact)




<!-- ABOUT THE PROJECT -->
## About The Project

The lack of an working open source API that allows users to fetch lyrics for a song without rate limiting led me to build this. I've hosted this API on Heroku temporarily. Since I'm always use up my monthly *free Heroku dyno hours*, dont be surprised if the the link stops working. I'll find a permanent solution soon. 

<br/>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.7+
* FastApi
* BeautifulSoup4
* Uvicorn

### Installation 

<br />

1. Clone the repo 
```sh
git clone https://github.com/radioactive11/the-lyrics-api
```

2. Install requirements
```sh
pip3 install -r requirements.txt
```

3. Start FastAPI server(by default at `localhost:8000`)

```sh
uvicorn main:app
```

## Usage
<br />

#### English Songs

The request body for English songs is:

```sh
curl --location --request GET 'https://the-lyrics-api.herokuapp.com/lyrics' \
--header 'Content-Type: application/json' \
--data-raw '{
    "artist": "Taylor Swift",
    "song": "State of Grace",
    "lang": "eng"
}'
```

#### Hindi Songs

The request body for Hindi songs is:

```sh
curl --location --request GET 'https://the-lyrics-api.herokuapp.com/lyrics' \
--header 'Content-Type: application/json' \
--data-raw '{
    "artist": "Arijit Singh",
    "song": "Darkhaast",
    "lang": "hin"
}'
```

*Note: By default, the language parameter is set to English so you can ignore it for English Songs*

#### Response Format:
```json
{
    "lyrics": "string"
}
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/radioactive11/the-lyrics-api/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request





<!-- CONTACT -->
## Contact

Arijit Roy - [GitHub](https://github.com/radioactive11) - roy.arijit2001@gmail.com


Endpoint: [https://the-lyrics-api.herokuapp.com/lyrics](https://the-lyrics-api.herokuapp.com/)


<img src = "STATIC_IMG/comic.png">


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/radiaoctive11/HealthBridge.svg?style=flat-square
[contributors-url]: https://github.com/radioactive11/the-lyrics-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/radiaoctive11/HealthBridge.svg?style=flat-square
[forks-url]: https://github.com/radioactive11/the-lyrics-api/network/members
[stars-shield]: https://img.shields.io/github/stars/radiaoctive11/HealthBridge.svg?style=flat-square
[stars-url]: https://github.com/radioactive11/the-lyrics-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/radiaoctive11/HealthBridge.svg?style=flat-square
[issues-url]: https://github.com/radioactive11/the-lyrics-api/issues
[license-shield]: https://img.shields.io/github/license/radiaoctive11/HealthBridge.svg?style=flat-square
[license-url]: https://github.com/radioactive11/the-lyrics-api/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: STATIC_IMG/ss1.png

[node-js]: "https://img.shields.io/badge/-JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"
