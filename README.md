
FaceLink is a social media application built using Django. It allows users to connect, chat, and interact with each other in a seamless way. The platform features real-time chat functionality and user-friendly social networking features.

## Features
- User authentication (Signup/Login)
- Friend system (Send/Accept friend requests)
- Real-time chat functionality
- Notifications system
- Profile management
- Media uploads (Profile pictures, GIFs, etc.)

## Tech Stack
- **Backend:** Django, Django Channels (for real-time chat)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be replaced with PostgreSQL or MySQL)
- **WebSockets:** Django Channels

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Virtualenv (optional but recommended)

### Setup Instructions

1. **Clone the Repository**
   ```sh
   git clone https://github.com/spidyshivam/facelink.git
   cd facelink
   ```

2. **Create a Virtual Environment** (optional but recommended)
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser (Admin Panel Access)**
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. **Collect Static Files**
   ```sh
   python manage.py collectstatic
   ```

7. **Run the Development Server**
   ```sh
   python manage.py runserver
   ```
   The app should now be accessible at `http://127.0.0.1:8000/`

## Running the Chat Server

To enable real-time chat, Django Channels must be running:
```sh
python manage.py runserver
```


## Deployment
For production deployment, ensure you:
- Use PostgreSQL instead of SQLite
- Configure `DEBUG = False` in `settings.py`
- Set up a proper ASGI server (e.g., Daphne or Uvicorn)
- Serve static files using Nginx

## Contributing
Feel free to fork the repository and submit pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License.

---
Made with ❤️ by Shivam Patel

