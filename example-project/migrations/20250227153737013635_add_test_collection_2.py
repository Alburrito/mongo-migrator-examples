"""
title: Add test collection 2
version: 20250227153737013635
last_version: 20250227153725838150
"""
from pymongo.database import Database

def upgrade(db: Database):
    db.create_collection("test_collection_2")

def downgrade(db: Database):
    db.drop_collection("test_collection_2")
