# -*- coding:utf8 -*-
"""
@author:z05035
@description:时间相关操作类
@time:2019/2/25 16:36

"""
import re
import time
import datetime
import calendar


class TimerOperator():

    @property
    def now_datetime(self):
        """
        获取当前时间
        :return: datetime.datetime(2019, 4, 30, 10, 55, 22, 252264)
        '2019-02-25 16:38:13.258846'
        """
        # datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return datetime.datetime.now()

    @property
    def now_time(self):
        """
        获取当前时间戳
        :return: eg:1551084192.5978465
        """
        return time.time()

    @property
    def now_time_13(self):
        """
        获取当前13位时间戳
        :return: eg:1553157050059
        """
        return int(round(time.time() * 1000))

    @property
    def year(self):
        return int(time.strftime('%Y', time.localtime(time.time())))

    @property
    def month(self):
        return int(time.strftime('%m', time.localtime(time.time())))

    @property
    def day(self):
        return int(time.strftime('%d', time.localtime(time.time())))

    @property
    def week(self):
        week_str = time.strftime('%a', time.localtime(time.time()))
        return self.change_weekdat(week_str)

    def isvaildtime(self, timedate, timestr):
        """
        判断时间是否符合对应格式
        :param timedate: 时间字符串
        :param timestr: 时间格式
        :return:
        """
        try:
            time.strptime(timedate, timestr)
            return True
        except Exception as e:
            print(f'时间格式异常:{e}')
            return False

    def get_now_time(self):
        """
        返回年月日时分秒
        :return:eg:'2019225164647'
        """
        return str(self.now_datetime.year) + str(self.now_datetime.month) + str(self.now_datetime.day) + str(
            self.now_datetime.hour) + str(self.now_datetime.minute) + str(self.now_datetime.second)

    def get_now_time2(self):
        """
        返回年-月-日-时-分-秒-星期
        :return:
        """
        return timeroperator.get_now_standardtime().replace(' ', '-').replace(':', '-') + '-' + str(timeroperator.week)

    def get_day_time(self):
        """
        返回年_月_日
        :return: eg:'2019_2_25'
        """
        return f'{str(self.now_datetime.year)}_{str(self.now_datetime.month)}_{str(self.now_datetime.day)}'

    def get_now_standardtime(self):
        """
        获取现在时间
        :return: eg:'2018-12-06 19:33:36'
        """
        return str(self.now_datetime).split('.')[0]

    def translate_time(self, datetimestr):
        """
        将 年-月-日 时:分:秒 转换为 年月日时分秒
        :param datetimestr: eg:'2018-12-06 19:33:36'
        :return: eg:'20181206193336'
        """
        if self.isvaildtime(datetimestr, '%Y-%m-%d %H:%M:%S'):
            translatetime = datetimestr.strip().split(' ')
            translatetime = ''.join(translatetime[0].split('-')) + ''.join(translatetime[1].split(':'))
            return translatetime

    def time_translate(self, datetimestr):
        """
        将 年-月-日 时:分:秒 转换为 时间戳
        :param datetimestr:eg:'2018-12-06 19:33:36'
        :return:eg:1544096016.0
        """
        translatetime = ""
        if self.isvaildtime(datetimestr, '%Y-%m-%d %H:%M:%S'):
            translatetime = time.mktime(time.strptime(datetimestr, '%Y-%m-%d %H:%M:%S'))
        elif self.isvaildtime(datetimestr, '%Y%m%d%H%M%S'):
            translatetime = time.mktime(time.strptime(datetimestr, '%Y%m%d%H%M%S'))
        return int(translatetime)

    def cal_diff(self, timestamp_list1, timestamp_list2, diff=0, thr=1):
        """
        计算日志时间差
        :param timestamp_list1:
        :param timestamp_list2:
        :param diff:时间差
        :param thr:阈值
        :return:
        """
        ret = -1
        i = 0
        j = 0
        delt = 5
        if timestamp_list1 and timestamp_list2:
            for i, item1 in enumerate(timestamp_list1):
                for j, item2 in enumerate(timestamp_list2):
                    timediff = abs(item1 - item2)
                    delt = abs(timediff - diff)
                    if delt <= thr:
                        ret = 0
                        break
                if delt <= 1:
                    break
        return ret, i, j

    def get_month(self, month):
        month_dict = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 6,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }
        if not isinstance(month, str):
            try:
                month = str(month)
                if len(month) == 1:
                    month = '0' + month
            except Exception as e:
                print(f'转换月份信息异常:{e}')
        return month_dict.get(month, 'error')

    def change_month(self, month):
        change_dict = {
            '01': 'Jan',
            '02': 'Feb',
            '03': 'Mar',
            '04': 'Apr',
            '05': 'May',
            '06': 'Jun',
            '07': 'Jul',
            '08': 'Aug',
            '09': 'Sep',
            '10': 'Oct',
            '11': 'Nov',
            '12': 'Dec',
        }
        if not isinstance(month, str):
            try:
                month = str(month)
                if len(month) == 1:
                    month = '0' + month
            except Exception as e:
                print(f'转换月份信息异常:{e}')
        return change_dict.get(month, 'error')

    def change_weekdat(self, weekday):
        change_dict_eng = {
            'Sun': 0,
            'Mon': 1,
            'Tue': 2,
            'Wed': 3,
            'Thu': 4,
            'Fri': 5,
            'Sat': 6,
        }
        month = ''
        if not isinstance(weekday, str):
            try:
                month = str(weekday)
            except Exception as e:
                print(f'转换星期信息异常:{e}')
        else:
            month = weekday
        return change_dict_eng.get(month, 'error')

    def change_weekday(self, weekday, language='eng'):
        change_dict_eng = {
            '0': 'Sun',
            '1': 'Mon',
            '2': 'Tues',
            '3': 'Wed',
            '4': 'Thur',
            '5': 'Fri',
            '6': 'Sat',
        }
        change_dict_chi = {
            '0': '星期天',
            '1': '星期一',
            '2': '星期二',
            '3': '星期三',
            '4': '星期四',
            '5': '星期五',
            '6': '星期六',
        }
        month = ''
        if not isinstance(weekday, str):
            try:
                month = str(weekday)
            except Exception as e:
                print(f'转换星期信息异常:{e}')
        else:
            month = weekday
        if language == 'eng':
            return change_dict_eng.get(month, 'error')
        else:
            return change_dict_chi.get(month, 'error')

    def change_weekday1(self, weekday, language='eng'):
        change_dict_eng = {
            '0': 'Sun',
            '1': 'Mon',
            '2': 'Tue',
            '3': 'Wed',
            '4': 'Thu',
            '5': 'Fri',
            '6': 'Sat',
        }
        change_dict_chi = {
            '0': '星期天',
            '1': '星期一',
            '2': '星期二',
            '3': '星期三',
            '4': '星期四',
            '5': '星期五',
            '6': '星期六',
        }
        month = ''
        if not isinstance(weekday, str):
            try:
                month = str(weekday)
            except Exception as e:
                print(f'转换星期信息异常:{e}')
        else:
            month = weekday
        if language == 'eng':
            return change_dict_eng.get(month, 'error')
        else:
            return change_dict_chi.get(month, 'error')

    def change_headerstime(self, data):
        """
        将 年-月-日 时:分:秒 转换为 页面头部信息
        @param data: eg:2018-09-06 09:42:25
        @return: eg:Wed%20Sep%205%2017%3A27%3A46%20UTC+0800%202018
        """
        data = data.strip()
        if not self.isvaildtime(data, '%Y-%m-%d %H:%M:%S'):
            return False
        li = data.strip().split(' ')
        year_month_day = li[0].split('-')
        h_m_s = li[1].split(':')
        year = year_month_day[0]
        month = year_month_day[1]
        day = int(year_month_day[2])
        weekday = datetime.datetime(int(year), int(month), int(day)).strftime("%w")
        month = self.change_month(month)
        weekday = self.change_weekday(weekday)
        result = f"{str(weekday)}%20{str(month)}%20{str(day)}%20{'%3A'.join(h_m_s.split(':'))}%20UTC+0800%20{str(year)}"
        return result

    def change_telnet_date(self, telnet_date):
        """
        将Telnet下拿到的date进行转换
            %y 两位数的年份表示（00-99）
            %Y 四位数的年份表示（000-9999）
            %m 月份（01-12）
            %d 月内中的一天（0-31）
            %H 24小时制小时数（0-23）
            %I 12小时制小时数（01-12）
            %M 分钟数（00=59）
            %S 秒（00-59）
            %a 本地简化星期名称
            %A 本地完整星期名称
            %b 本地简化的月份名称
            %B 本地完整的月份名称
            %c 本地相应的日期表示和时间表示
            %j 年内的一天（001-366）
            %p 本地A.M.或P.M.的等价符
            %U 一年中的星期数（00-53）星期天为星期的开始
            %w 星期（0-6），星期天为星期的开始
            %W 一年中的星期数（00-53）星期一为星期的开始
            %x 本地相应的日期表示
            %X 本地相应的时间表示
            %Z 当前时区的名称
            %% %号本身
        :param telnet_date:
        :return:
        """
        datedict = {}
        time_info = re.split(r'\s+', telnet_date)
        if len(time_info) >= 5:
            year = time_info[-1]
            month = time_info[1]
            day = time_info[2]
            hmm = time_info[3]
            timeZone = time_info[4]
            weekD = time_info[0]

            datedict["year"] = int(year)
            datedict["month"] = self.get_month(month)
            datedict["day"] = int(day)
            datedict["hour"] = int(hmm.split(":")[0])
            datedict["minute"] = int(hmm.split(":")[1])
            datedict["second"] = int(hmm.split(":")[2])
            datedict["weekD"] = self.change_weekdat(weekD)
            if timeZone.replace("GMT", "") == "":
                datedict["timeZone"] = 0
            else:
                datedict["timeZone"] = -int(timeZone.replace("GMT", ""))
        return datedict

    def isintime(self, startime, endtime, usrtime):
        """
        判断某个时间是否在时间段范围内
        :param startime:
        :param endtime:
        :param usrtime:
        :return:
        """
        if all([self.isvaildtime(startime, '%Y-%m-%d %H:%M:%S'),
                self.isvaildtime(endtime, '%Y-%m-%d %H:%M:%S'),
                self.isvaildtime(usrtime, '%Y-%m-%d %H:%M:%S')]):
            startime = datetime.datetime.strptime(startime, '%Y-%m-%d %H:%M:%S')
            endtime = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S')
            usrtime = datetime.datetime.strptime(usrtime, '%Y-%m-%d %H:%M:%S')
            # 判断时间是否在范围时间内
            if usrtime >= startime and usrtime <= endtime:
                return True
        return False

    def get_monthweekdaylist(self, year):
        """
        获取对应年份的星期信息
        12个月份每个月的星期数对应的日期列表，如[[[4,11,18,25],[5,12,19,26],[6,13,20,27],[7,14,21,28],[1,8,15,22,29],[2,9,16,23,30],[3,10,17,24,31]],]
        :param year: 年份
        :return:
        """
        monthList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        monthWeekDayList = []
        for i, month in enumerate(monthList):
            monthCalendar = calendar.monthcalendar(year, month)
            weekNameList = [[], [], [], [], [], [], []]  # 当月的星期列表
            for j, weekList in enumerate(monthCalendar):
                for k, item in enumerate(weekList):
                    if item != 0:
                        weekNameList[k].append(item)
            monthWeekDayList.append(weekNameList)
        return monthWeekDayList


timeroperator = TimerOperator()

if __name__ == '__main__':
    t = TimerOperator()
    print(timeroperator.get_now_standardtime().replace(' ', '-').replace(':', '-') + '-' + str(timeroperator.week))
