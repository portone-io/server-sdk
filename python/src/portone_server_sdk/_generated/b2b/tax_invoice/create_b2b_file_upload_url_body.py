from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreateB2bFileUploadUrlBody:
    """파일 업로드 URL 생성 요청 정보
    """
    file_name: str
    """파일 이름
    """


def _serialize_create_b2b_file_upload_url_body(obj: CreateB2bFileUploadUrlBody) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["fileName"] = obj.file_name
    return entity


def _deserialize_create_b2b_file_upload_url_body(obj: Any) -> CreateB2bFileUploadUrlBody:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "fileName" not in obj:
        raise KeyError("Missing required field 'fileName'")
    file_name = obj["fileName"]
    if not isinstance(file_name, str):
        raise ValueError("Expected str for file_name")
    return CreateB2bFileUploadUrlBody(file_name)
