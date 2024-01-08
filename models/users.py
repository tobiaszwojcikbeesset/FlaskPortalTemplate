
from models.base import Base, BaseIncr
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text
from sqlalchemy.orm import Relationship
from flask_login import UserMixin

class User(UserMixin, BaseIncr):
    __tablename__ = "users"
    login = Column(String(50), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    address = Relationship('Address', back_populates='user', passive_deletes=True)
    roles = Relationship('Role', secondary="user_roles", back_populates="users", passive_deletes=True)
    

    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.login}"

class Address(BaseIncr):
    __tablename__ = "adresses"

    name = Column(String(255))
    first_name = Column(String(50))
    last_name = Column(String(50))
    street = Column(String(150))
    country = Column(String(50))
    city = Column(String(100))
    phone_number = Column(String(15))
    postcode = Column(String(7))
    active = Column(Boolean, default=True)
    nip = Column(Integer)
    user_loid = Column(Integer, ForeignKey("users.loid", ondelete="CASCADE"), nullable=False, index=True)
    user = Relationship('User', back_populates="address" )

    def __repr__(self) -> str:
            return f"{self.__class__.__name__}: {self.first_name} {self.last_name}\n{self.street}\n{self.postcode}, {self.city}"

class Role(BaseIncr):
    __tablename__ = "roles"

    name = Column(String(80))
    slug = Column(String(80))

    users = Relationship('User', secondary="user_roles", back_populates="roles", passive_deletes=True)
    resources = Relationship('Resource', secondary="role_resources", back_populates="roles", passive_deletes=True)
    def __init__(self, name, slug):
        self.name = name
        self.slug = slug

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.name}"

    
class UserRole(Base):
    __tablename__ = "user_roles"

    user_loid = Column(Integer, ForeignKey('users.loid', ondelete="CASCADE"), primary_key=True)
    role_loid = Column(Integer, ForeignKey('roles.loid', ondelete="CASCADE"), primary_key=True)

class Resource(BaseIncr):
    __tablename__ = "resources"

    name = Column(String(255), unique=True, nullable = False)
    resource = Column(String(100), unique=True, nullable = False)
    description = Column(Text, nullable=True)
    roles = Relationship('Role', secondary="role_resources", back_populates="resources", passive_deletes=True)

class RoleResource(Base):
    __tablename__ = "role_resources"

    resource_loid = Column(Integer, ForeignKey('resources.loid', ondelete="CASCADE"), primary_key=True)
    role_loid = Column(Integer, ForeignKey('roles.loid', ondelete="CASCADE"), primary_key=True)
