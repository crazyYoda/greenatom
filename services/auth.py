from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from services.auth_service import AuthService, get_current_user
from services.user_auth import UserCreate, Token, User

router = APIRouter(
    prefix='/auth',
)


@router.post('/sign-up', response_model=Token)
def sing_up(user_data: UserCreate,
            service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post('/sign-in', response_model=Token)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends(),
            service: AuthService = Depends()):
    return service.autheticate_user(
        form_data.username,
        form_data.password,
    )


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user
