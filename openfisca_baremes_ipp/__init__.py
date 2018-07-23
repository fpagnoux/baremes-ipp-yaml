# -*- coding: utf-8 -*-

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem
from openfisca_core.entities import build_entity

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'Person',
    is_person = True,
    )

COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        super(CountryTaxBenefitSystem, self).__init__([Person])
        param_path = os.path.join(COUNTRY_DIR, 'parameters')
        self.load_parameters(param_path)
