from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


def solve(case):
    return "\n".join([str(sum([int(x) for x in n.split()])) if n != "/exit" else "Bye!" for n in case.split("\n") if n])


class CalcTest(StageTest):
    def generate(self) -> List[TestCase]:
        cases = ["17 9\n-2 5\n\n7\n/exit", # "26\n3\n7\nBye!"
                 "/exit", # "Bye!"
                 "100 200\n500\n300 400\n200\n\n\n-500\n/exit", # "300\n500\n700\n200\n-500\nBye!"
                 "801 199 -300 500\n10 20 30 40 50 -10 -20 -30 -40\n/exit"] # "1200\n50\nBye!"
        return [TestCase(stdin=case,
                         attach=solve(case))
                for case in cases]

    def check(self, reply: str, attach) -> CheckResult:
        return CheckResult(reply.strip() == attach.strip(), "")


if __name__ == '__main__':
    CalcTest("calculator.calculator").run_tests()
