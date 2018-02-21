# This file is part stock_origin_sale_sale module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
try:
    from trytond.modules.stock_origin_sale.tests.test_stock_origin_sale import suite
except ImportError:
    from .test_stock_origin_sale import suite

__all__ = ['suite']
