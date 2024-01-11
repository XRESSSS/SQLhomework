import asyncio

from sqlalchemy import insert, select, update, delete

from models import User, Order
from database import async_session_maker


async def create_user(
        name: str,
        login: str,
        password: str,
        age: int,
        nickname: str = None,
        notes: str = None,
) -> tuple:
    async with async_session_maker() as session:
        query = insert(User).values(
            name=name,
            login=login,
            password=password,
            age=age,
            nickname=nickname,
            notes=notes,
        ).returning(User.id, User.created_at, User.login)
        print(query)
        data = await session.execute(query)
        await session.commit()
        print(tuple(data))
        return tuple(data)[0]


async def fetch_users(skip: int = 0, limit: int = 10) -> list[User]:
    async with async_session_maker() as session:
        query = select(User).offset(skip).limit(limit)
        result = await session.execute(query)
        print(query)
        print(result.scalars().all()[0].login)
        return result.scalars().all()


async def get_user_by_id(user_id: int) -> User | None:
    async with async_session_maker() as session:
        query = select(User).filter_by(id=user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def update_user(user_id: int, values: dict):
    if not values:
        return
    async with async_session_maker() as session:
        query = update(User).where(User.id == user_id).values(**values)
        result = await session.execute(query)
        await session.commit()
        print(query)


async def delete_user(user_id: int):
    async with async_session_maker() as session:
        query = delete(User).where(User.id == user_id)
        await session.execute(query)
        await session.commit()
        print(query)


async def main():
    await asyncio.gather(
        # create_user(
        #     name='Evgeny',
        #     login='asalamaleikum',
        #     password='1234',
        #     age=25,
        #     nickname='xres',
        # ),
        # fetch_users(skip=1)
        # get_user_by_id(2),
        # update_user(1, {'name': 'Alex', 'age': 65})
        # delete_user(1)
    )


asyncio.run(main())
