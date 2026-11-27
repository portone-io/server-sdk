from __future__ import annotations
from typing import Any, Optional
from dataclasses import dataclass, field

@dataclass
class CreateB2bFileUploadUrlPayload:
    """파일 업로드 URL 생성 성공 응답
    """
    file_id: str
    """파일 아이디
    """
    url: str
    """파일 업로드 URL
    """


def _serialize_create_b2b_file_upload_url_payload(obj: CreateB2bFileUploadUrlPayload) -> Any:
    if isinstance(obj, dict):
        return obj
    entity = {}
    entity["fileId"] = obj.file_id
    entity["url"] = obj.url
    return entity


def _deserialize_create_b2b_file_upload_url_payload(obj: Any) -> CreateB2bFileUploadUrlPayload:
    if not isinstance(obj, dict):
        raise ValueError("Expected dict for obj")
    if "fileId" not in obj:
        raise KeyError("Missing required field 'fileId'")
    file_id = obj["fileId"]
    if not isinstance(file_id, str):
        raise ValueError("Expected str for file_id")
    if "url" not in obj:
        raise KeyError("Missing required field 'url'")
    url = obj["url"]
    if not isinstance(url, str):
        raise ValueError("Expected str for url")
    return CreateB2bFileUploadUrlPayload(file_id, url)
