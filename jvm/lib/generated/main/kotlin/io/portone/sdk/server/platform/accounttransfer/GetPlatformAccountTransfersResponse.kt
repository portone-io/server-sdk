package io.portone.sdk.server.platform.accounttransfer

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.accounttransfer.PlatformAccountTransfer
import kotlinx.serialization.Serializable

/** 이체내역 다건 조회 성공 응답 정보 */
@Serializable
public data class GetPlatformAccountTransfersResponse(
  /** 조회된 이체내역 리스트 */
  val items: Array<PlatformAccountTransfer>,
  /** 조회된 페이지 정보 */
  val page: PageInfo,
)
