# coding=utf-8

from handlers.public.loginhandle import LoginHandle
from handlers.public.fuzzhandle import *
# 路由配置
urls = [
    (r'/login', LoginHandle),
    (r"/fuzz-loadscriptlist", loadUserScriptList),
    (r"/fuzz-loadtemplatelist", loadTemplateList),
    (r"/fuzz-loadreportlist", loadReportList),
    (r"/fuzz-gettemplate", getTemplate),
    (r"/fuzz-getscript", getScript),
    (r"/fuzz-starttest", startFuzzingTest),
    (r"/fuzz-pcaprunning", pcapRunning),
    (r"/fuzz-testrunning", testRunning),
    (r"/fuzz-onetestrunning", onetestRunning),
    (r"/fuzz-stoptest", stopTest),
    (r"/fuzz-pausetest", pauseTest),
    (r"/fuzz-continuetest", continueTest),
    (r"/fuzz-savescript", saveFuzzingScript),
    (r"/fuzz-gettestdetail", getTestDetail),
    (r"/fuzz-getnetcard", getNetCartList),
    (r"/fuzz-gethtmlreport", getHtmlReport),
    (r"/fuzz-startpcapanalyse", analysePcap),
    (r"/fuzz-gettotaltestnumber", getFuzzingTestCaseNumber),
    (r"/fuzz-gettestnumberrunning", getTestNumberRunning),
    (r"/fuzz-gettotaltestinfo", getFuzzingTestCaseInfo),
    (r"/fuzz-deletereport", removeReportProc),
    (r"/fuzz-deleteallreport", removeAllReportProc),
    (r"/fuzz-casetestbegin", startRsfTest),
    (r"/fuzz-casetestresult", rsfRunning),
    (r"/fuzz-casetestbegin", startRsfCredTest),
    (r"/fuzz-casetestresult", rsfCredRunning)
]
