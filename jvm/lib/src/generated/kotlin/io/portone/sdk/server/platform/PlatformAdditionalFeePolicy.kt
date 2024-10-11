package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformFee
import io.portone.sdk.server.platform.PlatformPayer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 추가 수수료 정책
 *
 * 추가 수수료 정책는 고객사의 주문건에 대한 중개수수료에 별도로 추가로 부여되는 수수료입니다. 대표적인 사용 예시로 풀필먼트 수수료, 로켓배송 수수료, 마케팅 채널 수수료등이 있습니다.
 */
@Serializable
public data class PlatformAdditionalFeePolicy(
  /** 추가 수수료 정책 고유 아이디 */
  val id: String,
  val graphqlId: String,
  /** 추가 수수료 정책 이름 */
  val name: String,
  /** 책정 수수료 */
  val fee: PlatformFee,
  /** 부가세를 부담할 주체 */
  val vatPayer: PlatformPayer,
  /** 보관 여부 */
  val isArchived: Boolean,
  /** 변경 적용 시점 */
  val appliedAt: Instant,
  /** 해당 추가 수수료 정책에 대한 메모 */
  val memo: String? = null,
)
