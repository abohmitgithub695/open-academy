import odoorpc

odoo = odoorpc.ODOO('localhost', port=8069)

print(odoo.db.list())

odoo.login('my_database', 'admin', 'admin')

order_ids=odoo.env['event.event'].search([('id','=',4)])
print(order_ids)

order_ids=odoo.env['event.event'].browse(order_ids)

print(order_ids)

# for record in order_ids:
#     record.write({'organization':31})
# Current user
# user = odoo.env.user
# print(user.name)            # name of the user connected
# print(user.company_id.name) # the name of its company
# Simple 'raw' query
# user_data = odoo.execute('res.users', 'read', [user.id])
# print(user_data)

if 'event.event' in odoo.env:
    crm_leads = odoo.env['event.event'].search([('id','=',4)])
    for lead in crm_leads:
        print(".................",lead)
        lead_rec=odoo.env['event.event'].browse(lead)
        print(".................",lead_rec.name)
        lead_rec.name="abdulrahman"

#         products = [line.product_id.name for line in order.order_line]
#         print(products)

# Update data through a record
# user.name = "Brian Jones"