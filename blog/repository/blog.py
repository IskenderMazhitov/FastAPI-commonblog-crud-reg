from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No created blogs')
    return blogs


def create(request: schemas.Blog, db: Session, ):
    blog = db.query(models.Blog).filter(
        models.Blog.title == request.title).first()
    if blog:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="The article with this title is already existed")
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"BLOG WITH THIS ID {id} is not available")
    return blog

def update(id, request:schemas.Blog, db: Session):
    updated_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not updated_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with such {id} id is not definded")
    updated_blog.update(dict(request), synchronize_session='evaluate')
    db.commit()
    return 'updated successfully'

def destroy(id, db: Session):
    deleted_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not deleted_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with such {id}id is not definded")
    deleted_blog.delete(synchronize_session=False)
    db.commit()
    # print(deleted_blog)
    return


