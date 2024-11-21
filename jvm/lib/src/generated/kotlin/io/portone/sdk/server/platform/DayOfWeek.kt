package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 요일 */
@Serializable
public sealed interface DayOfWeek {
  public val value: String
  @SerialName("SUN")
  public data object Sun : DayOfWeek {
    override val value: String = "SUN"
  }
  @SerialName("MON")
  public data object Mon : DayOfWeek {
    override val value: String = "MON"
  }
  @SerialName("TUE")
  public data object Tue : DayOfWeek {
    override val value: String = "TUE"
  }
  @SerialName("WED")
  public data object Wed : DayOfWeek {
    override val value: String = "WED"
  }
  @SerialName("THU")
  public data object Thu : DayOfWeek {
    override val value: String = "THU"
  }
  @SerialName("FRI")
  public data object Fri : DayOfWeek {
    override val value: String = "FRI"
  }
  @SerialName("SAT")
  public data object Sat : DayOfWeek {
    override val value: String = "SAT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : DayOfWeek
}
