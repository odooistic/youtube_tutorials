from odoo import models, fields, api, _

class ProductTemplate(models.Model):
    _inherit= "product.template"
    

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        res = super(ProductTemplate, self).copy(default=default)
        res.write({
            'default_code': self.default_code
        })

        for seller in self.seller_ids:
            seller.copy({
                'product_tmpl_id': res.id
            })
        return res
    

class ProjectTask(models.Model):
    _inherit= "project.task"
    
    color = fields.Integer(compute='_compute_color', store=True)
    change_color = fields.Boolean(string='Change Color')
    project_meetings_ids = fields.One2many('project.meetings', 'task_id', string='Meetings')
    completed_meetings_ids = fields.One2many('task_completion_record', 'task_id', string="Completed Meetings")

    
    @api.depends('change_color')
    def _compute_color(self):
        for record in self:
            if record.change_color:
                record.color = 9
            else:
                record.color = 0
                
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # to_fix = fields.Boolean(string='Fix')
    # name = fields.Char(string='Name', compute='_get_task_name', store=True)
    
    # @api.depends('to_fix', 'name')
    # def _get_task_name(self):
    #     for record in self:
    #         if record.to_fix:
    #             record.name = ('[FIX]' + record.name)
    #         else:
    #             record.name = record.name.replace('[FIX]', '')
    
    
                
    
    
    
  
        