from pydantic import BaseModel, Field


class AnswerRequestBody(BaseModel):
    question_id: int = Field(gt=0, description="question id from response")
    answer: str = Field(min_length=1, max_length=128)
    user_email: str


class LetterRequestBody(BaseModel):
    question_id: int = Field(gt=0, description="question id from response")
    letter: str = Field(max_length=1, description="value for skipped letter")
    user_email: str


class UserLoginBody(BaseModel):
    email: str = Field(min_length=1, max_length=128)
