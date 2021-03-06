# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api, _
from openerp.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)


class product_uom(models.Model):
    _inherit = "product.uom"

    @api.multi
    def action_get_pyafipws_product_uoms(self):
        self.get_pyafipws_product_uoms()

    @api.multi
    def get_pyafipws_product_uoms(self, afip_ws='wsfex', company=False):
        self.ensure_one()
        # if not company, then we search one that uses argentinian localization
        if not company:
            company = self.env['res.company'].search(
                [('use_argentinian_localization', '=', True)],
                limit=1)
        if not company:
            raise Warning(_('No company found using argentinian localization'))
        ws = company.get_connection(afip_ws).connect()

        if afip_ws == "wsfex":
            res = ws.GetParamUMed(sep=' ')
        else:
            raise Warning(_('AFIP WS %s not implemented') % (
                afip_ws))
        title = _('Unit of mesures:\n%s' % '\n'.join(res))
        msg = " - ".join([
            ws.Excepcion,
            ws.ErrMsg,
            ws.Obs])
        _logger.info('%s\n%s' % (title, msg))
        raise Warning(title + msg)
