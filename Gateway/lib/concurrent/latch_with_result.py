from pylatch.threadlatch import CountDownLatch


class LatchWithResult:

    @staticmethod
    def create(result=None):
        return LatchWithResult(CountDownLatch(1), result)

    def __init__(self, latch, result=None):
        if not isinstance(latch, CountDownLatch):
            raise ValueError('latch must be a CountDownLatch')

        self.latch = latch
        self.result = result

    def set_result(self, result):
        self.result = result
        if self.latch.count == 1:
            self.latch.count_down()

    def get_result(self):
        return self.result
