from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit= "product.template"
    
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        res = super(ProductTemplate, self).copy(default=default)
        res.write({
            'default_code': False,
            'barcode': self.default_code,
            
        })
        
        return res