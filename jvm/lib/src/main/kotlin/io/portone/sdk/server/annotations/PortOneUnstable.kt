package io.portone.sdk.server.annotations

@RequiresOptIn(
    level = RequiresOptIn.Level.ERROR,
    message = "실험적 API입니다. 하위호환성 정책과 무관하게 변경 및 지원 종료될 수 있으니 이용에 유의하세요.",
)
@Retention(AnnotationRetention.BINARY)
@Target(AnnotationTarget.FUNCTION)
public annotation class PortOneUnstable
