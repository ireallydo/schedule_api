from sqlalchemy.orm import Session

from db.models import *
from db.dto import *
from db.dao import module_dao
from db.enums import WeekdaysEnum, LessonsEnum, ClassTypesEnum, SemestersEnum


def fill(db, input_data):
    return module_dao.create(db, input_data)

def get_all(db, skip, limit):
    return module_dao.get_all(db, skip, limit)

def get_by_name(db, module_name, skip, limit):
    return module_dao.get_all_by_name(db, module_name, skip, limit)

def patch(db, search_data, patch_data):
    module = module_dao.get_by(db, search_data)
    module_dao.patch(db, patch_data, module.id)
    return module_dao.get_by_id(db, module.id)

def delete(db, input_data):
    module = module_dao.get_by(db, input_data)
    return module_dao.delete(db, module.id)
