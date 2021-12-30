import re


class ProcessNumbers:

    def __init__(self):
        self.ones = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
        self.teens = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                      'nineteen')
        self.tens = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'hundred')
        self.magnitudes = ('', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion')

    @staticmethod
    def _validate(self, num):
        if self.is_str(num):
            num = self._sanitize(num)
        elif self.is_float(num):
            return False
        #    if not num == self.is_int(num):
        #        return False
        return num

    @staticmethod
    def _sanitize(num):
        return re.sub('[^0-9.]', '', num)

    #
    # @staticmethod
    # def is_int(num):
    #     try:
    #         int(num) and len(str(num)) > 0
    #         return True
    #     except ValueError:
    #         return False

    @staticmethod
    def is_str(num):
        try:
            str(num)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_float(num):
        if str(num.find('.', 0, 1)):
            return True
        return False

    def process(self, num, index, ln):

        if num == '0':
            return 'zero'

        length = len(num)

        if length > 3:
            return False

        num = num.zfill(3)
        words = ''

        hdigit = int(num[0])
        tdigit = int(num[1])
        odigit = int(num[2])

        words += '' if num[0] == '0' else self.ones[hdigit]
        words += ' hundred ' if not words == '' else ''

        if tdigit > 1:
            words += self.tens[tdigit - 2]
            words += ' '
            words += self.ones[odigit]

        elif tdigit == 1:
            words += self.teens[(int(tdigit + odigit) % 10) - 1]
        elif tdigit == 0:
            words += self.ones[odigit]
        if words.endswith('zero'):
            words = words[:-len('zero')]
        else:
            words += ' '

        if not len(words) == 0:
            words += self.magnitudes[index]

        return words

    def get_words(self, num):

        num = self._validate(self, num)
        if not num:
            return "400 BAD REQUEST"
        length = len(str(num))

        if length > 17:
            return 'This program supports up to 17 digit numbers.'

        count = length // 3 if length % 3 == 0 else length // 3 + 1
        copy = count
        words = []

        for i in range(length - 1, -1, -3):
            words.append(self.process(str(num)[0 if i - 2 < 0 else i - 2: i + 1], copy - count, length))
            count -= 1

        result = ''
        for s in reversed(words):
            temp = s + ' '
            result += temp

        return result

# pn = ProcessNumbers()
# result = pn.get_words(data)
