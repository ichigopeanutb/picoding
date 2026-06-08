#!/usr/bin/env bash
set -u

start_seconds=$(python3 - <<'PY'
import time
print(time.time())
PY
)

status="pass"
score="0"
tests_passed="0"
tests_failed="0"

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is required but was not found."
  status="fail"
fi

if [ "$status" = "pass" ] && [ -d tests ]; then
  if command -v python3 >/dev/null 2>&1; then
    pytest_output=$(python3 -m pytest tests 2>&1)
    pytest_status=$?
    echo "$pytest_output"
    if [ "$pytest_status" -ne 0 ]; then
      status="fail"
    fi
    if echo "$pytest_output" | grep -Eq '[0-9]+ passed'; then
      tests_passed=$(echo "$pytest_output" | grep -Eo '[0-9]+ passed' | tail -1 | awk '{print $1}')
    fi
    if echo "$pytest_output" | grep -Eq '[0-9]+ failed'; then
      tests_failed=$(echo "$pytest_output" | grep -Eo '[0-9]+ failed' | tail -1 | awk '{print $1}')
    fi
  fi
fi

if [ "$status" = "pass" ] && [ -f eval/run_eval.py ]; then
  eval_output=$(python3 eval/run_eval.py 2>&1)
  eval_status=$?
  echo "$eval_output"
  if [ "$eval_status" -ne 0 ]; then
    status="fail"
  fi
  eval_score=$(echo "$eval_output" | awk -F= '/^EVAL_SCORE=/{print $2}' | tail -1)
  if [ -n "$eval_score" ]; then
    score="$eval_score"
  fi
fi

runtime_seconds=$(python3 - "$start_seconds" <<'PY'
import sys
import time
start = float(sys.argv[1])
print(f"{time.time() - start:.3f}")
PY
)

echo "EVAL_STATUS=$status"
echo "EVAL_SCORE=$score"
echo "EVAL_TESTS_PASSED=$tests_passed"
echo "EVAL_TESTS_FAILED=$tests_failed"
echo "EVAL_RUNTIME_SECONDS=$runtime_seconds"

if [ "$status" = "pass" ]; then
  exit 0
fi

exit 1
