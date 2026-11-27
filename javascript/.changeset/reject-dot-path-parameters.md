---
"@portone/server-sdk": patch
---

API 경로 매개변수로 `.`, `..` 또는 이를 퍼센트 인코딩한 값이 전달되면 요청을 보내기 전에 `RangeError`를 발생시킵니다.
