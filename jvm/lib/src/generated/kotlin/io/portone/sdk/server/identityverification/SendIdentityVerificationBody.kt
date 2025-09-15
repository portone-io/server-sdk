package io.portone.sdk.server.identityverification

import io.portone.sdk.server.identityverification.IdentityVerificationMethod
import io.portone.sdk.server.identityverification.IdentityVerificationOperator
import io.portone.sdk.server.identityverification.SendIdentityVerificationBodyCustomer
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonObject

/** 본인인증 요청을 위한 입력 정보 */
@Serializable
internal data class SendIdentityVerificationBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
  /** 채널 키 */
  val channelKey: String,
  /** 고객 정보 */
  val customer: SendIdentityVerificationBodyCustomer,
  /** 사용자 지정 데이터 */
  val customData: String? = null,
  val bypass: JsonObject? = null,
  /** 통신사 */
  val `operator`: IdentityVerificationOperator,
  /** 본인인증 방식 */
  val method: IdentityVerificationMethod,
)


