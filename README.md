




<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]]()
[![MIT License][license-shield]][license-url]

## Project title
Django rest framework walkthrough

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Project name screenshot ][product-screenshot]](https://www.django-rest-framework.org/img/logo.png)

This is django restframework walkthrough where a complete Pastebin API is created which is fully web browsable, includes a schema-driven library and comes with complete authentication, per-object permissions as well as multirender formats.

### Built With
Django framework, Pygments, Coreapi Coreapi-cli
* [Django web framework](https://www.djangoproject.com/)
* [Pygments](http://pygments.org/docs/api/)
* [Coreapi](https://www.coreapi.org/)
* [Coreapi-cli](https://github.com/core-api/coreapi-cli)


<!-- GETTING STARTED -->
## Getting Started

Clone the project from github

`git clone https://github.com/Curti-s/drf.git`

### Prerequisites
```
pip install django djangorestframework pygments coreapi coreapi-cli
```

<!-- USAGE EXAMPLES -->
## Usage

```
python -m venv env
source env/bin/activate
cd tutorial
python manage.py makemigrations snippets
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```
In the web browser
`http://localhost:8000`

In the terminal `coreapi get http://127.0.0.1:8000/schema/`

Authenticate coreapi ` coreapi credentials add 127.0.0.1 <username>:<password> --auth basic`

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@wizCurtis81](https://twitter.com/wizCurtis81) - matthewscurtis.dev81@gmail.com

Project Link: [drf](https://github.com/Curti-s/drf)


<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[product-screenshot]: https://www.django-rest-framework.org/img/logo.png