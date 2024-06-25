from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class RegisterPaymentWizard(models.TransientModel):
    _name = 'register.payment'
    _description = 'Register Payment Wizard'

    sale_order_ids = fields.Many2many(
        'sale.order',  # Reference to sale.order model
        string='Sale Orders'
    )

    product_lines = fields.One2many(
        'register.payment.product.line',
        'wizard_id',
        string='Product Lines'
    )

    @api.model
    def default_get(self, fields_list):
        res = super(RegisterPaymentWizard, self).default_get(fields_list)

        # Get the sale order IDs from the context
        sale_order_ids = self.env.context.get('default_sale_order_ids', [])

        _logger.info("Received sale_order_ids from context: %s", sale_order_ids)

        if not sale_order_ids:
            _logger.warning("No sale_order_ids provided in context.")
            return res

        # Function to flatten the list
        def flatten_list(lst):
            for i in lst:
                if isinstance(i, list):
                    yield from flatten_list(i)
                else:
                    yield i

        # Use flatten_list to get a flat list of IDs
        flat_sale_order_ids = list(flatten_list(sale_order_ids))

        _logger.info("Flattened sale_order_ids: %s", flat_sale_order_ids)

        # Ensure all IDs are integers
        try:
            flat_sale_order_ids = [int(id) for id in flat_sale_order_ids]
        except ValueError as e:
            _logger.error("Error converting sale_order_ids to integers: %s", e)
            raise e

        _logger.info("Integer sale_order_ids: %s", flat_sale_order_ids)

        # Validate sale order IDs and check their existence
        valid_sale_order_ids = []
        for sale_order_id in flat_sale_order_ids:
            if self.env['sale.order'].browse(sale_order_id).exists():
                valid_sale_order_ids.append(sale_order_id)
                _logger.info("Sale order with ID %s is valid and accessible.", sale_order_id)
            else:
                _logger.warning("Sale order with ID %s not found or inaccessible.", sale_order_id)

        if not valid_sale_order_ids:
            _logger.error("No valid sale orders found to process.")
            return res

        # Prepare product lines from valid sale orders
        product_lines = []
        for order in self.env['sale.order'].browse(valid_sale_order_ids):
            for line in order.order_line:
                product_lines.append(Command.create({
                    'product_id': line.product_id.id,
                    'description': line.name,
                    'cost': line.price_unit,
                }))

        # Update the default values to return
        res.update({
            'sale_order_ids': [(6, 0, valid_sale_order_ids)],  # Correct way to set Many2many field
            'product_lines': product_lines
        })

        return res


class RegisterPaymentProductLine(models.TransientModel):
    _name = 'register.payment.product.line'
    _description = 'Register Payment Product Line'

    wizard_id = fields.Many2one('register.payment', string='Wizard')
    product_id = fields.Many2one('product.product', string='Product')
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')