# -*- coding: utf-8 -*-

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem
from openfisca_core.model_api import Variable, MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key = "person",
    plural = "persons",
    label = u'Person',
    is_person = True,
    )

COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class dummy_variable(Variable):
    entity = Person
    value_type = float
    definition_period = MONTH


class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        super(CountryTaxBenefitSystem, self).__init__([Person])
        param_path = os.path.join(COUNTRY_DIR, 'parameters')
        self.load_parameters(param_path)
        self.add_variable(dummy_variable)
