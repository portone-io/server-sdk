package io.portone.sdk.server.identityverification

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 본인인증 통신사 */
@Serializable
public sealed interface IdentityVerificationOperator {
  public val value: String
  /** SKT */
  @SerialName("SKT")
  public data object Skt : IdentityVerificationOperator {
    override val value: String = "SKT"
  }
  /** KT */
  @SerialName("KT")
  public data object Kt : IdentityVerificationOperator {
    override val value: String = "KT"
  }
  /** LGU */
  @SerialName("LGU")
  public data object Lgu : IdentityVerificationOperator {
    override val value: String = "LGU"
  }
  /** SKT 알뜰폰 */
  @SerialName("SKT_MVNO")
  public data object SktMvno : IdentityVerificationOperator {
    override val value: String = "SKT_MVNO"
  }
  /** KT 알뜰폰 */
  @SerialName("KT_MVNO")
  public data object KtMvno : IdentityVerificationOperator {
    override val value: String = "KT_MVNO"
  }
  /** LGU 알뜰폰 */
  @SerialName("LGU_MVNO")
  public data object LguMvno : IdentityVerificationOperator {
    override val value: String = "LGU_MVNO"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : IdentityVerificationOperator
}
