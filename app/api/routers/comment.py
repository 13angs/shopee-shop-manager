from fastapi import APIRouter, Depends, HTTPException
from app.api.models.comment import Comment
from app.api.dependencies.external_api import fetch_comment_data
from app.api.dependencies.authentication import verify_token

router = APIRouter()

@router.get("/comments/{comment_id}", response_model=Comment)
def read_comment(comment_id: int, payload: dict = Depends(verify_token)):
    # Fetch the comment data from your external provider
    # and return it as a Comment object
    comment_data = fetch_comment_data(comment_id)  # You need to implement this function
    if comment_data is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return Comment(**comment_data)
