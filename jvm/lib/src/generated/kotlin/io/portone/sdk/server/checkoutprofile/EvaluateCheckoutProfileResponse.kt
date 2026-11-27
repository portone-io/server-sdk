package io.portone.sdk.server.checkoutprofile

import io.portone.sdk.server.checkoutprofile.EvaluatedCheckoutMethod
import kotlinx.serialization.Serializable

/** 체크아웃 프로필 평가 성공 응답 */
@Serializable
public data class EvaluateCheckoutProfileResponse(
  /** 사용 가능한 결제수단 목록 */
  val methods: List<EvaluatedCheckoutMethod>? = null,
)


