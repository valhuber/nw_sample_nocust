from functools import wraps
import logging
from flask_jwt_extended import get_jwt, jwt_required, verify_jwt_in_request
from config.config import Config, Args
from security.system.authorization import Security
import api.system.api_utils as api_utils
from typing import List
import safrs
import sqlalchemy
from flask import request, jsonify
from safrs import jsonapi_rpc, SAFRSAPI
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import object_mapper
from sqlalchemy import extract, func
from database import models
from flask_cors import cross_origin
from logic_bank.rule_bank.rule_bank import RuleBank
import integration.system.RowDictMapper as row_dict_mapper

# Customize this file to add endpoints/services, using SQLAlchemy as required
#     Separate from expose_api_models.py, to simplify merge if project rebuilt
# Called by api_logic_server_run.py

app_logger = logging.getLogger("api_logic_server_app")

# called by api_logic_server_run.py, to customize api (new end points, services).
# separate from expose_api_models.py, to simplify merge if project recreated

def add_service(app, api, project_dir, swagger_host: str, PORT: str, method_decorators = []):
    pass

    api.expose_object(GraphicsServices)  # Swagger-visible services
    api.expose_object(GetTest)  # Swagger-visible services


"""
Illustrates #als: apis for graphics

* Custom service - visible in swagger
"""
class GraphicsServices(safrs.JABase):
    pass

    @classmethod
    @jsonapi_rpc(http_methods=['POST', 'GET'])
    def sales_by_region_query(self, *args, **kwargs):
        """        
        Illustrates:
        * Complex query with multiple joins, for graphics
        * That Thomas is a duck.
        
        """
        from database.models import Order, Region, OrderDetail
        db = safrs.DB
        session = db.session    # sqlalchemy.orm.scoping.scoped_session
        # Security.set_user_sa()  # an endpoint that requires no auth header (see also @bypass_security)

        # SQLAlchemy query
        query = sales_by_region = (
    session.query(
        Region.RegionDescription,
        func.sum(OrderDetail.Quantity * OrderDetail.UnitPrice * (1 - OrderDetail.Discount)).label("TotalSales")
    )
    .join(Order, Order.ShipRegion == Region.RegionDescription)
    .join(OrderDetail, OrderDetail.OrderId == Order.Id)
    .filter(Order.ShippedDate.isnot(None))  # Consider only shipped orders
    .group_by(Region.RegionDescription)
    .order_by(func.sum(OrderDetail.Quantity * OrderDetail.UnitPrice * (1 - OrderDetail.Discount)).desc())
) 
        # Execute query and fetch results
        results = query.all()
        
        return jsonify( { "result": results } )


class GetTest(safrs.JABase):  # type: ignore

    @classmethod
    @jsonapi_rpc(http_methods=['POST','GET'])
    def test(self, *args, **kwargs):
        return {"result":1}