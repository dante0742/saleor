import os

import pytest

from ....account.models import Address
from ...models import PluginConfiguration
from .. import AvataxConfiguration
from ..plugin import AvataxPlugin


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("Authorization", "Basic Og==")],
    }


@pytest.fixture
def plugin_configuration(db, channel_USD):
    default_username = os.environ.get("AVALARA_USERNAME", "test")
    default_password = os.environ.get("AVALARA_PASSWORD", "test")

    def set_configuration(
        username=default_username,
        password=default_password,
        sandbox=True,
        channel=None,
        active=True,
        from_street_address="Teczowa 7",
        from_city="Wroclaw",
        from_country="PL",
        from_country_area="",
        from_postal_code="53-601",
        shipping_tax_code="FR000000",
    ):
        channel = channel or channel_USD
        data = {
            "active": active,
            "name": AvataxPlugin.PLUGIN_NAME,
            "channel": channel,
            "configuration": [
                {"name": "Username or account", "value": username},
                {"name": "Password or license", "value": password},
                {"name": "Use sandbox", "value": sandbox},
                {"name": "Company name", "value": "DEFAULT"},
                {"name": "Autocommit", "value": False},
                {"name": "from_street_address", "value": from_street_address},
                {"name": "from_city", "value": from_city},
                {"name": "from_country", "value": from_country},
                {"name": "from_country_area", "value": from_country_area},
                {"name": "from_postal_code", "value": from_postal_code},
                {"name": "shipping_tax_code", "value": shipping_tax_code},
            ],
        }
        configuration = PluginConfiguration.objects.create(
            identifier=AvataxPlugin.PLUGIN_ID, **data
        )
        return configuration

    return set_configuration


@pytest.fixture
def avatax_config():
    return AvataxConfiguration(
        username_or_account=os.environ.get("AVALARA_USERNAME", "test"),
        password_or_license=os.environ.get("AVALARA_PASSWORD", "test"),
        use_sandbox=True,
        from_street_address="Tęczowa 7",
        from_city="WROCŁAW",
        from_country_area="",
        from_postal_code="53-601",
        from_country="PL",
    )


@pytest.fixture
def ship_to_pl_address(db):
    return Address.objects.create(
        first_name="Eleanor",
        last_name="Smith",
        street_address_1="Oławska 10",
        city="WROCŁAW",
        postal_code="53-105",
        country="PL",
        phone="+48713988155",
    )


