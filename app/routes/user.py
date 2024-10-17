# routes/user.py
from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import async_session
from app.models import UserDB
from app.schemas import UserCreate, UserLogin, ErrorResponse, Token
from app.utils.jwt_handler import create_access_token
from app.utils.security import verify_password, hash_password

router = APIRouter(tags=["User"])

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

@router.post("/registrar/", response_model=Token, responses={
    409: {
        "description": "Erro de Validação",
        "model": ErrorResponse,
        "content": {
            "application/json": {
                "example": {
                    "detail": "Email já encontrado na base de dados"
                }
            }
        }
    },
    422: {
        "description": "Erro de Validação",
        "model": ErrorResponse,
        "content": {
            "application/json": {
                "example": {
                    "detail": "Dados de entrada inválidos"
                }
            }
        }
    }
})
async def create_user(
    user: UserCreate = Body(..., example={
    "nome": "Disciplina Cloud",
    "email": "cloud@insper.edu.br",
    "senha": "cloud0"
}), session: AsyncSession = Depends(get_session)):
    new_user = UserDB(
        nome=user.nome,
        email=user.email,
        senha=hash_password(user.senha)
    )
    session.add(new_user)
    try:
        await session.commit()
        await session.refresh(new_user)

        # Exemplo no endpoint de registro
        access_token = create_access_token(data={"sub": new_user.email})
        return {"jwt": access_token}
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=409, detail="Email já encontrado na base de dados")

@router.post("/login/", response_model=Token)
async def login_user(
    user: UserLogin = Body(...),
    session: AsyncSession = Depends(get_session)
):
    # Verificar se o email existe no banco de dados
    result = await session.execute(select(UserDB).where(UserDB.email == user.email))
    db_user = result.scalar_one_or_none()
    if db_user is None:
        # Email não encontrado
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")
    
    hashed_input_password = hash_password(user.senha)

    # Verificar se a senha está correta
    if not verify_password(hashed_input_password, db_user.senha):
        # Senha incorreta
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")
    
    # Gerar o token JWT
    access_token = create_access_token(data={"sub": db_user.email})
    return {"jwt": access_token}
