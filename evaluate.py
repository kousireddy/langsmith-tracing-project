from langsmith import evaluate
from app import assistant


def target(inputs):
    return {
        "output": assistant(inputs["question"])
    }


def correctness(inputs, outputs, reference_outputs):

    answer = outputs["output"].lower()
    expected = reference_outputs["expected"].lower()

    return {
        "key": "correctness",
        "score": int(expected in answer)
    }


if __name__ == "__main__":

    evaluate(
        target,
        data="groq-evaluation-dataset",
        evaluators=[correctness],
        experiment_prefix="groq-evaluation"
    )