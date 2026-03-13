from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    code: str


class ReviewRequest(BaseModel):
    original_code: str
    user_fix: str


class IssueResponse(BaseModel):
    line: int
    problem: str
    suggestion: str


class AnalyzeResponse(BaseModel):
    score: int
    issues: list[IssueResponse]
    improved_code: str


class ReviewResponse(BaseModel):
    score: int
    feedback: str
    comparison: str