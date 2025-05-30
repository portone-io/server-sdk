from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class B2bBusinessInfo:
    """사업자등록 정보
    """
    brn: str
    """사업자등록번호
    """
    name: str
    """상호
    """
    ceo_name: str
    """대표자명
    """
    zip_code: str
    """우편번호
    """
    address: str
    """주소
    """
    business_entity_type: str
    """사업자 유형
    """
    business_status: str
    """사업 상태
    """
    taxation_type: str
    """과세 유형
    """
    opening_date: str
    """개업일
    """
    business_type: str
    """업태
    """
    business_class: str
    """종목
    """
    business_category_code: str
    """업종코드
    """
    simplified_taxation_type_date: Optional[str] = field(default=None)
    """간이과세-일반과세 전환일
    """
    closing_date: Optional[str] = field(default=None)
    """폐업일
    """
    corp_reg_no: Optional[str] = field(default=None)
    """법인등록번호
    """
    phone_number: Optional[str] = field(default=None)
    """전화번호
    """
    tax_office_code: Optional[str] = field(default=None)
    """관할세무서코드
    """
    tax_office_name: Optional[str] = field(default=None)
    """관할세무서명
    """


def _serialize_b2b_business_info(obj: B2bBusinessInfo) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["brn"] = obj.brn
    entity["name"] = obj.name
    entity["ceoName"] = obj.ceo_name
    entity["zipCode"] = obj.zip_code
    entity["address"] = obj.address
    entity["businessEntityType"] = obj.business_entity_type
    entity["businessStatus"] = obj.business_status
    entity["taxationType"] = obj.taxation_type
    entity["openingDate"] = obj.opening_date
    entity["businessType"] = obj.business_type
    entity["businessClass"] = obj.business_class
    entity["businessCategoryCode"] = obj.business_category_code
    if obj.simplified_taxation_type_date is not None:
        entity["simplifiedTaxationTypeDate"] = obj.simplified_taxation_type_date
    if obj.closing_date is not None:
        entity["closingDate"] = obj.closing_date
    if obj.corp_reg_no is not None:
        entity["corpRegNo"] = obj.corp_reg_no
    if obj.phone_number is not None:
        entity["phoneNumber"] = obj.phone_number
    if obj.tax_office_code is not None:
        entity["taxOfficeCode"] = obj.tax_office_code
    if obj.tax_office_name is not None:
        entity["taxOfficeName"] = obj.tax_office_name
    return entity


def _deserialize_b2b_business_info(obj: Any) -> B2bBusinessInfo:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "brn" not in obj:
        raise KeyError(f"'brn' is not in {obj}")
    brn = obj["brn"]
    if not isinstance(brn, str):
        raise ValueError(f"{repr(brn)} is not str")
    if "name" not in obj:
        raise KeyError(f"'name' is not in {obj}")
    name = obj["name"]
    if not isinstance(name, str):
        raise ValueError(f"{repr(name)} is not str")
    if "ceoName" not in obj:
        raise KeyError(f"'ceoName' is not in {obj}")
    ceo_name = obj["ceoName"]
    if not isinstance(ceo_name, str):
        raise ValueError(f"{repr(ceo_name)} is not str")
    if "zipCode" not in obj:
        raise KeyError(f"'zipCode' is not in {obj}")
    zip_code = obj["zipCode"]
    if not isinstance(zip_code, str):
        raise ValueError(f"{repr(zip_code)} is not str")
    if "address" not in obj:
        raise KeyError(f"'address' is not in {obj}")
    address = obj["address"]
    if not isinstance(address, str):
        raise ValueError(f"{repr(address)} is not str")
    if "businessEntityType" not in obj:
        raise KeyError(f"'businessEntityType' is not in {obj}")
    business_entity_type = obj["businessEntityType"]
    if not isinstance(business_entity_type, str):
        raise ValueError(f"{repr(business_entity_type)} is not str")
    if "businessStatus" not in obj:
        raise KeyError(f"'businessStatus' is not in {obj}")
    business_status = obj["businessStatus"]
    if not isinstance(business_status, str):
        raise ValueError(f"{repr(business_status)} is not str")
    if "taxationType" not in obj:
        raise KeyError(f"'taxationType' is not in {obj}")
    taxation_type = obj["taxationType"]
    if not isinstance(taxation_type, str):
        raise ValueError(f"{repr(taxation_type)} is not str")
    if "openingDate" not in obj:
        raise KeyError(f"'openingDate' is not in {obj}")
    opening_date = obj["openingDate"]
    if not isinstance(opening_date, str):
        raise ValueError(f"{repr(opening_date)} is not str")
    if "businessType" not in obj:
        raise KeyError(f"'businessType' is not in {obj}")
    business_type = obj["businessType"]
    if not isinstance(business_type, str):
        raise ValueError(f"{repr(business_type)} is not str")
    if "businessClass" not in obj:
        raise KeyError(f"'businessClass' is not in {obj}")
    business_class = obj["businessClass"]
    if not isinstance(business_class, str):
        raise ValueError(f"{repr(business_class)} is not str")
    if "businessCategoryCode" not in obj:
        raise KeyError(f"'businessCategoryCode' is not in {obj}")
    business_category_code = obj["businessCategoryCode"]
    if not isinstance(business_category_code, str):
        raise ValueError(f"{repr(business_category_code)} is not str")
    if "simplifiedTaxationTypeDate" in obj:
        simplified_taxation_type_date = obj["simplifiedTaxationTypeDate"]
        if not isinstance(simplified_taxation_type_date, str):
            raise ValueError(f"{repr(simplified_taxation_type_date)} is not str")
    else:
        simplified_taxation_type_date = None
    if "closingDate" in obj:
        closing_date = obj["closingDate"]
        if not isinstance(closing_date, str):
            raise ValueError(f"{repr(closing_date)} is not str")
    else:
        closing_date = None
    if "corpRegNo" in obj:
        corp_reg_no = obj["corpRegNo"]
        if not isinstance(corp_reg_no, str):
            raise ValueError(f"{repr(corp_reg_no)} is not str")
    else:
        corp_reg_no = None
    if "phoneNumber" in obj:
        phone_number = obj["phoneNumber"]
        if not isinstance(phone_number, str):
            raise ValueError(f"{repr(phone_number)} is not str")
    else:
        phone_number = None
    if "taxOfficeCode" in obj:
        tax_office_code = obj["taxOfficeCode"]
        if not isinstance(tax_office_code, str):
            raise ValueError(f"{repr(tax_office_code)} is not str")
    else:
        tax_office_code = None
    if "taxOfficeName" in obj:
        tax_office_name = obj["taxOfficeName"]
        if not isinstance(tax_office_name, str):
            raise ValueError(f"{repr(tax_office_name)} is not str")
    else:
        tax_office_name = None
    return B2bBusinessInfo(brn, name, ceo_name, zip_code, address, business_entity_type, business_status, taxation_type, opening_date, business_type, business_class, business_category_code, simplified_taxation_type_date, closing_date, corp_reg_no, phone_number, tax_office_code, tax_office_name)
