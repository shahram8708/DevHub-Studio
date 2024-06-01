# DevHub Studio

DevHub Studio is an innovative online coding platform designed to allow users to write, run, and debug code in various programming languages. Built with a sleek and responsive interface, DevHub Studio provides a seamless coding experience, especially optimized for mobile devices.

## Website

Access the live platform at [DevHub Studio](https://devhub-studio.onrender.com/).

## GitHub Repository

View the source code and contribute at [DevHub Studio GitHub Repo](https://github.com/shahram8708/DevHub-Studio).

## Features

- **Multi-language Support**: Write and execute code in numerous programming languages including Python, Java, C++, and more.
- **Responsive Design**: Optimized for use on mobile devices, ensuring a smooth and user-friendly experience.
- **Code Editor**: A powerful code editor with syntax highlighting, line numbers, and a clean, distraction-free interface.
- **Instant Execution**: Run your code instantly and view the output in real-time.
- **Search Functionality**: Easily search for supported programming languages.
- **Seamless UI**: Intuitive design with easy navigation between code editor and output viewer.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Flask
- Requests library

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/shahram8708/DevHub-Studio.git
    cd DevHub-Studio
    ```

2. Install the necessary packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:

    ```sh
    python app.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

### Usage

- **Home Page**: The home page features a code editor and output display area.
- **Select Language**: Use the dropdown menu to select the desired programming language.
- **Write Code**: Write your code in the provided editor.
- **Run Code**: Click the "Run Code" button to execute your code. The output will be displayed in the output container.
- **Search Languages**: Use the search bar to filter and quickly find specific programming languages.

## Code Explanation

### `app.py`

The Flask application handles the backend logic.

- **Home Route** (`/`): Renders the `index.html` template.
- **Run Code Route** (`/run`): Accepts POST requests with the code and language to execute using the JDoodle API.

### `index.html`

The HTML file provides the frontend interface.

- **Editor Container**: Contains the code editor and language selection dropdown.
- **Output Container**: Displays the result of the executed code.
- **JavaScript Functions**: Handles the code execution and language search functionalities.

## API Integration

DevHub Studio uses the JDoodle API to compile and run code. Ensure you have a JDoodle account and API credentials.

```python
JDoodle_CLIENT_ID = 'your_client_id'
JDoodle_CLIENT_SECRET = 'your_client_secret'
```

Replace the placeholders with your actual JDoodle API credentials.

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to the branch.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For more details, visit the [DevHub Studio GitHub Repository](https://github.com/shahram8708/DevHub-Studio).
