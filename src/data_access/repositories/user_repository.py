from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound

from src.data_access.database.models.users import UserEntity
from src.data_access.database.models.user_type_entity import UserTypeEntity
from src.common.models.library_management. user import user_types as enum_typ
from src.common.models.library_management.user import User, UserInDatabase, UserType
from src.data_access.repositories.base_repository import SqlAlchemyRelationalRepositoryBase

__all__ = [
    "UserSqlAlchemyRelationalRepository"
]


NO_IMPLEMENTATION = "No implementation"


class UserSqlAlchemyRelationalRepository(SqlAlchemyRelationalRepositoryBase):
    def __init__(self, context: Session) -> None:
        super().__init__(context=context)

    def add(self, *args, **kwargs) -> Optional[User]:
        raise NotImplementedError("Must be implemented by the specific user type subclass.")

    def add_user(self, user_type: enum_typ.UserTypes, **kwargs):
        user_model: UserInDatabase = UserInDatabase.parse_obj(kwargs)
        user_type = UserTypeEntity(**UserType(user_type=user_type).dict())
        db_user_type_query = self.context.query(UserTypeEntity)
        db_user_type = db_user_type_query.filter(UserTypeEntity.user_type == user_type.user_type).first()
        if db_user_type is not None:
            user_type = db_user_type
        db_user = self.context.query(UserEntity)
        try:
            db_user = db_user.filter(UserEntity.email_address == user_model.email_address).scalar()
            if db_user is not None:
                return UserInDatabase.from_orm(db_user)
        except MultipleResultsFound:
            return UserInDatabase.from_orm(db_user)
        else:
            user_entity = UserEntity(user_type=user_type, **user_model.dict())
            self.context.add(user_entity)
            self.sync()
        return UserInDatabase.from_orm(user_entity)

    def list(self, *args, **kwargs) -> List[User]:
        return super().list(*args, entity_model=UserEntity, app_out_model=User, **kwargs)

    def get(self, **filters):
        db_user = self.context.query(UserEntity).filter_by(**filters).first()
        if db_user is not None:
            return User.from_orm(db_user)

    def update(self, **kwargs):
        raise NotImplementedError(NO_IMPLEMENTATION)

    def delete(self, id_):
        raise NotImplementedError(NO_IMPLEMENTATION)