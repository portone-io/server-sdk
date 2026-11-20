from __future__ import annotations
from dataclasses import field
from typing import Any, Optional
from dataclasses import dataclass, field
from ..checkout_profile.evaluated_checkout_method import EvaluatedCheckoutMethod, _deserialize_evaluated_checkout_method, _serialize_evaluated_checkout_method

@dataclass
class EvaluateCheckoutProfileResponse:
    """체크아웃 프로필 평가 성공 응답
    """
    methods: Optional[list[EvaluatedCheckoutMethod]] = field(default=None)
    """사용 가능한 결제수단 목록
    """


def _serialize_evaluate_checkout_profile_response(obj: EvaluateCheckoutProfileResponse) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    if obj.methods is not None:
        entity["methods"] = list(map(_serialize_evaluated_checkout_method, obj.methods))
    return entity


def _deserialize_evaluate_checkout_profile_response(obj: Any) -> EvaluateCheckoutProfileResponse:
    if not isinstance(obj, dict):
        raise ValueError(f"{repr(obj)} is not dict")
    if "methods" in obj:
        methods = obj["methods"]
        if not isinstance(methods, list):
            raise ValueError(f"{repr(methods)} is not list")
        for i, item in enumerate(methods):
            item = _deserialize_evaluated_checkout_method(item)
            methods[i] = item
    else:
        methods = None
    return EvaluateCheckoutProfileResponse(methods)
