#!/bin/bash

# 사용법: ./remove_consistent_copy_visibility.sh path/to/your/kotlin/files

TARGET_DIR="$1"

if [ -z "$TARGET_DIR" ]; then
  echo "❌ 대상 디렉토리를 인자로 입력해주세요."
  echo "사용법: ./remove_consistent_copy_visibility.sh path/to/your/kotlin/files"
  exit 1
fi

echo "🚀 @ConsistentCopyVisibility 및 관련 import 제거 중..."
find "$TARGET_DIR" -type f -name "*.kt" | while read -r file; do
  # @ConsistentCopyVisibility 애노테이션 제거
  sed -i '' '/@ConsistentCopyVisibility/d' "$file"

  # import 문 제거 (전체 경로, 짧은 경로 모두 포함 가능)
  sed -i '' '/import .*ConsistentCopyVisibility/d' "$file"

  echo "🧹 cleaned: $file"
done

echo "✅ 모두 완료!"