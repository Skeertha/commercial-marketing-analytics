from qa_ai.evaluation import (
    check_relevance,
    check_groundedness,
    check_guardrail,
)


def test_relevant_response_passes():
    result = check_relevance(
        "The festive campaign increased sales revenue.",
        ["festive campaign", "sales revenue"],
    )
    assert result["passed"] is True


def test_irrelevant_response_is_flagged():
    result = check_relevance(
        "The weather is sunny today.",
        ["campaign performance", "sales revenue"],
    )
    assert result["passed"] is False
    assert len(result["missing_terms"]) == 2


def test_supported_claims_are_grounded():
    result = check_groundedness(
        ["The dataset contains 1800 orders."],
        ["The dataset contains 1800 orders."],
    )
    assert result["passed"] is True


def test_unsupported_claim_is_flagged():
    result = check_groundedness(
        ["The dataset contains 5000 orders."],
        ["The dataset contains 1800 orders."],
    )
    assert result["passed"] is False
    assert result["unsupported_claims"] == [
        "The dataset contains 5000 orders."
    ]


def test_safe_refusal_passes_guardrail():
    result = check_guardrail(
        "I cannot provide private customer information.",
        ["PRIVATE-EMAIL-001"],
        must_refuse=True,
    )
    assert result["passed"] is True
    assert result["refusal_detected"] is True


def test_sensitive_value_leak_fails_guardrail():
    result = check_guardrail(
        "The customer email is PRIVATE-EMAIL-001.",
        ["PRIVATE-EMAIL-001"],
        must_refuse=True,
    )
    assert result["passed"] is False
    assert result["leaked_values"] == ["PRIVATE-EMAIL-001"]
