from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, TIMESTAMP
from sqlalchemy.sql import func
from .database import Base

class DistributionCenter(Base):
    __tablename__ = "distribution_centers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    age = Column(Integer)
    gender = Column(String)
    state = Column(String)
    city = Column(String)
    postal_code = Column(String)
    country = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    traffic_source = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Float)
    category = Column(String)
    name = Column(String)
    brand = Column(String)
    retail_price = Column(Float)
    department = Column(String)
    sku = Column(String)
    distribution_center_id = Column(Integer, ForeignKey("distribution_centers.id"))

class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())
    sold_at = Column(TIMESTAMP)
    cost = Column(Float)
    product_category = Column(String)
    product_name = Column(String)
    product_brand = Column(String)
    product_retail_price = Column(Float)
    product_department = Column(String)
    product_sku = Column(String)
    product_distribution_center_id = Column(Integer, ForeignKey("distribution_centers.id"))

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)
    gender = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
    returned_at = Column(TIMESTAMP)
    shipped_at = Column(TIMESTAMP)
    delivered_at = Column(TIMESTAMP)
    num_of_item = Column(Integer)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    inventory_item_id = Column(Integer, ForeignKey("inventory_items.id"))
    status = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
    shipped_at = Column(TIMESTAMP)
    delivered_at = Column(TIMESTAMP)
    returned_at = Column(TIMESTAMP)


class Conversation(Base):
    __tablename__ = "conversations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    conversation_id = Column(Integer, ForeignKey("conversations.id"))
    sender = Column(String)  # 'user' or 'ai'
    message = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
