# Password Generator 🔑

Welcome to the **Password Generator** app! This interactive tool allows you to create strong, random passwords based on your custom criteria. You can choose the length, include digits, and add special characters to enhance your password's security.

The app is built using **Python** and **Streamlit**, providing an easy-to-use interface to generate secure passwords with just a few clicks.

## Features

- **Customizable Password Length:** Choose a password length between 10 and 30 characters.
- **Include Digits:** Option to add digits (0-9) to your password for added complexity.
- **Add Special Characters:** Add special characters (e.g., `!@#$%^&*`) to your password for extra security.
- **Balloons on Success:** Fun balloons animation once the password is generated!
- **Security Disclaimer:** The app uses Python's `secrets` module for generating passwords but is not suitable for sensitive applications.

## Technologies Used

- **Python:** The primary language used to develop the app's backend.
- **Streamlit:** A framework for building interactive web apps.
- **string Module:** For constructing passwords using letters, digits, and special characters.
- **random Module:** For selecting characters randomly to form the password.

## Installation

Follow these steps to run the **Password Generator** app locally:

### Prerequisites

Ensure that **Python** and **Streamlit** are installed. If not, you can install **Streamlit** using pip:

```bash
pip install streamlit

