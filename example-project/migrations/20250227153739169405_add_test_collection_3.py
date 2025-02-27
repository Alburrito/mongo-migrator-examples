"""
title: Add test collection 3
version: 20250227153739169405
last_version: 20250227153737013635
"""
from pymongo.database import Database

def upgrade(db: Database):
    db.create_collection("test_collection_3")

def downgrade(db: Database):
    db.drop_collection("test_collection_3")
