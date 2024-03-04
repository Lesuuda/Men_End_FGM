# Men End FGM

## Overview

Men End FGM is a project aimed at raising awareness and advocating for the end of Female Genital Mutilation (FGM). This README provides essential information for developers, contributors, and users interested in the project.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Installation](#installation)
   - [Running the Application](#running-the-application)
2. [Project Structure](#project-structure)
3. [Contributing](#contributing)
4. [License](#license)
5. [Contact](#contact)

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Men_End_FGM.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Men_End_FGM
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Run migrations:

   ```bash
   python manage.py migrate
   ```

2. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at `http://127.0.0.1:8000/`.

## Project Structure

- **web_project/**: Django project directory containing settings, URLs, and other configurations.
- **app/**: Main Django app directory containing models, views, and templates.
- **static/**: Directory for static files like CSS, JavaScript, and images.
- **templates/**: HTML templates for rendering views.
- **media/**: Directory for user-uploaded media files.

## Contributing

We welcome contributions from the community! If you want to contribute, please follow our [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

