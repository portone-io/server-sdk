import { Definition, Property } from "./definition.ts"

export const webhookCommonProperties = [
  {
    name: "timestamp",
    description:
      "해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.",
    required: true,
    overrides: false,
    type: "string",
    format: "date-time",
  },
] satisfies Property[]

export const webhook = {
  name: "Webhook",
  description: "2024-04-25 버전의 웹훅 형식",
  type: "object",
  properties: [],
  extends: [],
  interface: {
    discriminant: "type",
    coproduct: ["WebhookTransaction", "WebhookBillingKey"],
    open: true,
  },
} satisfies Definition
