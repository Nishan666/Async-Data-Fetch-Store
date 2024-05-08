# Async Scheme Data Fetcher

This Python script asynchronously fetches mutual fund scheme data from an API and stores it in JSON files. It utilizes asyncio and aiohttp for asynchronous HTTP requests to improve efficiency.

## Prerequisites

Before running the script, ensure you have Python and pip installed on your system.

- **Python Installation:** If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).
- **PIP Installation:** PIP usually comes pre-installed with Python. You can verify if it's installed by running `pip --version` in your terminal/command prompt. If not installed, you can [install pip](https://pip.pypa.io/en/stable/installation/) manually.

## Installation and Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Nishan666/Async-Data-Fetch-Store.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd async-scheme-data-fetcher
    ```

3. **Create a virtual environment (optional but recommended):**

    ```bash
    # On Windows
    python -m venv venv
    
    # On macOS/Linux
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**

    ```bash
    # On Windows
    venv\Scripts\activate
    
    # On macOS/Linux
    source venv/bin/activate
    ```

5. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the script:**

    ```bash
    python fetch_data.py
    ```

   This will start fetching mutual fund scheme data in batches and store it in JSON files in the `scheme_data` folder.

## Configuration

- You can modify the `start_scheme_code`, `end_scheme_code`, `batch_size`, and `progress_threshold` parameters in the `fetch_data.py` script to customize the fetching behavior according to your requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
