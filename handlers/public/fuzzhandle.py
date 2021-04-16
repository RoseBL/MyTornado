from handlers.base.basehandle import BaseHandler
# 加载用户
class loadUserScriptList(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("loadUserScriptList")


class loadTemplateList(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("loadTemplateList")


class loadReportList(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("loadReportList")


class getScript(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getScript")

class startFuzzingTest(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("startFuzzingTest")


class pcapRunning(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("pcapRunning")


class testRunning(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("testRunning")


class onetestRunning(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("onetestRunning")


class stopTest(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("stopTest")


class pauseTest(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("pauseTest")


class continueTest(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("continueTest")


class saveFuzzingScript(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("saveFuzzingScript")


class getTestDetail(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getTestDetail")


class getNetCartList(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getNetCartList")


class getHtmlReport(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getHtmlReport")


class analysePcap(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("analysePcap")


class getFuzzingTestCaseNumber(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getFuzzingTestCaseNumber")


class getTestNumberRunning(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getTestNumberRunning")


class getFuzzingTestCaseInfo(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("getFuzzingTestCaseInfo")


class removeReportProc(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("removeReportProc")


class removeAllReportProc(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("removeAllReportProc")


class startRsfTest(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("startRsfTest")


class rsfRunning(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("rsfRunning")


class startRsfCredTest(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("startRsfCredTest")


class rsfCredRunning(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        # 从querystring查询字符串中获取id参数的值，若无则默认为0.
        print("rsfCredRunning")


class getTemplate(BaseHandler):
    # 定义get方法对HTTP的GET请求做出响应
    def get(self):
        templatename = self.get_query_argument("templatename")
        _dc = self.get_query_argument("_dc")
        page = self.get_query_argument("page")
        start = self.get_query_argument("start")
        limit = self.get_query_argument("limit")
        print(templatename)
        print(page)
        # write方法将字符串写入HTTP响应
        a = 9 // 2
        self.write(str(a))