@pytest.fixture
def avalara_response_for_checkout_with_items_and_shipping():
    return {
        "id": 0,
        "code": "8657e84b-c5ab-4c27-bcc2-c8d3ebbe771b",
        "companyId": 242975,
        "date": "2021-03-18",
        "paymentDate": "2021-03-18",
        "status": "Temporary",
        "type": "SalesOrder",
        "batchCode": "",
        "currencyCode": "USD",
        "exchangeRateCurrencyCode": "USD",
        "customerUsageType": "",
        "entityUseCode": "",
        "customerVendorCode": "0",
        "customerCode": "0",
        "exemptNo": "",
        "reconciled": False,
        "locationCode": "",
        "reportingLocationCode": "",
        "purchaseOrderNo": "",
        "referenceCode": "",
        "salespersonCode": "",
        "totalAmount": 12.2,
        "totalExempt": 0.0,
        "totalDiscount": 0.0,
        "totalTax": 2.8,
        "totalTaxable": 12.2,
        "totalTaxCalculated": 2.8,
        "adjustmentReason": "NotAdjusted",
        "locked": False,
        "version": 1,
        "exchangeRateEffectiveDate": "2021-03-18",
        "exchangeRate": 1.0,
        "email": "",
        "modifiedDate": "2021-03-18T13:23:21.7641305Z",
        "modifiedUserId": 283192,
        "taxDate": "2021-03-18T00:00:00Z",
        "lines": [
            {
                "id": 0,
                "transactionId": 0,
                "lineNumber": "1",
                "customerUsageType": "",
                "entityUseCode": "",
                "description": "Test product",
                "discountAmount": 0.0,
                "exemptAmount": 0.0,
                "exemptCertId": 0,
                "exemptNo": "",
                "isItemTaxable": True,
                "itemCode": "123",
                "lineAmount": 4.07,
                "quantity": 1.0,
                "ref1": "",
                "ref2": "",
                "reportingDate": "2021-03-18",
                "tax": 0.93,
                "taxableAmount": 4.07,
                "taxCalculated": 0.93,
                "taxCode": "O9999999",
                "taxCodeId": 5340,
                "taxDate": "2021-03-18",
                "taxIncluded": True,
                "details": [
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "PL",
                        "jurisName": "POLAND",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.23,
                        "tax": 0.93,
                        "taxableAmount": 4.07,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 0.93,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 4.07,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 0.93,
                        "reportingTaxCalculated": 0.93,
                        "liabilityType": "Seller",
                    },
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "EU",
                        "jurisName": "EUROPE",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.13,
                        "tax": 0.93,
                        "taxableAmount": 4.07,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 0.93,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 4.07,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 0.93,
                        "reportingTaxCalculated": 0.93,
                        "liabilityType": "Seller",
                    },
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "EU",
                        "jurisName": "EUROPE",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.13,
                        "tax": 0.0,
                        "taxableAmount": 0,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 0,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 0,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 0.0,
                        "reportingTaxCalculated": 0.0,
                        "liabilityType": "Seller",
                    },
                ],
                "nonPassthroughDetails": [],
                "hsCode": "",
                "costInsuranceFreight": 0.0,
                "vatCode": "PLS-230O--PL",
                "vatNumberTypeId": 0,
            },
            {
                "id": 0,
                "transactionId": 0,
                "lineNumber": "2",
                "customerUsageType": "",
                "entityUseCode": "",
                "discountAmount": 0.0,
                "exemptAmount": 0.0,
                "exemptCertId": 0,
                "exemptNo": "",
                "isItemTaxable": True,
                "itemCode": "Shipping",
                "lineAmount": 8.13,
                "quantity": 1.0,
                "ref1": "",
                "ref2": "",
                "reportingDate": "2021-03-18",
                "tax": 1.87,
                "taxableAmount": 8.13,
                "taxCalculated": 1.87,
                "taxCode": "FR020100",
                "taxCodeId": 4784,
                "taxDate": "2021-03-18",
                "taxIncluded": True,
                "details": [
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "PL",
                        "jurisName": "POLAND",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.23,
                        "tax": 1.87,
                        "taxableAmount": 8.13,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 1.87,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 8.13,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 1.87,
                        "reportingTaxCalculated": 1.87,
                        "liabilityType": "Seller",
                    },
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "EU",
                        "jurisName": "EUROPE",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.23,
                        "tax": 1.87,
                        "taxableAmount": 8.13,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 1.87,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 8.13,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 1.87,
                        "reportingTaxCalculated": 1.87,
                        "liabilityType": "Seller",
                    },
                ],
                "nonPassthroughDetails": [],
                "hsCode": "",
                "costInsuranceFreight": 0.0,
                "vatCode": "PLS-230F--PL",
                "vatNumberTypeId": 0,
            },
        ],
        "addresses": [
            {
                "id": 0,
                "transactionId": 0,
                "boundaryLevel": "Zip5",
                "line1": "Teczowa 7",
                "line2": "",
                "line3": "",
                "city": "WROCLAW",
                "region": "",
                "postalCode": "53-601",
                "country": "PL",
                "taxRegionId": 205102,
                "latitude": "",
                "longitude": "",
            }
        ],
        "summary": [
            {
                "country": "PL",
                "region": "PL",
                "jurisType": "Country",
                "jurisCode": "PL",
                "jurisName": "POLAND",
                "taxAuthorityType": 45,
                "stateAssignedNo": "",
                "taxType": "Output",
                "taxSubType": "O",
                "taxName": "Standard Rate",
                "rateType": "Standard",
                "taxable": 12.2,
                "rate": 0.23,
                "tax": 2.8,
                "taxCalculated": 2.8,
                "nonTaxable": 0.0,
                "exemption": 0.0,
            }
        ],
    }


