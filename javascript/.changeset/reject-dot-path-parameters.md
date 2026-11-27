---
"@portone/server-sdk": patch
---

API 경로 매개변수 값이 정확히 `.` 또는 `..`이면 요청을 보내기 전에 `RangeError`를 발생시킵니다.
