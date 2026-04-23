package io.portone.sdk.server.b2b.counterparty

import io.portone.sdk.server.b2b.counterparty.B2bCounterpartyContactInput
import kotlin.String
import kotlinx.serialization.Serializable

/** 거래처 입력 정보 */
@Serializable
public data class B2bCounterpartyInput(
  /**
   * 사업자등록번호
   *
   * `-` 없이 숫자로만 구성됩니다.
   */
  val brn: String,
  /** 거래처명 */
  val name: String? = null,
  /** 대표자 성명 */
  val representativeName: String? = null,
  /** 주소 */
  val address: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
  /** 담당자 정보 */
  val contact: B2bCounterpartyContactInput? = null,
  /**
   * 추가 담당자 목록
   *
   * 최대 5명까지 등록할 수 있습니다.
   */
  val additionalContacts: List<B2bCounterpartyContactInput>? = null,
  /** 메모 */
  val memo: String? = null,
)