@pytest.fixture
def avalara_response_with_line_details_and_zero_tax_with_returned_rate():
    return {
        "id": 0,
        "code": "8657e84b-c5ab-4c27-bcc2-c8d3ebbe771b",
        "companyId": 242975,
        "date": "2021-03-18",
        "paymentDate": "2021-03-18",
        "status": "Temporary",
        "type": "SalesOrder",
        "batchCode": "",
        "currencyCode": "USD",
        "exchangeRateCurrencyCode": "USD",
        "customerUsageType": "",
        "entityUseCode": "",
        "customerVendorCode": "0",
        "customerCode": "0",
        "exemptNo": "",
        "reconciled": False,
        "locationCode": "",
        "reportingLocationCode": "",
        "purchaseOrderNo": "",
        "referenceCode": "",
        "salespersonCode": "",
        "totalAmount": 12.2,
        "totalExempt": 0.0,
        "totalDiscount": 0.0,
        "totalTax": 2.8,
        "totalTaxable": 12.2,
        "totalTaxCalculated": 2.8,
        "adjustmentReason": "NotAdjusted",
        "locked": False,
        "version": 1,
        "exchangeRateEffectiveDate": "2021-03-18",
        "exchangeRate": 1.0,
        "email": "",
        "modifiedDate": "2021-03-18T13:23:21.7641305Z",
        "modifiedUserId": 283192,
        "taxDate": "2021-03-18T00:00:00Z",
        "lines": [
            {
                "id": 0,
                "transactionId": 0,
                "lineNumber": "1",
                "customerUsageType": "",
                "entityUseCode": "",
                "description": "Test product",
                "discountAmount": 0.0,
                "exemptAmount": 0.0,
                "exemptCertId": 0,
                "exemptNo": "",
                "isItemTaxable": True,
                "itemCode": "123",
                "lineAmount": 4.07,
                "quantity": 1.0,
                "ref1": "",
                "ref2": "",
                "reportingDate": "2021-03-18",
                "tax": 0.93,
                "taxableAmount": 4.07,
                "taxCalculated": 0.93,
                "taxCode": "O9999999",
                "taxCodeId": 5340,
                "taxDate": "2021-03-18",
                "taxIncluded": True,
                "details": [
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "PL",
                        "jurisName": "POLAND",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.23,
                        "tax": 0,
                        "taxableAmount": 0,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 00,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 0,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 0,
                        "reportingTaxCalculated": 0,
                        "liabilityType": "Seller",
                    },
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "EU",
                        "jurisName": "EUROPE",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.13,
                        "tax": 0,
                        "taxableAmount": 0,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 0,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 0,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 0.0,
                        "reportingTaxCalculated": 0.0,
                        "liabilityType": "Seller",
                    },
                ],
                "nonPassthroughDetails": [],
                "hsCode": "",
                "costInsuranceFreight": 0.0,
                "vatCode": "PLS-230O--PL",
                "vatNumberTypeId": 0,
            },
            {
                "id": 0,
                "transactionId": 0,
                "lineNumber": "2",
                "customerUsageType": "",
                "entityUseCode": "",
                "discountAmount": 0.0,
                "exemptAmount": 0.0,
                "exemptCertId": 0,
                "exemptNo": "",
                "isItemTaxable": True,
                "itemCode": "Shipping",
                "lineAmount": 8.13,
                "quantity": 1.0,
                "ref1": "",
                "ref2": "",
                "reportingDate": "2021-03-18",
                "tax": 1.87,
                "taxableAmount": 8.13,
                "taxCalculated": 1.87,
                "taxCode": "FR020100",
                "taxCodeId": 4784,
                "taxDate": "2021-03-18",
                "taxIncluded": True,
                "details": [
                    {
                        "id": 0,
                        "transactionLineId": 0,
                        "transactionId": 0,
                        "country": "PL",
                        "region": "PL",
                        "exemptAmount": 0.0,
                        "jurisCode": "PL",
                        "jurisName": "POLAND",
                        "stateAssignedNo": "",
                        "jurisType": "CNT",
                        "jurisdictionType": "Country",
                        "nonTaxableAmount": 0.0,
                        "rate": 0.23,
                        "tax": 0,
                        "taxableAmount": 0,
                        "taxType": "Output",
                        "taxSubTypeId": "O",
                        "taxName": "Standard Rate",
                        "taxAuthorityTypeId": 45,
                        "taxCalculated": 0,
                        "rateType": "Standard",
                        "rateTypeCode": "S",
                        "unitOfBasis": "PerCurrencyUnit",
                        "isNonPassThru": False,
                        "isFee": False,
                        "reportingTaxableUnits": 0,
                        "reportingNonTaxableUnits": 0.0,
                        "reportingExemptUnits": 0.0,
                        "reportingTax": 0,
                        "reportingTaxCalculated": 0,
                        "liabilityType": "Seller",
                    },
                ],
                "nonPassthroughDetails": [],
                "hsCode": "",
                "costInsuranceFreight": 0.0,
                "vatCode": "PLS-230F--PL",
                "vatNumberTypeId": 0,
            },
        ],
        "addresses": [
            {
                "id": 0,
                "transactionId": 0,
                "boundaryLevel": "Zip5",
                "line1": "Teczowa 7",
                "line2": "",
                "line3": "",
                "city": "WROCLAW",
                "region": "",
                "postalCode": "53-601",
                "country": "PL",
                "taxRegionId": 205102,
                "latitude": "",
                "longitude": "",
            }
        ],
        "summary": [
            {
                "country": "PL",
                "region": "PL",
                "jurisType": "Country",
                "jurisCode": "PL",
                "jurisName": "POLAND",
                "taxAuthorityType": 45,
                "stateAssignedNo": "",
                "taxType": "Output",
                "taxSubType": "O",
                "taxName": "Standard Rate",
                "rateType": "Standard",
                "taxable": 12.2,
                "rate": 0.23,
                "tax": 2.8,
                "taxCalculated": 2.8,
                "nonTaxable": 0.0,
                "exemption": 0.0,
            }
        ],
    }
