#_*_coding:utf-8_*_
__author__ = 'kom'

import os
import web
from jinja2 import Environment,FileSystemLoader
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

def render(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})

    jinja_env = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'template')),
        extensions=extensions,
    )
    jinja_env.globals.update(globals)

    #jinja_env.update_template_context(context)
    return jinja_env.get_template(template_name).render(context)


engine = create_engine('mysql+mysqldb://hostname/dbname?charset=utf8', encoding='utf8' ,echo=True)

def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(autoflush=True, bind=engine))
    try:
        return handler()
    except web.HTTPError:
        web.ctx.orm.commit()
        raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()
