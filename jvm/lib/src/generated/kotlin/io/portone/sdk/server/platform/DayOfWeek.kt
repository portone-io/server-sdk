package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요일 */
@Serializable
public sealed class DayOfWeek {
  @SerialName("SUN")
  public data object Sun : DayOfWeek()
  @SerialName("MON")
  public data object Mon : DayOfWeek()
  @SerialName("TUE")
  public data object Tue : DayOfWeek()
  @SerialName("WED")
  public data object Wed : DayOfWeek()
  @SerialName("THU")
  public data object Thu : DayOfWeek()
  @SerialName("FRI")
  public data object Fri : DayOfWeek()
  @SerialName("SAT")
  public data object Sat : DayOfWeek()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : DayOfWeek()
}
