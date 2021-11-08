import os
from datetime import datetime
from typing import List

import fastapi
from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks, Depends, Header, status

from services.auth_service import get_current_user
from schemas import GetListImages
from DB.models import Image, User
from services.services import write_image, delete_old_file
from uuid import uuid4
from services.auth import router as auth_router

image_router = APIRouter()
image_router.include_router(auth_router)


@image_router.post('/frame/')
async def upload_img(
        background_tasks: BackgroundTasks,
        images: List[UploadFile] = File(...),
        uploading_files: int = fastapi.Query(description='Max number of files - 15', ge=1, le=15, default=None),
        user: User = Depends(get_current_user),
):
    if len(images) > uploading_files:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Too many files"
        )
    else:
        for img in images:
            path = f'data/{datetime.now().strftime("%Y%m%d")}'
            file_name = f'{path}/{uuid4()}.jpeg'
            if not os.path.isdir(path):
                os.mkdir(path)
            if img.content_type == 'image/jpeg':
                background_tasks.add_task(write_image, file_name, img)
                await Image.objects.create(file=file_name, create_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            else:
                raise HTTPException(status_code=418, detail="It isn't jpeg")
    return {'status': "OK"}


@image_router.get("/user/imagelist", response_model=List[GetListImages])
async def get_list_images(user: User = Depends(get_current_user)):
    return await Image.objects.all()


@image_router.get('/frame/{image_pk}', response_model=Image)
async def get_images(image_pk: int,
                     user: User = Depends(get_current_user)
                     ):
    return await Image.objects.get(pk=image_pk)


@image_router.delete('/frame/{image_pk}')
async def delete_images(background_tasks: BackgroundTasks,
                        image_pk: int,
                        user: User = Depends(get_current_user)):
    object = await Image.objects.get(pk=image_pk)
    path_file = object.file
    await Image.objects.delete(pk=image_pk)
    background_tasks.add_task(delete_old_file, path_file)
    return 'DELETED'
