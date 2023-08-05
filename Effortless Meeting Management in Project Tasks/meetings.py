from odoo import models, fields, api, _

class ProjectMeetings(models.Model):
    
    _name = 'project.meetings'
    _description = 'Project Meetings'
    
    name = fields.Char(string='Meeting Name')
    task_id = fields.Many2one('project.task', string='Task', required= True)
    project_id = fields.Many2one('project.project', string='Project', related='task_id.project_id')
    scheduled_meeting_date = fields.Date(string='Scheduled Meeting Date')
    actual_meeting_date = fields.Date(string='Actual Meeting Date')
    completed = fields.Boolean(string='Completed')
    active = fields.Boolean(default=True)
    
    def write(self, vals):
        res = super(ProjectMeetings, self).write(vals)
        if 'completed' in vals and vals['completed']:
            for record in self:

                completion_vals = {
                    'name': record.name,
                    'task_id': record.task_id.id,
                    'scheduled_meeting_date': record.scheduled_meeting_date,
                    'actual_meeting_date': record.actual_meeting_date,
                    'partner_id': record.task_id.partner_id.id,
                }
                self.env['task_completion_record'].create(completion_vals)
                record.active = False  
        return res
    
    
class ProjectMeetingsCompleted(models.Model):
    
    _name = 'task_completion_record'
    _description = 'Completed Meetings'
    
    name = fields.Char(string='Meeting Name')
    task_id = fields.Many2one('project.task', string='Task')
    scheduled_meeting_date = fields.Date(string='Scheduled Meeting Date')
    actual_meeting_date = fields.Date(string='Actual Meeting Date')
    partner_id = fields.Many2one('res.partner', string='Parter')
