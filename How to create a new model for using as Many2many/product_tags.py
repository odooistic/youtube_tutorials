from odoo import models, fields, api, _

class ProductTagsExtension(models.Model):
    _name= "product.tags"
    
    name = fields.Char(string='Tag Name')
    active = fields.Boolean('Active', default=True)
    color = fields.Integer(string='Color')