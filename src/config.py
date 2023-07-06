from dotenv import load_dotenv
import os


load_dotenv()


class Config:

    """all credential"""

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
