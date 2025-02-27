"""
title: Add test collection 1
version: 20250227153725838150
last_version: None
"""
from pymongo.database import Database

def upgrade(db: Database):
    db.create_collection("test_collection_1")

def downgrade(db: Database):
    # Implement this method in the generated migration file
    db.drop_collection("test_collection_1")
