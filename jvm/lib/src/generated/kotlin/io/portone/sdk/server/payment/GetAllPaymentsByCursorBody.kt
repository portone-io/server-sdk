package io.portone.sdk.server.payment

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 건 커서 기반 대용량 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetAllPaymentsByCursorBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
  /**
   * 결제 건 생성시점 범위 조건의 시작
   *
   * 값을 입력하지 않으면 end의 90일 전으로 설정됩니다.
   */
  val `from`: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 결제 건 생성시점 범위 조건의 끝
   *
   * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
   */
  val until: @Serializable(InstantSerializer::class) Instant? = null,
  /**
   * 커서
   *
   * 결제 건 리스트 중 어디서부터 읽어야 할지 가리키는 값입니다. 최초 요청일 경우 값을 입력하지 마시되, 두번째 요청 부터는 이전 요청 응답값의 cursor를 입력해주시면 됩니다.
   */
  val cursor: String? = null,
  /**
   * 페이지 크기
   *
   * 미입력 시 기본값은 10 이며 최대 1000까지 허용
   */
  val size: Int? = null,
)


