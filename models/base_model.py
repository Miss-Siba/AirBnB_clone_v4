#!/usr/bin/python3
"""
Contains class BaseModel
"""


from datetime import datetime
import models
import json
import os
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

storage_t = os.environ.get('HBNB_TYPE_STORAGE')

if storage_t == "db":
    Base = declarative_base()
else:
    class Base:
        pass

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __is_serializable(self, obj_v):
        try:
            obj_to_str = json.dumps(obj_v)
            return isinstance(obj_to_str, str)
        except:
            return False

    def bm_update(self, name, value):
        setattr(self, name, value)
        if storage_t != 'db':
            self.save()

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        if storage_t != 'db':
            self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        bm_dict = {}
        for key, value in self.__dict__.items():
            if self.__is_serializable(value):
                bm_dict[key] = value
            else:
                bm_dict[key] = str(value)
        bm_dict['__class__'] = type(self).__name__
        if '_sa_instance_state' in bm_dict:
            bm_dict.pop('_sa_instance_state')
        if storage_t == "db" and 'password' in bm_dict:
            bm_dict.pop('password')
        return bm_dict

    def delete(self):
        models.storage.delete(self)

