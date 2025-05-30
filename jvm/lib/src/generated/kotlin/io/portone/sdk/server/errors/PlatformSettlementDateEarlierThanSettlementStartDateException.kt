package io.portone.sdk.server.errors

import io.portone.sdk.server.errors.PlatformSettlementDateEarlierThanSettlementStartDateError
import java.lang.Exception
import kotlin.String


/** 정산일이 정산 시작일보다 빠른 경우 */
public class PlatformSettlementDateEarlierThanSettlementStartDateException internal constructor(
  cause: PlatformSettlementDateEarlierThanSettlementStartDateError
) : PortOneException(cause.message), CreatePlatformOrderCancelTransferException, CreatePlatformOrderTransferException {
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  public val settlementStartDate: String = cause.settlementStartDate
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  public val settlementDate: String = cause.settlementDate
}
