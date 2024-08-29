from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from . import models, schemas, database

# JWT secret and algorithm
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password:str, hashed_password:str):
    """ 
    verify the plain text with the hashed password 
    """
    return pwd_context.verify(plain_password,hashed_password)

def get_password_hash(password:str):
    """ 
    Hash the password
    """
    return pwd_context.hash(password)

def authenticate_user(db:Session, username:str, password:str ):
    """ 
    Authenticate the User and validate the password
    """

    # Query the database 
    user = db.query(models.User).filter(models.User.username==username).first()

    if not user:
        return False 

    # Validate the given password with the hashed password
    if not verify_password(password,user.hashed_password):
        return False
    
    return user


def create_access_token(data:dict, expires_delta:timedelta=None):
    """ 
    Create access token
    """

    # Copy the data in the dictionary to a new dict 
    to_encode = data.copy() 

    # Add a default timing 
    if expires_delta: 
        expire = datetime.now() + expires_delta 
    else: 
        expire = datetime.now() + timedelta(minutes=15)

    # Add expiry to the data to be encoded
    to_encode.update({"exp":expire})
    
    # Encode the jwt and return it 
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
