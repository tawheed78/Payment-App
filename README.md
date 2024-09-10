"# Payment App" 
# Django Payment Integration Project

Welcome to the Django Payment Integration Project! This project demonstrates how to integrate various payment gateways (e.g., Razorpay) into a Django web application. Users can make payments by selecting a payment gateway and entering the required details.

## Features

- **Payment Gateway Integration**: Supports Razorpay for handling payments.
- **Dynamic Amount Input**: Users can specify the amount to be paid.
- **Payment Status Handling**: Verifies and displays payment success or failure.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Configuration](#configuration)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Create a `.env` File**:
  
    ```
    Update `.env` with your API keys and other sensitive data:
    ```
    DJANGO_SECRET_KEY=your_secret_key_here (SECRET_KEY)
    RAZORPAY_API_KEY=your_razorpay_api_key_here (API_KEY)
    RAZORPAY_API_SECRET=your_razorpay_api_secret_here (API_SECRET)
    ```

6. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

8. **Access the Application**:
    Open your browser and go to `http://127.0.0.1:8000/home/`.

## Usage

1. **Home Page**: Enter the amount and select the payment gateway from the dropdown.
2. **Payment Processing**: Follow the on-screen instructions to complete the payment.
3. **Payment Status**: Upon completion, you will be redirected to a success or failure page based on the transaction outcome.

## Configuration

1. **Settings**: Update `settings.py` to include your environment variable configurations.
2. **Payment Gateway**: Ensure that you have configured your Razorpay (or other gateways) API keys correctly in the `.env` file.



## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**:
    ```bash
    git checkout -b feature/your-feature
    ```
3. **Commit Your Changes**:
    ```bash
    git commit -m "Add feature"
    ```
4. **Push to the Branch**:
    ```bash
    git push origin feature/your-feature
    ```
5. **Open a Pull Request**

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for checking out the Django Payment Integration Project! Feel free to open issues or contribute improvements. If you have any questions, don’t hesitate to reach out.

