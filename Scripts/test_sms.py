import pytest

from Base.get_driver import get_driver
from Page.page_sms import PageSMS


class TestSMS():
    def setup_class(self):
        self.driver = get_driver("com.android.mms", ".ui.ConversationList")
        self.sms = PageSMS(self.driver)
        # 点击添加短信按钮和输入固定手机号
        self.sms.page_add_sms_and_phone("18666666666")

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("input_text", ["哈喽", "你好", "瓦特？"])
    def test_sms(self, input_text):
        # 输入短信内容
        self.sms.page_input_sms_text(input_text)
        print("正准备发送 %s 内容" % input_text)
        # 点击发送短信
        self.sms.page_send_sms_btn()
        print(" %s 内容发送成功" % input_text)
        # 断言 短信是否发送成功
        assert input_text in self.sms.get_result_list()
        print(" %s 内容断言成功，已存在%s列表中" % (input_text, self.sms.get_result_list()))

    @pytest.mark.run(order=2)
    def test_delete_sms(self):
        # 删除短信
        self.sms.page_delete_sms_list()
        # 断言删除是否干净
        assert self.sms.if_sms_list()
