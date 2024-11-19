from pydantic import BaseModel, Field


class UserCred(BaseModel):
    """
    Request Body for User credentials for sign up and login
    """

    email: str = Field(..., example="example@email.com")
    password: str = Field(..., example="password")


class SignUpSuccess(BaseModel):
    """
    Response Body for a successful sign up and DB update
    Manually done here for testing purposes
    """

    message: bool


class LoginSuccess(BaseModel):
    """
    Response Body for a successful login
    Returns the JWT token and add the same to the header
    """

    access_token: str
    token_type: str


class TokenSuccess(BaseModel):
    """
    Response Body for a successful token verification
    """

    message: str
    file_name: str


class AddBookRequest(BaseModel):
    """
    Request Body for adding a book to the database
    """
    title = Field(..., example="Book Title")
    author = Field(..., example="Author Name")
    version = Field(..., example="1.0")
    isbn = Field(..., example="978-3-16-148410-0")
    count = Field(..., example=5)

class AddBookSuccess(BaseModel):
    """
    Response Body for a successful book addition
    """

    message: str

class RentBookRequest(BaseModel):
    """
    Request Body for renting a book
    """
    email = Field(..., example="user@example.com")
    book_title = Field(..., example="Book Title")

class RentBookSuccess(BaseModel):
    """
    Response Body for a successful book rent
    """
    
    message: str